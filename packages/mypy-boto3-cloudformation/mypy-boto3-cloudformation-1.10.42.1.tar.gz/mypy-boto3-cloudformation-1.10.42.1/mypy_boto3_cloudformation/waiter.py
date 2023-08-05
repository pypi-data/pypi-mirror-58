"Main interface for cloudformation service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudformation.type_defs import WaiterConfigTypeDef


__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)


class ChangeSetCreateCompleteWaiter(Boto3Waiter):
    """
    [Waiter.ChangeSetCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ChangeSetName: str,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ChangeSetCreateComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete.wait)
        """


class StackCreateCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackCreateComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete.wait)
        """


class StackDeleteCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackDeleteComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackDeleteComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete.wait)
        """


class StackExistsWaiter(Boto3Waiter):
    """
    [Waiter.StackExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists.wait)
        """


class StackImportCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackImportComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackImportComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete.wait)
        """


class StackUpdateCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackUpdateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackUpdateComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete.wait)
        """


class TypeRegistrationCompleteWaiter(Boto3Waiter):
    """
    [Waiter.TypeRegistrationComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, RegistrationToken: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TypeRegistrationComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete.wait)
        """
