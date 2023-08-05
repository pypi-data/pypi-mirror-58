"Main interface for accessanalyzer service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CreateAnalyzerResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseTypeDef", {"arn": str}, total=False
)

CriterionTypeDef = TypedDict(
    "CriterionTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)

_RequiredAnalyzedResourceTypeDef = TypedDict(
    "_RequiredAnalyzedResourceTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "isPublic": bool,
        "resourceArn": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
        "updatedAt": datetime,
    },
)
_OptionalAnalyzedResourceTypeDef = TypedDict(
    "_OptionalAnalyzedResourceTypeDef",
    {
        "actions": List[str],
        "error": str,
        "sharedVia": List[str],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
    },
    total=False,
)


class AnalyzedResourceTypeDef(_RequiredAnalyzedResourceTypeDef, _OptionalAnalyzedResourceTypeDef):
    pass


GetAnalyzedResourceResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseTypeDef", {"resource": AnalyzedResourceTypeDef}, total=False
)

_RequiredAnalyzerSummaryTypeDef = TypedDict(
    "_RequiredAnalyzerSummaryTypeDef",
    {"arn": str, "createdAt": datetime, "name": str, "type": Literal["ACCOUNT"]},
)
_OptionalAnalyzerSummaryTypeDef = TypedDict(
    "_OptionalAnalyzerSummaryTypeDef",
    {"lastResourceAnalyzed": str, "lastResourceAnalyzedAt": datetime, "tags": Dict[str, str]},
    total=False,
)


class AnalyzerSummaryTypeDef(_RequiredAnalyzerSummaryTypeDef, _OptionalAnalyzerSummaryTypeDef):
    pass


GetAnalyzerResponseTypeDef = TypedDict(
    "GetAnalyzerResponseTypeDef", {"analyzer": AnalyzerSummaryTypeDef}
)

ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, CriterionTypeDef],
        "ruleName": str,
        "updatedAt": datetime,
    },
)

GetArchiveRuleResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseTypeDef", {"archiveRule": ArchiveRuleSummaryTypeDef}
)

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


GetFindingResponseTypeDef = TypedDict(
    "GetFindingResponseTypeDef", {"finding": FindingTypeDef}, total=False
)

InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef", {"filter": Dict[str, CriterionTypeDef], "ruleName": str}
)

AnalyzedResourceSummaryTypeDef = TypedDict(
    "AnalyzedResourceSummaryTypeDef",
    {
        "resourceArn": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
    },
)

_RequiredListAnalyzedResourcesResponseTypeDef = TypedDict(
    "_RequiredListAnalyzedResourcesResponseTypeDef",
    {"analyzedResources": List[AnalyzedResourceSummaryTypeDef]},
)
_OptionalListAnalyzedResourcesResponseTypeDef = TypedDict(
    "_OptionalListAnalyzedResourcesResponseTypeDef", {"nextToken": str}, total=False
)


class ListAnalyzedResourcesResponseTypeDef(
    _RequiredListAnalyzedResourcesResponseTypeDef, _OptionalListAnalyzedResourcesResponseTypeDef
):
    pass


_RequiredListAnalyzersResponseTypeDef = TypedDict(
    "_RequiredListAnalyzersResponseTypeDef", {"analyzers": List[AnalyzerSummaryTypeDef]}
)
_OptionalListAnalyzersResponseTypeDef = TypedDict(
    "_OptionalListAnalyzersResponseTypeDef", {"nextToken": str}, total=False
)


class ListAnalyzersResponseTypeDef(
    _RequiredListAnalyzersResponseTypeDef, _OptionalListAnalyzersResponseTypeDef
):
    pass


_RequiredListArchiveRulesResponseTypeDef = TypedDict(
    "_RequiredListArchiveRulesResponseTypeDef", {"archiveRules": List[ArchiveRuleSummaryTypeDef]}
)
_OptionalListArchiveRulesResponseTypeDef = TypedDict(
    "_OptionalListArchiveRulesResponseTypeDef", {"nextToken": str}, total=False
)


class ListArchiveRulesResponseTypeDef(
    _RequiredListArchiveRulesResponseTypeDef, _OptionalListArchiveRulesResponseTypeDef
):
    pass


_RequiredFindingSummaryTypeDef = TypedDict(
    "_RequiredFindingSummaryTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
        "updatedAt": datetime,
    },
)
_OptionalFindingSummaryTypeDef = TypedDict(
    "_OptionalFindingSummaryTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
    },
    total=False,
)


class FindingSummaryTypeDef(_RequiredFindingSummaryTypeDef, _OptionalFindingSummaryTypeDef):
    pass


_RequiredListFindingsResponseTypeDef = TypedDict(
    "_RequiredListFindingsResponseTypeDef", {"findings": List[FindingSummaryTypeDef]}
)
_OptionalListFindingsResponseTypeDef = TypedDict(
    "_OptionalListFindingsResponseTypeDef", {"nextToken": str}, total=False
)


class ListFindingsResponseTypeDef(
    _RequiredListFindingsResponseTypeDef, _OptionalListFindingsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef", {"attributeName": str, "orderBy": Literal["ASC", "DESC"]}, total=False
)
