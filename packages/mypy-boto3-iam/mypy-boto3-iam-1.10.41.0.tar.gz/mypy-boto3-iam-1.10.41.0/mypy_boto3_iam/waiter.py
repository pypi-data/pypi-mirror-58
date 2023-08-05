"Main interface for iam service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_iam.type_defs import WaiterConfigTypeDef


__all__ = (
    "InstanceProfileExistsWaiter",
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "UserExistsWaiter",
)


class InstanceProfileExistsWaiter(Boto3Waiter):
    """
    [Waiter.InstanceProfileExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.InstanceProfileExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, InstanceProfileName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [InstanceProfileExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.InstanceProfileExists.wait)
        """


class PolicyExistsWaiter(Boto3Waiter):
    """
    [Waiter.PolicyExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.PolicyExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, PolicyArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [PolicyExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.PolicyExists.wait)
        """


class RoleExistsWaiter(Boto3Waiter):
    """
    [Waiter.RoleExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.RoleExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, RoleName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [RoleExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.RoleExists.wait)
        """


class UserExistsWaiter(Boto3Waiter):
    """
    [Waiter.UserExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.UserExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, UserName: str = None, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [UserExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Waiter.UserExists.wait)
        """
