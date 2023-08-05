"Main interface for sts service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sts.client as client_scope
from mypy_boto3_sts.type_defs import (
    AssumeRoleResponseTypeDef,
    AssumeRoleWithSAMLResponseTypeDef,
    AssumeRoleWithWebIdentityResponseTypeDef,
    DecodeAuthorizationMessageResponseTypeDef,
    GetAccessKeyInfoResponseTypeDef,
    GetCallerIdentityResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetSessionTokenResponseTypeDef,
    PolicyDescriptorTypeTypeDef,
    TagTypeDef,
)


__all__ = ("STSClient",)


class STSClient(BaseClient):
    """
    [STS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
        Tags: List[TagTypeDef] = None,
        TransitiveTagKeys: List[str] = None,
        ExternalId: str = None,
        SerialNumber: str = None,
        TokenCode: str = None,
    ) -> AssumeRoleResponseTypeDef:
        """
        [Client.assume_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.assume_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assume_role_with_saml(
        self,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> AssumeRoleWithSAMLResponseTypeDef:
        """
        [Client.assume_role_with_saml documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.assume_role_with_saml)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assume_role_with_web_identity(
        self,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str = None,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> AssumeRoleWithWebIdentityResponseTypeDef:
        """
        [Client.assume_role_with_web_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.assume_role_with_web_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decode_authorization_message(
        self, EncodedMessage: str
    ) -> DecodeAuthorizationMessageResponseTypeDef:
        """
        [Client.decode_authorization_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.decode_authorization_message)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_access_key_info(self, AccessKeyId: str) -> GetAccessKeyInfoResponseTypeDef:
        """
        [Client.get_access_key_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.get_access_key_info)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_caller_identity(self) -> GetCallerIdentityResponseTypeDef:
        """
        [Client.get_caller_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.get_caller_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_federation_token(
        self,
        Name: str,
        Policy: str = None,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        DurationSeconds: int = None,
        Tags: List[TagTypeDef] = None,
    ) -> GetFederationTokenResponseTypeDef:
        """
        [Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.get_federation_token)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_session_token(
        self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None
    ) -> GetSessionTokenResponseTypeDef:
        """
        [Client.get_session_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sts.html#STS.Client.get_session_token)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    IDPCommunicationErrorException: Boto3ClientError
    IDPRejectedClaimException: Boto3ClientError
    InvalidAuthorizationMessageException: Boto3ClientError
    InvalidIdentityTokenException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    PackedPolicyTooLargeException: Boto3ClientError
    RegionDisabledException: Boto3ClientError
