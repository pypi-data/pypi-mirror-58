"Main interface for iot-jobs-data service Client"
from __future__ import annotations

import sys
from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iot_jobs_data.client as client_scope
from mypy_boto3_iot_jobs_data.type_defs import (
    DescribeJobExecutionResponseTypeDef,
    GetPendingJobExecutionsResponseTypeDef,
    StartNextPendingJobExecutionResponseTypeDef,
    UpdateJobExecutionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTJobsDataPlaneClient",)


class IoTJobsDataPlaneClient(BaseClient):
    """
    [IoTJobsDataPlane.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job_execution(
        self,
        jobId: str,
        thingName: str,
        includeJobDocument: bool = None,
        executionNumber: int = None,
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        [Client.describe_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.describe_job_execution)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pending_job_executions(self, thingName: str) -> GetPendingJobExecutionsResponseTypeDef:
        """
        [Client.get_pending_job_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.get_pending_job_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_next_pending_job_execution(
        self, thingName: str, statusDetails: Dict[str, str] = None, stepTimeoutInMinutes: int = None
    ) -> StartNextPendingJobExecutionResponseTypeDef:
        """
        [Client.start_next_pending_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.start_next_pending_job_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job_execution(
        self,
        jobId: str,
        thingName: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        statusDetails: Dict[str, str] = None,
        stepTimeoutInMinutes: int = None,
        expectedVersion: int = None,
        includeJobExecutionState: bool = None,
        includeJobDocument: bool = None,
        executionNumber: int = None,
    ) -> UpdateJobExecutionResponseTypeDef:
        """
        [Client.update_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.update_job_execution)
        """


class Exceptions:
    CertificateValidationException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidStateTransitionException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TerminalStateException: Boto3ClientError
    ThrottlingException: Boto3ClientError
