"Main interface for mediatailor service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediatailor.type_defs import (
    ListPlaybackConfigurationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListPlaybackConfigurationsPaginator",)


class ListPlaybackConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlaybackConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPlaybackConfigurationsResponseTypeDef, None, None]:
        """
        [ListPlaybackConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations.paginate)
        """
