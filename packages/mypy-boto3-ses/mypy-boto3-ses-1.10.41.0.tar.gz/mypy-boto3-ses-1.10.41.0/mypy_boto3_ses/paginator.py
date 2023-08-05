"Main interface for ses service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ses.type_defs import (
    ListConfigurationSetsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListIdentitiesResponseTypeDef,
    ListReceiptRuleSetsResponseTypeDef,
    ListTemplatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListConfigurationSetsPaginator",
    "ListCustomVerificationEmailTemplatesPaginator",
    "ListIdentitiesPaginator",
    "ListReceiptRuleSetsPaginator",
    "ListTemplatesPaginator",
)


class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListConfigurationSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConfigurationSetsResponseTypeDef, None, None]:
        """
        [ListConfigurationSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListConfigurationSets.paginate)
        """


class ListCustomVerificationEmailTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListCustomVerificationEmailTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCustomVerificationEmailTemplatesResponseTypeDef, None, None]:
        """
        [ListCustomVerificationEmailTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates.paginate)
        """


class ListIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListIdentities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        IdentityType: Literal["EmailAddress", "Domain"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListIdentitiesResponseTypeDef, None, None]:
        """
        [ListIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListIdentities.paginate)
        """


class ListReceiptRuleSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListReceiptRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListReceiptRuleSetsResponseTypeDef, None, None]:
        """
        [ListReceiptRuleSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets.paginate)
        """


class ListTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListTemplates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTemplatesResponseTypeDef, None, None]:
        """
        [ListTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ses.html#SES.Paginator.ListTemplates.paginate)
        """
