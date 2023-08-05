"Main interface for signer service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_signer.type_defs import (
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
)


class ListSigningJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Paginator.ListSigningJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        status: Literal["InProgress", "Failed", "Succeeded"] = None,
        platformId: str = None,
        requestedBy: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSigningJobsResponseTypeDef, None, None]:
        """
        [ListSigningJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Paginator.ListSigningJobs.paginate)
        """


class ListSigningPlatformsPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningPlatforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSigningPlatformsResponseTypeDef, None, None]:
        """
        [ListSigningPlatforms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms.paginate)
        """


class ListSigningProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Paginator.ListSigningProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, includeCanceled: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSigningProfilesResponseTypeDef, None, None]:
        """
        [ListSigningProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Paginator.ListSigningProfiles.paginate)
        """
