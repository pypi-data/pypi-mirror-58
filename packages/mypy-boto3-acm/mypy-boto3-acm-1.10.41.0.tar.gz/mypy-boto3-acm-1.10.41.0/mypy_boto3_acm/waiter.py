"Main interface for acm service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_acm.type_defs import WaiterConfigTypeDef


__all__ = ("CertificateValidatedWaiter",)


class CertificateValidatedWaiter(Boto3Waiter):
    """
    [Waiter.CertificateValidated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Waiter.CertificateValidated)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, CertificateArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [CertificateValidated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Waiter.CertificateValidated.wait)
        """
