"Main interface for batch service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_batch.type_defs import (
    DescribeComputeEnvironmentsResponseTypeDef,
    DescribeJobDefinitionsResponseTypeDef,
    DescribeJobQueuesResponseTypeDef,
    ListJobsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeComputeEnvironmentsPaginator",
    "DescribeJobDefinitionsPaginator",
    "DescribeJobQueuesPaginator",
    "ListJobsPaginator",
)


class DescribeComputeEnvironmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeComputeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, computeEnvironments: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeComputeEnvironmentsResponseTypeDef, None, None]:
        """
        [DescribeComputeEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments.paginate)
        """


class DescribeJobDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        jobDefinitions: List[str] = None,
        jobDefinitionName: str = None,
        status: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeJobDefinitionsResponseTypeDef, None, None]:
        """
        [DescribeJobDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions.paginate)
        """


class DescribeJobQueuesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeJobQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, jobQueues: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeJobQueuesResponseTypeDef, None, None]:
        """
        [DescribeJobQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.DescribeJobQueues.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsResponseTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/batch.html#Batch.Paginator.ListJobs.paginate)
        """
