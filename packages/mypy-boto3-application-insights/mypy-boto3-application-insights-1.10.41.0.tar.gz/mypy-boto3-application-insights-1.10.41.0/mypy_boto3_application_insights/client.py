"Main interface for application-insights service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_application_insights.client as client_scope
from mypy_boto3_application_insights.type_defs import (
    CreateApplicationResponseTypeDef,
    CreateLogPatternResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeComponentConfigurationRecommendationResponseTypeDef,
    DescribeComponentConfigurationResponseTypeDef,
    DescribeComponentResponseTypeDef,
    DescribeLogPatternResponseTypeDef,
    DescribeObservationResponseTypeDef,
    DescribeProblemObservationsResponseTypeDef,
    DescribeProblemResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListLogPatternSetsResponseTypeDef,
    ListLogPatternsResponseTypeDef,
    ListProblemsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateLogPatternResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationInsightsClient",)


class ApplicationInsightsClient(BaseClient):
    """
    [ApplicationInsights.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.create_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_component(
        self, ResourceGroupName: str, ComponentName: str, ResourceList: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.create_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.create_component)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_log_pattern(
        self, ResourceGroupName: str, PatternSetName: str, PatternName: str, Pattern: str, Rank: int
    ) -> CreateLogPatternResponseTypeDef:
        """
        [Client.create_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.create_log_pattern)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_application(self, ResourceGroupName: str) -> Dict[str, Any]:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.delete_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_component(self, ResourceGroupName: str, ComponentName: str) -> Dict[str, Any]:
        """
        [Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.delete_component)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_log_pattern(
        self, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.delete_log_pattern)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_application(self, ResourceGroupName: str) -> DescribeApplicationResponseTypeDef:
        """
        [Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_component(
        self, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentResponseTypeDef:
        """
        [Client.describe_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_component)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_component_configuration(
        self, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentConfigurationResponseTypeDef:
        """
        [Client.describe_component_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_component_configuration_recommendation(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        Tier: Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
    ) -> DescribeComponentConfigurationRecommendationResponseTypeDef:
        """
        [Client.describe_component_configuration_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration_recommendation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_log_pattern(
        self, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> DescribeLogPatternResponseTypeDef:
        """
        [Client.describe_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_log_pattern)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_observation(self, ObservationId: str) -> DescribeObservationResponseTypeDef:
        """
        [Client.describe_observation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_observation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_problem(self, ProblemId: str) -> DescribeProblemResponseTypeDef:
        """
        [Client.describe_problem documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_problem_observations(
        self, ProblemId: str
    ) -> DescribeProblemObservationsResponseTypeDef:
        """
        [Client.describe_problem_observations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem_observations)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_applications(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.list_applications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_components(
        self, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        [Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.list_components)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_log_pattern_sets(
        self, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLogPatternSetsResponseTypeDef:
        """
        [Client.list_log_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.list_log_pattern_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_log_patterns(
        self,
        ResourceGroupName: str,
        PatternSetName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListLogPatternsResponseTypeDef:
        """
        [Client.list_log_patterns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.list_log_patterns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_problems(
        self,
        ResourceGroupName: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListProblemsResponseTypeDef:
        """
        [Client.list_problems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.list_problems)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        RemoveSNSTopic: bool = None,
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.update_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_component(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        NewComponentName: str = None,
        ResourceList: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.update_component)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_component_configuration(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        Monitor: bool = None,
        Tier: Literal[
            "DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"
        ] = None,
        ComponentConfiguration: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_component_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.update_component_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_log_pattern(
        self,
        ResourceGroupName: str,
        PatternSetName: str,
        PatternName: str,
        Pattern: str = None,
        Rank: int = None,
    ) -> UpdateLogPatternResponseTypeDef:
        """
        [Client.update_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/application-insights.html#ApplicationInsights.Client.update_log_pattern)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TagsAlreadyExistException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    ValidationException: Boto3ClientError
