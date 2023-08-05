"Main interface for glue service"
from mypy_boto3_glue.client import GlueClient as Client, GlueClient
from mypy_boto3_glue.paginator import (
    GetClassifiersPaginator,
    GetConnectionsPaginator,
    GetCrawlerMetricsPaginator,
    GetCrawlersPaginator,
    GetDatabasesPaginator,
    GetDevEndpointsPaginator,
    GetJobRunsPaginator,
    GetJobsPaginator,
    GetPartitionsPaginator,
    GetSecurityConfigurationsPaginator,
    GetTableVersionsPaginator,
    GetTablesPaginator,
    GetTriggersPaginator,
    GetUserDefinedFunctionsPaginator,
)


__all__ = (
    "Client",
    "GetClassifiersPaginator",
    "GetConnectionsPaginator",
    "GetCrawlerMetricsPaginator",
    "GetCrawlersPaginator",
    "GetDatabasesPaginator",
    "GetDevEndpointsPaginator",
    "GetJobRunsPaginator",
    "GetJobsPaginator",
    "GetPartitionsPaginator",
    "GetSecurityConfigurationsPaginator",
    "GetTableVersionsPaginator",
    "GetTablesPaginator",
    "GetTriggersPaginator",
    "GetUserDefinedFunctionsPaginator",
    "GlueClient",
)
