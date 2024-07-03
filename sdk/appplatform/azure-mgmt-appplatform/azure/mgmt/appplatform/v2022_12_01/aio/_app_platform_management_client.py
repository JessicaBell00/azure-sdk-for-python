# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING
from typing_extensions import Self

from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from azure.mgmt.core.policies import AsyncARMAutoResourceProviderRegistrationPolicy

from .. import models as _models
from ..._serialization import Deserializer, Serializer
from ._configuration import AppPlatformManagementClientConfiguration
from .operations import (
    ApiPortalCustomDomainsOperations,
    ApiPortalsOperations,
    AppsOperations,
    BindingsOperations,
    BuildServiceAgentPoolOperations,
    BuildServiceBuilderOperations,
    BuildServiceOperations,
    BuildpackBindingOperations,
    CertificatesOperations,
    ConfigServersOperations,
    ConfigurationServicesOperations,
    CustomDomainsOperations,
    DeploymentsOperations,
    GatewayCustomDomainsOperations,
    GatewayRouteConfigsOperations,
    GatewaysOperations,
    MonitoringSettingsOperations,
    Operations,
    RuntimeVersionsOperations,
    ServiceRegistriesOperations,
    ServicesOperations,
    SkusOperations,
    StoragesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AppPlatformManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """REST API for Azure Spring Apps.

    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.appplatform.v2022_12_01.aio.operations.ServicesOperations
    :ivar config_servers: ConfigServersOperations operations
    :vartype config_servers:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.ConfigServersOperations
    :ivar configuration_services: ConfigurationServicesOperations operations
    :vartype configuration_services:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.ConfigurationServicesOperations
    :ivar service_registries: ServiceRegistriesOperations operations
    :vartype service_registries:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.ServiceRegistriesOperations
    :ivar build_service: BuildServiceOperations operations
    :vartype build_service:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.BuildServiceOperations
    :ivar buildpack_binding: BuildpackBindingOperations operations
    :vartype buildpack_binding:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.BuildpackBindingOperations
    :ivar build_service_builder: BuildServiceBuilderOperations operations
    :vartype build_service_builder:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.BuildServiceBuilderOperations
    :ivar build_service_agent_pool: BuildServiceAgentPoolOperations operations
    :vartype build_service_agent_pool:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.BuildServiceAgentPoolOperations
    :ivar monitoring_settings: MonitoringSettingsOperations operations
    :vartype monitoring_settings:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.MonitoringSettingsOperations
    :ivar apps: AppsOperations operations
    :vartype apps: azure.mgmt.appplatform.v2022_12_01.aio.operations.AppsOperations
    :ivar bindings: BindingsOperations operations
    :vartype bindings: azure.mgmt.appplatform.v2022_12_01.aio.operations.BindingsOperations
    :ivar storages: StoragesOperations operations
    :vartype storages: azure.mgmt.appplatform.v2022_12_01.aio.operations.StoragesOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.appplatform.v2022_12_01.aio.operations.CertificatesOperations
    :ivar custom_domains: CustomDomainsOperations operations
    :vartype custom_domains:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.CustomDomainsOperations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments: azure.mgmt.appplatform.v2022_12_01.aio.operations.DeploymentsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.appplatform.v2022_12_01.aio.operations.Operations
    :ivar runtime_versions: RuntimeVersionsOperations operations
    :vartype runtime_versions:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.RuntimeVersionsOperations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.appplatform.v2022_12_01.aio.operations.SkusOperations
    :ivar gateways: GatewaysOperations operations
    :vartype gateways: azure.mgmt.appplatform.v2022_12_01.aio.operations.GatewaysOperations
    :ivar gateway_route_configs: GatewayRouteConfigsOperations operations
    :vartype gateway_route_configs:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.GatewayRouteConfigsOperations
    :ivar gateway_custom_domains: GatewayCustomDomainsOperations operations
    :vartype gateway_custom_domains:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.GatewayCustomDomainsOperations
    :ivar api_portals: ApiPortalsOperations operations
    :vartype api_portals: azure.mgmt.appplatform.v2022_12_01.aio.operations.ApiPortalsOperations
    :ivar api_portal_custom_domains: ApiPortalCustomDomainsOperations operations
    :vartype api_portal_custom_domains:
     azure.mgmt.appplatform.v2022_12_01.aio.operations.ApiPortalCustomDomainsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-12-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AppPlatformManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                AsyncARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.services = ServicesOperations(self._client, self._config, self._serialize, self._deserialize, "2022-12-01")
        self.config_servers = ConfigServersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.configuration_services = ConfigurationServicesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.service_registries = ServiceRegistriesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.build_service = BuildServiceOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.buildpack_binding = BuildpackBindingOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.build_service_builder = BuildServiceBuilderOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.build_service_agent_pool = BuildServiceAgentPoolOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.monitoring_settings = MonitoringSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.apps = AppsOperations(self._client, self._config, self._serialize, self._deserialize, "2022-12-01")
        self.bindings = BindingsOperations(self._client, self._config, self._serialize, self._deserialize, "2022-12-01")
        self.storages = StoragesOperations(self._client, self._config, self._serialize, self._deserialize, "2022-12-01")
        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.custom_domains = CustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.deployments = DeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize, "2022-12-01")
        self.runtime_versions = RuntimeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.skus = SkusOperations(self._client, self._config, self._serialize, self._deserialize, "2022-12-01")
        self.gateways = GatewaysOperations(self._client, self._config, self._serialize, self._deserialize, "2022-12-01")
        self.gateway_route_configs = GatewayRouteConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.gateway_custom_domains = GatewayCustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.api_portals = ApiPortalsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )
        self.api_portal_custom_domains = ApiPortalCustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2022-12-01"
        )

    def _send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
