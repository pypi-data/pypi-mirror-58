"Main interface for acm service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_acm.client as client_scope

# pylint: disable=import-self
import mypy_boto3_acm.paginator as paginator_scope
from mypy_boto3_acm.type_defs import (
    CertificateOptionsTypeDef,
    DescribeCertificateResponseTypeDef,
    DomainValidationOptionTypeDef,
    ExportCertificateResponseTypeDef,
    FiltersTypeDef,
    GetCertificateResponseTypeDef,
    ImportCertificateResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListTagsForCertificateResponseTypeDef,
    RequestCertificateResponseTypeDef,
    TagTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_acm.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ACMClient",)


class ACMClient(BaseClient):
    """
    [ACM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_certificate(self, CertificateArn: str, Tags: List[TagTypeDef]) -> None:
        """
        [Client.add_tags_to_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.add_tags_to_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_certificate(self, CertificateArn: str) -> None:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.delete_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificate(self, CertificateArn: str) -> DescribeCertificateResponseTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.describe_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_certificate(
        self, CertificateArn: str, Passphrase: Union[bytes, IO]
    ) -> ExportCertificateResponseTypeDef:
        """
        [Client.export_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.export_certificate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_certificate(self, CertificateArn: str) -> GetCertificateResponseTypeDef:
        """
        [Client.get_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.get_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_certificate(
        self,
        Certificate: Union[bytes, IO],
        PrivateKey: Union[bytes, IO],
        CertificateArn: str = None,
        CertificateChain: Union[bytes, IO] = None,
        Tags: List[TagTypeDef] = None,
    ) -> ImportCertificateResponseTypeDef:
        """
        [Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.import_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_certificates(
        self,
        CertificateStatuses: List[
            Literal[
                "PENDING_VALIDATION",
                "ISSUED",
                "INACTIVE",
                "EXPIRED",
                "VALIDATION_TIMED_OUT",
                "REVOKED",
                "FAILED",
            ]
        ] = None,
        Includes: FiltersTypeDef = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> ListCertificatesResponseTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.list_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_certificate(
        self, CertificateArn: str
    ) -> ListTagsForCertificateResponseTypeDef:
        """
        [Client.list_tags_for_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.list_tags_for_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_certificate(self, CertificateArn: str, Tags: List[TagTypeDef]) -> None:
        """
        [Client.remove_tags_from_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.remove_tags_from_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def renew_certificate(self, CertificateArn: str) -> None:
        """
        [Client.renew_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.renew_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_certificate(
        self,
        DomainName: str,
        ValidationMethod: Literal["EMAIL", "DNS"] = None,
        SubjectAlternativeNames: List[str] = None,
        IdempotencyToken: str = None,
        DomainValidationOptions: List[DomainValidationOptionTypeDef] = None,
        Options: CertificateOptionsTypeDef = None,
        CertificateAuthorityArn: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> RequestCertificateResponseTypeDef:
        """
        [Client.request_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.request_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resend_validation_email(
        self, CertificateArn: str, Domain: str, ValidationDomain: str
    ) -> None:
        """
        [Client.resend_validation_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.resend_validation_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_certificate_options(
        self, CertificateArn: str, Options: CertificateOptionsTypeDef
    ) -> None:
        """
        [Client.update_certificate_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Client.update_certificate_options)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> paginator_scope.ListCertificatesPaginator:
        """
        [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Paginator.ListCertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["certificate_validated"]
    ) -> waiter_scope.CertificateValidatedWaiter:
        """
        [Waiter.CertificateValidated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm.html#ACM.Waiter.CertificateValidated)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidArgsException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidDomainValidationOptionsException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RequestInProgressException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
