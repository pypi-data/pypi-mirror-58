"Main interface for stepfunctions service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_stepfunctions.type_defs import (
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListStateMachinesPaginator",
)


class GetExecutionHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        executionArn: str,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetExecutionHistoryOutputTypeDef, None, None]:
        """
        [GetExecutionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory.paginate)
        """


class ListActivitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListActivitiesOutputTypeDef, None, None]:
        """
        [ListActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.ListActivities.paginate)
        """


class ListExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListExecutionsOutputTypeDef, None, None]:
        """
        [ListExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions.paginate)
        """


class ListStateMachinesPaginator(Boto3Paginator):
    """
    [Paginator.ListStateMachines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStateMachinesOutputTypeDef, None, None]:
        """
        [ListStateMachines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines.paginate)
        """
