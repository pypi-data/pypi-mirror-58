"Main interface for sdb service"
from mypy_boto3_sdb.client import SimpleDBClient as Client, SimpleDBClient
from mypy_boto3_sdb.paginator import ListDomainsPaginator, SelectPaginator


__all__ = ("Client", "ListDomainsPaginator", "SelectPaginator", "SimpleDBClient")
