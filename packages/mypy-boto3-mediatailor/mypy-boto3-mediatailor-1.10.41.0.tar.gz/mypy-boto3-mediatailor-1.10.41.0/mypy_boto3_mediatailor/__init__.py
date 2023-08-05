"Main interface for mediatailor service"
from mypy_boto3_mediatailor.client import MediaTailorClient as Client, MediaTailorClient
from mypy_boto3_mediatailor.paginator import ListPlaybackConfigurationsPaginator


__all__ = ("Client", "ListPlaybackConfigurationsPaginator", "MediaTailorClient")
