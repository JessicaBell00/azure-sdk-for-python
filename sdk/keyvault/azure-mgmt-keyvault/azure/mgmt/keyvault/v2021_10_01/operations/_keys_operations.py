# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_create_if_not_exist_request(
    resource_group_name: str, vault_name: str, key_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/keys/{keyName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
        "keyName": _SERIALIZER.url("key_name", key_name, "str", pattern=r"^[a-zA-Z0-9-]{1,127}$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, vault_name: str, key_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/keys/{keyName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
        "keyName": _SERIALIZER.url("key_name", key_name, "str", pattern=r"^[a-zA-Z0-9-]{1,127}$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(resource_group_name: str, vault_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/keys",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_version_request(
    resource_group_name: str, vault_name: str, key_name: str, key_version: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/keys/{keyName}/versions/{keyVersion}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
        "keyName": _SERIALIZER.url("key_name", key_name, "str", pattern=r"^[a-zA-Z0-9-]{1,127}$"),
        "keyVersion": _SERIALIZER.url("key_version", key_version, "str", pattern=r"^[a-fA-F0-9]{32}$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_versions_request(
    resource_group_name: str, vault_name: str, key_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/keys/{keyName}/versions",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
        "keyName": _SERIALIZER.url("key_name", key_name, "str", pattern=r"^[a-zA-Z0-9-]{1,127}$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class KeysOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.keyvault.v2021_10_01.KeyVaultManagementClient`'s
        :attr:`keys` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @overload
    def create_if_not_exist(
        self,
        resource_group_name: str,
        vault_name: str,
        key_name: str,
        parameters: _models.KeyCreateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Key:
        """Creates the first version of a new key if it does not exist. If it already exists, then the
        existing key is returned without any write operations being performed. This API does not create
        subsequent versions, and does not update existing keys.

        :param resource_group_name: The name of the resource group which contains the specified key
         vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault which contains the key to be created. Required.
        :type vault_name: str
        :param key_name: The name of the key to be created. The value you provide may be copied
         globally for the purpose of running the service. The value provided should not include
         personally identifiable or sensitive information. Required.
        :type key_name: str
        :param parameters: The parameters used to create the specified key. Required.
        :type parameters: ~azure.mgmt.keyvault.v2021_10_01.models.KeyCreateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Key or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_10_01.models.Key
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_if_not_exist(
        self,
        resource_group_name: str,
        vault_name: str,
        key_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Key:
        """Creates the first version of a new key if it does not exist. If it already exists, then the
        existing key is returned without any write operations being performed. This API does not create
        subsequent versions, and does not update existing keys.

        :param resource_group_name: The name of the resource group which contains the specified key
         vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault which contains the key to be created. Required.
        :type vault_name: str
        :param key_name: The name of the key to be created. The value you provide may be copied
         globally for the purpose of running the service. The value provided should not include
         personally identifiable or sensitive information. Required.
        :type key_name: str
        :param parameters: The parameters used to create the specified key. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Key or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_10_01.models.Key
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_if_not_exist(
        self,
        resource_group_name: str,
        vault_name: str,
        key_name: str,
        parameters: Union[_models.KeyCreateParameters, IO[bytes]],
        **kwargs: Any
    ) -> _models.Key:
        """Creates the first version of a new key if it does not exist. If it already exists, then the
        existing key is returned without any write operations being performed. This API does not create
        subsequent versions, and does not update existing keys.

        :param resource_group_name: The name of the resource group which contains the specified key
         vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault which contains the key to be created. Required.
        :type vault_name: str
        :param key_name: The name of the key to be created. The value you provide may be copied
         globally for the purpose of running the service. The value provided should not include
         personally identifiable or sensitive information. Required.
        :type key_name: str
        :param parameters: The parameters used to create the specified key. Is either a
         KeyCreateParameters type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.keyvault.v2021_10_01.models.KeyCreateParameters or IO[bytes]
        :return: Key or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_10_01.models.Key
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-10-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Key] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "KeyCreateParameters")

        _request = build_create_if_not_exist_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            key_name=key_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Key", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get(self, resource_group_name: str, vault_name: str, key_name: str, **kwargs: Any) -> _models.Key:
        """Gets the current version of the specified key from the specified key vault.

        :param resource_group_name: The name of the resource group which contains the specified key
         vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the vault which contains the key to be retrieved. Required.
        :type vault_name: str
        :param key_name: The name of the key to be retrieved. Required.
        :type key_name: str
        :return: Key or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_10_01.models.Key
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-10-01"))
        cls: ClsType[_models.Key] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            key_name=key_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Key", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(self, resource_group_name: str, vault_name: str, **kwargs: Any) -> Iterable["_models.Key"]:
        """Lists the keys in the specified key vault.

        :param resource_group_name: The name of the resource group which contains the specified key
         vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the vault which contains the keys to be retrieved. Required.
        :type vault_name: str
        :return: An iterator like instance of either Key or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.keyvault.v2021_10_01.models.Key]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-10-01"))
        cls: ClsType[_models.KeyListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    resource_group_name=resource_group_name,
                    vault_name=vault_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("KeyListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def get_version(
        self, resource_group_name: str, vault_name: str, key_name: str, key_version: str, **kwargs: Any
    ) -> _models.Key:
        """Gets the specified version of the specified key in the specified key vault.

        :param resource_group_name: The name of the resource group which contains the specified key
         vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the vault which contains the key version to be retrieved.
         Required.
        :type vault_name: str
        :param key_name: The name of the key version to be retrieved. Required.
        :type key_name: str
        :param key_version: The version of the key to be retrieved. Required.
        :type key_version: str
        :return: Key or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_10_01.models.Key
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-10-01"))
        cls: ClsType[_models.Key] = kwargs.pop("cls", None)

        _request = build_get_version_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            key_name=key_name,
            key_version=key_version,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Key", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list_versions(
        self, resource_group_name: str, vault_name: str, key_name: str, **kwargs: Any
    ) -> Iterable["_models.Key"]:
        """Lists the versions of the specified key in the specified key vault.

        :param resource_group_name: The name of the resource group which contains the specified key
         vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the vault which contains the key versions to be retrieved.
         Required.
        :type vault_name: str
        :param key_name: The name of the key versions to be retrieved. Required.
        :type key_name: str
        :return: An iterator like instance of either Key or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.keyvault.v2021_10_01.models.Key]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-10-01"))
        cls: ClsType[_models.KeyListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_versions_request(
                    resource_group_name=resource_group_name,
                    vault_name=vault_name,
                    key_name=key_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("KeyListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
