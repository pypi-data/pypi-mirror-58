"Main interface for application-insights service"
from mypy_boto3_application_insights.client import (
    ApplicationInsightsClient as Client,
    ApplicationInsightsClient,
)


__all__ = ("ApplicationInsightsClient", "Client")
