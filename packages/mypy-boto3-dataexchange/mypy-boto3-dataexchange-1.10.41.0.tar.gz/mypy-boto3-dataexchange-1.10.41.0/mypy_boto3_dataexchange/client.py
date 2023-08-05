"Main interface for dataexchange service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_dataexchange.client as client_scope

# pylint: disable=import-self
import mypy_boto3_dataexchange.paginator as paginator_scope
from mypy_boto3_dataexchange.type_defs import (
    CreateDataSetResponseTypeDef,
    CreateJobResponseTypeDef,
    CreateRevisionResponseTypeDef,
    GetAssetResponseTypeDef,
    GetDataSetResponseTypeDef,
    GetJobResponseTypeDef,
    GetRevisionResponseTypeDef,
    ListDataSetRevisionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListRevisionAssetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RequestDetailsTypeDef,
    UpdateAssetResponseTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateRevisionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DataExchangeClient",)


class DataExchangeClient(BaseClient):
    """
    [DataExchange.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job(self, JobId: str) -> None:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.cancel_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_data_set(
        self,
        AssetType: Literal["S3_SNAPSHOT"],
        Description: str,
        Name: str,
        Tags: Dict[str, str] = None,
    ) -> CreateDataSetResponseTypeDef:
        """
        [Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.create_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        Details: RequestDetailsTypeDef,
        Type: Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.create_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_revision(
        self, DataSetId: str, Comment: str = None, Tags: Dict[str, str] = None
    ) -> CreateRevisionResponseTypeDef:
        """
        [Client.create_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.create_revision)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_asset(self, AssetId: str, DataSetId: str, RevisionId: str) -> None:
        """
        [Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.delete_asset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_data_set(self, DataSetId: str) -> None:
        """
        [Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.delete_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_revision(self, DataSetId: str, RevisionId: str) -> None:
        """
        [Client.delete_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.delete_revision)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_asset(self, AssetId: str, DataSetId: str, RevisionId: str) -> GetAssetResponseTypeDef:
        """
        [Client.get_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.get_asset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_data_set(self, DataSetId: str) -> GetDataSetResponseTypeDef:
        """
        [Client.get_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.get_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job(self, JobId: str) -> GetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.get_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_revision(self, DataSetId: str, RevisionId: str) -> GetRevisionResponseTypeDef:
        """
        [Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.get_revision)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_data_set_revisions(
        self, DataSetId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDataSetRevisionsResponseTypeDef:
        """
        [Client.list_data_set_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.list_data_set_revisions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_data_sets(
        self, MaxResults: int = None, NextToken: str = None, Origin: str = None
    ) -> ListDataSetsResponseTypeDef:
        """
        [Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.list_data_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self,
        DataSetId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        RevisionId: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_revision_assets(
        self, DataSetId: str, RevisionId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRevisionAssetsResponseTypeDef:
        """
        [Client.list_revision_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.list_revision_assets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_job(self, JobId: str) -> Dict[str, Any]:
        """
        [Client.start_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.start_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_asset(
        self, AssetId: str, DataSetId: str, Name: str, RevisionId: str
    ) -> UpdateAssetResponseTypeDef:
        """
        [Client.update_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.update_asset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_set(
        self, DataSetId: str, Description: str = None, Name: str = None
    ) -> UpdateDataSetResponseTypeDef:
        """
        [Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.update_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_revision(
        self, DataSetId: str, RevisionId: str, Comment: str = None, Finalized: bool = None
    ) -> UpdateRevisionResponseTypeDef:
        """
        [Client.update_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Client.update_revision)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_data_set_revisions"]
    ) -> paginator_scope.ListDataSetRevisionsPaginator:
        """
        [Paginator.ListDataSetRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_data_sets"]
    ) -> paginator_scope.ListDataSetsPaginator:
        """
        [Paginator.ListDataSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_revision_assets"]
    ) -> paginator_scope.ListRevisionAssetsPaginator:
        """
        [Paginator.ListRevisionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceLimitExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
