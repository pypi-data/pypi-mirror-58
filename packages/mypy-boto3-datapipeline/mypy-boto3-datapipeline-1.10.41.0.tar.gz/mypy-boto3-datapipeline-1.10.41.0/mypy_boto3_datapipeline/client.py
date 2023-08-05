"Main interface for datapipeline service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_datapipeline.client as client_scope

# pylint: disable=import-self
import mypy_boto3_datapipeline.paginator as paginator_scope
from mypy_boto3_datapipeline.type_defs import (
    CreatePipelineOutputTypeDef,
    DescribeObjectsOutputTypeDef,
    DescribePipelinesOutputTypeDef,
    EvaluateExpressionOutputTypeDef,
    FieldTypeDef,
    GetPipelineDefinitionOutputTypeDef,
    InstanceIdentityTypeDef,
    ListPipelinesOutputTypeDef,
    ParameterObjectTypeDef,
    ParameterValueTypeDef,
    PipelineObjectTypeDef,
    PollForTaskOutputTypeDef,
    PutPipelineDefinitionOutputTypeDef,
    QueryObjectsOutputTypeDef,
    QueryTypeDef,
    ReportTaskProgressOutputTypeDef,
    ReportTaskRunnerHeartbeatOutputTypeDef,
    TagTypeDef,
    ValidatePipelineDefinitionOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DataPipelineClient",)


class DataPipelineClient(BaseClient):
    """
    [DataPipeline.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate_pipeline(
        self,
        pipelineId: str,
        parameterValues: List[ParameterValueTypeDef] = None,
        startTimestamp: datetime = None,
    ) -> Dict[str, Any]:
        """
        [Client.activate_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.activate_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags(self, pipelineId: str, tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.add_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_pipeline(
        self, name: str, uniqueId: str, description: str = None, tags: List[TagTypeDef] = None
    ) -> CreatePipelineOutputTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.create_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate_pipeline(self, pipelineId: str, cancelActive: bool = None) -> Dict[str, Any]:
        """
        [Client.deactivate_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.deactivate_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_pipeline(self, pipelineId: str) -> None:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.delete_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_objects(
        self,
        pipelineId: str,
        objectIds: List[str],
        evaluateExpressions: bool = None,
        marker: str = None,
    ) -> DescribeObjectsOutputTypeDef:
        """
        [Client.describe_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.describe_objects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pipelines(self, pipelineIds: List[str]) -> DescribePipelinesOutputTypeDef:
        """
        [Client.describe_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.describe_pipelines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def evaluate_expression(
        self, pipelineId: str, objectId: str, expression: str
    ) -> EvaluateExpressionOutputTypeDef:
        """
        [Client.evaluate_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.evaluate_expression)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pipeline_definition(
        self, pipelineId: str, version: str = None
    ) -> GetPipelineDefinitionOutputTypeDef:
        """
        [Client.get_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.get_pipeline_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pipelines(self, marker: str = None) -> ListPipelinesOutputTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.list_pipelines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def poll_for_task(
        self,
        workerGroup: str,
        hostname: str = None,
        instanceIdentity: InstanceIdentityTypeDef = None,
    ) -> PollForTaskOutputTypeDef:
        """
        [Client.poll_for_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.poll_for_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List[PipelineObjectTypeDef],
        parameterObjects: List[ParameterObjectTypeDef] = None,
        parameterValues: List[ParameterValueTypeDef] = None,
    ) -> PutPipelineDefinitionOutputTypeDef:
        """
        [Client.put_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.put_pipeline_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def query_objects(
        self,
        pipelineId: str,
        sphere: str,
        query: QueryTypeDef = None,
        marker: str = None,
        limit: int = None,
    ) -> QueryObjectsOutputTypeDef:
        """
        [Client.query_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.query_objects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags(self, pipelineId: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.remove_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def report_task_progress(
        self, taskId: str, fields: List[FieldTypeDef] = None
    ) -> ReportTaskProgressOutputTypeDef:
        """
        [Client.report_task_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.report_task_progress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def report_task_runner_heartbeat(
        self, taskrunnerId: str, workerGroup: str = None, hostname: str = None
    ) -> ReportTaskRunnerHeartbeatOutputTypeDef:
        """
        [Client.report_task_runner_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.report_task_runner_heartbeat)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_status(self, pipelineId: str, objectIds: List[str], status: str) -> None:
        """
        [Client.set_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.set_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_task_status(
        self,
        taskId: str,
        taskStatus: Literal["FINISHED", "FAILED", "FALSE"],
        errorId: str = None,
        errorMessage: str = None,
        errorStackTrace: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_task_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.set_task_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def validate_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List[PipelineObjectTypeDef],
        parameterObjects: List[ParameterObjectTypeDef] = None,
        parameterValues: List[ParameterValueTypeDef] = None,
    ) -> ValidatePipelineDefinitionOutputTypeDef:
        """
        [Client.validate_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Client.validate_pipeline_definition)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_objects"]
    ) -> paginator_scope.DescribeObjectsPaginator:
        """
        [Paginator.DescribeObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_pipelines"]
    ) -> paginator_scope.ListPipelinesPaginator:
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["query_objects"]
    ) -> paginator_scope.QueryObjectsPaginator:
        """
        [Paginator.QueryObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceError: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    PipelineDeletedException: Boto3ClientError
    PipelineNotFoundException: Boto3ClientError
    TaskNotFoundException: Boto3ClientError
