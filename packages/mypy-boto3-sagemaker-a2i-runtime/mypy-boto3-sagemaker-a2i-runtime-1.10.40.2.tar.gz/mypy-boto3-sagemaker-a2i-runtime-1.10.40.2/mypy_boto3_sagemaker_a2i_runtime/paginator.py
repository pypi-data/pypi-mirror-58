"Main interface for sagemaker-a2i-runtime service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sagemaker_a2i_runtime.type_defs import (
    ListHumanLoopsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListHumanLoopsPaginator",)


class ListHumanLoopsPaginator(Boto3Paginator):
    """
    [Paginator.ListHumanLoops documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListHumanLoopsResponseTypeDef, None, None]:
        """
        [ListHumanLoops.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops.paginate)
        """
