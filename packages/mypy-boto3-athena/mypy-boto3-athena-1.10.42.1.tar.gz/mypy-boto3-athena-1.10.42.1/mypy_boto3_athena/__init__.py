"Main interface for athena service"
from mypy_boto3_athena.client import AthenaClient, AthenaClient as Client
from mypy_boto3_athena.paginator import (
    GetQueryResultsPaginator,
    ListNamedQueriesPaginator,
    ListQueryExecutionsPaginator,
)


__all__ = (
    "AthenaClient",
    "Client",
    "GetQueryResultsPaginator",
    "ListNamedQueriesPaginator",
    "ListQueryExecutionsPaginator",
)
