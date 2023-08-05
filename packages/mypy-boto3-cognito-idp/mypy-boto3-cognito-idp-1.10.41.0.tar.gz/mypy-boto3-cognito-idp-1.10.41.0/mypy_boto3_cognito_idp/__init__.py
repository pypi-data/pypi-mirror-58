"Main interface for cognito-idp service"
from mypy_boto3_cognito_idp.client import (
    CognitoIdentityProviderClient,
    CognitoIdentityProviderClient as Client,
)
from mypy_boto3_cognito_idp.paginator import (
    AdminListGroupsForUserPaginator,
    AdminListUserAuthEventsPaginator,
    ListGroupsPaginator,
    ListIdentityProvidersPaginator,
    ListResourceServersPaginator,
    ListUserPoolClientsPaginator,
    ListUserPoolsPaginator,
    ListUsersInGroupPaginator,
    ListUsersPaginator,
)


__all__ = (
    "AdminListGroupsForUserPaginator",
    "AdminListUserAuthEventsPaginator",
    "Client",
    "CognitoIdentityProviderClient",
    "ListGroupsPaginator",
    "ListIdentityProvidersPaginator",
    "ListResourceServersPaginator",
    "ListUserPoolClientsPaginator",
    "ListUserPoolsPaginator",
    "ListUsersInGroupPaginator",
    "ListUsersPaginator",
)
