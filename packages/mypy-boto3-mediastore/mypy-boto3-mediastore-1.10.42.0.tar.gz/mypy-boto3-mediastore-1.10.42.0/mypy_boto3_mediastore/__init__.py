"Main interface for mediastore service"
from mypy_boto3_mediastore.client import MediaStoreClient, MediaStoreClient as Client
from mypy_boto3_mediastore.paginator import ListContainersPaginator


__all__ = ("Client", "ListContainersPaginator", "MediaStoreClient")
