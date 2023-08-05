"Main interface for cognito-identity service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cognito_identity.type_defs import (
    ListIdentityPoolsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListIdentityPoolsPaginator",)


class ListIdentityPoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListIdentityPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListIdentityPoolsResponseTypeDef, None, None]:
        """
        [ListIdentityPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools.paginate)
        """
