"Main interface for sagemaker service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sagemaker.type_defs import (
    ListAlgorithmsOutputTypeDef,
    ListAppsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListProcessingJobsResponseTypeDef,
    ListSubscribedWorkteamsResponseTypeDef,
    ListTagsOutputTypeDef,
    ListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ListTrainingJobsResponseTypeDef,
    ListTransformJobsResponseTypeDef,
    ListTrialComponentsResponseTypeDef,
    ListTrialsResponseTypeDef,
    ListUserProfilesResponseTypeDef,
    ListWorkteamsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchExpressionTypeDef,
    SearchResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAlgorithmsPaginator",
    "ListAppsPaginator",
    "ListAutoMLJobsPaginator",
    "ListCandidatesForAutoMLJobPaginator",
    "ListCodeRepositoriesPaginator",
    "ListCompilationJobsPaginator",
    "ListDomainsPaginator",
    "ListEndpointConfigsPaginator",
    "ListEndpointsPaginator",
    "ListExperimentsPaginator",
    "ListFlowDefinitionsPaginator",
    "ListHumanTaskUisPaginator",
    "ListHyperParameterTuningJobsPaginator",
    "ListLabelingJobsPaginator",
    "ListLabelingJobsForWorkteamPaginator",
    "ListModelPackagesPaginator",
    "ListModelsPaginator",
    "ListMonitoringExecutionsPaginator",
    "ListMonitoringSchedulesPaginator",
    "ListNotebookInstanceLifecycleConfigsPaginator",
    "ListNotebookInstancesPaginator",
    "ListProcessingJobsPaginator",
    "ListSubscribedWorkteamsPaginator",
    "ListTagsPaginator",
    "ListTrainingJobsPaginator",
    "ListTrainingJobsForHyperParameterTuningJobPaginator",
    "ListTransformJobsPaginator",
    "ListTrialComponentsPaginator",
    "ListTrialsPaginator",
    "ListUserProfilesPaginator",
    "ListWorkteamsPaginator",
    "SearchPaginator",
)


class ListAlgorithmsPaginator(Boto3Paginator):
    """
    [Paginator.ListAlgorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAlgorithmsOutputTypeDef, None, None]:
        """
        [ListAlgorithms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms.paginate)
        """


class ListAppsPaginator(Boto3Paginator):
    """
    [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAppsResponseTypeDef, None, None]:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListApps.paginate)
        """


class ListAutoMLJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListAutoMLJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAutoMLJobsResponseTypeDef, None, None]:
        """
        [ListAutoMLJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs.paginate)
        """


class ListCandidatesForAutoMLJobPaginator(Boto3Paginator):
    """
    [Paginator.ListCandidatesForAutoMLJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoMLJobName: str,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        CandidateNameEquals: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCandidatesForAutoMLJobResponseTypeDef, None, None]:
        """
        [ListCandidatesForAutoMLJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob.paginate)
        """


class ListCodeRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListCodeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCodeRepositoriesOutputTypeDef, None, None]:
        """
        [ListCodeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories.paginate)
        """


class ListCompilationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListCompilationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCompilationJobsResponseTypeDef, None, None]:
        """
        [ListCompilationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs.paginate)
        """


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDomainsResponseTypeDef, None, None]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains.paginate)
        """


class ListEndpointConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListEndpointConfigsOutputTypeDef, None, None]:
        """
        [ListEndpointConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs.paginate)
        """


class ListEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListEndpointsOutputTypeDef, None, None]:
        """
        [ListEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints.paginate)
        """


class ListExperimentsPaginator(Boto3Paginator):
    """
    [Paginator.ListExperiments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListExperimentsResponseTypeDef, None, None]:
        """
        [ListExperiments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments.paginate)
        """


class ListFlowDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFlowDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListFlowDefinitionsResponseTypeDef, None, None]:
        """
        [ListFlowDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions.paginate)
        """


