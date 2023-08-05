"Main interface for stepfunctions service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_stepfunctions.client as client_scope

# pylint: disable=import-self
import mypy_boto3_stepfunctions.paginator as paginator_scope
from mypy_boto3_stepfunctions.type_defs import (
    CreateActivityOutputTypeDef,
    CreateStateMachineOutputTypeDef,
    DescribeActivityOutputTypeDef,
    DescribeExecutionOutputTypeDef,
    DescribeStateMachineForExecutionOutputTypeDef,
    DescribeStateMachineOutputTypeDef,
    GetActivityTaskOutputTypeDef,
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LoggingConfigurationTypeDef,
    StartExecutionOutputTypeDef,
    StopExecutionOutputTypeDef,
    TagTypeDef,
    UpdateStateMachineOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SFNClient",)


class SFNClient(BaseClient):
    """
    [SFN.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_activity(
        self, name: str, tags: List[TagTypeDef] = None
    ) -> CreateActivityOutputTypeDef:
        """
        [Client.create_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.create_activity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_state_machine(
        self,
        name: str,
        definition: str,
        roleArn: str,
        type: Literal["STANDARD", "EXPRESS"] = None,
        loggingConfiguration: LoggingConfigurationTypeDef = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateStateMachineOutputTypeDef:
        """
        [Client.create_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.create_state_machine)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_activity(self, activityArn: str) -> Dict[str, Any]:
        """
        [Client.delete_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.delete_activity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_state_machine(self, stateMachineArn: str) -> Dict[str, Any]:
        """
        [Client.delete_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.delete_state_machine)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_activity(self, activityArn: str) -> DescribeActivityOutputTypeDef:
        """
        [Client.describe_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.describe_activity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_execution(self, executionArn: str) -> DescribeExecutionOutputTypeDef:
        """
        [Client.describe_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.describe_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_state_machine(self, stateMachineArn: str) -> DescribeStateMachineOutputTypeDef:
        """
        [Client.describe_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.describe_state_machine)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_state_machine_for_execution(
        self, executionArn: str
    ) -> DescribeStateMachineForExecutionOutputTypeDef:
        """
        [Client.describe_state_machine_for_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_for_execution)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_activity_task(
        self, activityArn: str, workerName: str = None
    ) -> GetActivityTaskOutputTypeDef:
        """
        [Client.get_activity_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.get_activity_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_execution_history(
        self,
        executionArn: str,
        maxResults: int = None,
        reverseOrder: bool = None,
        nextToken: str = None,
    ) -> GetExecutionHistoryOutputTypeDef:
        """
        [Client.get_execution_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.get_execution_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_activities(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListActivitiesOutputTypeDef:
        """
        [Client.list_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.list_activities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_executions(
        self,
        stateMachineArn: str,
        statusFilter: Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListExecutionsOutputTypeDef:
        """
        [Client.list_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.list_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_state_machines(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListStateMachinesOutputTypeDef:
        """
        [Client.list_state_machines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.list_state_machines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_task_failure(
        self, taskToken: str, error: str = None, cause: str = None
    ) -> Dict[str, Any]:
        """
        [Client.send_task_failure documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.send_task_failure)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_task_heartbeat(self, taskToken: str) -> Dict[str, Any]:
        """
        [Client.send_task_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.send_task_heartbeat)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_task_success(self, taskToken: str, output: str) -> Dict[str, Any]:
        """
        [Client.send_task_success documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.send_task_success)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_execution(
        self, stateMachineArn: str, name: str = None, input: str = None
    ) -> StartExecutionOutputTypeDef:
        """
        [Client.start_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.start_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_execution(
        self, executionArn: str, error: str = None, cause: str = None
    ) -> StopExecutionOutputTypeDef:
        """
        [Client.stop_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.stop_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_state_machine(
        self,
        stateMachineArn: str,
        definition: str = None,
        roleArn: str = None,
        loggingConfiguration: LoggingConfigurationTypeDef = None,
    ) -> UpdateStateMachineOutputTypeDef:
        """
        [Client.update_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Client.update_state_machine)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_execution_history"]
    ) -> paginator_scope.GetExecutionHistoryPaginator:
        """
        [Paginator.GetExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_activities"]
    ) -> paginator_scope.ListActivitiesPaginator:
        """
        [Paginator.ListActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_executions"]
    ) -> paginator_scope.ListExecutionsPaginator:
        """
        [Paginator.ListExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_state_machines"]
    ) -> paginator_scope.ListStateMachinesPaginator:
        """
        [Paginator.ListStateMachines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
        """


class Exceptions:
    ActivityDoesNotExist: Boto3ClientError
    ActivityLimitExceeded: Boto3ClientError
    ActivityWorkerLimitExceeded: Boto3ClientError
    ClientError: Boto3ClientError
    ExecutionAlreadyExists: Boto3ClientError
    ExecutionDoesNotExist: Boto3ClientError
    ExecutionLimitExceeded: Boto3ClientError
    InvalidArn: Boto3ClientError
    InvalidDefinition: Boto3ClientError
    InvalidExecutionInput: Boto3ClientError
    InvalidLoggingConfiguration: Boto3ClientError
    InvalidName: Boto3ClientError
    InvalidOutput: Boto3ClientError
    InvalidToken: Boto3ClientError
    MissingRequiredParameter: Boto3ClientError
    ResourceNotFound: Boto3ClientError
    StateMachineAlreadyExists: Boto3ClientError
    StateMachineDeleting: Boto3ClientError
    StateMachineDoesNotExist: Boto3ClientError
    StateMachineLimitExceeded: Boto3ClientError
    StateMachineTypeNotSupported: Boto3ClientError
    TaskDoesNotExist: Boto3ClientError
    TaskTimedOut: Boto3ClientError
    TooManyTags: Boto3ClientError
