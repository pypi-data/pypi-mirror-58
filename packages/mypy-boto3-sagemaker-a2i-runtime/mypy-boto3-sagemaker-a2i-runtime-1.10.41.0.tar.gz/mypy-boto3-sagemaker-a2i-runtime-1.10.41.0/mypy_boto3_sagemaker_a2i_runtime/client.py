"Main interface for sagemaker-a2i-runtime service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sagemaker_a2i_runtime.client as client_scope

# pylint: disable=import-self
import mypy_boto3_sagemaker_a2i_runtime.paginator as paginator_scope
from mypy_boto3_sagemaker_a2i_runtime.type_defs import (
    DescribeHumanLoopResponseTypeDef,
    HumanLoopInputContentTypeDef,
    HumanReviewDataAttributesTypeDef,
    ListHumanLoopsResponseTypeDef,
    StartHumanLoopResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AugmentedAIRuntimeClient",)


class AugmentedAIRuntimeClient(BaseClient):
    """
    [AugmentedAIRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_human_loop(self, HumanLoopName: str) -> Dict[str, Any]:
        """
        [Client.delete_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.delete_human_loop)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_human_loop(self, HumanLoopName: str) -> DescribeHumanLoopResponseTypeDef:
        """
        [Client.describe_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.describe_human_loop)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_human_loops(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListHumanLoopsResponseTypeDef:
        """
        [Client.list_human_loops documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.list_human_loops)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_human_loop(
        self,
        HumanLoopName: str,
        FlowDefinitionArn: str,
        HumanLoopInput: HumanLoopInputContentTypeDef,
        DataAttributes: HumanReviewDataAttributesTypeDef = None,
    ) -> StartHumanLoopResponseTypeDef:
        """
        [Client.start_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.start_human_loop)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_human_loop(self, HumanLoopName: str) -> Dict[str, Any]:
        """
        [Client.stop_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.stop_human_loop)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_human_loops"]
    ) -> paginator_scope.ListHumanLoopsPaginator:
        """
        [Paginator.ListHumanLoops documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
