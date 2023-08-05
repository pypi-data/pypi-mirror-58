"Main interface for dax service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dax.type_defs import (
    DescribeClustersResponseTypeDef,
    DescribeDefaultParametersResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeClustersPaginator",
    "DescribeDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeSubnetGroupsPaginator",
    "ListTagsPaginator",
)


class DescribeClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ClusterNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeClustersResponseTypeDef, None, None]:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeClusters.paginate)
        """


class DescribeDefaultParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeDefaultParametersResponseTypeDef, None, None]:
        """
        [DescribeDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceName: str = None,
        SourceType: Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventsResponseTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeEvents.paginate)
        """


class DescribeParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ParameterGroupNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeParameterGroupsResponseTypeDef, None, None]:
        """
        [DescribeParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups.paginate)
        """


class DescribeParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeParametersResponseTypeDef, None, None]:
        """
        [DescribeParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeParameters.paginate)
        """


class DescribeSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SubnetGroupNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeSubnetGroupsResponseTypeDef, None, None]:
        """
        [DescribeSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.ListTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsResponseTypeDef, None, None]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dax.html#DAX.Paginator.ListTags.paginate)
        """
