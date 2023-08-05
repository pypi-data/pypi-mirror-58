"Main interface for route53 service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_route53.type_defs import WaiterConfigTypeDef


__all__ = ("ResourceRecordSetsChangedWaiter",)


class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    """
    [Waiter.ResourceRecordSetsChanged documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ResourceRecordSetsChanged.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged.wait)
        """
