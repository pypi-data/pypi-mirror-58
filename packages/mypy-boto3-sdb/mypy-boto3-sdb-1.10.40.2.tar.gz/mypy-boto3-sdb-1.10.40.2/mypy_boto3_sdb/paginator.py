"Main interface for sdb service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sdb.type_defs import (
    ListDomainsResultTypeDef,
    PaginatorConfigTypeDef,
    SelectResultTypeDef,
)


__all__ = ("ListDomainsPaginator", "SelectPaginator")


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sdb.html#SimpleDB.Paginator.ListDomains)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDomainsResultTypeDef, None, None]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sdb.html#SimpleDB.Paginator.ListDomains.paginate)
        """


class SelectPaginator(Boto3Paginator):
    """
    [Paginator.Select documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sdb.html#SimpleDB.Paginator.Select)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SelectExpression: str,
        ConsistentRead: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SelectResultTypeDef, None, None]:
        """
        [Select.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sdb.html#SimpleDB.Paginator.Select.paginate)
        """
