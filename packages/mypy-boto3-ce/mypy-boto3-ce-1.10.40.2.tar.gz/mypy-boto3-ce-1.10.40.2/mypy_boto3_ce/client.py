"Main interface for ce service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ce.client as client_scope
from mypy_boto3_ce.type_defs import (
    CostCategoryRuleTypeDef,
    CreateCostCategoryDefinitionResponseTypeDef,
    DateIntervalTypeDef,
    DeleteCostCategoryDefinitionResponseTypeDef,
    DescribeCostCategoryDefinitionResponseTypeDef,
    ExpressionTypeDef,
    GetCostAndUsageResponseTypeDef,
    GetCostAndUsageWithResourcesResponseTypeDef,
    GetCostForecastResponseTypeDef,
    GetDimensionValuesResponseTypeDef,
    GetReservationCoverageResponseTypeDef,
    GetReservationPurchaseRecommendationResponseTypeDef,
    GetReservationUtilizationResponseTypeDef,
    GetRightsizingRecommendationResponseTypeDef,
    GetSavingsPlansCoverageResponseTypeDef,
    GetSavingsPlansPurchaseRecommendationResponseTypeDef,
    GetSavingsPlansUtilizationDetailsResponseTypeDef,
    GetSavingsPlansUtilizationResponseTypeDef,
    GetTagsResponseTypeDef,
    GetUsageForecastResponseTypeDef,
    GroupDefinitionTypeDef,
    ListCostCategoryDefinitionsResponseTypeDef,
    ServiceSpecificationTypeDef,
    UpdateCostCategoryDefinitionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CostExplorerClient",)


class CostExplorerClient(BaseClient):
    """
    [CostExplorer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cost_category_definition(
        self,
        Name: str,
        RuleVersion: Literal["CostCategoryExpression.v1"],
        Rules: List[CostCategoryRuleTypeDef],
    ) -> CreateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.create_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.create_cost_category_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cost_category_definition(
        self, CostCategoryArn: str
    ) -> DeleteCostCategoryDefinitionResponseTypeDef:
        """
        [Client.delete_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.delete_cost_category_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cost_category_definition(
        self, CostCategoryArn: str, EffectiveOn: str = None
    ) -> DescribeCostCategoryDefinitionResponseTypeDef:
        """
        [Client.describe_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.describe_cost_category_definition)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cost_and_usage(
        self,
        TimePeriod: DateIntervalTypeDef,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ExpressionTypeDef = None,
        Metrics: List[str] = None,
        GroupBy: List[GroupDefinitionTypeDef] = None,
        NextPageToken: str = None,
    ) -> GetCostAndUsageResponseTypeDef:
        """
        [Client.get_cost_and_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cost_and_usage_with_resources(
        self,
        TimePeriod: DateIntervalTypeDef,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ExpressionTypeDef = None,
        Metrics: List[str] = None,
        GroupBy: List[GroupDefinitionTypeDef] = None,
        NextPageToken: str = None,
    ) -> GetCostAndUsageWithResourcesResponseTypeDef:
        """
        [Client.get_cost_and_usage_with_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage_with_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cost_forecast(
        self,
        TimePeriod: DateIntervalTypeDef,
        Metric: Literal[
            "BLENDED_COST",
            "UNBLENDED_COST",
            "AMORTIZED_COST",
            "NET_UNBLENDED_COST",
            "NET_AMORTIZED_COST",
            "USAGE_QUANTITY",
            "NORMALIZED_USAGE_AMOUNT",
        ],
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"],
        Filter: ExpressionTypeDef = None,
        PredictionIntervalLevel: int = None,
    ) -> GetCostForecastResponseTypeDef:
        """
        [Client.get_cost_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_cost_forecast)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dimension_values(
        self,
        TimePeriod: DateIntervalTypeDef,
        Dimension: Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        SearchString: str = None,
        Context: Literal["COST_AND_USAGE", "RESERVATIONS", "SAVINGS_PLANS"] = None,
        NextPageToken: str = None,
    ) -> GetDimensionValuesResponseTypeDef:
        """
        [Client.get_dimension_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_dimension_values)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reservation_coverage(
        self,
        TimePeriod: DateIntervalTypeDef,
        GroupBy: List[GroupDefinitionTypeDef] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ExpressionTypeDef = None,
        Metrics: List[str] = None,
        NextPageToken: str = None,
    ) -> GetReservationCoverageResponseTypeDef:
        """
        [Client.get_reservation_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_reservation_coverage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reservation_purchase_recommendation(
        self,
        Service: str,
        AccountId: str = None,
        AccountScope: Literal["PAYER", "LINKED"] = None,
        LookbackPeriodInDays: Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"] = None,
        TermInYears: Literal["ONE_YEAR", "THREE_YEARS"] = None,
        PaymentOption: Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ] = None,
        ServiceSpecification: ServiceSpecificationTypeDef = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> GetReservationPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_reservation_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_reservation_purchase_recommendation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reservation_utilization(
        self,
        TimePeriod: DateIntervalTypeDef,
        GroupBy: List[GroupDefinitionTypeDef] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ExpressionTypeDef = None,
        NextPageToken: str = None,
    ) -> GetReservationUtilizationResponseTypeDef:
        """
        [Client.get_reservation_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_reservation_utilization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_rightsizing_recommendation(
        self,
        Service: str,
        Filter: ExpressionTypeDef = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> GetRightsizingRecommendationResponseTypeDef:
        """
        [Client.get_rightsizing_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_rightsizing_recommendation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_coverage(
        self,
        TimePeriod: DateIntervalTypeDef,
        GroupBy: List[GroupDefinitionTypeDef] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ExpressionTypeDef = None,
        Metrics: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetSavingsPlansCoverageResponseTypeDef:
        """
        [Client.get_savings_plans_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_savings_plans_coverage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_purchase_recommendation(
        self,
        SavingsPlansType: Literal["COMPUTE_SP", "EC2_INSTANCE_SP"],
        TermInYears: Literal["ONE_YEAR", "THREE_YEARS"],
        PaymentOption: Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ],
        LookbackPeriodInDays: Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
        NextPageToken: str = None,
        PageSize: int = None,
    ) -> GetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_savings_plans_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_savings_plans_purchase_recommendation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_utilization(
        self,
        TimePeriod: DateIntervalTypeDef,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ExpressionTypeDef = None,
    ) -> GetSavingsPlansUtilizationResponseTypeDef:
        """
        [Client.get_savings_plans_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_utilization_details(
        self,
        TimePeriod: DateIntervalTypeDef,
        Filter: ExpressionTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        [Client.get_savings_plans_utilization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tags(
        self,
        TimePeriod: DateIntervalTypeDef,
        SearchString: str = None,
        TagKey: str = None,
        NextPageToken: str = None,
    ) -> GetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_usage_forecast(
        self,
        TimePeriod: DateIntervalTypeDef,
        Metric: Literal[
            "BLENDED_COST",
            "UNBLENDED_COST",
            "AMORTIZED_COST",
            "NET_UNBLENDED_COST",
            "NET_AMORTIZED_COST",
            "USAGE_QUANTITY",
            "NORMALIZED_USAGE_AMOUNT",
        ],
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"],
        Filter: ExpressionTypeDef = None,
        PredictionIntervalLevel: int = None,
    ) -> GetUsageForecastResponseTypeDef:
        """
        [Client.get_usage_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.get_usage_forecast)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_cost_category_definitions(
        self, EffectiveOn: str = None, NextToken: str = None
    ) -> ListCostCategoryDefinitionsResponseTypeDef:
        """
        [Client.list_cost_category_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.list_cost_category_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_cost_category_definition(
        self,
        CostCategoryArn: str,
        RuleVersion: Literal["CostCategoryExpression.v1"],
        Rules: List[CostCategoryRuleTypeDef],
    ) -> UpdateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.update_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ce.html#CostExplorer.Client.update_cost_category_definition)
        """


class Exceptions:
    BillExpirationException: Boto3ClientError
    ClientError: Boto3ClientError
    DataUnavailableException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RequestChangedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    UnresolvableUsageUnitException: Boto3ClientError
