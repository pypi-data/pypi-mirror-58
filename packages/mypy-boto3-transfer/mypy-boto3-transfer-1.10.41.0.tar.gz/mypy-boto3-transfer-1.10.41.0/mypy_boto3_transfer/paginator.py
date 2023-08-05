"Main interface for transfer service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_transfer.type_defs import ListServersResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListServersPaginator",)


class ListServersPaginator(Boto3Paginator):
    """
    [Paginator.ListServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Paginator.ListServers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListServersResponseTypeDef, None, None]:
        """
        [ListServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Paginator.ListServers.paginate)
        """
