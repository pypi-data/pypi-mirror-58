"Main interface for service-quotas service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_service_quotas.type_defs import (
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAWSDefaultServiceQuotasPaginator",
    "ListRequestedServiceQuotaChangeHistoryPaginator",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginator",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginator",
    "ListServiceQuotasPaginator",
    "ListServicesPaginator",
)


class ListAWSDefaultServiceQuotasPaginator(Boto3Paginator):
    """
    [Paginator.ListAWSDefaultServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ServiceCode: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAWSDefaultServiceQuotasResponseTypeDef, None, None]:
        """
        [ListAWSDefaultServiceQuotas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas.paginate)
        """


class ListRequestedServiceQuotaChangeHistoryPaginator(Boto3Paginator):
    """
    [Paginator.ListRequestedServiceQuotaChangeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRequestedServiceQuotaChangeHistoryResponseTypeDef, None, None]:
        """
        [ListRequestedServiceQuotaChangeHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory.paginate)
        """


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginator(Boto3Paginator):
    """
    [Paginator.ListRequestedServiceQuotaChangeHistoryByQuota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef, None, None]:
        """
        [ListRequestedServiceQuotaChangeHistoryByQuota.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota.paginate)
        """


class ListServiceQuotaIncreaseRequestsInTemplatePaginator(Boto3Paginator):
    """
    [Paginator.ListServiceQuotaIncreaseRequestsInTemplate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef, None, None]:
        """
        [ListServiceQuotaIncreaseRequestsInTemplate.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate.paginate)
        """


class ListServiceQuotasPaginator(Boto3Paginator):
    """
    [Paginator.ListServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ServiceCode: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListServiceQuotasResponseTypeDef, None, None]:
        """
        [ListServiceQuotas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListServicesResponseTypeDef, None, None]:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices.paginate)
        """
