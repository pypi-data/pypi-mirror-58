"Main interface for cognito-identity service"
from mypy_boto3_cognito_identity.client import (
    CognitoIdentityClient,
    CognitoIdentityClient as Client,
)
from mypy_boto3_cognito_identity.paginator import ListIdentityPoolsPaginator


__all__ = ("Client", "CognitoIdentityClient", "ListIdentityPoolsPaginator")
