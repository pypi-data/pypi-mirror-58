"Main interface for cur service"
from mypy_boto3_cur.client import (
    CostandUsageReportServiceClient as Client,
    CostandUsageReportServiceClient,
)
from mypy_boto3_cur.paginator import DescribeReportDefinitionsPaginator


__all__ = ("Client", "CostandUsageReportServiceClient", "DescribeReportDefinitionsPaginator")
