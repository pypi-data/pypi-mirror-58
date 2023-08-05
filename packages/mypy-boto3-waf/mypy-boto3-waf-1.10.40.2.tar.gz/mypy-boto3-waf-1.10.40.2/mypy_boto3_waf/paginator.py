"Main interface for waf service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_waf.type_defs import (
    GetRateBasedRuleManagedKeysResponseTypeDef,
    ListActivatedRulesInRuleGroupResponseTypeDef,
    ListByteMatchSetsResponseTypeDef,
    ListGeoMatchSetsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRateBasedRulesResponseTypeDef,
    ListRegexMatchSetsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListRulesResponseTypeDef,
    ListSizeConstraintSetsResponseTypeDef,
    ListSqlInjectionMatchSetsResponseTypeDef,
    ListSubscribedRuleGroupsResponseTypeDef,
    ListWebACLsResponseTypeDef,
    ListXssMatchSetsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetRateBasedRuleManagedKeysPaginator",
    "ListActivatedRulesInRuleGroupPaginator",
    "ListByteMatchSetsPaginator",
    "ListGeoMatchSetsPaginator",
    "ListIPSetsPaginator",
    "ListLoggingConfigurationsPaginator",
    "ListRateBasedRulesPaginator",
    "ListRegexMatchSetsPaginator",
    "ListRegexPatternSetsPaginator",
    "ListRuleGroupsPaginator",
    "ListRulesPaginator",
    "ListSizeConstraintSetsPaginator",
    "ListSqlInjectionMatchSetsPaginator",
    "ListSubscribedRuleGroupsPaginator",
    "ListWebACLsPaginator",
    "ListXssMatchSetsPaginator",
)


class GetRateBasedRuleManagedKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetRateBasedRuleManagedKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RuleId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRateBasedRuleManagedKeysResponseTypeDef, None, None]:
        """
        [GetRateBasedRuleManagedKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys.paginate)
        """


class ListActivatedRulesInRuleGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListActivatedRulesInRuleGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RuleGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListActivatedRulesInRuleGroupResponseTypeDef, None, None]:
        """
        [ListActivatedRulesInRuleGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup.paginate)
        """


class ListByteMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListByteMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListByteMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListByteMatchSetsResponseTypeDef, None, None]:
        """
        [ListByteMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListByteMatchSets.paginate)
        """


class ListGeoMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListGeoMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGeoMatchSetsResponseTypeDef, None, None]:
        """
        [ListGeoMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets.paginate)
        """


class ListIPSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListIPSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListIPSetsResponseTypeDef, None, None]:
        """
        [ListIPSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListIPSets.paginate)
        """


class ListLoggingConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListLoggingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLoggingConfigurationsResponseTypeDef, None, None]:
        """
        [ListLoggingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations.paginate)
        """


class ListRateBasedRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRateBasedRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRateBasedRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRateBasedRulesResponseTypeDef, None, None]:
        """
        [ListRateBasedRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRateBasedRules.paginate)
        """


class ListRegexMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRegexMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRegexMatchSetsResponseTypeDef, None, None]:
        """
        [ListRegexMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets.paginate)
        """


class ListRegexPatternSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRegexPatternSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRegexPatternSetsResponseTypeDef, None, None]:
        """
        [ListRegexPatternSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets.paginate)
        """


class ListRuleGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRuleGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRuleGroupsResponseTypeDef, None, None]:
        """
        [ListRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRuleGroups.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRulesResponseTypeDef, None, None]:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListRules.paginate)
        """


class ListSizeConstraintSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListSizeConstraintSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSizeConstraintSetsResponseTypeDef, None, None]:
        """
        [ListSizeConstraintSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets.paginate)
        """


class ListSqlInjectionMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListSqlInjectionMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSqlInjectionMatchSetsResponseTypeDef, None, None]:
        """
        [ListSqlInjectionMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets.paginate)
        """


class ListSubscribedRuleGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscribedRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscribedRuleGroupsResponseTypeDef, None, None]:
        """
        [ListSubscribedRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups.paginate)
        """


class ListWebACLsPaginator(Boto3Paginator):
    """
    [Paginator.ListWebACLs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListWebACLs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListWebACLsResponseTypeDef, None, None]:
        """
        [ListWebACLs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListWebACLs.paginate)
        """


class ListXssMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListXssMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListXssMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListXssMatchSetsResponseTypeDef, None, None]:
        """
        [ListXssMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/waf.html#WAF.Paginator.ListXssMatchSets.paginate)
        """
