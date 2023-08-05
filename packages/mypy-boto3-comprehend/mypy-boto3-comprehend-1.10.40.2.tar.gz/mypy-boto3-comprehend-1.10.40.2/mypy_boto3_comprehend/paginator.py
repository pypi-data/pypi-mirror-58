"Main interface for comprehend service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_comprehend.type_defs import (
    DocumentClassificationJobFilterTypeDef,
    DocumentClassifierFilterTypeDef,
    DominantLanguageDetectionJobFilterTypeDef,
    EntitiesDetectionJobFilterTypeDef,
    EntityRecognizerFilterTypeDef,
    KeyPhrasesDetectionJobFilterTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
    PaginatorConfigTypeDef,
    SentimentDetectionJobFilterTypeDef,
    TopicsDetectionJobFilterTypeDef,
)


__all__ = (
    "ListDocumentClassificationJobsPaginator",
    "ListDocumentClassifiersPaginator",
    "ListDominantLanguageDetectionJobsPaginator",
    "ListEntitiesDetectionJobsPaginator",
    "ListEntityRecognizersPaginator",
    "ListKeyPhrasesDetectionJobsPaginator",
    "ListSentimentDetectionJobsPaginator",
    "ListTopicsDetectionJobsPaginator",
)


class ListDocumentClassificationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDocumentClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: DocumentClassificationJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDocumentClassificationJobsResponseTypeDef, None, None]:
        """
        [ListDocumentClassificationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs.paginate)
        """


class ListDocumentClassifiersPaginator(Boto3Paginator):
    """
    [Paginator.ListDocumentClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: DocumentClassifierFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDocumentClassifiersResponseTypeDef, None, None]:
        """
        [ListDocumentClassifiers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers.paginate)
        """


class ListDominantLanguageDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDominantLanguageDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: DominantLanguageDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDominantLanguageDetectionJobsResponseTypeDef, None, None]:
        """
        [ListDominantLanguageDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs.paginate)
        """


class ListEntitiesDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListEntitiesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: EntitiesDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListEntitiesDetectionJobsResponseTypeDef, None, None]:
        """
        [ListEntitiesDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs.paginate)
        """


class ListEntityRecognizersPaginator(Boto3Paginator):
    """
    [Paginator.ListEntityRecognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: EntityRecognizerFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListEntityRecognizersResponseTypeDef, None, None]:
        """
        [ListEntityRecognizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers.paginate)
        """


class ListKeyPhrasesDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListKeyPhrasesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: KeyPhrasesDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListKeyPhrasesDetectionJobsResponseTypeDef, None, None]:
        """
        [ListKeyPhrasesDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs.paginate)
        """


class ListSentimentDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListSentimentDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: SentimentDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSentimentDetectionJobsResponseTypeDef, None, None]:
        """
        [ListSentimentDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs.paginate)
        """


class ListTopicsDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTopicsDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: TopicsDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTopicsDetectionJobsResponseTypeDef, None, None]:
        """
        [ListTopicsDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs.paginate)
        """
