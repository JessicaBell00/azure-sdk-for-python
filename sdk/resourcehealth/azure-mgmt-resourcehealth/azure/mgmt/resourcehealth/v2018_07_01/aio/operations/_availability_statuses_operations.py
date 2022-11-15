# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._availability_statuses_operations import (
    build_get_by_resource_request,
    build_list_by_resource_group_request,
    build_list_by_subscription_id_request,
    build_list_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AvailabilityStatusesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.resourcehealth.v2018_07_01.aio.MicrosoftResourceHealth`'s
        :attr:`availability_statuses` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_subscription_id(
        self, filter: Optional[str] = None, expand: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.AvailabilityStatus"]:
        """Lists the current availability status for all the resources in the subscription.

        :param filter: A valid odata query to limit the events returned. The logical operators and, or,
         equal, not equal, and top are supported. For example, $filter=Properties/EventType eq
         'ServiceIssue' or Properties/EventType eq 'PlannedMaintenance' OR
         %24filter=Properties%2FEventType%20eq%20%27ServiceIssue%27%20or%20Properties%2FEventType%20eq%20%27PlannedMaintenance%27.
         Default value is None.
        :type filter: str
        :param expand: Setting $expand=recommendedactions in url query expands the recommendedactions
         in the response. Default value is None.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AvailabilityStatus or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resourcehealth.v2018_07_01.models.AvailabilityStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AvailabilityStatusListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_subscription_id_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    expand=expand,
                    api_version=api_version,
                    template_url=self.list_by_subscription_id.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AvailabilityStatusListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_subscription_id.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/availabilityStatuses"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, filter: Optional[str] = None, expand: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.AvailabilityStatus"]:
        """Lists the current availability status for all the resources in the resource group.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param filter: A valid odata query to limit the events returned. The logical operators and, or,
         equal, not equal, and top are supported. For example, $filter=Properties/EventType eq
         'ServiceIssue' or Properties/EventType eq 'PlannedMaintenance' OR
         %24filter=Properties%2FEventType%20eq%20%27ServiceIssue%27%20or%20Properties%2FEventType%20eq%20%27PlannedMaintenance%27.
         Default value is None.
        :type filter: str
        :param expand: Setting $expand=recommendedactions in url query expands the recommendedactions
         in the response. Default value is None.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AvailabilityStatus or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resourcehealth.v2018_07_01.models.AvailabilityStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AvailabilityStatusListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    expand=expand,
                    api_version=api_version,
                    template_url=self.list_by_resource_group.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AvailabilityStatusListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ResourceHealth/availabilityStatuses"}  # type: ignore

    @distributed_trace_async
    async def get_by_resource(
        self, resource_uri: str, filter: Optional[str] = None, expand: Optional[str] = None, **kwargs: Any
    ) -> _models.AvailabilityStatus:
        """Gets current availability status for a single resource.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Currently the API support not nested and one nesting level resource types :
         /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name}
         and
         /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}.
         Required.
        :type resource_uri: str
        :param filter: A valid odata query to limit the events returned. The logical operators and, or,
         equal, not equal, and top are supported. For example, $filter=Properties/EventType eq
         'ServiceIssue' or Properties/EventType eq 'PlannedMaintenance' OR
         %24filter=Properties%2FEventType%20eq%20%27ServiceIssue%27%20or%20Properties%2FEventType%20eq%20%27PlannedMaintenance%27.
         Default value is None.
        :type filter: str
        :param expand: Setting $expand=recommendedactions in url query expands the recommendedactions
         in the response. Default value is None.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.resourcehealth.v2018_07_01.models.AvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AvailabilityStatus]

        request = build_get_by_resource_request(
            resource_uri=resource_uri,
            filter=filter,
            expand=expand,
            api_version=api_version,
            template_url=self.get_by_resource.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AvailabilityStatus", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_resource.metadata = {"url": "/{resourceUri}/providers/Microsoft.ResourceHealth/availabilityStatuses/current"}  # type: ignore

    @distributed_trace
    def list(
        self, resource_uri: str, filter: Optional[str] = None, expand: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.AvailabilityStatus"]:
        """Lists all historical availability transitions and impacting events for a single resource.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Currently the API support not nested and one nesting level resource types :
         /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name}
         and
         /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}.
         Required.
        :type resource_uri: str
        :param filter: A valid odata query to limit the events returned. The logical operators and, or,
         equal, not equal, and top are supported. For example, $filter=Properties/EventType eq
         'ServiceIssue' or Properties/EventType eq 'PlannedMaintenance' OR
         %24filter=Properties%2FEventType%20eq%20%27ServiceIssue%27%20or%20Properties%2FEventType%20eq%20%27PlannedMaintenance%27.
         Default value is None.
        :type filter: str
        :param expand: Setting $expand=recommendedactions in url query expands the recommendedactions
         in the response. Default value is None.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AvailabilityStatus or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resourcehealth.v2018_07_01.models.AvailabilityStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AvailabilityStatusListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_uri=resource_uri,
                    filter=filter,
                    expand=expand,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AvailabilityStatusListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{resourceUri}/providers/Microsoft.ResourceHealth/availabilityStatuses"}  # type: ignore
