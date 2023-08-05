"Main interface for personalize service"
from mypy_boto3_personalize.client import PersonalizeClient as Client, PersonalizeClient
from mypy_boto3_personalize.paginator import (
    ListBatchInferenceJobsPaginator,
    ListCampaignsPaginator,
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListEventTrackersPaginator,
    ListRecipesPaginator,
    ListSchemasPaginator,
    ListSolutionVersionsPaginator,
    ListSolutionsPaginator,
)


__all__ = (
    "Client",
    "ListBatchInferenceJobsPaginator",
    "ListCampaignsPaginator",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListEventTrackersPaginator",
    "ListRecipesPaginator",
    "ListSchemasPaginator",
    "ListSolutionVersionsPaginator",
    "ListSolutionsPaginator",
    "PersonalizeClient",
)
