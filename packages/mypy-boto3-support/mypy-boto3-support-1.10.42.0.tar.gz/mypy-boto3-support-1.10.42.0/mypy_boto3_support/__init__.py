"Main interface for support service"
from mypy_boto3_support.client import SupportClient as Client, SupportClient
from mypy_boto3_support.paginator import DescribeCasesPaginator, DescribeCommunicationsPaginator


__all__ = ("Client", "DescribeCasesPaginator", "DescribeCommunicationsPaginator", "SupportClient")
