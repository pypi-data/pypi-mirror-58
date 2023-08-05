"Main interface for mq service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mq.type_defs import ListBrokersResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListBrokersPaginator",)


class ListBrokersPaginator(Boto3Paginator):
    """
    [Paginator.ListBrokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Paginator.ListBrokers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBrokersResponseTypeDef, None, None]:
        """
        [ListBrokers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Paginator.ListBrokers.paginate)
        """
