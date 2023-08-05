"Main interface for mediaconnect service"
from mypy_boto3_mediaconnect.client import MediaConnectClient, MediaConnectClient as Client
from mypy_boto3_mediaconnect.paginator import ListEntitlementsPaginator, ListFlowsPaginator


__all__ = ("Client", "ListEntitlementsPaginator", "ListFlowsPaginator", "MediaConnectClient")