class ListHumanTaskUisPaginator(Boto3Paginator):
    """
    [Paginator.ListHumanTaskUis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListHumanTaskUisResponseTypeDef, None, None]:
        """
        [ListHumanTaskUis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis.paginate)
        """


class ListHyperParameterTuningJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListHyperParameterTuningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "Status", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListHyperParameterTuningJobsResponseTypeDef, None, None]:
        """
        [ListHyperParameterTuningJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs.paginate)
        """


class ListLabelingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListLabelingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListLabelingJobsResponseTypeDef, None, None]:
        """
        [ListLabelingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs.paginate)
        """


class ListLabelingJobsForWorkteamPaginator(Boto3Paginator):
    """
    [Paginator.ListLabelingJobsForWorkteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkteamArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListLabelingJobsForWorkteamResponseTypeDef, None, None]:
        """
        [ListLabelingJobsForWorkteam.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam.paginate)
        """


class ListModelPackagesPaginator(Boto3Paginator):
    """
    [Paginator.ListModelPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListModelPackagesOutputTypeDef, None, None]:
        """
        [ListModelPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages.paginate)
        """


class ListModelsPaginator(Boto3Paginator):
    """
    [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListModelsOutputTypeDef, None, None]:
        """
        [ListModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListModels.paginate)
        """


class ListMonitoringExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListMonitoringExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: Literal["CreationTime", "ScheduledTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        ScheduledTimeBefore: datetime = None,
        ScheduledTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListMonitoringExecutionsResponseTypeDef, None, None]:
        """
        [ListMonitoringExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions.paginate)
        """


class ListMonitoringSchedulesPaginator(Boto3Paginator):
    """
    [Paginator.ListMonitoringSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EndpointName: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal["Pending", "Failed", "Scheduled", "Stopped"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListMonitoringSchedulesResponseTypeDef, None, None]:
        """
        [ListMonitoringSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules.paginate)
        """


class ListNotebookInstanceLifecycleConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListNotebookInstanceLifecycleConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListNotebookInstanceLifecycleConfigsOutputTypeDef, None, None]:
        """
        [ListNotebookInstanceLifecycleConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs.paginate)
        """


class ListNotebookInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListNotebookInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ] = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListNotebookInstancesOutputTypeDef, None, None]:
        """
        [ListNotebookInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances.paginate)
        """


class ListProcessingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListProcessingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListProcessingJobsResponseTypeDef, None, None]:
        """
        [ListProcessingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs.paginate)
        """


class ListSubscribedWorkteamsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscribedWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, NameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscribedWorkteamsResponseTypeDef, None, None]:
        """
        [ListSubscribedWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsOutputTypeDef, None, None]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTags.paginate)
        """


class ListTrainingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrainingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTrainingJobsResponseTypeDef, None, None]:
        """
        [ListTrainingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs.paginate)
        """


class ListTrainingJobsForHyperParameterTuningJobPaginator(Boto3Paginator):
    """
    [Paginator.ListTrainingJobsForHyperParameterTuningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HyperParameterTuningJobName: str,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTrainingJobsForHyperParameterTuningJobResponseTypeDef, None, None]:
        """
        [ListTrainingJobsForHyperParameterTuningJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob.paginate)
        """


class ListTransformJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTransformJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTransformJobsResponseTypeDef, None, None]:
        """
        [ListTransformJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs.paginate)
        """


class ListTrialComponentsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrialComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTrialComponentsResponseTypeDef, None, None]:
        """
        [ListTrialComponents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents.paginate)
        """


class ListTrialsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ExperimentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTrialsResponseTypeDef, None, None]:
        """
        [ListTrials.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials.paginate)
        """


class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "LastModifiedTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListUserProfilesResponseTypeDef, None, None]:
        """
        [ListUserProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles.paginate)
        """


class ListWorkteamsPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreateDate"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListWorkteamsResponseTypeDef, None, None]:
        """
        [ListWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams.paginate)
        """


class SearchPaginator(Boto3Paginator):
    """
    [Paginator.Search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.Search)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Resource: Literal[
            "TrainingJob", "Experiment", "ExperimentTrial", "ExperimentTrialComponent"
        ],
        SearchExpression: SearchExpressionTypeDef = None,
        SortBy: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchResponseTypeDef, None, None]:
        """
        [Search.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sagemaker.html#SageMaker.Paginator.Search.paginate)
        """
