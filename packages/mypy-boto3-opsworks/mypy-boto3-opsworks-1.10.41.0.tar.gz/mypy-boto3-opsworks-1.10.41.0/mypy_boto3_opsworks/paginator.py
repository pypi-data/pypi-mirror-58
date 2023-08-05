"Main interface for opsworks service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_opsworks.type_defs import DescribeEcsClustersResultTypeDef, PaginatorConfigTypeDef


__all__ = ("DescribeEcsClustersPaginator",)


class DescribeEcsClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEcsClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEcsClustersResultTypeDef, None, None]:
        """
        [DescribeEcsClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters.paginate)
        """
