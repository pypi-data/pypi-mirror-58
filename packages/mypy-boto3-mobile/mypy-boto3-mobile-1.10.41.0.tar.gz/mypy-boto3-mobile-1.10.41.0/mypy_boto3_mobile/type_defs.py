"Main interface for mobile service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)

ProjectDetailsTypeDef = TypedDict(
    "ProjectDetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": Literal["NORMAL", "SYNCING", "IMPORTING"],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List[ResourceTypeDef],
    },
    total=False,
)

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef", {"details": ProjectDetailsTypeDef}, total=False
)

DeleteProjectResultTypeDef = TypedDict(
    "DeleteProjectResultTypeDef",
    {"deletedResources": List[ResourceTypeDef], "orphanedResources": List[ResourceTypeDef]},
    total=False,
)

BundleDetailsTypeDef = TypedDict(
    "BundleDetailsTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[
            Literal["OSX", "WINDOWS", "LINUX", "OBJC", "SWIFT", "ANDROID", "JAVASCRIPT"]
        ],
    },
    total=False,
)

DescribeBundleResultTypeDef = TypedDict(
    "DescribeBundleResultTypeDef", {"details": BundleDetailsTypeDef}, total=False
)

DescribeProjectResultTypeDef = TypedDict(
    "DescribeProjectResultTypeDef", {"details": ProjectDetailsTypeDef}, total=False
)

ExportBundleResultTypeDef = TypedDict(
    "ExportBundleResultTypeDef", {"downloadUrl": str}, total=False
)

ExportProjectResultTypeDef = TypedDict(
    "ExportProjectResultTypeDef",
    {"downloadUrl": str, "shareUrl": str, "snapshotId": str},
    total=False,
)

ListBundlesResultTypeDef = TypedDict(
    "ListBundlesResultTypeDef",
    {"bundleList": List[BundleDetailsTypeDef], "nextToken": str},
    total=False,
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef", {"name": str, "projectId": str}, total=False
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {"projects": List[ProjectSummaryTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef", {"details": ProjectDetailsTypeDef}, total=False
)
