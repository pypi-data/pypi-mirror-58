"Main interface for mediastore service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediastore.type_defs import ListContainersOutputTypeDef, PaginatorConfigTypeDef


__all__ = ("ListContainersPaginator",)


class ListContainersPaginator(Boto3Paginator):
    """
    [Paginator.ListContainers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore.html#MediaStore.Paginator.ListContainers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListContainersOutputTypeDef, None, None]:
        """
        [ListContainers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediastore.html#MediaStore.Paginator.ListContainers.paginate)
        """
