"Main interface for sagemaker-a2i-runtime service"
from mypy_boto3_sagemaker_a2i_runtime.client import (
    AugmentedAIRuntimeClient,
    AugmentedAIRuntimeClient as Client,
)
from mypy_boto3_sagemaker_a2i_runtime.paginator import ListHumanLoopsPaginator


__all__ = ("AugmentedAIRuntimeClient", "Client", "ListHumanLoopsPaginator")
