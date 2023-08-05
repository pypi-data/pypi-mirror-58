"Main interface for servicecatalog service Paginators"
from __future__ import annotations

import sys
from typing import Dict, Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_servicecatalog.type_defs import (
    AccessLevelFilterTypeDef,
    ListAcceptedPortfolioSharesOutputTypeDef,
    ListConstraintsForPortfolioOutputTypeDef,
    ListLaunchPathsOutputTypeDef,
    ListOrganizationPortfolioAccessOutputTypeDef,
    ListPortfoliosForProductOutputTypeDef,
    ListPortfoliosOutputTypeDef,
    ListPrincipalsForPortfolioOutputTypeDef,
    ListProvisionedProductPlansOutputTypeDef,
    ListProvisioningArtifactsForServiceActionOutputTypeDef,
    ListRecordHistoryOutputTypeDef,
    ListRecordHistorySearchFilterTypeDef,
    ListResourcesForTagOptionOutputTypeDef,
    ListServiceActionsForProvisioningArtifactOutputTypeDef,
    ListServiceActionsOutputTypeDef,
    ListTagOptionsFiltersTypeDef,
    ListTagOptionsOutputTypeDef,
    PaginatorConfigTypeDef,
    ScanProvisionedProductsOutputTypeDef,
    SearchProductsAsAdminOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAcceptedPortfolioSharesPaginator",
    "ListConstraintsForPortfolioPaginator",
    "ListLaunchPathsPaginator",
    "ListOrganizationPortfolioAccessPaginator",
    "ListPortfoliosPaginator",
    "ListPortfoliosForProductPaginator",
    "ListPrincipalsForPortfolioPaginator",
    "ListProvisionedProductPlansPaginator",
    "ListProvisioningArtifactsForServiceActionPaginator",
    "ListRecordHistoryPaginator",
    "ListResourcesForTagOptionPaginator",
    "ListServiceActionsPaginator",
    "ListServiceActionsForProvisioningArtifactPaginator",
    "ListTagOptionsPaginator",
    "ScanProvisionedProductsPaginator",
    "SearchProductsAsAdminPaginator",
)


class ListAcceptedPortfolioSharesPaginator(Boto3Paginator):
    """
    [Paginator.ListAcceptedPortfolioShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAcceptedPortfolioSharesOutputTypeDef, None, None]:
        """
        [ListAcceptedPortfolioShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares.paginate)
        """


class ListConstraintsForPortfolioPaginator(Boto3Paginator):
    """
    [Paginator.ListConstraintsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListConstraintsForPortfolioOutputTypeDef, None, None]:
        """
        [ListConstraintsForPortfolio.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio.paginate)
        """


class ListLaunchPathsPaginator(Boto3Paginator):
    """
    [Paginator.ListLaunchPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListLaunchPathsOutputTypeDef, None, None]:
        """
        [ListLaunchPaths.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths.paginate)
        """


class ListOrganizationPortfolioAccessPaginator(Boto3Paginator):
    """
    [Paginator.ListOrganizationPortfolioAccess documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PortfolioId: str,
        OrganizationNodeType: Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"],
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOrganizationPortfolioAccessOutputTypeDef, None, None]:
        """
        [ListOrganizationPortfolioAccess.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess.paginate)
        """


class ListPortfoliosPaginator(Boto3Paginator):
    """
    [Paginator.ListPortfolios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AcceptLanguage: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPortfoliosOutputTypeDef, None, None]:
        """
        [ListPortfolios.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios.paginate)
        """


class ListPortfoliosForProductPaginator(Boto3Paginator):
    """
    [Paginator.ListPortfoliosForProduct documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPortfoliosForProductOutputTypeDef, None, None]:
        """
        [ListPortfoliosForProduct.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct.paginate)
        """


class ListPrincipalsForPortfolioPaginator(Boto3Paginator):
    """
    [Paginator.ListPrincipalsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPrincipalsForPortfolioOutputTypeDef, None, None]:
        """
        [ListPrincipalsForPortfolio.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio.paginate)
        """


class ListProvisionedProductPlansPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisionedProductPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListProvisionedProductPlansOutputTypeDef, None, None]:
        """
        [ListProvisionedProductPlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans.paginate)
        """


class ListProvisioningArtifactsForServiceActionPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisioningArtifactsForServiceAction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceActionId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListProvisioningArtifactsForServiceActionOutputTypeDef, None, None]:
        """
        [ListProvisioningArtifactsForServiceAction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction.paginate)
        """


class ListRecordHistoryPaginator(Boto3Paginator):
    """
    [Paginator.ListRecordHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        SearchFilter: ListRecordHistorySearchFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRecordHistoryOutputTypeDef, None, None]:
        """
        [ListRecordHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory.paginate)
        """


class ListResourcesForTagOptionPaginator(Boto3Paginator):
    """
    [Paginator.ListResourcesForTagOption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListResourcesForTagOptionOutputTypeDef, None, None]:
        """
        [ListResourcesForTagOption.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption.paginate)
        """


class ListServiceActionsPaginator(Boto3Paginator):
    """
    [Paginator.ListServiceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AcceptLanguage: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListServiceActionsOutputTypeDef, None, None]:
        """
        [ListServiceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions.paginate)
        """


class ListServiceActionsForProvisioningArtifactPaginator(Boto3Paginator):
    """
    [Paginator.ListServiceActionsForProvisioningArtifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListServiceActionsForProvisioningArtifactOutputTypeDef, None, None]:
        """
        [ListServiceActionsForProvisioningArtifact.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact.paginate)
        """


class ListTagOptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListTagOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: ListTagOptionsFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTagOptionsOutputTypeDef, None, None]:
        """
        [ListTagOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions.paginate)
        """


class ScanProvisionedProductsPaginator(Boto3Paginator):
    """
    [Paginator.ScanProvisionedProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ScanProvisionedProductsOutputTypeDef, None, None]:
        """
        [ScanProvisionedProducts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts.paginate)
        """


class SearchProductsAsAdminPaginator(Boto3Paginator):
    """
    [Paginator.SearchProductsAsAdmin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[
            Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"], List[str]
        ] = None,
        SortBy: Literal["Title", "VersionCount", "CreationDate"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        ProductSource: Literal["ACCOUNT"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchProductsAsAdminOutputTypeDef, None, None]:
        """
        [SearchProductsAsAdmin.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin.paginate)
        """
