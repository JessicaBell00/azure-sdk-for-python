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
from ._configuration import KeyVaultManagementClientConfiguration
from .operations import (
    KeysOperations,
    MHSMPrivateEndpointConnectionsOperations,
    MHSMPrivateLinkResourcesOperations,
    MHSMRegionsOperations,
    ManagedHsmKeysOperations,
    ManagedHsmsOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    SecretsOperations,
    VaultsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class KeyVaultManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Azure management API provides a RESTful set of web services that interact with Azure Key
    Vault.

    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.keyvault.v2023_07_01.aio.operations.KeysOperations
    :ivar managed_hsm_keys: ManagedHsmKeysOperations operations
    :vartype managed_hsm_keys:
     azure.mgmt.keyvault.v2023_07_01.aio.operations.ManagedHsmKeysOperations
    :ivar vaults: VaultsOperations operations
    :vartype vaults: azure.mgmt.keyvault.v2023_07_01.aio.operations.VaultsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.keyvault.v2023_07_01.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.keyvault.v2023_07_01.aio.operations.PrivateLinkResourcesOperations
    :ivar managed_hsms: ManagedHsmsOperations operations
    :vartype managed_hsms: azure.mgmt.keyvault.v2023_07_01.aio.operations.ManagedHsmsOperations
    :ivar mhsm_private_endpoint_connections: MHSMPrivateEndpointConnectionsOperations operations
    :vartype mhsm_private_endpoint_connections:
     azure.mgmt.keyvault.v2023_07_01.aio.operations.MHSMPrivateEndpointConnectionsOperations
    :ivar mhsm_private_link_resources: MHSMPrivateLinkResourcesOperations operations
    :vartype mhsm_private_link_resources:
     azure.mgmt.keyvault.v2023_07_01.aio.operations.MHSMPrivateLinkResourcesOperations
    :ivar mhsm_regions: MHSMRegionsOperations operations
    :vartype mhsm_regions: azure.mgmt.keyvault.v2023_07_01.aio.operations.MHSMRegionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.keyvault.v2023_07_01.aio.operations.Operations
    :ivar secrets: SecretsOperations operations
    :vartype secrets: azure.mgmt.keyvault.v2023_07_01.aio.operations.SecretsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-07-01". Note that overriding this
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
        self._config = KeyVaultManagementClientConfiguration(
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
        self.keys = KeysOperations(self._client, self._config, self._serialize, self._deserialize, "2023-07-01")
        self.managed_hsm_keys = ManagedHsmKeysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01"
        )
        self.vaults = VaultsOperations(self._client, self._config, self._serialize, self._deserialize, "2023-07-01")
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01"
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01"
        )
        self.managed_hsms = ManagedHsmsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01"
        )
        self.mhsm_private_endpoint_connections = MHSMPrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01"
        )
        self.mhsm_private_link_resources = MHSMPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01"
        )
        self.mhsm_regions = MHSMRegionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01"
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize, "2023-07-01")
        self.secrets = SecretsOperations(self._client, self._config, self._serialize, self._deserialize, "2023-07-01")

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
