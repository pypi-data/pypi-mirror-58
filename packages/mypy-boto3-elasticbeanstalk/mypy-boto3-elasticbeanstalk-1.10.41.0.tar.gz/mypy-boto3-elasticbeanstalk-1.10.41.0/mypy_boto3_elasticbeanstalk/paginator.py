"Main interface for elasticbeanstalk service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elasticbeanstalk.type_defs import (
    ApplicationVersionDescriptionsMessageTypeDef,
    DescribeEnvironmentManagedActionHistoryResultTypeDef,
    EnvironmentDescriptionsMessageTypeDef,
    EventDescriptionsMessageTypeDef,
    ListPlatformVersionsResultTypeDef,
    PaginatorConfigTypeDef,
    PlatformFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ListPlatformVersionsPaginator",
)


class DescribeApplicationVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabels: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ApplicationVersionDescriptionsMessageTypeDef, None, None]:
        """
        [DescribeApplicationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions.paginate)
        """


class DescribeEnvironmentManagedActionHistoryPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEnvironmentManagedActionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEnvironmentManagedActionHistoryResultTypeDef, None, None]:
        """
        [DescribeEnvironmentManagedActionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory.paginate)
        """


class DescribeEnvironmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[EnvironmentDescriptionsMessageTypeDef, None, None]:
        """
        [DescribeEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[EventDescriptionsMessageTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents.paginate)
        """


class ListPlatformVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlatformVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[PlatformFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPlatformVersionsResultTypeDef, None, None]:
        """
        [ListPlatformVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions.paginate)
        """
