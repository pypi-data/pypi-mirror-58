"Main interface for importexport service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_importexport.type_defs import ListJobsOutputTypeDef, PaginatorConfigTypeDef


__all__ = ("ListJobsPaginator",)


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/importexport.html#ImportExport.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, APIVersion: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListJobsOutputTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/importexport.html#ImportExport.Paginator.ListJobs.paginate)
        """
