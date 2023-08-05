"Main interface for mediastore-data service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_mediastore_data.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mediastore_data.paginator as paginator_scope
from mypy_boto3_mediastore_data.type_defs import (
    DescribeObjectResponseTypeDef,
    GetObjectResponseTypeDef,
    ListItemsResponseTypeDef,
    PutObjectResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaStoreDataClient",)


class MediaStoreDataClient(BaseClient):
    """
    [MediaStoreData.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_object(self, Path: str) -> Dict[str, Any]:
        """
        [Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client.delete_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_object(self, Path: str) -> DescribeObjectResponseTypeDef:
        """
        [Client.describe_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client.describe_object)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object(self, Path: str, Range: str = None) -> GetObjectResponseTypeDef:
        """
        [Client.get_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client.get_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_items(
        self, Path: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListItemsResponseTypeDef:
        """
        [Client.list_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client.list_items)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object(
        self,
        Body: Union[bytes, IO],
        Path: str,
        ContentType: str = None,
        CacheControl: str = None,
        StorageClass: Literal["TEMPORAL"] = None,
        UploadAvailability: Literal["STANDARD", "STREAMING"] = None,
    ) -> PutObjectResponseTypeDef:
        """
        [Client.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Client.put_object)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_items"]
    ) -> paginator_scope.ListItemsPaginator:
        """
        [Paginator.ListItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ContainerNotFoundException: Boto3ClientError
    InternalServerError: Boto3ClientError
    ObjectNotFoundException: Boto3ClientError
    RequestedRangeNotSatisfiableException: Boto3ClientError
