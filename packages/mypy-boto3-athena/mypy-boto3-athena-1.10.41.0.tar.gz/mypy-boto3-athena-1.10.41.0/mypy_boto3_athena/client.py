"Main interface for athena service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_athena.client as client_scope

# pylint: disable=import-self
import mypy_boto3_athena.paginator as paginator_scope
from mypy_boto3_athena.type_defs import (
    BatchGetNamedQueryOutputTypeDef,
    BatchGetQueryExecutionOutputTypeDef,
    CreateNamedQueryOutputTypeDef,
    GetNamedQueryOutputTypeDef,
    GetQueryExecutionOutputTypeDef,
    GetQueryResultsOutputTypeDef,
    GetWorkGroupOutputTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListQueryExecutionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWorkGroupsOutputTypeDef,
    QueryExecutionContextTypeDef,
    ResultConfigurationTypeDef,
    StartQueryExecutionOutputTypeDef,
    TagTypeDef,
    WorkGroupConfigurationTypeDef,
    WorkGroupConfigurationUpdatesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AthenaClient",)


class AthenaClient(BaseClient):
    """
    [Athena.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_named_query(self, NamedQueryIds: List[str]) -> BatchGetNamedQueryOutputTypeDef:
        """
        [Client.batch_get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.batch_get_named_query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_query_execution(
        self, QueryExecutionIds: List[str]
    ) -> BatchGetQueryExecutionOutputTypeDef:
        """
        [Client.batch_get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.batch_get_query_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_named_query(
        self,
        Name: str,
        Database: str,
        QueryString: str,
        Description: str = None,
        ClientRequestToken: str = None,
        WorkGroup: str = None,
    ) -> CreateNamedQueryOutputTypeDef:
        """
        [Client.create_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.create_named_query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_work_group(
        self,
        Name: str,
        Configuration: WorkGroupConfigurationTypeDef = None,
        Description: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.create_work_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_named_query(self, NamedQueryId: str) -> Dict[str, Any]:
        """
        [Client.delete_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.delete_named_query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_work_group(
        self, WorkGroup: str, RecursiveDeleteOption: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.delete_work_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_named_query(self, NamedQueryId: str) -> GetNamedQueryOutputTypeDef:
        """
        [Client.get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.get_named_query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_query_execution(self, QueryExecutionId: str) -> GetQueryExecutionOutputTypeDef:
        """
        [Client.get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.get_query_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_query_results(
        self, QueryExecutionId: str, NextToken: str = None, MaxResults: int = None
    ) -> GetQueryResultsOutputTypeDef:
        """
        [Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.get_query_results)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_work_group(self, WorkGroup: str) -> GetWorkGroupOutputTypeDef:
        """
        [Client.get_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.get_work_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_named_queries(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ListNamedQueriesOutputTypeDef:
        """
        [Client.list_named_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.list_named_queries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_query_executions(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ListQueryExecutionsOutputTypeDef:
        """
        [Client.list_query_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.list_query_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_work_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkGroupsOutputTypeDef:
        """
        [Client.list_work_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.list_work_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_query_execution(
        self,
        QueryString: str,
        ClientRequestToken: str = None,
        QueryExecutionContext: QueryExecutionContextTypeDef = None,
        ResultConfiguration: ResultConfigurationTypeDef = None,
        WorkGroup: str = None,
    ) -> StartQueryExecutionOutputTypeDef:
        """
        [Client.start_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.start_query_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_query_execution(self, QueryExecutionId: str) -> Dict[str, Any]:
        """
        [Client.stop_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.stop_query_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_work_group(
        self,
        WorkGroup: str,
        Description: str = None,
        ConfigurationUpdates: WorkGroupConfigurationUpdatesTypeDef = None,
        State: Literal["ENABLED", "DISABLED"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Client.update_work_group)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_query_results"]
    ) -> paginator_scope.GetQueryResultsPaginator:
        """
        [Paginator.GetQueryResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Paginator.GetQueryResults)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_named_queries"]
    ) -> paginator_scope.ListNamedQueriesPaginator:
        """
        [Paginator.ListNamedQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Paginator.ListNamedQueries)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_query_executions"]
    ) -> paginator_scope.ListQueryExecutionsPaginator:
        """
        [Paginator.ListQueryExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
