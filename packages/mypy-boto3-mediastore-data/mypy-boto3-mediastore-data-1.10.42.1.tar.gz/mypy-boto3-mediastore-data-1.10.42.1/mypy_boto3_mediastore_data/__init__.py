"Main interface for mediastore-data service"
from mypy_boto3_mediastore_data.client import MediaStoreDataClient as Client, MediaStoreDataClient
from mypy_boto3_mediastore_data.paginator import ListItemsPaginator


__all__ = ("Client", "ListItemsPaginator", "MediaStoreDataClient")
