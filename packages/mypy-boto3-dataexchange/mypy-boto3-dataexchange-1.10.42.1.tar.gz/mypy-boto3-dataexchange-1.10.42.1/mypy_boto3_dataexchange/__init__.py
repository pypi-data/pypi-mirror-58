"Main interface for dataexchange service"
from mypy_boto3_dataexchange.client import DataExchangeClient as Client, DataExchangeClient
from mypy_boto3_dataexchange.paginator import (
    ListDataSetRevisionsPaginator,
    ListDataSetsPaginator,
    ListJobsPaginator,
    ListRevisionAssetsPaginator,
)


__all__ = (
    "Client",
    "DataExchangeClient",
    "ListDataSetRevisionsPaginator",
    "ListDataSetsPaginator",
    "ListJobsPaginator",
    "ListRevisionAssetsPaginator",
)
