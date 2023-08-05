#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extensión de pydatajson para la federación de metadatos de datasets a través
de la API de CKAN.
"""

from __future__ import print_function, unicode_literals
import logging
import traceback
from ckanapi.errors import NotFound, CKANAPIError
from requests import RequestException
import time

from pydatajson.constants import REQUESTS_TIMEOUT, DEFAULT_TIMEZONE
from pydatajson.custom_exceptions import NumericDistributionIdentifierError
from .ckan_utils import map_dataset_to_package, map_theme_to_group,\
    map_distributions_to_resources
from pydatajson.custom_remote_ckan import CustomRemoteCKAN as RemoteCKAN
from .search import get_datasets
from .helpers import resource_files_download

logger = logging.getLogger('pydatajson.federation')


def push_dataset_to_ckan(catalog, owner_org, dataset_origin_identifier,
                         portal_url, apikey, catalog_id=None,
                         demote_superThemes=True, demote_themes=True,
                         download_strategy=None, generate_new_access_url=None,
                         origin_tz=DEFAULT_TIMEZONE, dst_tz=DEFAULT_TIMEZONE):
    """Escribe la metadata de un dataset en el portal pasado por parámetro.

        Args:
            catalog (DataJson): El catálogo de origen que contiene el dataset.
            owner_org (str): La organización a la cual pertence el dataset.
            dataset_origin_identifier (str): El id del dataset que se va a
                federar.
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear o actualizar el dataset.
            catalog_id (str or None): El prefijo con el que va a preceder
                el id del dataset en catálogo destino.
            demote_superThemes(bool): Si está en true, los ids de los super
                themes del dataset, se propagan como grupo.
            demote_themes(bool): Si está en true, los labels de los themes
                del dataset, pasan a ser tags. Sino, se pasan como grupo.
            download_strategy(callable): Una función (catálogo, distribución)->
                bool. Sobre las distribuciones que evalúa True, descarga el
                recurso en el downloadURL y lo sube al portal de destino.
                Por default no sube ninguna distribución.
            generate_new_access_url(list): Se pasan los ids de las
                distribuciones cuyo accessURL se regenerar en el portal de
                destino. Para el resto, el portal debe mantiene el valor pasado
                en el DataJson.
            origin_tz(str): Timezone de origen, un string (EJ: Africa/Bamako)
                el cual identifica el timezone del emisor del DataJson.
            dst_tz(str): Timezone de destino, un string
                (EJ: Antarctica/Palmer) el cual identifica el timezone del
                receptor del DataJson, comunmente el timezone del servidor.
        Returns:
            str: El id del dataset en el catálogo de destino.
    """
    dataset = catalog.get_dataset(dataset_origin_identifier)
    if not dataset:
        print(dataset_origin_identifier, "no está en el catálogo.")

    ckan_portal = RemoteCKAN(portal_url, apikey=apikey,
                             verify_ssl=catalog.verify_ssl,
                             requests_timeout=catalog.requests_timeout)

    package = map_dataset_to_package(catalog,
                                     dataset,
                                     owner_org,
                                     catalog_id=catalog_id,
                                     demote_superThemes=demote_superThemes,
                                     demote_themes=demote_themes,
                                     origin_tz=origin_tz,
                                     dst_tz=dst_tz)

    # Get license id
    if dataset.get('license'):
        license_list = ckan_portal.call_action('license_list')
        try:
            ckan_license = next(
                license_item for license_item in license_list if
                license_item['title'] == dataset['license'] or
                license_item['url'] == dataset['license']
            )
            package['license_id'] = ckan_license['id']
        except StopIteration:
            package['license_id'] = 'notspecified'
    else:
        package['license_id'] = 'notspecified'

    try:
        pushed_package = ckan_portal.call_action(
            'package_update', data_dict=package)
    except NotFound:
        pushed_package = ckan_portal.call_action(
            'package_create', data_dict=package)

    with resource_files_download(catalog, dataset.get('distribution', []),
                                 download_strategy) as resource_files:
        resources_update(portal_url, apikey, dataset.get('distribution', []),
                         resource_files, generate_new_access_url, catalog_id)

    ckan_portal.close()
    return pushed_package['id']


def resources_update(portal_url, apikey, distributions,
                     resource_files, generate_new_access_url=None,
                     catalog_id=None, verify_ssl=False,
                     requests_timeout=REQUESTS_TIMEOUT):
    """Sube archivos locales a sus distribuciones correspondientes en el portal
     pasado por parámetro.

            Args:
                portal_url (str): La URL del portal CKAN de destino.
                apikey (str): La apikey de un usuario con los permisos que le
                    permitan crear o actualizar el dataset.
                distributions(list): Lista de distribuciones posibles para
                    actualizar.
                resource_files(dict): Diccionario con entradas
                    id_de_distribucion:path_al_recurso a subir
                generate_new_access_url(list): Lista de ids de distribuciones a
                    las cuales se actualizará el accessURL con los valores
                    generados por el portal de destino
                catalog_id(str): prependea el id al id del recurso para
                    encontrarlo antes de subirlo
                verify_ssl(bool): Verificar certificados SSL
                requests_timeout(int): cantidad en segundos para timeoutear un
                request al server.
            Returns:
                list: los ids de los recursos modificados
        """
    ckan_portal = RemoteCKAN(portal_url, apikey=apikey, verify_ssl=verify_ssl,
                             requests_timeout=requests_timeout)
    result = []
    generate_new_access_url = generate_new_access_url or []
    ckan_resources = map_distributions_to_resources(distributions)
    for resource in ckan_resources:
        if resource['id'] in generate_new_access_url:
            resource.update({'accessURL': ''})
        if resource['id'] in resource_files:
            resource.update({'resource_type': 'file.upload',
                             'upload':
                                 open(resource_files[resource['id']], 'rb')})
        resource['id'] = catalog_id + '_' + resource['id'] \
            if catalog_id else resource['id']
        try:
            pushed = ckan_portal.action.resource_patch(**resource)
            result.append(pushed['id'])
        except CKANAPIError as e:
            logger.exception(
                "Error actualizando distribución {}: {}"
                .format(resource['id'], str(e)))
    return result


def remove_dataset_from_ckan(identifier, portal_url, apikey, verify_ssl=False,
                             requests_timeout=REQUESTS_TIMEOUT):
    ckan_portal = RemoteCKAN(portal_url, apikey=apikey, verify_ssl=verify_ssl,
                             requests_timeout=requests_timeout)
    ckan_portal.call_action('dataset_purge', data_dict={'id': identifier})


def remove_harvested_ds_from_ckan(catalog, portal_url, apikey,
                                  catalog_id=None, original_ids=None):
    catalog_id = catalog_id or catalog.get("identifier")
    assert catalog_id, "Necesita un identificador de catálogo."

    if not original_ids:
        original_ids = catalog.get_datasets(meta_field="identifier")
    harvested_ids = ["_".join([catalog_id, original_id])
                     for original_id in original_ids]

    for harvested_id in harvested_ids:
        try:
            remove_dataset_from_ckan(harvested_id, portal_url, apikey)
            logger.info("{} eliminado de {}".format(harvested_id, catalog_id))
        except Exception:
            logger.exception(
                "{} de {} no existe.".format(
                    harvested_id, catalog_id))


def remove_datasets_from_ckan(portal_url, apikey, filter_in=None,
                              filter_out=None, only_time_series=False,
                              organization=None, verify_ssl=False,
                              requests_timeout=REQUESTS_TIMEOUT):
    """Borra un dataset en el portal pasado por parámetro.

            Args:
                portal_url (str): La URL del portal CKAN de destino.
                apikey (str): La apikey de un usuario con los permisos que le
                    permitan borrar el dataset.
                filter_in(dict): Diccionario de filtrado positivo, similar al
                    de search.get_datasets.
                filter_out(dict): Diccionario de filtrado negativo, similar al
                    de search.get_datasets.
                only_time_series(bool): Filtrar solo los datasets que tengan
                    recursos con series de tiempo.
                organization(str): Filtrar solo los datasets que pertenezcan a
                    cierta organizacion.
                verify_ssl(bool): Verificar certificados SSL
                requests_timeout(int): cantidad en segundos para timeoutear un
                request al server.
            Returns:
                None
    """
    ckan_portal = RemoteCKAN(portal_url, apikey=apikey, verify_ssl=verify_ssl,
                             requests_timeout=requests_timeout)
    identifiers = []
    datajson_filters = filter_in or filter_out or only_time_series
    if datajson_filters:
        identifiers += get_datasets(
            portal_url + '/data.json',
            filter_in=filter_in, filter_out=filter_out,
            only_time_series=only_time_series, meta_field='identifier'
        )
    if organization:
        query = 'organization:"' + organization + '"'
        search_result = ckan_portal.call_action('package_search', data_dict={
            'q': query, 'rows': 500, 'start': 0})
        org_identifiers = [dataset['id']
                           for dataset in search_result['results']]
        start = 500
        while search_result['count'] > start:
            search_result = ckan_portal.call_action(
                'package_search', data_dict={
                    'q': query, 'rows': 500, 'start': start})
            org_identifiers += [dataset['id']
                                for dataset in search_result['results']]
            start += 500

        if datajson_filters:
            identifiers = set(identifiers).intersection(set(org_identifiers))
        else:
            identifiers = org_identifiers

    for identifier in identifiers:
        ckan_portal.call_action('dataset_purge', data_dict={'id': identifier})


def push_theme_to_ckan(catalog, portal_url, apikey,
                       identifier=None, label=None):
    """Escribe la metadata de un theme en el portal pasado por parámetro.

            Args:
                catalog (DataJson): El catálogo de origen que contiene el
                    theme.
                portal_url (str): La URL del portal CKAN de destino.
                apikey (str): La apikey de un usuario con los permisos que le
                    permitan crear o actualizar el dataset.
                identifier (str): El identificador para buscar el theme en la
                    taxonomia.
                label (str): El label para buscar el theme en la taxonomia.
            Returns:
                str: El name del theme en el catálogo de destino.
        """
    ckan_portal = RemoteCKAN(portal_url, apikey=apikey,
                             verify_ssl=catalog.verify_ssl,
                             requests_timeout=catalog.requests_timeout)
    theme = catalog.get_theme(identifier=identifier, label=label)
    group = map_theme_to_group(theme)
    pushed_group = ckan_portal.call_action('group_create', data_dict=group)
    return pushed_group['name']


def restore_dataset_to_ckan(catalog, owner_org, dataset_origin_identifier,
                            portal_url, apikey, download_strategy=None,
                            generate_new_access_url=None,
                            origin_tz=DEFAULT_TIMEZONE,
                            dst_tz=DEFAULT_TIMEZONE):
    """Restaura la metadata de un dataset en el portal pasado por parámetro.

        Args:
            catalog (DataJson): El catálogo de origen que contiene el dataset.
            owner_org (str): La organización a la cual pertence el dataset.
            dataset_origin_identifier (str): El id del dataset que se va a
                restaurar.
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear o actualizar el dataset.
            download_strategy(callable): Una función (catálogo, distribución)->
                bool. Sobre las distribuciones que evalúa True, descarga el
                recurso en el downloadURL y lo sube al portal de destino.
                Por default no sube ninguna distribución.
            generate_new_access_url(list): Se pasan los ids de las
                    distribuciones cuyo accessURL se regenerar en el portal de
                    destino. Para el resto, el portal debe mantiene el valor
                    pasado en el DataJson.
            origin_tz(str): Timezone de origen, un string (EJ: Africa/Bamako)
                el cual identifica el timezone del emisor del DataJson.
            dst_tz(str): Timezone de destino, un string
                (EJ: Antarctica/Palmer) el cual identifica el timezone del
                receptor del DataJson, comunmente el timezone del servidor.
        Returns:
            str: El id del dataset restaurado.
    """

    conditions = {
        "dataset": {
            "identifier": dataset_origin_identifier
        }
    }
    distributions = catalog.get_distributions(filter_in=conditions)

    for distribution in distributions:
        if distribution["identifier"].isdigit():
            raise NumericDistributionIdentifierError(
                'No puede restaurarse la distribucion con id "{}" dado que '
                'este es numerico. Por favor, cambielo e intente de '
                'nuevo'.format(distribution["identifier"]))

    return push_dataset_to_ckan(
        catalog, owner_org, dataset_origin_identifier,
        portal_url, apikey, catalog_id=None, demote_superThemes=False,
        demote_themes=False, download_strategy=download_strategy,
        generate_new_access_url=generate_new_access_url,
        origin_tz=origin_tz, dst_tz=dst_tz
    )


def harvest_dataset_to_ckan(catalog, owner_org, dataset_origin_identifier,
                            portal_url, apikey, catalog_id,
                            download_strategy=None,
                            origin_tz=DEFAULT_TIMEZONE,
                            dst_tz=DEFAULT_TIMEZONE):
    """Federa la metadata de un dataset en el portal pasado por parámetro.

        Args:
            catalog (DataJson): El catálogo de origen que contiene el dataset.
            owner_org (str): La organización a la cual pertence el dataset.
            dataset_origin_identifier (str): El id del dataset que se va a
                restaurar.
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear o actualizar el dataset.
            catalog_id(str): El id que prependea al dataset y recursos
            download_strategy(callable): Una función (catálogo, distribución)->
                bool. Sobre las distribuciones que evalúa True, descarga el
                recurso en el downloadURL y lo sube al portal de destino.
                Por default no sube ninguna distribución.
            origin_tz(str): Timezone de origen, un string (EJ: Africa/Bamako)
                el cual identifica el timezone del emisor del DataJson.
            dst_tz(str): Timezone de destino, un string
                (EJ: Antarctica/Palmer) el cual identifica el timezone del
                receptor del DataJson, comunmente el timezone del servidor.
        Returns:
            str: El id del dataset restaurado.
    """

    return push_dataset_to_ckan(catalog, owner_org, dataset_origin_identifier,
                                portal_url, apikey, catalog_id=catalog_id,
                                download_strategy=download_strategy,
                                origin_tz=origin_tz, dst_tz=dst_tz)


def harvest_catalog_to_ckan(catalog, portal_url, apikey, catalog_id,
                            dataset_list=None, owner_org=None,
                            download_strategy=None,
                            origin_tz=DEFAULT_TIMEZONE,
                            dst_tz=DEFAULT_TIMEZONE):
    """Federa los datasets de un catálogo al portal pasado por parámetro.

        Args:
            catalog (DataJson): El catálogo de origen que se federa.
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear o actualizar el dataset.
            catalog_id (str): El prefijo con el que va a preceder el id del
                dataset en catálogo destino.
            dataset_list(list(str)): Los ids de los datasets a federar. Si no
                se pasa una lista, todos los datasests se federan.
            owner_org (str): La organización a la cual pertencen los datasets.
                Si no se pasa, se utiliza el catalog_id.
            download_strategy(callable): Una función (catálogo, distribución)->
                bool. Sobre las distribuciones que evalúa True, descarga el
                recurso en el downloadURL y lo sube al portal de destino.
                Por default no sube ninguna distribución.
            origin_tz(str): Timezone de origen, un string (EJ: Africa/Bamako)
                el cual identifica el timezone del emisor del DataJson.
            dst_tz(str): Timezone de destino, un string
                (EJ: Antarctica/Palmer) el cual identifica el timezone del
                receptor del DataJson, comunmente el timezone del servidor.
        Returns:
            str: El id del dataset en el catálogo de destino.
    """
    # Evitar entrar con valor falsy
    harvested = []
    if dataset_list is None:
        try:
            dataset_list = [ds['identifier'] for ds in catalog.datasets]
        except KeyError:
            logger.warning('Hay datasets sin identificadores')
            return harvested
    owner_org = owner_org or catalog_id
    errors = {}
    for dataset_id in dataset_list:
        try:
            harvested_id = harvest_dataset_to_ckan(catalog, owner_org,
                                                   dataset_id, portal_url,
                                                   apikey, catalog_id,
                                                   download_strategy,
                                                   origin_tz=origin_tz,
                                                   dst_tz=dst_tz)
            harvested.append(harvested_id)
        except Exception as e:
            msg = "Error federando catalogo: %s, dataset: %s al portal: %s\n"\
                  % (catalog_id, dataset_id, portal_url)
            msg += str(e)
            logger.warning(msg)
            errors[dataset_id] = str(e)

    return harvested, errors


def push_new_themes(catalog, portal_url, apikey):
    """Toma un catálogo y escribe los temas de la taxonomía que no están
    presentes.

        Args:
            catalog (DataJson): El catálogo de origen que contiene la
                taxonomía.
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear o actualizar los temas.
        Returns:
            str: Los ids de los temas creados.
    """
    ckan_portal = RemoteCKAN(portal_url, apikey=apikey,
                             verify_ssl=catalog.verify_ssl,
                             requests_timeout=catalog.requests_timeout)
    existing_themes = ckan_portal.call_action('group_list')
    new_themes = [theme['id'] for theme in catalog.get('themeTaxonomy', [])
                  if theme['id'] not in existing_themes]
    pushed_names = []
    for new_theme in new_themes:
        name = push_theme_to_ckan(
            catalog, portal_url, apikey, identifier=new_theme)
        pushed_names.append(name)
    return pushed_names


def get_organizations_from_ckan(portal_url, verify_ssl=False,
                                requests_timeout=REQUESTS_TIMEOUT):
    """Toma la url de un portal y devuelve su árbol de organizaciones.

            Args:
                portal_url (str): La URL del portal CKAN de origen.
                verify_ssl(bool): Verificar certificados SSL
                requests_timeout(int): cantidad en segundos para timeoutear un
                    request al server.
            Returns:
                list: Lista de diccionarios anidados con la información de
                las organizaciones.
        """
    ckan_portal = RemoteCKAN(portal_url, verify_ssl=verify_ssl,
                             requests_timeout=requests_timeout)
    return ckan_portal.call_action('group_tree',
                                   data_dict={'type': 'organization'})


def get_organization_from_ckan(portal_url, org_id, verify_ssl=False,
                               requests_timeout=REQUESTS_TIMEOUT):
    """Toma la url de un portal y un id, y devuelve la organización a buscar.

            Args:
                portal_url (str): La URL del portal CKAN de origen.
                org_id (str): El id de la organización a buscar.
                verify_ssl(bool): Verificar certificados SSL
                requests_timeout(int): cantidad en segundos para timeoutear un
                    request al server.
            Returns:
                dict: Diccionario con la información de la organización.
        """
    ckan_portal = RemoteCKAN(portal_url, verify_ssl=verify_ssl,
                             requests_timeout=requests_timeout)
    return ckan_portal.call_action('organization_show',
                                   data_dict={'id': org_id})


def push_organization_tree_to_ckan(portal_url, apikey, org_tree, parent=None):
    """Toma un árbol de organizaciones y lo replica en el portal de
    destino.

            Args:
                portal_url (str): La URL del portal CKAN de destino.
                apikey (str): La apikey de un usuario con los permisos que le
                    permitan crear las organizaciones.
                org_tree(list): lista de diccionarios con la data de las
                    organizaciones a crear.
                parent(str): campo name de la organizacion padre.
            Returns:
                (list): Devuelve el arbol de organizaciones recorridas,
                    junto con el status detallando si la creación fue
                    exitosa o no.

    """
    created = []
    for node in org_tree:
        pushed_org = push_organization_to_ckan(portal_url,
                                               apikey,
                                               node,
                                               parent=parent)
        if pushed_org['success']:
            pushed_org['children'] = push_organization_tree_to_ckan(
                portal_url, apikey, node['children'], parent=node['name'])

        created.append(pushed_org)
    return created


def push_organization_to_ckan(portal_url, apikey, organization, parent=None,
                              verify_ssl=False,
                              requests_timeout=REQUESTS_TIMEOUT):
    """Toma una organización y la crea en el portal de destino.
        Args:
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear la organización.
            organization(dict): Datos de la organización a crear.
            parent(str): Campo name de la organización padre.
            verify_ssl(bool): Verificar certificados SSL
            requests_timeout(int): cantidad en segundos para timeoutear un
                request al server.
        Returns:
            (dict): Devuelve el diccionario de la organizacion enviada,
                junto con el status detallando si la creación fue
                exitosa o no.

    """
    portal = RemoteCKAN(portal_url, apikey=apikey, verify_ssl=verify_ssl,
                        requests_timeout=requests_timeout)
    if parent:
        organization['groups'] = [{'name': parent}]
    try:
        pushed_org = portal.call_action('organization_create',
                                        data_dict=organization)
        pushed_org['success'] = True
    except Exception as e:
        logger.exception('Ocurrió un error creando la organización {}: {}'
                         .format(organization['title'], str(e)))
        pushed_org = {'name': organization, 'success': False}

    return pushed_org


def remove_organization_from_ckan(portal_url, apikey, organization_id,
                                  verify_ssl=False,
                                  requests_timeout=REQUESTS_TIMEOUT):
    """Toma un id de organización y la purga del portal de destino.
        Args:
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan borrar la organización.
            organization_id(str): Id o name de la organización a borrar.
            verify_ssl(bool): Verificar certificados SSL
            requests_timeout(int): cantidad en segundos para timeoutear un
                request al server.
        Returns:
            None.

    """
    portal = RemoteCKAN(portal_url, apikey=apikey, verify_ssl=verify_ssl,
                        requests_timeout=requests_timeout)
    try:
        portal.call_action('organization_purge',
                           data_dict={'id': organization_id})

    except Exception as e:
        logger.exception('Ocurrió un error borrando la organización {}: {}'
                         .format(organization_id, str(e)))


def remove_organizations_from_ckan(portal_url, apikey, organization_list):
    """Toma una lista de ids de organización y las purga del portal de destino.
        Args:
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan borrar la organización.
            organization_list(list): Id o name de las organizaciones a borrar.
        Returns:
            None.

    """
    for org in organization_list:
        remove_organization_from_ckan(portal_url, apikey, org)


def restore_organizations_to_ckan(catalog, organizations, portal_url, apikey,
                                  download_strategy=None,
                                  generate_new_access_url=None,
                                  origin_tz=DEFAULT_TIMEZONE,
                                  dst_tz=DEFAULT_TIMEZONE,
                                  time_delay=0.1):
    """Restaura los datasets indicados para c/organización de un catálogo al
        portal pasado. Si hay temas presentes en el DataJson que no están en el
        portal de CKAN, los genera. Las organizaciones ya deben estar creadas.

        Args:
            catalog (DataJson): El catálogo de origen que se restaura.
            organizations (dict): Datasets a restaurar por c/organización donde
                {"organizacion_id": [dataset_id1, dataset_id2, ...]}
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear o actualizar el dataset.
            download_strategy(callable): Una función (catálogo, distribución)->
                bool. Sobre las distribuciones que evalúa True, descarga el
                recurso en el downloadURL y lo sube al portal de destino.
                Por default no sube ninguna distribución.
            generate_new_access_url(list): Se pasan los ids de las
                distribuciones cuyo accessURL se regenerar en el portal de
                destino. Para el resto, el portal debe mantiene el valor
                pasado en el DataJson.
            origin_tz(str): Timezone de origen, un string (EJ: Africa/Bamako)
                el cual identifica el timezone del emisor del DataJson.
            dst_tz(str): Timezone de destino, un string
                (EJ: Antarctica/Palmer) el cual identifica el timezone del
                receptor del DataJson, comunmente el timezone del servidor.
            time_delay(int): Segundos que espera entre cada request para no
                saturar al CKAN de destino.
        Returns:
            list(str): La lista de ids de datasets subidos.
    """
    pushed_datasets = {}
    for org in organizations:
        org_pushed_datasets = restore_organization_to_ckan(
            catalog, org,
            portal_url,
            apikey,
            dataset_list=organizations[org],
            origin_tz=origin_tz,
            dst_tz=dst_tz,
            time_delay=time_delay
        )
        pushed_datasets[org] = org_pushed_datasets

    return pushed_datasets


def restore_organization_to_ckan(catalog, owner_org, portal_url, apikey,
                                 dataset_list=None, download_strategy=None,
                                 generate_new_access_url=None,
                                 origin_tz=DEFAULT_TIMEZONE,
                                 dst_tz=DEFAULT_TIMEZONE,
                                 time_delay=0.1):
    """Restaura los datasets de la organización de un catálogo al portal pasado
       por parámetro. Si hay temas presentes en el DataJson que no están en el
       portal de CKAN, los genera.

        Args:
            catalog (DataJson): El catálogo de origen que se restaura.
            portal_url (str): La URL del portal CKAN de destino.
            apikey (str): La apikey de un usuario con los permisos que le
                permitan crear o actualizar el dataset.
            dataset_list(list(str)): Los ids de los datasets a restaurar. Si no
                se pasa una lista, todos los datasests se restauran.
            owner_org (str): La organización a la cual pertencen los datasets.
            download_strategy(callable): Una función (catálogo, distribución)->
                bool. Sobre las distribuciones que evalúa True, descarga el
                recurso en el downloadURL y lo sube al portal de destino.
                Por default no sube ninguna distribución.
            generate_new_access_url(list): Se pasan los ids de las
                    distribuciones cuyo accessURL se regenerar en el portal de
                    destino. Para el resto, el portal debe mantiene el valor
                    pasado en el DataJson.
            origin_tz(str): Timezone de origen, un string (EJ: Africa/Bamako)
                el cual identifica el timezone del emisor del DataJson.
            dst_tz(str): Timezone de destino, un string
                (EJ: Antarctica/Palmer) el cual identifica el timezone del
                receptor del DataJson, comunmente el timezone del servidor.
            time_delay(int): Segundos que espera entre cada request para no
                saturar al CKAN de destino.
        Returns:
            list(str): La lista de ids de datasets subidos.
    """
    push_new_themes(catalog, portal_url, apikey)
    restored = []
    if dataset_list is None:
        try:
            dataset_list = [ds['identifier'] for ds in catalog.datasets]
        except KeyError:
            logger.exception('Hay datasets sin identificadores')
            return restored

    for dataset_id in dataset_list:
        try:
            restored_id = restore_dataset_to_ckan(catalog, owner_org,
                                                  dataset_id, portal_url,
                                                  apikey, download_strategy,
                                                  generate_new_access_url,
                                                  origin_tz=origin_tz,
                                                  dst_tz=dst_tz)
            restored.append(restored_id)
            time.sleep(time_delay)
        except (CKANAPIError, KeyError, AttributeError, RequestException,
                NumericDistributionIdentifierError) as e:
            logger.exception('Ocurrió un error restaurando el dataset {}: {}'
                             .format(dataset_id, str(e)))
    return restored


def restore_catalog_to_ckan(catalog, origin_portal_url, destination_portal_url,
                            apikey, download_strategy=None,
                            generate_new_access_url=None,
                            origin_tz=DEFAULT_TIMEZONE,
                            dst_tz=DEFAULT_TIMEZONE,
                            time_delay=0.1):
    """Restaura los datasets de un catálogo original al portal pasado
       por parámetro. Si hay temas presentes en el DataJson que no están en
       el portal de CKAN, los genera.

            Args:
                catalog (DataJson): El catálogo de origen que se restaura.
                origin_portal_url (str): La URL del portal CKAN de origen.
                destination_portal_url (str): La URL del portal CKAN de
                    destino.
                apikey (str): La apikey de un usuario con los permisos que le
                    permitan crear o actualizar el dataset.
                download_strategy(callable): Una función
                    (catálogo, distribución)-> bool. Sobre las distribuciones
                    que evalúa True, descarga el recurso en el downloadURL y lo
                    sube al portal de destino. Por default no sube ninguna
                    distribución.
                generate_new_access_url(list): Se pasan los ids de las
                    distribuciones cuyo accessURL se regenerar en el portal de
                    destino. Para el resto, el portal debe mantiene el valor
                    pasado en el DataJson.
                origin_tz(str): Timezone de origen, un string
                    (EJ: Africa/Bamako) el cual identifica el timezone
                    del emisor del DataJson.
                dst_tz(str): Timezone de destino, un string
                    (EJ: Antarctica/Palmer) el cual identifica el timezone del
                    receptor del DataJson, comunmente el timezone del servidor.
                time_delay(int): Segundos que espera entre cada request para no
                    saturar al CKAN de destino.
            Returns:
                dict: Diccionario con key organización y value la lista de ids
                    de datasets subidos a esa organización
        """
    catalog['homepage'] = catalog.get('homepage') or origin_portal_url
    res = {}
    origin_portal = RemoteCKAN(origin_portal_url,
                               verify_ssl=catalog.verify_ssl,
                               requests_timeout=catalog.requests_timeout)

    try:
        org_list = origin_portal.action.organization_list()

    except CKANAPIError as e:
        logger.exception(
            'Ocurrió un error buscando las organizaciones del portal {}: {}'
            .format(origin_portal_url, str(e)))
        print(e)
        return res

    for org in org_list:
        print("Restaurando organizacion {}".format(org))

        try:
            response = origin_portal.action.organization_show(
                id=org, include_datasets=True)
            datasets = [package['id'] for package in response['packages']]

            pushed_datasets = restore_organization_to_ckan(
                catalog, org, destination_portal_url, apikey,
                dataset_list=datasets, download_strategy=download_strategy,
                generate_new_access_url=generate_new_access_url,
                origin_tz=origin_tz, dst_tz=dst_tz, time_delay=time_delay
            )
            res[org] = pushed_datasets
        except Exception as e:
            print(e)
            print(traceback.print_exc())

    return res
