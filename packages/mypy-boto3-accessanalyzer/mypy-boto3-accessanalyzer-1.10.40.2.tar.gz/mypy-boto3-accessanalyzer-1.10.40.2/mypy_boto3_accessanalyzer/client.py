"Main interface for accessanalyzer service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_accessanalyzer.client as client_scope
from mypy_boto3_accessanalyzer.type_defs import (
    CreateAnalyzerResponseTypeDef,
    CriterionTypeDef,
    GetAnalyzedResourceResponseTypeDef,
    GetAnalyzerResponseTypeDef,
    GetArchiveRuleResponseTypeDef,
    GetFindingResponseTypeDef,
    InlineArchiveRuleTypeDef,
    ListAnalyzedResourcesResponseTypeDef,
    ListAnalyzersResponseTypeDef,
    ListArchiveRulesResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SortCriteriaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AccessAnalyzerClient",)


class AccessAnalyzerClient(BaseClient):
    """
    [AccessAnalyzer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_analyzer(
        self,
        analyzerName: str,
        type: Literal["ACCOUNT"],
        archiveRules: List[InlineArchiveRuleTypeDef] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAnalyzerResponseTypeDef:
        """
        [Client.create_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_analyzer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_archive_rule(
        self,
        analyzerName: str,
        filter: Dict[str, CriterionTypeDef],
        ruleName: str,
        clientToken: str = None,
    ) -> None:
        """
        [Client.create_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_archive_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_analyzer(self, analyzerName: str, clientToken: str = None) -> None:
        """
        [Client.delete_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_analyzer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_archive_rule(
        self, analyzerName: str, ruleName: str, clientToken: str = None
    ) -> None:
        """
        [Client.delete_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_archive_rule)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_analyzed_resource(
        self, analyzerArn: str, resourceArn: str
    ) -> GetAnalyzedResourceResponseTypeDef:
        """
        [Client.get_analyzed_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzed_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_analyzer(self, analyzerName: str) -> GetAnalyzerResponseTypeDef:
        """
        [Client.get_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_archive_rule(self, analyzerName: str, ruleName: str) -> GetArchiveRuleResponseTypeDef:
        """
        [Client.get_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_archive_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_finding(self, analyzerArn: str, id: str) -> GetFindingResponseTypeDef:
        """
        [Client.get_finding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_finding)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_analyzed_resources(
        self,
        analyzerArn: str,
        maxResults: int = None,
        nextToken: str = None,
        resourceType: Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ] = None,
    ) -> ListAnalyzedResourcesResponseTypeDef:
        """
        [Client.list_analyzed_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzed_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_analyzers(
        self, maxResults: int = None, nextToken: str = None, type: Literal["ACCOUNT"] = None
    ) -> ListAnalyzersResponseTypeDef:
        """
        [Client.list_analyzers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_archive_rules(
        self, analyzerName: str, maxResults: int = None, nextToken: str = None
    ) -> ListArchiveRulesResponseTypeDef:
        """
        [Client.list_archive_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_archive_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_findings(
        self,
        analyzerArn: str,
        filter: Dict[str, CriterionTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        sort: SortCriteriaTypeDef = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_resource_scan(self, analyzerArn: str, resourceArn: str) -> None:
        """
        [Client.start_resource_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.start_resource_scan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_archive_rule(
        self,
        analyzerName: str,
        filter: Dict[str, CriterionTypeDef],
        ruleName: str,
        clientToken: str = None,
    ) -> None:
        """
        [Client.update_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_archive_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_findings(
        self,
        analyzerArn: str,
        status: Literal["ACTIVE", "ARCHIVED"],
        clientToken: str = None,
        ids: List[str] = None,
        resourceArn: str = None,
    ) -> None:
        """
        [Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_findings)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
