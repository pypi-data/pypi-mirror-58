"Main interface for cloudformation service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudformation.type_defs import (
    DescribeAccountLimitsOutputTypeDef,
    DescribeChangeSetOutputTypeDef,
    DescribeStackEventsOutputTypeDef,
    DescribeStacksOutputTypeDef,
    ListChangeSetsOutputTypeDef,
    ListExportsOutputTypeDef,
    ListImportsOutputTypeDef,
    ListStackInstancesOutputTypeDef,
    ListStackResourcesOutputTypeDef,
    ListStackSetOperationResultsOutputTypeDef,
    ListStackSetOperationsOutputTypeDef,
    ListStackSetsOutputTypeDef,
    ListStacksOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeChangeSetPaginator",
    "DescribeStackEventsPaginator",
    "DescribeStacksPaginator",
    "ListChangeSetsPaginator",
    "ListExportsPaginator",
    "ListImportsPaginator",
    "ListStackInstancesPaginator",
    "ListStackResourcesPaginator",
    "ListStackSetOperationResultsPaginator",
    "ListStackSetOperationsPaginator",
    "ListStackSetsPaginator",
    "ListStacksPaginator",
)


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAccountLimitsOutputTypeDef, None, None]:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeChangeSetPaginator(Boto3Paginator):
    """
    [Paginator.DescribeChangeSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChangeSetName: str,
        StackName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeChangeSetOutputTypeDef, None, None]:
        """
        [DescribeChangeSet.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet.paginate)
        """


class DescribeStackEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStackEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeStackEventsOutputTypeDef, None, None]:
        """
        [DescribeStackEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents.paginate)
        """


class DescribeStacksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeStacksOutputTypeDef, None, None]:
        """
        [DescribeStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks.paginate)
        """


class ListChangeSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListChangeSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListChangeSetsOutputTypeDef, None, None]:
        """
        [ListChangeSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets.paginate)
        """


class ListExportsPaginator(Boto3Paginator):
    """
    [Paginator.ListExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListExportsOutputTypeDef, None, None]:
        """
        [ListExports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports.paginate)
        """


class ListImportsPaginator(Boto3Paginator):
    """
    [Paginator.ListImports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ExportName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListImportsOutputTypeDef, None, None]:
        """
        [ListImports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports.paginate)
        """


class ListStackInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListStackInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackSetName: str,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListStackInstancesOutputTypeDef, None, None]:
        """
        [ListStackInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances.paginate)
        """


class ListStackResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListStackResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStackResourcesOutputTypeDef, None, None]:
        """
        [ListStackResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources.paginate)
        """


class ListStackSetOperationResultsPaginator(Boto3Paginator):
    """
    [Paginator.ListStackSetOperationResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackSetName: str, OperationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStackSetOperationResultsOutputTypeDef, None, None]:
        """
        [ListStackSetOperationResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults.paginate)
        """


class ListStackSetOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListStackSetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackSetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStackSetOperationsOutputTypeDef, None, None]:
        """
        [ListStackSetOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations.paginate)
        """


class ListStackSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListStackSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Status: Literal["ACTIVE", "DELETED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListStackSetsOutputTypeDef, None, None]:
        """
        [ListStackSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets.paginate)
        """


class ListStacksPaginator(Boto3Paginator):
    """
    [Paginator.ListStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackStatusFilter: List[
            Literal[
                "CREATE_IN_PROGRESS",
                "CREATE_FAILED",
                "CREATE_COMPLETE",
                "ROLLBACK_IN_PROGRESS",
                "ROLLBACK_FAILED",
                "ROLLBACK_COMPLETE",
                "DELETE_IN_PROGRESS",
                "DELETE_FAILED",
                "DELETE_COMPLETE",
                "UPDATE_IN_PROGRESS",
                "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_COMPLETE",
                "UPDATE_ROLLBACK_IN_PROGRESS",
                "UPDATE_ROLLBACK_FAILED",
                "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_ROLLBACK_COMPLETE",
                "REVIEW_IN_PROGRESS",
                "IMPORT_IN_PROGRESS",
                "IMPORT_COMPLETE",
                "IMPORT_ROLLBACK_IN_PROGRESS",
                "IMPORT_ROLLBACK_FAILED",
                "IMPORT_ROLLBACK_COMPLETE",
            ]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListStacksOutputTypeDef, None, None]:
        """
        [ListStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks.paginate)
        """
