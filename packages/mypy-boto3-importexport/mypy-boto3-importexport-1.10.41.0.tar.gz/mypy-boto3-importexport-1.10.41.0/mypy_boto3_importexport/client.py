"Main interface for importexport service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_importexport.client as client_scope

# pylint: disable=import-self
import mypy_boto3_importexport.paginator as paginator_scope
from mypy_boto3_importexport.type_defs import (
    CancelJobOutputTypeDef,
    CreateJobOutputTypeDef,
    GetShippingLabelOutputTypeDef,
    GetStatusOutputTypeDef,
    ListJobsOutputTypeDef,
    UpdateJobOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ImportExportClient",)


class ImportExportClient(BaseClient):
    """
    [ImportExport.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job(self, JobId: str, APIVersion: str = None) -> CancelJobOutputTypeDef:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.cancel_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        JobType: Literal["Import", "Export"],
        Manifest: str,
        ValidateOnly: bool,
        ManifestAddendum: str = None,
        APIVersion: str = None,
    ) -> CreateJobOutputTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.create_job)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_shipping_label(
        self,
        jobIds: List[str],
        name: str = None,
        company: str = None,
        phoneNumber: str = None,
        country: str = None,
        stateOrProvince: str = None,
        city: str = None,
        postalCode: str = None,
        street1: str = None,
        street2: str = None,
        street3: str = None,
        APIVersion: str = None,
    ) -> GetShippingLabelOutputTypeDef:
        """
        [Client.get_shipping_label documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.get_shipping_label)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_status(self, JobId: str, APIVersion: str = None) -> GetStatusOutputTypeDef:
        """
        [Client.get_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.get_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self, MaxJobs: int = None, Marker: str = None, APIVersion: str = None
    ) -> ListJobsOutputTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job(
        self,
        JobId: str,
        Manifest: str,
        JobType: Literal["Import", "Export"],
        ValidateOnly: bool,
        APIVersion: str = None,
    ) -> UpdateJobOutputTypeDef:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Client.update_job)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/importexport.html#ImportExport.Paginator.ListJobs)
        """


class Exceptions:
    BucketPermissionException: Boto3ClientError
    CanceledJobIdException: Boto3ClientError
    ClientError: Boto3ClientError
    CreateJobQuotaExceededException: Boto3ClientError
    ExpiredJobIdException: Boto3ClientError
    InvalidAccessKeyIdException: Boto3ClientError
    InvalidAddressException: Boto3ClientError
    InvalidCustomsException: Boto3ClientError
    InvalidFileSystemException: Boto3ClientError
    InvalidJobIdException: Boto3ClientError
    InvalidManifestFieldException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidVersionException: Boto3ClientError
    MalformedManifestException: Boto3ClientError
    MissingCustomsException: Boto3ClientError
    MissingManifestFieldException: Boto3ClientError
    MissingParameterException: Boto3ClientError
    MultipleRegionsException: Boto3ClientError
    NoSuchBucketException: Boto3ClientError
    UnableToCancelJobIdException: Boto3ClientError
    UnableToUpdateJobIdException: Boto3ClientError
