"Main interface for mobile service"
from mypy_boto3_mobile.client import MobileClient, MobileClient as Client
from mypy_boto3_mobile.paginator import ListBundlesPaginator, ListProjectsPaginator


__all__ = ("Client", "ListBundlesPaginator", "ListProjectsPaginator", "MobileClient")
