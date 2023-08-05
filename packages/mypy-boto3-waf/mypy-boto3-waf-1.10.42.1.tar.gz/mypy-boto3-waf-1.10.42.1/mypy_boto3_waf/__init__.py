"Main interface for waf service"
from mypy_boto3_waf.client import WAFClient as Client, WAFClient
from mypy_boto3_waf.paginator import (
    GetRateBasedRuleManagedKeysPaginator,
    ListActivatedRulesInRuleGroupPaginator,
    ListByteMatchSetsPaginator,
    ListGeoMatchSetsPaginator,
    ListIPSetsPaginator,
    ListLoggingConfigurationsPaginator,
    ListRateBasedRulesPaginator,
    ListRegexMatchSetsPaginator,
    ListRegexPatternSetsPaginator,
    ListRuleGroupsPaginator,
    ListRulesPaginator,
    ListSizeConstraintSetsPaginator,
    ListSqlInjectionMatchSetsPaginator,
    ListSubscribedRuleGroupsPaginator,
    ListWebACLsPaginator,
    ListXssMatchSetsPaginator,
)


__all__ = (
    "Client",
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
    "WAFClient",
)
