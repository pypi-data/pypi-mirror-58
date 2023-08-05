"Main interface for cur service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cur.type_defs import (
    DescribeReportDefinitionsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeReportDefinitionsPaginator",)


class DescribeReportDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReportDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeReportDefinitionsResponseTypeDef, None, None]:
        """
        [DescribeReportDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions.paginate)
        """
