"Main interface for dataexchange service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dataexchange.type_defs import (
    ListDataSetRevisionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListRevisionAssetsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListDataSetRevisionsPaginator",
    "ListDataSetsPaginator",
    "ListJobsPaginator",
    "ListRevisionAssetsPaginator",
)


class ListDataSetRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSetRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DataSetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDataSetRevisionsResponseTypeDef, None, None]:
        """
        [ListDataSetRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions.paginate)
        """


class ListDataSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Origin: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDataSetsResponseTypeDef, None, None]:
        """
        [ListDataSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DataSetId: str = None,
        RevisionId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsResponseTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs.paginate)
        """


class ListRevisionAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRevisionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DataSetId: str, RevisionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRevisionAssetsResponseTypeDef, None, None]:
        """
        [ListRevisionAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets.paginate)
        """
