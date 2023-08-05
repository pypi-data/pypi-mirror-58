"Main interface for elasticbeanstalk service"
from mypy_boto3_elasticbeanstalk.client import (
    ElasticBeanstalkClient,
    ElasticBeanstalkClient as Client,
)
from mypy_boto3_elasticbeanstalk.paginator import (
    DescribeApplicationVersionsPaginator,
    DescribeEnvironmentManagedActionHistoryPaginator,
    DescribeEnvironmentsPaginator,
    DescribeEventsPaginator,
    ListPlatformVersionsPaginator,
)


__all__ = (
    "Client",
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ElasticBeanstalkClient",
    "ListPlatformVersionsPaginator",
)
