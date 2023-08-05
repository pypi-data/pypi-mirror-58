"Main interface for sms service"
from mypy_boto3_sms.client import SMSClient as Client, SMSClient
from mypy_boto3_sms.paginator import (
    GetConnectorsPaginator,
    GetReplicationJobsPaginator,
    GetReplicationRunsPaginator,
    GetServersPaginator,
    ListAppsPaginator,
)


__all__ = (
    "Client",
    "GetConnectorsPaginator",
    "GetReplicationJobsPaginator",
    "GetReplicationRunsPaginator",
    "GetServersPaginator",
    "ListAppsPaginator",
    "SMSClient",
)
