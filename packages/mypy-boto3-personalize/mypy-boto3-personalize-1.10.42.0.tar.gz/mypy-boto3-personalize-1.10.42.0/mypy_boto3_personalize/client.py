"Main interface for personalize service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_personalize.client as client_scope

# pylint: disable=import-self
import mypy_boto3_personalize.paginator as paginator_scope
from mypy_boto3_personalize.type_defs import (
    BatchInferenceJobInputTypeDef,
    BatchInferenceJobOutputTypeDef,
    CreateBatchInferenceJobResponseTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateEventTrackerResponseTypeDef,
    CreateSchemaResponseTypeDef,
    CreateSolutionResponseTypeDef,
    CreateSolutionVersionResponseTypeDef,
    DataSourceTypeDef,
    DescribeAlgorithmResponseTypeDef,
    DescribeBatchInferenceJobResponseTypeDef,
    DescribeCampaignResponseTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeEventTrackerResponseTypeDef,
    DescribeFeatureTransformationResponseTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    DescribeSolutionResponseTypeDef,
    DescribeSolutionVersionResponseTypeDef,
    GetSolutionMetricsResponseTypeDef,
    ListBatchInferenceJobsResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSolutionVersionsResponseTypeDef,
    ListSolutionsResponseTypeDef,
    SolutionConfigTypeDef,
    UpdateCampaignResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PersonalizeClient",)


class PersonalizeClient(BaseClient):
    """
    [Personalize.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_batch_inference_job(
        self,
        jobName: str,
        solutionVersionArn: str,
        jobInput: BatchInferenceJobInputTypeDef,
        jobOutput: BatchInferenceJobOutputTypeDef,
        roleArn: str,
        numResults: int = None,
    ) -> CreateBatchInferenceJobResponseTypeDef:
        """
        [Client.create_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_batch_inference_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_campaign(
        self, name: str, solutionVersionArn: str, minProvisionedTPS: int
    ) -> CreateCampaignResponseTypeDef:
        """
        [Client.create_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset(
        self, name: str, schemaArn: str, datasetGroupArn: str, datasetType: str
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset_group(
        self, name: str, roleArn: str = None, kmsKeyArn: str = None
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        [Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_dataset_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset_import_job(
        self, jobName: str, datasetArn: str, dataSource: DataSourceTypeDef, roleArn: str
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        [Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_dataset_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_tracker(
        self, name: str, datasetGroupArn: str
    ) -> CreateEventTrackerResponseTypeDef:
        """
        [Client.create_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_event_tracker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_schema(self, name: str, schema: str) -> CreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_solution(
        self,
        name: str,
        datasetGroupArn: str,
        performHPO: bool = None,
        performAutoML: bool = None,
        recipeArn: str = None,
        eventType: str = None,
        solutionConfig: SolutionConfigTypeDef = None,
    ) -> CreateSolutionResponseTypeDef:
        """
        [Client.create_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_solution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_solution_version(
        self, solutionArn: str, trainingMode: Literal["FULL", "UPDATE"] = None
    ) -> CreateSolutionVersionResponseTypeDef:
        """
        [Client.create_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.create_solution_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_campaign(self, campaignArn: str) -> None:
        """
        [Client.delete_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.delete_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset(self, datasetArn: str) -> None:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.delete_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset_group(self, datasetGroupArn: str) -> None:
        """
        [Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.delete_dataset_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_tracker(self, eventTrackerArn: str) -> None:
        """
        [Client.delete_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.delete_event_tracker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_schema(self, schemaArn: str) -> None:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.delete_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_solution(self, solutionArn: str) -> None:
        """
        [Client.delete_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.delete_solution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_algorithm(self, algorithmArn: str) -> DescribeAlgorithmResponseTypeDef:
        """
        [Client.describe_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_algorithm)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_batch_inference_job(
        self, batchInferenceJobArn: str
    ) -> DescribeBatchInferenceJobResponseTypeDef:
        """
        [Client.describe_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_batch_inference_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_campaign(self, campaignArn: str) -> DescribeCampaignResponseTypeDef:
        """
        [Client.describe_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset(self, datasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset_group(self, datasetGroupArn: str) -> DescribeDatasetGroupResponseTypeDef:
        """
        [Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_dataset_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset_import_job(
        self, datasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        [Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_dataset_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_tracker(self, eventTrackerArn: str) -> DescribeEventTrackerResponseTypeDef:
        """
        [Client.describe_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_event_tracker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_feature_transformation(
        self, featureTransformationArn: str
    ) -> DescribeFeatureTransformationResponseTypeDef:
        """
        [Client.describe_feature_transformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_feature_transformation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_recipe(self, recipeArn: str) -> DescribeRecipeResponseTypeDef:
        """
        [Client.describe_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_recipe)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_schema(self, schemaArn: str) -> DescribeSchemaResponseTypeDef:
        """
        [Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_solution(self, solutionArn: str) -> DescribeSolutionResponseTypeDef:
        """
        [Client.describe_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_solution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_solution_version(
        self, solutionVersionArn: str
    ) -> DescribeSolutionVersionResponseTypeDef:
        """
        [Client.describe_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.describe_solution_version)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_solution_metrics(self, solutionVersionArn: str) -> GetSolutionMetricsResponseTypeDef:
        """
        [Client.get_solution_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.get_solution_metrics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_batch_inference_jobs(
        self, solutionVersionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListBatchInferenceJobsResponseTypeDef:
        """
        [Client.list_batch_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_batch_inference_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_campaigns(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListCampaignsResponseTypeDef:
        """
        [Client.list_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_campaigns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dataset_groups(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_dataset_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dataset_import_jobs(
        self, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_dataset_import_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_datasets(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_datasets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_event_trackers(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListEventTrackersResponseTypeDef:
        """
        [Client.list_event_trackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_event_trackers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_recipes(
        self,
        recipeProvider: Literal["SERVICE"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListRecipesResponseTypeDef:
        """
        [Client.list_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_recipes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_schemas(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListSchemasResponseTypeDef:
        """
        [Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_schemas)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_solution_versions(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionVersionsResponseTypeDef:
        """
        [Client.list_solution_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_solution_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_solutions(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionsResponseTypeDef:
        """
        [Client.list_solutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.list_solutions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_campaign(
        self, campaignArn: str, solutionVersionArn: str = None, minProvisionedTPS: int = None
    ) -> UpdateCampaignResponseTypeDef:
        """
        [Client.update_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Client.update_campaign)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_batch_inference_jobs"]
    ) -> paginator_scope.ListBatchInferenceJobsPaginator:
        """
        [Paginator.ListBatchInferenceJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_campaigns"]
    ) -> paginator_scope.ListCampaignsPaginator:
        """
        [Paginator.ListCampaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> paginator_scope.ListDatasetGroupsPaginator:
        """
        [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> paginator_scope.ListDatasetImportJobsPaginator:
        """
        [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_datasets"]
    ) -> paginator_scope.ListDatasetsPaginator:
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_event_trackers"]
    ) -> paginator_scope.ListEventTrackersPaginator:
        """
        [Paginator.ListEventTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_recipes"]
    ) -> paginator_scope.ListRecipesPaginator:
        """
        [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_schemas"]
    ) -> paginator_scope.ListSchemasPaginator:
        """
        [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_solution_versions"]
    ) -> paginator_scope.ListSolutionVersionsPaginator:
        """
        [Paginator.ListSolutionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_solutions"]
    ) -> paginator_scope.ListSolutionsPaginator:
        """
        [Paginator.ListSolutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
