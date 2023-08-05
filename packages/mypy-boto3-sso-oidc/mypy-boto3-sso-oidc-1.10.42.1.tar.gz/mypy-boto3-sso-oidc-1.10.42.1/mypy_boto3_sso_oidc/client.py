"Main interface for sso-oidc service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sso_oidc.client as client_scope
from mypy_boto3_sso_oidc.type_defs import (
    CreateTokenResponseTypeDef,
    RegisterClientResponseTypeDef,
    StartDeviceAuthorizationResponseTypeDef,
)


__all__ = ("SSOOIDCClient",)


class SSOOIDCClient(BaseClient):
    """
    [SSOOIDC.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sso-oidc.html#SSOOIDC.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sso-oidc.html#SSOOIDC.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_token(
        self,
        clientId: str,
        clientSecret: str,
        grantType: str,
        deviceCode: str,
        code: str = None,
        refreshToken: str = None,
        scope: List[str] = None,
        redirectUri: str = None,
    ) -> CreateTokenResponseTypeDef:
        """
        [Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sso-oidc.html#SSOOIDC.Client.create_token)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sso-oidc.html#SSOOIDC.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_client(
        self, clientName: str, clientType: str, scopes: List[str] = None
    ) -> RegisterClientResponseTypeDef:
        """
        [Client.register_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sso-oidc.html#SSOOIDC.Client.register_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_device_authorization(
        self, clientId: str, clientSecret: str, startUrl: str
    ) -> StartDeviceAuthorizationResponseTypeDef:
        """
        [Client.start_device_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sso-oidc.html#SSOOIDC.Client.start_device_authorization)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AuthorizationPendingException: Boto3ClientError
    ClientError: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidClientException: Boto3ClientError
    InvalidClientMetadataException: Boto3ClientError
    InvalidGrantException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidScopeException: Boto3ClientError
    SlowDownException: Boto3ClientError
    UnauthorizedClientException: Boto3ClientError
    UnsupportedGrantTypeException: Boto3ClientError
