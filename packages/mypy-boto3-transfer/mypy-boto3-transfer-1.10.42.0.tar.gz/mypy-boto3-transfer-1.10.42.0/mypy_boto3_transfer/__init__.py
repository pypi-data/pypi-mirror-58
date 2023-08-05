"Main interface for transfer service"
from mypy_boto3_transfer.client import TransferClient as Client, TransferClient
from mypy_boto3_transfer.paginator import ListServersPaginator


__all__ = ("Client", "ListServersPaginator", "TransferClient")
