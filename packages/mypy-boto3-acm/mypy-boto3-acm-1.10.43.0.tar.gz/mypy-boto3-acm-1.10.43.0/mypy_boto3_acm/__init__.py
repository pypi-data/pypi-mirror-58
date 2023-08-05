"Main interface for acm service"
from mypy_boto3_acm.client import ACMClient as Client, ACMClient
from mypy_boto3_acm.paginator import ListCertificatesPaginator
from mypy_boto3_acm.waiter import CertificateValidatedWaiter


__all__ = ("ACMClient", "CertificateValidatedWaiter", "Client", "ListCertificatesPaginator")
