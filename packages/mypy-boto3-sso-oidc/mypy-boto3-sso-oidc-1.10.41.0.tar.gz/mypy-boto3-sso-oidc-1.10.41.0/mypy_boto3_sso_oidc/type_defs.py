"Main interface for sso-oidc service type defs"
from __future__ import annotations

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {"accessToken": str, "tokenType": str, "expiresIn": int, "refreshToken": str, "idToken": str},
    total=False,
)

RegisterClientResponseTypeDef = TypedDict(
    "RegisterClientResponseTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "clientIdIssuedAt": int,
        "clientSecretExpiresAt": int,
        "authorizationEndpoint": str,
        "tokenEndpoint": str,
    },
    total=False,
)

StartDeviceAuthorizationResponseTypeDef = TypedDict(
    "StartDeviceAuthorizationResponseTypeDef",
    {
        "deviceCode": str,
        "userCode": str,
        "verificationUri": str,
        "verificationUriComplete": str,
        "expiresIn": int,
        "interval": int,
    },
    total=False,
)
