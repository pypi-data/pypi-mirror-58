"Main interface for batch service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_batch.client as client_scope

# pylint: disable=import-self
import mypy_boto3_batch.paginator as paginator_scope
from mypy_boto3_batch.type_defs import (
    ArrayPropertiesTypeDef,
    ComputeEnvironmentOrderTypeDef,
    ComputeResourceTypeDef,
    ComputeResourceUpdateTypeDef,
    ContainerOverridesTypeDef,
    ContainerPropertiesTypeDef,
    CreateComputeEnvironmentResponseTypeDef,
    CreateJobQueueResponseTypeDef,
    DescribeComputeEnvironmentsResponseTypeDef,
    DescribeJobDefinitionsResponseTypeDef,
    DescribeJobQueuesResponseTypeDef,
    DescribeJobsResponseTypeDef,
    JobDependencyTypeDef,
    JobTimeoutTypeDef,
    ListJobsResponseTypeDef,
    NodeOverridesTypeDef,
    NodePropertiesTypeDef,
    RegisterJobDefinitionResponseTypeDef,
    RetryStrategyTypeDef,
    SubmitJobResponseTypeDef,
    UpdateComputeEnvironmentResponseTypeDef,
    UpdateJobQueueResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BatchClient",)


class BatchClient(BaseClient):
    """
    [Batch.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.cancel_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_compute_environment(
        self,
        computeEnvironmentName: str,
        type: Literal["MANAGED", "UNMANAGED"],
        serviceRole: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        computeResources: ComputeResourceTypeDef = None,
    ) -> CreateComputeEnvironmentResponseTypeDef:
        """
        [Client.create_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.create_compute_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job_queue(
        self,
        jobQueueName: str,
        priority: int,
        computeEnvironmentOrder: List[ComputeEnvironmentOrderTypeDef],
        state: Literal["ENABLED", "DISABLED"] = None,
    ) -> CreateJobQueueResponseTypeDef:
        """
        [Client.create_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.create_job_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_compute_environment(self, computeEnvironment: str) -> Dict[str, Any]:
        """
        [Client.delete_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.delete_compute_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job_queue(self, jobQueue: str) -> Dict[str, Any]:
        """
        [Client.delete_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.delete_job_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_job_definition(self, jobDefinition: str) -> Dict[str, Any]:
        """
        [Client.deregister_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.deregister_job_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_compute_environments(
        self, computeEnvironments: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeComputeEnvironmentsResponseTypeDef:
        """
        [Client.describe_compute_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.describe_compute_environments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job_definitions(
        self,
        jobDefinitions: List[str] = None,
        maxResults: int = None,
        jobDefinitionName: str = None,
        status: str = None,
        nextToken: str = None,
    ) -> DescribeJobDefinitionsResponseTypeDef:
        """
        [Client.describe_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.describe_job_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job_queues(
        self, jobQueues: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeJobQueuesResponseTypeDef:
        """
        [Client.describe_job_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.describe_job_queues)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_jobs(self, jobs: List[str]) -> DescribeJobsResponseTypeDef:
        """
        [Client.describe_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.describe_jobs)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_job_definition(
        self,
        jobDefinitionName: str,
        type: Literal["container", "multinode"],
        parameters: Dict[str, str] = None,
        containerProperties: ContainerPropertiesTypeDef = None,
        nodeProperties: NodePropertiesTypeDef = None,
        retryStrategy: RetryStrategyTypeDef = None,
        timeout: JobTimeoutTypeDef = None,
    ) -> RegisterJobDefinitionResponseTypeDef:
        """
        [Client.register_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.register_job_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def submit_job(
        self,
        jobName: str,
        jobQueue: str,
        jobDefinition: str,
        arrayProperties: ArrayPropertiesTypeDef = None,
        dependsOn: List[JobDependencyTypeDef] = None,
        parameters: Dict[str, str] = None,
        containerOverrides: ContainerOverridesTypeDef = None,
        nodeOverrides: NodeOverridesTypeDef = None,
        retryStrategy: RetryStrategyTypeDef = None,
        timeout: JobTimeoutTypeDef = None,
    ) -> SubmitJobResponseTypeDef:
        """
        [Client.submit_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.submit_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        """
        [Client.terminate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.terminate_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_compute_environment(
        self,
        computeEnvironment: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        computeResources: ComputeResourceUpdateTypeDef = None,
        serviceRole: str = None,
    ) -> UpdateComputeEnvironmentResponseTypeDef:
        """
        [Client.update_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.update_compute_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job_queue(
        self,
        jobQueue: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        priority: int = None,
        computeEnvironmentOrder: List[ComputeEnvironmentOrderTypeDef] = None,
    ) -> UpdateJobQueueResponseTypeDef:
        """
        [Client.update_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Client.update_job_queue)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_compute_environments"]
    ) -> paginator_scope.DescribeComputeEnvironmentsPaginator:
        """
        [Paginator.DescribeComputeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_job_definitions"]
    ) -> paginator_scope.DescribeJobDefinitionsPaginator:
        """
        [Paginator.DescribeJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_job_queues"]
    ) -> paginator_scope.DescribeJobQueuesPaginator:
        """
        [Paginator.DescribeJobQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/batch.html#Batch.Paginator.ListJobs)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    ServerException: Boto3ClientError
