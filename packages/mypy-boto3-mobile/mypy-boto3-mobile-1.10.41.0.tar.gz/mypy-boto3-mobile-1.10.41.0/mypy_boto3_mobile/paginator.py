"Main interface for mobile service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mobile.type_defs import (
    ListBundlesResultTypeDef,
    ListProjectsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListBundlesPaginator", "ListProjectsPaginator")


class ListBundlesPaginator(Boto3Paginator):
    """
    [Paginator.ListBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mobile.html#Mobile.Paginator.ListBundles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBundlesResultTypeDef, None, None]:
        """
        [ListBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mobile.html#Mobile.Paginator.ListBundles.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mobile.html#Mobile.Paginator.ListProjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProjectsResultTypeDef, None, None]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mobile.html#Mobile.Paginator.ListProjects.paginate)
        """
