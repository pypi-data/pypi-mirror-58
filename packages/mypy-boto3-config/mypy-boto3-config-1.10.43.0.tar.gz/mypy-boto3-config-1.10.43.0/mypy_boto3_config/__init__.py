"Main interface for config service"
from mypy_boto3_config.client import ConfigServiceClient, ConfigServiceClient as Client
from mypy_boto3_config.paginator import (
    DescribeAggregateComplianceByConfigRulesPaginator,
    DescribeAggregationAuthorizationsPaginator,
    DescribeComplianceByConfigRulePaginator,
    DescribeComplianceByResourcePaginator,
    DescribeConfigRuleEvaluationStatusPaginator,
    DescribeConfigRulesPaginator,
    DescribeConfigurationAggregatorSourcesStatusPaginator,
    DescribeConfigurationAggregatorsPaginator,
    DescribePendingAggregationRequestsPaginator,
    DescribeRemediationExecutionStatusPaginator,
    DescribeRetentionConfigurationsPaginator,
    GetAggregateComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByResourcePaginator,
    GetResourceConfigHistoryPaginator,
    ListAggregateDiscoveredResourcesPaginator,
    ListDiscoveredResourcesPaginator,
)


__all__ = (
    "Client",
    "ConfigServiceClient",
    "DescribeAggregateComplianceByConfigRulesPaginator",
    "DescribeAggregationAuthorizationsPaginator",
    "DescribeComplianceByConfigRulePaginator",
    "DescribeComplianceByResourcePaginator",
    "DescribeConfigRuleEvaluationStatusPaginator",
    "DescribeConfigRulesPaginator",
    "DescribeConfigurationAggregatorSourcesStatusPaginator",
    "DescribeConfigurationAggregatorsPaginator",
    "DescribePendingAggregationRequestsPaginator",
    "DescribeRemediationExecutionStatusPaginator",
    "DescribeRetentionConfigurationsPaginator",
    "GetAggregateComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByResourcePaginator",
    "GetResourceConfigHistoryPaginator",
    "ListAggregateDiscoveredResourcesPaginator",
    "ListDiscoveredResourcesPaginator",
)
