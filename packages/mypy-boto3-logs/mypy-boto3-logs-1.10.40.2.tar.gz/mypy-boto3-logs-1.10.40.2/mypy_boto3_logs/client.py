"Main interface for logs service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_logs.client as client_scope

# pylint: disable=import-self
import mypy_boto3_logs.paginator as paginator_scope
from mypy_boto3_logs.type_defs import (
    CreateExportTaskResponseTypeDef,
    DescribeDestinationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeLogGroupsResponseTypeDef,
    DescribeLogStreamsResponseTypeDef,
    DescribeMetricFiltersResponseTypeDef,
    DescribeQueriesResponseTypeDef,
    DescribeResourcePoliciesResponseTypeDef,
    DescribeSubscriptionFiltersResponseTypeDef,
    FilterLogEventsResponseTypeDef,
    GetLogEventsResponseTypeDef,
    GetLogGroupFieldsResponseTypeDef,
    GetLogRecordResponseTypeDef,
    GetQueryResultsResponseTypeDef,
    InputLogEventTypeDef,
    ListTagsLogGroupResponseTypeDef,
    MetricTransformationTypeDef,
    PutDestinationResponseTypeDef,
    PutLogEventsResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    StartQueryResponseTypeDef,
    StopQueryResponseTypeDef,
    TestMetricFilterResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudWatchLogsClient",)


class CloudWatchLogsClient(BaseClient):
    """
    [CloudWatchLogs.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_kms_key(self, logGroupName: str, kmsKeyId: str) -> None:
        """
        [Client.associate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.associate_kms_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_export_task(self, taskId: str) -> None:
        """
        [Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.cancel_export_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_export_task(
        self,
        logGroupName: str,
        fromTime: int,
        to: int,
        destination: str,
        taskName: str = None,
        logStreamNamePrefix: str = None,
        destinationPrefix: str = None,
    ) -> CreateExportTaskResponseTypeDef:
        """
        [Client.create_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.create_export_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_log_group(
        self, logGroupName: str, kmsKeyId: str = None, tags: Dict[str, str] = None
    ) -> None:
        """
        [Client.create_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.create_log_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        """
        [Client.create_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.create_log_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_destination(self, destinationName: str) -> None:
        """
        [Client.delete_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.delete_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_log_group(self, logGroupName: str) -> None:
        """
        [Client.delete_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.delete_log_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        """
        [Client.delete_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.delete_log_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_metric_filter(self, logGroupName: str, filterName: str) -> None:
        """
        [Client.delete_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.delete_metric_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_policy(self, policyName: str = None) -> None:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.delete_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_retention_policy(self, logGroupName: str) -> None:
        """
        [Client.delete_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.delete_retention_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_subscription_filter(self, logGroupName: str, filterName: str) -> None:
        """
        [Client.delete_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_destinations(
        self, DestinationNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeDestinationsResponseTypeDef:
        """
        [Client.describe_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_destinations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_export_tasks(
        self,
        taskId: str = None,
        statusCode: Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ] = None,
        nextToken: str = None,
        limit: int = None,
    ) -> DescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_export_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_log_groups(
        self, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeLogGroupsResponseTypeDef:
        """
        [Client.describe_log_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_log_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_log_streams(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: Literal["LogStreamName", "LastEventTime"] = None,
        descending: bool = None,
        nextToken: str = None,
        limit: int = None,
    ) -> DescribeLogStreamsResponseTypeDef:
        """
        [Client.describe_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_log_streams)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_metric_filters(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
        metricName: str = None,
        metricNamespace: str = None,
    ) -> DescribeMetricFiltersResponseTypeDef:
        """
        [Client.describe_metric_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_metric_filters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_queries(
        self,
        logGroupName: str = None,
        status: Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeQueriesResponseTypeDef:
        """
        [Client.describe_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_queries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resource_policies(
        self, nextToken: str = None, limit: int = None
    ) -> DescribeResourcePoliciesResponseTypeDef:
        """
        [Client.describe_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_resource_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_subscription_filters(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
    ) -> DescribeSubscriptionFiltersResponseTypeDef:
        """
        [Client.describe_subscription_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.describe_subscription_filters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_kms_key(self, logGroupName: str) -> None:
        """
        [Client.disassociate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.disassociate_kms_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter_log_events(
        self,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        nextToken: str = None,
        limit: int = None,
        interleaved: bool = None,
    ) -> FilterLogEventsResponseTypeDef:
        """
        [Client.filter_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.filter_log_events)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        startTime: int = None,
        endTime: int = None,
        nextToken: str = None,
        limit: int = None,
        startFromHead: bool = None,
    ) -> GetLogEventsResponseTypeDef:
        """
        [Client.get_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.get_log_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_log_group_fields(
        self, logGroupName: str, time: int = None
    ) -> GetLogGroupFieldsResponseTypeDef:
        """
        [Client.get_log_group_fields documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.get_log_group_fields)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_log_record(self, logRecordPointer: str) -> GetLogRecordResponseTypeDef:
        """
        [Client.get_log_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.get_log_record)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_query_results(self, queryId: str) -> GetQueryResultsResponseTypeDef:
        """
        [Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.get_query_results)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_log_group(self, logGroupName: str) -> ListTagsLogGroupResponseTypeDef:
        """
        [Client.list_tags_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.list_tags_log_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_destination(
        self, destinationName: str, targetArn: str, roleArn: str
    ) -> PutDestinationResponseTypeDef:
        """
        [Client.put_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.put_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_destination_policy(self, destinationName: str, accessPolicy: str) -> None:
        """
        [Client.put_destination_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.put_destination_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        logEvents: List[InputLogEventTypeDef],
        sequenceToken: str = None,
    ) -> PutLogEventsResponseTypeDef:
        """
        [Client.put_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.put_log_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_metric_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: List[MetricTransformationTypeDef],
    ) -> None:
        """
        [Client.put_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.put_metric_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_resource_policy(
        self, policyName: str = None, policyDocument: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.put_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_retention_policy(self, logGroupName: str, retentionInDays: int) -> None:
        """
        [Client.put_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.put_retention_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_subscription_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: str = None,
        distribution: Literal["Random", "ByLogStream"] = None,
    ) -> None:
        """
        [Client.put_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_query(
        self,
        startTime: int,
        endTime: int,
        queryString: str,
        logGroupName: str = None,
        logGroupNames: List[str] = None,
        limit: int = None,
    ) -> StartQueryResponseTypeDef:
        """
        [Client.start_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.start_query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_query(self, queryId: str) -> StopQueryResponseTypeDef:
        """
        [Client.stop_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.stop_query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_log_group(self, logGroupName: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.tag_log_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_metric_filter(
        self, filterPattern: str, logEventMessages: List[str]
    ) -> TestMetricFilterResponseTypeDef:
        """
        [Client.test_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.test_metric_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_log_group(self, logGroupName: str, tags: List[str]) -> None:
        """
        [Client.untag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Client.untag_log_group)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_destinations"]
    ) -> paginator_scope.DescribeDestinationsPaginator:
        """
        [Paginator.DescribeDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> paginator_scope.DescribeExportTasksPaginator:
        """
        [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_log_groups"]
    ) -> paginator_scope.DescribeLogGroupsPaginator:
        """
        [Paginator.DescribeLogGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_log_streams"]
    ) -> paginator_scope.DescribeLogStreamsPaginator:
        """
        [Paginator.DescribeLogStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_metric_filters"]
    ) -> paginator_scope.DescribeMetricFiltersPaginator:
        """
        [Paginator.DescribeMetricFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_queries"]
    ) -> paginator_scope.DescribeQueriesPaginator:
        """
        [Paginator.DescribeQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_resource_policies"]
    ) -> paginator_scope.DescribeResourcePoliciesPaginator:
        """
        [Paginator.DescribeResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_subscription_filters"]
    ) -> paginator_scope.DescribeSubscriptionFiltersPaginator:
        """
        [Paginator.DescribeSubscriptionFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["filter_log_events"]
    ) -> paginator_scope.FilterLogEventsPaginator:
        """
        [Paginator.FilterLogEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DataAlreadyAcceptedException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidSequenceTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedQueryException: Boto3ClientError
    OperationAbortedException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    UnrecognizedClientException: Boto3ClientError
