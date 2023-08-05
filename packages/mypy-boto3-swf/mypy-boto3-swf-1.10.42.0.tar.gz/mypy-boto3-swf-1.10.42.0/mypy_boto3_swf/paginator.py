"Main interface for swf service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_swf.type_defs import (
    ActivityTypeInfosTypeDef,
    CloseStatusFilterTypeDef,
    DecisionTaskTypeDef,
    DomainInfosTypeDef,
    ExecutionTimeFilterTypeDef,
    HistoryTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
    TaskListTypeDef,
    WorkflowExecutionFilterTypeDef,
    WorkflowExecutionInfosTypeDef,
    WorkflowExecutionTypeDef,
    WorkflowTypeFilterTypeDef,
    WorkflowTypeInfosTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetWorkflowExecutionHistoryPaginator",
    "ListActivityTypesPaginator",
    "ListClosedWorkflowExecutionsPaginator",
    "ListDomainsPaginator",
    "ListOpenWorkflowExecutionsPaginator",
    "ListWorkflowTypesPaginator",
    "PollForDecisionTaskPaginator",
)


class GetWorkflowExecutionHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetWorkflowExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        execution: WorkflowExecutionTypeDef,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[HistoryTypeDef, None, None]:
        """
        [GetWorkflowExecutionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory.paginate)
        """


class ListActivityTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListActivityTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListActivityTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ActivityTypeInfosTypeDef, None, None]:
        """
        [ListActivityTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListActivityTypes.paginate)
        """


class ListClosedWorkflowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListClosedWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef = None,
        closeTimeFilter: ExecutionTimeFilterTypeDef = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        closeStatusFilter: CloseStatusFilterTypeDef = None,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[WorkflowExecutionInfosTypeDef, None, None]:
        """
        [ListClosedWorkflowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions.paginate)
        """


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListDomains)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DomainInfosTypeDef, None, None]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListDomains.paginate)
        """


class ListOpenWorkflowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListOpenWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        reverseOrder: bool = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[WorkflowExecutionInfosTypeDef, None, None]:
        """
        [ListOpenWorkflowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions.paginate)
        """


class ListWorkflowTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkflowTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[WorkflowTypeInfosTypeDef, None, None]:
        """
        [ListWorkflowTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes.paginate)
        """


class PollForDecisionTaskPaginator(Boto3Paginator):
    """
    [Paginator.PollForDecisionTask documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        taskList: TaskListTypeDef,
        identity: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DecisionTaskTypeDef, None, None]:
        """
        [PollForDecisionTask.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/swf.html#SWF.Paginator.PollForDecisionTask.paginate)
        """
