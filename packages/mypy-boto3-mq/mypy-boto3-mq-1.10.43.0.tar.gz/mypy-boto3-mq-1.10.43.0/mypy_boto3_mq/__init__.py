"Main interface for mq service"
from mypy_boto3_mq.client import MQClient as Client, MQClient
from mypy_boto3_mq.paginator import ListBrokersPaginator


__all__ = ("Client", "ListBrokersPaginator", "MQClient")
