"Main interface for config service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_config.type_defs import (
    ConfigRuleComplianceFiltersTypeDef,
    DescribeAggregateComplianceByConfigRulesResponseTypeDef,
    DescribeAggregationAuthorizationsResponseTypeDef,
    DescribeComplianceByConfigRuleResponseTypeDef,
    DescribeComplianceByResourceResponseTypeDef,
    DescribeConfigRuleEvaluationStatusResponseTypeDef,
    DescribeConfigRulesResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusResponseTypeDef,
    DescribeConfigurationAggregatorsResponseTypeDef,
    DescribePendingAggregationRequestsResponseTypeDef,
    DescribeRemediationExecutionStatusResponseTypeDef,
    DescribeRetentionConfigurationsResponseTypeDef,
    GetAggregateComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByResourceResponseTypeDef,
    GetResourceConfigHistoryResponseTypeDef,
    ListAggregateDiscoveredResourcesResponseTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    PaginatorConfigTypeDef,
    ResourceFiltersTypeDef,
    ResourceKeyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
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


class DescribeAggregateComplianceByConfigRulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAggregateComplianceByConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        Filters: ConfigRuleComplianceFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAggregateComplianceByConfigRulesResponseTypeDef, None, None]:
        """
        [DescribeAggregateComplianceByConfigRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules.paginate)
        """


class DescribeAggregationAuthorizationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAggregationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAggregationAuthorizationsResponseTypeDef, None, None]:
        """
        [DescribeAggregationAuthorizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations.paginate)
        """


class DescribeComplianceByConfigRulePaginator(Boto3Paginator):
    """
    [Paginator.DescribeComplianceByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeComplianceByConfigRuleResponseTypeDef, None, None]:
        """
        [DescribeComplianceByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule.paginate)
        """


class DescribeComplianceByResourcePaginator(Boto3Paginator):
    """
    [Paginator.DescribeComplianceByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeComplianceByResourceResponseTypeDef, None, None]:
        """
        [DescribeComplianceByResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource.paginate)
        """


class DescribeConfigRuleEvaluationStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigRuleEvaluationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ConfigRuleNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeConfigRuleEvaluationStatusResponseTypeDef, None, None]:
        """
        [DescribeConfigRuleEvaluationStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus.paginate)
        """


class DescribeConfigRulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ConfigRuleNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeConfigRulesResponseTypeDef, None, None]:
        """
        [DescribeConfigRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules.paginate)
        """


class DescribeConfigurationAggregatorSourcesStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigurationAggregatorSourcesStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[Literal["FAILED", "SUCCEEDED", "OUTDATED"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeConfigurationAggregatorSourcesStatusResponseTypeDef, None, None]:
        """
        [DescribeConfigurationAggregatorSourcesStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus.paginate)
        """


class DescribeConfigurationAggregatorsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigurationAggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeConfigurationAggregatorsResponseTypeDef, None, None]:
        """
        [DescribeConfigurationAggregators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators.paginate)
        """


class DescribePendingAggregationRequestsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePendingAggregationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribePendingAggregationRequestsResponseTypeDef, None, None]:
        """
        [DescribePendingAggregationRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests.paginate)
        """


class DescribeRemediationExecutionStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRemediationExecutionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[ResourceKeyTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeRemediationExecutionStatusResponseTypeDef, None, None]:
        """
        [DescribeRemediationExecutionStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus.paginate)
        """


class DescribeRetentionConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRetentionConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RetentionConfigurationNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeRetentionConfigurationsResponseTypeDef, None, None]:
        """
        [DescribeRetentionConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations.paginate)
        """


class GetAggregateComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    [Paginator.GetAggregateComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetAggregateComplianceDetailsByConfigRuleResponseTypeDef, None, None]:
        """
        [GetAggregateComplianceDetailsByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule.paginate)
        """


class GetComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    [Paginator.GetComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetComplianceDetailsByConfigRuleResponseTypeDef, None, None]:
        """
        [GetComplianceDetailsByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule.paginate)
        """


class GetComplianceDetailsByResourcePaginator(Boto3Paginator):
    """
    [Paginator.GetComplianceDetailsByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetComplianceDetailsByResourceResponseTypeDef, None, None]:
        """
        [GetComplianceDetailsByResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource.paginate)
        """


class GetResourceConfigHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetResourceConfigHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: Literal["Reverse", "Forward"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetResourceConfigHistoryResponseTypeDef, None, None]:
        """
        [GetResourceConfigHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory.paginate)
        """


class ListAggregateDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListAggregateDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        Filters: ResourceFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAggregateDiscoveredResourcesResponseTypeDef, None, None]:
        """
        [ListAggregateDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources.paginate)
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        resourceIds: List[str] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDiscoveredResourcesResponseTypeDef, None, None]:
        """
        [ListDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources.paginate)
        """
