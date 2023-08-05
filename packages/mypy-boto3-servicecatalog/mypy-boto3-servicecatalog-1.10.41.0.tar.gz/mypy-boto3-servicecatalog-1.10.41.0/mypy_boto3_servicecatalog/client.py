"Main interface for servicecatalog service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_servicecatalog.client as client_scope

# pylint: disable=import-self
import mypy_boto3_servicecatalog.paginator as paginator_scope
from mypy_boto3_servicecatalog.type_defs import (
    AccessLevelFilterTypeDef,
    BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef,
    BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef,
    CopyProductOutputTypeDef,
    CreateConstraintOutputTypeDef,
    CreatePortfolioOutputTypeDef,
    CreatePortfolioShareOutputTypeDef,
    CreateProductOutputTypeDef,
    CreateProvisionedProductPlanOutputTypeDef,
    CreateProvisioningArtifactOutputTypeDef,
    CreateServiceActionOutputTypeDef,
    CreateTagOptionOutputTypeDef,
    DeletePortfolioShareOutputTypeDef,
    DescribeConstraintOutputTypeDef,
    DescribeCopyProductStatusOutputTypeDef,
    DescribePortfolioOutputTypeDef,
    DescribePortfolioShareStatusOutputTypeDef,
    DescribeProductAsAdminOutputTypeDef,
    DescribeProductOutputTypeDef,
    DescribeProductViewOutputTypeDef,
    DescribeProvisionedProductOutputTypeDef,
    DescribeProvisionedProductPlanOutputTypeDef,
    DescribeProvisioningArtifactOutputTypeDef,
    DescribeProvisioningParametersOutputTypeDef,
    DescribeRecordOutputTypeDef,
    DescribeServiceActionExecutionParametersOutputTypeDef,
    DescribeServiceActionOutputTypeDef,
    DescribeTagOptionOutputTypeDef,
    ExecuteProvisionedProductPlanOutputTypeDef,
    ExecuteProvisionedProductServiceActionOutputTypeDef,
    GetAWSOrganizationsAccessStatusOutputTypeDef,
    ListAcceptedPortfolioSharesOutputTypeDef,
    ListBudgetsForResourceOutputTypeDef,
    ListConstraintsForPortfolioOutputTypeDef,
    ListLaunchPathsOutputTypeDef,
    ListOrganizationPortfolioAccessOutputTypeDef,
    ListPortfolioAccessOutputTypeDef,
    ListPortfoliosForProductOutputTypeDef,
    ListPortfoliosOutputTypeDef,
    ListPrincipalsForPortfolioOutputTypeDef,
    ListProvisionedProductPlansOutputTypeDef,
    ListProvisioningArtifactsForServiceActionOutputTypeDef,
    ListProvisioningArtifactsOutputTypeDef,
    ListRecordHistoryOutputTypeDef,
    ListRecordHistorySearchFilterTypeDef,
    ListResourcesForTagOptionOutputTypeDef,
    ListServiceActionsForProvisioningArtifactOutputTypeDef,
    ListServiceActionsOutputTypeDef,
    ListStackInstancesForProvisionedProductOutputTypeDef,
    ListTagOptionsFiltersTypeDef,
    ListTagOptionsOutputTypeDef,
    OrganizationNodeTypeDef,
    ProvisionProductOutputTypeDef,
    ProvisioningArtifactPropertiesTypeDef,
    ProvisioningParameterTypeDef,
    ProvisioningPreferencesTypeDef,
    ScanProvisionedProductsOutputTypeDef,
    SearchProductsAsAdminOutputTypeDef,
    SearchProductsOutputTypeDef,
    SearchProvisionedProductsOutputTypeDef,
    ServiceActionAssociationTypeDef,
    TagTypeDef,
    TerminateProvisionedProductOutputTypeDef,
    UpdateConstraintOutputTypeDef,
    UpdatePortfolioOutputTypeDef,
    UpdateProductOutputTypeDef,
    UpdateProvisionedProductOutputTypeDef,
    UpdateProvisionedProductPropertiesOutputTypeDef,
    UpdateProvisioningArtifactOutputTypeDef,
    UpdateProvisioningParameterTypeDef,
    UpdateProvisioningPreferencesTypeDef,
    UpdateServiceActionOutputTypeDef,
    UpdateTagOptionOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceCatalogClient",)


class ServiceCatalogClient(BaseClient):
    """
    [ServiceCatalog.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.accept_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.accept_portfolio_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_budget_with_resource(self, BudgetName: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Client.associate_budget_with_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_budget_with_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_principal_with_portfolio(
        self,
        PortfolioId: str,
        PrincipalARN: str,
        PrincipalType: Literal["IAM"],
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_principal_with_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_principal_with_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_product_with_portfolio(
        self,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: str = None,
        SourcePortfolioId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_product_with_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_product_with_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_service_action_with_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_service_action_with_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_service_action_with_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_tag_option_with_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_tag_option_with_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_tag_option_with_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_associate_service_action_with_provisioning_artifact(
        self,
        ServiceActionAssociations: List[ServiceActionAssociationTypeDef],
        AcceptLanguage: str = None,
    ) -> BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef:
        """
        [Client.batch_associate_service_action_with_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_associate_service_action_with_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        ServiceActionAssociations: List[ServiceActionAssociationTypeDef],
        AcceptLanguage: str = None,
    ) -> BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef:
        """
        [Client.batch_disassociate_service_action_from_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_disassociate_service_action_from_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_product(
        self,
        SourceProductArn: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        TargetProductId: str = None,
        TargetProductName: str = None,
        SourceProvisioningArtifactIdentifiers: List[Dict[Literal["Id"], str]] = None,
        CopyOptions: List[Literal["CopyTags"]] = None,
    ) -> CopyProductOutputTypeDef:
        """
        [Client.copy_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.copy_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_constraint(
        self,
        PortfolioId: str,
        ProductId: str,
        Parameters: str,
        Type: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
    ) -> CreateConstraintOutputTypeDef:
        """
        [Client.create_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_constraint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_portfolio(
        self,
        DisplayName: str,
        ProviderName: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreatePortfolioOutputTypeDef:
        """
        [Client.create_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: OrganizationNodeTypeDef = None,
    ) -> CreatePortfolioShareOutputTypeDef:
        """
        [Client.create_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_product(
        self,
        Name: str,
        Owner: str,
        ProductType: Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        ProvisioningArtifactParameters: ProvisioningArtifactPropertiesTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateProductOutputTypeDef:
        """
        [Client.create_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_provisioned_product_plan(
        self,
        PlanName: str,
        PlanType: Literal["CLOUDFORMATION"],
        ProductId: str,
        ProvisionedProductName: str,
        ProvisioningArtifactId: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        NotificationArns: List[str] = None,
        PathId: str = None,
        ProvisioningParameters: List[UpdateProvisioningParameterTypeDef] = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateProvisionedProductPlanOutputTypeDef:
        """
        [Client.create_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioned_product_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_provisioning_artifact(
        self,
        ProductId: str,
        Parameters: ProvisioningArtifactPropertiesTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> CreateProvisioningArtifactOutputTypeDef:
        """
        [Client.create_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_service_action(
        self,
        Name: str,
        DefinitionType: Literal["SSM_AUTOMATION"],
        Definition: Dict[Literal["Name", "Version", "AssumeRole", "Parameters"], str],
        IdempotencyToken: str,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> CreateServiceActionOutputTypeDef:
        """
        [Client.create_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_service_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tag_option(self, Key: str, Value: str) -> CreateTagOptionOutputTypeDef:
        """
        [Client.create_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.create_tag_option)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_constraint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: OrganizationNodeTypeDef = None,
    ) -> DeletePortfolioShareOutputTypeDef:
        """
        [Client.delete_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_product(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_provisioned_product_plan(
        self, PlanId: str, AcceptLanguage: str = None, IgnoreErrors: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioned_product_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_provisioning_artifact(
        self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_service_action(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_service_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tag_option(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_tag_option)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_constraint(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeConstraintOutputTypeDef:
        """
        [Client.describe_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_constraint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_copy_product_status(
        self, CopyProductToken: str, AcceptLanguage: str = None
    ) -> DescribeCopyProductStatusOutputTypeDef:
        """
        [Client.describe_copy_product_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_copy_product_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_portfolio(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribePortfolioOutputTypeDef:
        """
        [Client.describe_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_portfolio_share_status(
        self, PortfolioShareToken: str
    ) -> DescribePortfolioShareStatusOutputTypeDef:
        """
        [Client.describe_portfolio_share_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio_share_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_product(self, Id: str, AcceptLanguage: str = None) -> DescribeProductOutputTypeDef:
        """
        [Client.describe_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_product_as_admin(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeProductAsAdminOutputTypeDef:
        """
        [Client.describe_product_as_admin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_as_admin)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_product_view(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeProductViewOutputTypeDef:
        """
        [Client.describe_product_view documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_view)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_provisioned_product(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeProvisionedProductOutputTypeDef:
        """
        [Client.describe_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_provisioned_product_plan(
        self, PlanId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> DescribeProvisionedProductPlanOutputTypeDef:
        """
        [Client.describe_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_provisioning_artifact(
        self,
        ProvisioningArtifactId: str,
        ProductId: str,
        AcceptLanguage: str = None,
        Verbose: bool = None,
    ) -> DescribeProvisioningArtifactOutputTypeDef:
        """
        [Client.describe_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_provisioning_parameters(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        PathId: str = None,
    ) -> DescribeProvisioningParametersOutputTypeDef:
        """
        [Client.describe_provisioning_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_record(
        self, Id: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> DescribeRecordOutputTypeDef:
        """
        [Client.describe_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_record)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_service_action(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeServiceActionOutputTypeDef:
        """
        [Client.describe_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_service_action_execution_parameters(
        self, ProvisionedProductId: str, ServiceActionId: str, AcceptLanguage: str = None
    ) -> DescribeServiceActionExecutionParametersOutputTypeDef:
        """
        [Client.describe_service_action_execution_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action_execution_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tag_option(self, Id: str) -> DescribeTagOptionOutputTypeDef:
        """
        [Client.describe_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_tag_option)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        [Client.disable_aws_organizations_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.disable_aws_organizations_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_budget_from_resource(self, BudgetName: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_budget_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_budget_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_principal_from_portfolio(
        self, PortfolioId: str, PrincipalARN: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_principal_from_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_principal_from_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_product_from_portfolio(
        self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_product_from_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_product_from_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_service_action_from_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_service_action_from_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_service_action_from_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_tag_option_from_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_tag_option_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_tag_option_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        [Client.enable_aws_organizations_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.enable_aws_organizations_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_provisioned_product_plan(
        self, PlanId: str, IdempotencyToken: str, AcceptLanguage: str = None
    ) -> ExecuteProvisionedProductPlanOutputTypeDef:
        """
        [Client.execute_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_provisioned_product_service_action(
        self,
        ProvisionedProductId: str,
        ServiceActionId: str,
        ExecuteToken: str,
        AcceptLanguage: str = None,
        Parameters: Dict[str, List[str]] = None,
    ) -> ExecuteProvisionedProductServiceActionOutputTypeDef:
        """
        [Client.execute_provisioned_product_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_service_action)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_aws_organizations_access_status(self) -> GetAWSOrganizationsAccessStatusOutputTypeDef:
        """
        [Client.get_aws_organizations_access_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.get_aws_organizations_access_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accepted_portfolio_shares(
        self,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
    ) -> ListAcceptedPortfolioSharesOutputTypeDef:
        """
        [Client.list_accepted_portfolio_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_accepted_portfolio_shares)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_budgets_for_resource(
        self,
        ResourceId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListBudgetsForResourceOutputTypeDef:
        """
        [Client.list_budgets_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_budgets_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_constraints_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListConstraintsForPortfolioOutputTypeDef:
        """
        [Client.list_constraints_for_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_constraints_for_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_launch_paths(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListLaunchPathsOutputTypeDef:
        """
        [Client.list_launch_paths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_launch_paths)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_organization_portfolio_access(
        self,
        PortfolioId: str,
        OrganizationNodeType: Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"],
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ListOrganizationPortfolioAccessOutputTypeDef:
        """
        [Client.list_organization_portfolio_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_organization_portfolio_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_portfolio_access(
        self, PortfolioId: str, AcceptLanguage: str = None
    ) -> ListPortfolioAccessOutputTypeDef:
        """
        [Client.list_portfolio_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolio_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_portfolios(
        self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> ListPortfoliosOutputTypeDef:
        """
        [Client.list_portfolios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_portfolios_for_product(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ListPortfoliosForProductOutputTypeDef:
        """
        [Client.list_portfolios_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios_for_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_principals_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListPrincipalsForPortfolioOutputTypeDef:
        """
        [Client.list_principals_for_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_principals_for_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioned_product_plans(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
    ) -> ListProvisionedProductPlansOutputTypeDef:
        """
        [Client.list_provisioned_product_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioned_product_plans)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioning_artifacts(
        self, ProductId: str, AcceptLanguage: str = None
    ) -> ListProvisioningArtifactsOutputTypeDef:
        """
        [Client.list_provisioning_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioning_artifacts_for_service_action(
        self,
        ServiceActionId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> ListProvisioningArtifactsForServiceActionOutputTypeDef:
        """
        [Client.list_provisioning_artifacts_for_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts_for_service_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_record_history(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        SearchFilter: ListRecordHistorySearchFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListRecordHistoryOutputTypeDef:
        """
        [Client.list_record_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_record_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resources_for_tag_option(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListResourcesForTagOptionOutputTypeDef:
        """
        [Client.list_resources_for_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_resources_for_tag_option)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_service_actions(
        self, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> ListServiceActionsOutputTypeDef:
        """
        [Client.list_service_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_service_actions_for_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> ListServiceActionsForProvisioningArtifactOutputTypeDef:
        """
        [Client.list_service_actions_for_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions_for_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stack_instances_for_provisioned_product(
        self,
        ProvisionedProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ListStackInstancesForProvisionedProductOutputTypeDef:
        """
        [Client.list_stack_instances_for_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_stack_instances_for_provisioned_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tag_options(
        self,
        Filters: ListTagOptionsFiltersTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListTagOptionsOutputTypeDef:
        """
        [Client.list_tag_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.list_tag_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def provision_product(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ProvisionedProductName: str,
        ProvisionToken: str,
        AcceptLanguage: str = None,
        PathId: str = None,
        ProvisioningParameters: List[ProvisioningParameterTypeDef] = None,
        ProvisioningPreferences: ProvisioningPreferencesTypeDef = None,
        Tags: List[TagTypeDef] = None,
        NotificationArns: List[str] = None,
    ) -> ProvisionProductOutputTypeDef:
        """
        [Client.provision_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.provision_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.reject_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.reject_portfolio_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def scan_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ScanProvisionedProductsOutputTypeDef:
        """
        [Client.scan_provisioned_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.scan_provisioned_products)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_products(
        self,
        AcceptLanguage: str = None,
        Filters: Dict[
            Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"], List[str]
        ] = None,
        PageSize: int = None,
        SortBy: Literal["Title", "VersionCount", "CreationDate"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PageToken: str = None,
    ) -> SearchProductsOutputTypeDef:
        """
        [Client.search_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_products_as_admin(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[
            Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"], List[str]
        ] = None,
        SortBy: Literal["Title", "VersionCount", "CreationDate"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PageToken: str = None,
        PageSize: int = None,
        ProductSource: Literal["ACCOUNT"] = None,
    ) -> SearchProductsAsAdminOutputTypeDef:
        """
        [Client.search_products_as_admin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products_as_admin)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        Filters: Dict[Literal["SearchQuery"], List[str]] = None,
        SortBy: str = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> SearchProvisionedProductsOutputTypeDef:
        """
        [Client.search_provisioned_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.search_provisioned_products)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_provisioned_product(
        self,
        TerminateToken: str,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        IgnoreErrors: bool = None,
        AcceptLanguage: str = None,
    ) -> TerminateProvisionedProductOutputTypeDef:
        """
        [Client.terminate_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.terminate_provisioned_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_constraint(
        self, Id: str, AcceptLanguage: str = None, Description: str = None, Parameters: str = None
    ) -> UpdateConstraintOutputTypeDef:
        """
        [Client.update_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_constraint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_portfolio(
        self,
        Id: str,
        AcceptLanguage: str = None,
        DisplayName: str = None,
        Description: str = None,
        ProviderName: str = None,
        AddTags: List[TagTypeDef] = None,
        RemoveTags: List[str] = None,
    ) -> UpdatePortfolioOutputTypeDef:
        """
        [Client.update_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_portfolio)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_product(
        self,
        Id: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Owner: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        AddTags: List[TagTypeDef] = None,
        RemoveTags: List[str] = None,
    ) -> UpdateProductOutputTypeDef:
        """
        [Client.update_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_provisioned_product(
        self,
        UpdateToken: str,
        AcceptLanguage: str = None,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        ProductId: str = None,
        ProvisioningArtifactId: str = None,
        PathId: str = None,
        ProvisioningParameters: List[UpdateProvisioningParameterTypeDef] = None,
        ProvisioningPreferences: UpdateProvisioningPreferencesTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> UpdateProvisionedProductOutputTypeDef:
        """
        [Client.update_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_provisioned_product_properties(
        self,
        ProvisionedProductId: str,
        ProvisionedProductProperties: Dict[Literal["OWNER"], str],
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> UpdateProvisionedProductPropertiesOutputTypeDef:
        """
        [Client.update_provisioned_product_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Description: str = None,
        Active: bool = None,
        Guidance: Literal["DEFAULT", "DEPRECATED"] = None,
    ) -> UpdateProvisioningArtifactOutputTypeDef:
        """
        [Client.update_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioning_artifact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_service_action(
        self,
        Id: str,
        Name: str = None,
        Definition: Dict[Literal["Name", "Version", "AssumeRole", "Parameters"], str] = None,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> UpdateServiceActionOutputTypeDef:
        """
        [Client.update_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_service_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_tag_option(
        self, Id: str, Value: str = None, Active: bool = None
    ) -> UpdateTagOptionOutputTypeDef:
        """
        [Client.update_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Client.update_tag_option)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accepted_portfolio_shares"]
    ) -> paginator_scope.ListAcceptedPortfolioSharesPaginator:
        """
        [Paginator.ListAcceptedPortfolioShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_constraints_for_portfolio"]
    ) -> paginator_scope.ListConstraintsForPortfolioPaginator:
        """
        [Paginator.ListConstraintsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_launch_paths"]
    ) -> paginator_scope.ListLaunchPathsPaginator:
        """
        [Paginator.ListLaunchPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_organization_portfolio_access"]
    ) -> paginator_scope.ListOrganizationPortfolioAccessPaginator:
        """
        [Paginator.ListOrganizationPortfolioAccess documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_portfolios"]
    ) -> paginator_scope.ListPortfoliosPaginator:
        """
        [Paginator.ListPortfolios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_portfolios_for_product"]
    ) -> paginator_scope.ListPortfoliosForProductPaginator:
        """
        [Paginator.ListPortfoliosForProduct documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_principals_for_portfolio"]
    ) -> paginator_scope.ListPrincipalsForPortfolioPaginator:
        """
        [Paginator.ListPrincipalsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_provisioned_product_plans"]
    ) -> paginator_scope.ListProvisionedProductPlansPaginator:
        """
        [Paginator.ListProvisionedProductPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_provisioning_artifacts_for_service_action"]
    ) -> paginator_scope.ListProvisioningArtifactsForServiceActionPaginator:
        """
        [Paginator.ListProvisioningArtifactsForServiceAction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_record_history"]
    ) -> paginator_scope.ListRecordHistoryPaginator:
        """
        [Paginator.ListRecordHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resources_for_tag_option"]
    ) -> paginator_scope.ListResourcesForTagOptionPaginator:
        """
        [Paginator.ListResourcesForTagOption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_service_actions"]
    ) -> paginator_scope.ListServiceActionsPaginator:
        """
        [Paginator.ListServiceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_service_actions_for_provisioning_artifact"]
    ) -> paginator_scope.ListServiceActionsForProvisioningArtifactPaginator:
        """
        [Paginator.ListServiceActionsForProvisioningArtifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tag_options"]
    ) -> paginator_scope.ListTagOptionsPaginator:
        """
        [Paginator.ListTagOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["scan_provisioned_products"]
    ) -> paginator_scope.ScanProvisionedProductsPaginator:
        """
        [Paginator.ScanProvisionedProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_products_as_admin"]
    ) -> paginator_scope.SearchProductsAsAdminPaginator:
        """
        [Paginator.SearchProductsAsAdmin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DuplicateResourceException: Boto3ClientError
    InvalidParametersException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OperationNotSupportedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TagOptionNotMigratedException: Boto3ClientError
