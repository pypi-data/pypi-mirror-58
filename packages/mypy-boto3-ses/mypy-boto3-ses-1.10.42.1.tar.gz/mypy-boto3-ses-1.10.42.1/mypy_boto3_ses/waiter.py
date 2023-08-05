"Main interface for ses service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_ses.type_defs import WaiterConfigTypeDef


__all__ = ("IdentityExistsWaiter",)


class IdentityExistsWaiter(Boto3Waiter):
    """
    [Waiter.IdentityExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ses.html#SES.Waiter.IdentityExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Identities: List[str], WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [IdentityExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ses.html#SES.Waiter.IdentityExists.wait)
        """
