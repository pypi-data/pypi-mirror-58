"Main interface for savingsplans service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_savingsplans.client as client_scope
from mypy_boto3_savingsplans.type_defs import (
    CreateSavingsPlanResponseTypeDef,
    DescribeSavingsPlanRatesResponseTypeDef,
    DescribeSavingsPlansOfferingRatesResponseTypeDef,
    DescribeSavingsPlansOfferingsResponseTypeDef,
    DescribeSavingsPlansResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SavingsPlanFilterTypeDef,
    SavingsPlanOfferingFilterElementTypeDef,
    SavingsPlanOfferingRateFilterElementTypeDef,
    SavingsPlanRateFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SavingsPlansClient",)


class SavingsPlansClient(BaseClient):
    """
    [SavingsPlans.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_savings_plan(
        self,
        savingsPlanOfferingId: str,
        commitment: str,
        upfrontPaymentAmount: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateSavingsPlanResponseTypeDef:
        """
        [Client.create_savings_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.create_savings_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plan_rates(
        self,
        savingsPlanId: str,
        filters: List[SavingsPlanRateFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlanRatesResponseTypeDef:
        """
        [Client.describe_savings_plan_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plan_rates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plans(
        self,
        savingsPlanArns: List[str] = None,
        savingsPlanIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        states: List[Literal["payment-pending", "payment-failed", "active", "retired"]] = None,
        filters: List[SavingsPlanFilterTypeDef] = None,
    ) -> DescribeSavingsPlansResponseTypeDef:
        """
        [Client.describe_savings_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plans_offering_rates(
        self,
        savingsPlanOfferingIds: List[str] = None,
        savingsPlanPaymentOptions: List[
            Literal["All Upfront", "Partial Upfront", "No Upfront"]
        ] = None,
        savingsPlanTypes: List[Literal["Compute", "EC2Instance"]] = None,
        products: List[Literal["EC2", "Fargate"]] = None,
        serviceCodes: List[Literal["AmazonEC2", "AmazonECS"]] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[SavingsPlanOfferingRateFilterElementTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlansOfferingRatesResponseTypeDef:
        """
        [Client.describe_savings_plans_offering_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offering_rates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plans_offerings(
        self,
        offeringIds: List[str] = None,
        paymentOptions: List[Literal["All Upfront", "Partial Upfront", "No Upfront"]] = None,
        productType: Literal["EC2", "Fargate"] = None,
        planTypes: List[Literal["Compute", "EC2Instance"]] = None,
        durations: List[int] = None,
        currencies: List[Literal["CNY", "USD"]] = None,
        descriptions: List[str] = None,
        serviceCodes: List[str] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[SavingsPlanOfferingFilterElementTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlansOfferingsResponseTypeDef:
        """
        [Client.describe_savings_plans_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offerings)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/savingsplans.html#SavingsPlans.Client.untag_resource)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ValidationException: Boto3ClientError
