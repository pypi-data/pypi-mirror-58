"Main interface for cognito-identity service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_cognito_identity.client as client_scope

# pylint: disable=import-self
import mypy_boto3_cognito_identity.paginator as paginator_scope
from mypy_boto3_cognito_identity.type_defs import (
    CognitoIdentityProviderTypeDef,
    DeleteIdentitiesResponseTypeDef,
    GetCredentialsForIdentityResponseTypeDef,
    GetIdResponseTypeDef,
    GetIdentityPoolRolesResponseTypeDef,
    GetOpenIdTokenForDeveloperIdentityResponseTypeDef,
    GetOpenIdTokenResponseTypeDef,
    IdentityDescriptionTypeDef,
    IdentityPoolTypeDef,
    ListIdentitiesResponseTypeDef,
    ListIdentityPoolsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LookupDeveloperIdentityResponseTypeDef,
    MergeDeveloperIdentitiesResponseTypeDef,
    RoleMappingTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CognitoIdentityClient",)


class CognitoIdentityClient(BaseClient):
    """
    [CognitoIdentity.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_identity_pool(
        self,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        AllowClassicFlow: bool = None,
        SupportedLoginProviders: Dict[str, str] = None,
        DeveloperProviderName: str = None,
        OpenIdConnectProviderARNs: List[str] = None,
        CognitoIdentityProviders: List[CognitoIdentityProviderTypeDef] = None,
        SamlProviderARNs: List[str] = None,
        IdentityPoolTags: Dict[str, str] = None,
    ) -> IdentityPoolTypeDef:
        """
        [Client.create_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.create_identity_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_identities(self, IdentityIdsToDelete: List[str]) -> DeleteIdentitiesResponseTypeDef:
        """
        [Client.delete_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_identity_pool(self, IdentityPoolId: str) -> None:
        """
        [Client.delete_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identity_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity(self, IdentityId: str) -> IdentityDescriptionTypeDef:
        """
        [Client.describe_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity_pool(self, IdentityPoolId: str) -> IdentityPoolTypeDef:
        """
        [Client.describe_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity_pool)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_credentials_for_identity(
        self, IdentityId: str, Logins: Dict[str, str] = None, CustomRoleArn: str = None
    ) -> GetCredentialsForIdentityResponseTypeDef:
        """
        [Client.get_credentials_for_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.get_credentials_for_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_id(
        self, IdentityPoolId: str, AccountId: str = None, Logins: Dict[str, str] = None
    ) -> GetIdResponseTypeDef:
        """
        [Client.get_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.get_id)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_pool_roles(self, IdentityPoolId: str) -> GetIdentityPoolRolesResponseTypeDef:
        """
        [Client.get_identity_pool_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.get_identity_pool_roles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_open_id_token(
        self, IdentityId: str, Logins: Dict[str, str] = None
    ) -> GetOpenIdTokenResponseTypeDef:
        """
        [Client.get_open_id_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_open_id_token_for_developer_identity(
        self,
        IdentityPoolId: str,
        Logins: Dict[str, str],
        IdentityId: str = None,
        TokenDuration: int = None,
    ) -> GetOpenIdTokenForDeveloperIdentityResponseTypeDef:
        """
        [Client.get_open_id_token_for_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token_for_developer_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_identities(
        self, IdentityPoolId: str, MaxResults: int, NextToken: str = None, HideDisabled: bool = None
    ) -> ListIdentitiesResponseTypeDef:
        """
        [Client.list_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_identity_pools(
        self, MaxResults: int, NextToken: str = None
    ) -> ListIdentityPoolsResponseTypeDef:
        """
        [Client.list_identity_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identity_pools)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def lookup_developer_identity(
        self,
        IdentityPoolId: str,
        IdentityId: str = None,
        DeveloperUserIdentifier: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> LookupDeveloperIdentityResponseTypeDef:
        """
        [Client.lookup_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.lookup_developer_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_developer_identities(
        self,
        SourceUserIdentifier: str,
        DestinationUserIdentifier: str,
        DeveloperProviderName: str,
        IdentityPoolId: str,
    ) -> MergeDeveloperIdentitiesResponseTypeDef:
        """
        [Client.merge_developer_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.merge_developer_identities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_identity_pool_roles(
        self,
        IdentityPoolId: str,
        Roles: Dict[str, str],
        RoleMappings: Dict[str, RoleMappingTypeDef] = None,
    ) -> None:
        """
        [Client.set_identity_pool_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.set_identity_pool_roles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unlink_developer_identity(
        self,
        IdentityId: str,
        IdentityPoolId: str,
        DeveloperProviderName: str,
        DeveloperUserIdentifier: str,
    ) -> None:
        """
        [Client.unlink_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_developer_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unlink_identity(
        self, IdentityId: str, Logins: Dict[str, str], LoginsToRemove: List[str]
    ) -> None:
        """
        [Client.unlink_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_identity_pool(
        self,
        IdentityPoolId: str,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        AllowClassicFlow: bool = None,
        SupportedLoginProviders: Dict[str, str] = None,
        DeveloperProviderName: str = None,
        OpenIdConnectProviderARNs: List[str] = None,
        CognitoIdentityProviders: List[CognitoIdentityProviderTypeDef] = None,
        SamlProviderARNs: List[str] = None,
        IdentityPoolTags: Dict[str, str] = None,
    ) -> IdentityPoolTypeDef:
        """
        [Client.update_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Client.update_identity_pool)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_identity_pools"]
    ) -> paginator_scope.ListIdentityPoolsPaginator:
        """
        [Paginator.ListIdentityPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DeveloperUserAlreadyRegisteredException: Boto3ClientError
    ExternalServiceException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidIdentityPoolConfigurationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
