"Main interface for sagemaker service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_sagemaker.type_defs import WaiterConfigTypeDef


__all__ = (
    "EndpointDeletedWaiter",
    "EndpointInServiceWaiter",
    "NotebookInstanceDeletedWaiter",
    "NotebookInstanceInServiceWaiter",
    "NotebookInstanceStoppedWaiter",
    "ProcessingJobCompletedOrStoppedWaiter",
    "TrainingJobCompletedOrStoppedWaiter",
    "TransformJobCompletedOrStoppedWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, EndpointName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [EndpointDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted.wait)
        """


class EndpointInServiceWaiter(Boto3Waiter):
    """
    [Waiter.EndpointInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, EndpointName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [EndpointInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService.wait)
        """


class NotebookInstanceDeletedWaiter(Boto3Waiter):
    """
    [Waiter.NotebookInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [NotebookInstanceDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted.wait)
        """


class NotebookInstanceInServiceWaiter(Boto3Waiter):
    """
    [Waiter.NotebookInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [NotebookInstanceInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService.wait)
        """


class NotebookInstanceStoppedWaiter(Boto3Waiter):
    """
    [Waiter.NotebookInstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [NotebookInstanceStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped.wait)
        """


class ProcessingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Waiter.ProcessingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ProcessingJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ProcessingJobCompletedOrStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped.wait)
        """


class TrainingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Waiter.TrainingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, TrainingJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TrainingJobCompletedOrStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped.wait)
        """


class TransformJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Waiter.TransformJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, TransformJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TransformJobCompletedOrStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped.wait)
        """
