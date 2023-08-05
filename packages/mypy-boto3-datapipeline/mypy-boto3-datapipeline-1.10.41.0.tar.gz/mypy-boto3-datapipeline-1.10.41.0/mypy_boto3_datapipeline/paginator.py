"Main interface for datapipeline service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_datapipeline.type_defs import (
    DescribeObjectsOutputTypeDef,
    ListPipelinesOutputTypeDef,
    PaginatorConfigTypeDef,
    QueryObjectsOutputTypeDef,
    QueryTypeDef,
)


__all__ = ("DescribeObjectsPaginator", "ListPipelinesPaginator", "QueryObjectsPaginator")


class DescribeObjectsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineId: str,
        objectIds: List[str],
        evaluateExpressions: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeObjectsOutputTypeDef, None, None]:
        """
        [DescribeObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPipelinesOutputTypeDef, None, None]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines.paginate)
        """


class QueryObjectsPaginator(Boto3Paginator):
    """
    [Paginator.QueryObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineId: str,
        sphere: str,
        query: QueryTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[QueryObjectsOutputTypeDef, None, None]:
        """
        [QueryObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects.paginate)
        """
