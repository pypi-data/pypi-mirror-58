"Main interface for datapipeline service"
from mypy_boto3_datapipeline.client import DataPipelineClient as Client, DataPipelineClient
from mypy_boto3_datapipeline.paginator import (
    DescribeObjectsPaginator,
    ListPipelinesPaginator,
    QueryObjectsPaginator,
)


__all__ = (
    "Client",
    "DataPipelineClient",
    "DescribeObjectsPaginator",
    "ListPipelinesPaginator",
    "QueryObjectsPaginator",
)
