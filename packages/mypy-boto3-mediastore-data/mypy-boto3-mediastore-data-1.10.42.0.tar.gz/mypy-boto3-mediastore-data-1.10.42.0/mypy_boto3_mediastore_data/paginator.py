"Main interface for mediastore-data service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediastore_data.type_defs import ListItemsResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListItemsPaginator",)


class ListItemsPaginator(Boto3Paginator):
    """
    [Paginator.ListItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Path: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListItemsResponseTypeDef, None, None]:
        """
        [ListItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems.paginate)
        """
