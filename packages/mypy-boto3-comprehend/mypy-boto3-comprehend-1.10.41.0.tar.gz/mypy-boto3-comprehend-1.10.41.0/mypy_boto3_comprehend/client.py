"Main interface for comprehend service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_comprehend.client as client_scope

# pylint: disable=import-self
import mypy_boto3_comprehend.paginator as paginator_scope
from mypy_boto3_comprehend.type_defs import (
    BatchDetectDominantLanguageResponseTypeDef,
    BatchDetectEntitiesResponseTypeDef,
    BatchDetectKeyPhrasesResponseTypeDef,
    BatchDetectSentimentResponseTypeDef,
    BatchDetectSyntaxResponseTypeDef,
    ClassifyDocumentResponseTypeDef,
    CreateDocumentClassifierResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEntityRecognizerResponseTypeDef,
    DescribeDocumentClassificationJobResponseTypeDef,
    DescribeDocumentClassifierResponseTypeDef,
    DescribeDominantLanguageDetectionJobResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEntitiesDetectionJobResponseTypeDef,
    DescribeEntityRecognizerResponseTypeDef,
    DescribeKeyPhrasesDetectionJobResponseTypeDef,
    DescribeSentimentDetectionJobResponseTypeDef,
    DescribeTopicsDetectionJobResponseTypeDef,
    DetectDominantLanguageResponseTypeDef,
    DetectEntitiesResponseTypeDef,
    DetectKeyPhrasesResponseTypeDef,
    DetectSentimentResponseTypeDef,
    DetectSyntaxResponseTypeDef,
    DocumentClassificationJobFilterTypeDef,
    DocumentClassifierFilterTypeDef,
    DocumentClassifierInputDataConfigTypeDef,
    DocumentClassifierOutputDataConfigTypeDef,
    DominantLanguageDetectionJobFilterTypeDef,
    EndpointFilterTypeDef,
    EntitiesDetectionJobFilterTypeDef,
    EntityRecognizerFilterTypeDef,
    EntityRecognizerInputDataConfigTypeDef,
    InputDataConfigTypeDef,
    KeyPhrasesDetectionJobFilterTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEndpointsResponseTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    SentimentDetectionJobFilterTypeDef,
    StartDocumentClassificationJobResponseTypeDef,
    StartDominantLanguageDetectionJobResponseTypeDef,
    StartEntitiesDetectionJobResponseTypeDef,
    StartKeyPhrasesDetectionJobResponseTypeDef,
    StartSentimentDetectionJobResponseTypeDef,
    StartTopicsDetectionJobResponseTypeDef,
    StopDominantLanguageDetectionJobResponseTypeDef,
    StopEntitiesDetectionJobResponseTypeDef,
    StopKeyPhrasesDetectionJobResponseTypeDef,
    StopSentimentDetectionJobResponseTypeDef,
    TagTypeDef,
    TopicsDetectionJobFilterTypeDef,
    VpcConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComprehendClient",)


class ComprehendClient(BaseClient):
    """
    [Comprehend.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_dominant_language(
        self, TextList: List[str]
    ) -> BatchDetectDominantLanguageResponseTypeDef:
        """
        [Client.batch_detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.batch_detect_dominant_language)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_entities(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> BatchDetectEntitiesResponseTypeDef:
        """
        [Client.batch_detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.batch_detect_entities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_key_phrases(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> BatchDetectKeyPhrasesResponseTypeDef:
        """
        [Client.batch_detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.batch_detect_key_phrases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_sentiment(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> BatchDetectSentimentResponseTypeDef:
        """
        [Client.batch_detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.batch_detect_sentiment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_syntax(
        self, TextList: List[str], LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> BatchDetectSyntaxResponseTypeDef:
        """
        [Client.batch_detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.batch_detect_syntax)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def classify_document(self, Text: str, EndpointArn: str) -> ClassifyDocumentResponseTypeDef:
        """
        [Client.classify_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.classify_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_document_classifier(
        self,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: DocumentClassifierInputDataConfigTypeDef,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List[TagTypeDef] = None,
        OutputDataConfig: DocumentClassifierOutputDataConfigTypeDef = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> CreateDocumentClassifierResponseTypeDef:
        """
        [Client.create_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.create_document_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_endpoint(
        self,
        EndpointName: str,
        ModelArn: str,
        DesiredInferenceUnits: int,
        ClientRequestToken: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateEndpointResponseTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.create_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_entity_recognizer(
        self,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: EntityRecognizerInputDataConfigTypeDef,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List[TagTypeDef] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> CreateEntityRecognizerResponseTypeDef:
        """
        [Client.create_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.create_entity_recognizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Client.delete_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.delete_document_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint(self, EndpointArn: str) -> Dict[str, Any]:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.delete_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.delete_entity_recognizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_document_classification_job(
        self, JobId: str
    ) -> DescribeDocumentClassificationJobResponseTypeDef:
        """
        [Client.describe_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_document_classification_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_document_classifier(
        self, DocumentClassifierArn: str
    ) -> DescribeDocumentClassifierResponseTypeDef:
        """
        [Client.describe_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_document_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dominant_language_detection_job(
        self, JobId: str
    ) -> DescribeDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.describe_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_dominant_language_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoint(self, EndpointArn: str) -> DescribeEndpointResponseTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_entities_detection_job(
        self, JobId: str
    ) -> DescribeEntitiesDetectionJobResponseTypeDef:
        """
        [Client.describe_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_entities_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_entity_recognizer(
        self, EntityRecognizerArn: str
    ) -> DescribeEntityRecognizerResponseTypeDef:
        """
        [Client.describe_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_entity_recognizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_key_phrases_detection_job(
        self, JobId: str
    ) -> DescribeKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.describe_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_key_phrases_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_sentiment_detection_job(
        self, JobId: str
    ) -> DescribeSentimentDetectionJobResponseTypeDef:
        """
        [Client.describe_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_sentiment_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_topics_detection_job(
        self, JobId: str
    ) -> DescribeTopicsDetectionJobResponseTypeDef:
        """
        [Client.describe_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.describe_topics_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_dominant_language(self, Text: str) -> DetectDominantLanguageResponseTypeDef:
        """
        [Client.detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_entities(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> DetectEntitiesResponseTypeDef:
        """
        [Client.detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.detect_entities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_key_phrases(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> DetectKeyPhrasesResponseTypeDef:
        """
        [Client.detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.detect_key_phrases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_sentiment(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> DetectSentimentResponseTypeDef:
        """
        [Client.detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.detect_sentiment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_syntax(
        self, Text: str, LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> DetectSyntaxResponseTypeDef:
        """
        [Client.detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.detect_syntax)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_document_classification_jobs(
        self,
        Filter: DocumentClassificationJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDocumentClassificationJobsResponseTypeDef:
        """
        [Client.list_document_classification_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_document_classification_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_document_classifiers(
        self,
        Filter: DocumentClassifierFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDocumentClassifiersResponseTypeDef:
        """
        [Client.list_document_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_document_classifiers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dominant_language_detection_jobs(
        self,
        Filter: DominantLanguageDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDominantLanguageDetectionJobsResponseTypeDef:
        """
        [Client.list_dominant_language_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_dominant_language_detection_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_endpoints(
        self, Filter: EndpointFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListEndpointsResponseTypeDef:
        """
        [Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_entities_detection_jobs(
        self,
        Filter: EntitiesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEntitiesDetectionJobsResponseTypeDef:
        """
        [Client.list_entities_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_entities_detection_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_entity_recognizers(
        self,
        Filter: EntityRecognizerFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEntityRecognizersResponseTypeDef:
        """
        [Client.list_entity_recognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_entity_recognizers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_key_phrases_detection_jobs(
        self,
        Filter: KeyPhrasesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListKeyPhrasesDetectionJobsResponseTypeDef:
        """
        [Client.list_key_phrases_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_key_phrases_detection_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_sentiment_detection_jobs(
        self,
        Filter: SentimentDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListSentimentDetectionJobsResponseTypeDef:
        """
        [Client.list_sentiment_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_sentiment_detection_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_topics_detection_jobs(
        self,
        Filter: TopicsDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTopicsDetectionJobsResponseTypeDef:
        """
        [Client.list_topics_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.list_topics_detection_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_document_classification_job(
        self,
        DocumentClassifierArn: str,
        InputDataConfig: InputDataConfigTypeDef,
        OutputDataConfig: OutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> StartDocumentClassificationJobResponseTypeDef:
        """
        [Client.start_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.start_document_classification_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_dominant_language_detection_job(
        self,
        InputDataConfig: InputDataConfigTypeDef,
        OutputDataConfig: OutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> StartDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.start_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.start_dominant_language_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_entities_detection_job(
        self,
        InputDataConfig: InputDataConfigTypeDef,
        OutputDataConfig: OutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        EntityRecognizerArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> StartEntitiesDetectionJobResponseTypeDef:
        """
        [Client.start_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.start_entities_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_key_phrases_detection_job(
        self,
        InputDataConfig: InputDataConfigTypeDef,
        OutputDataConfig: OutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> StartKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.start_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.start_key_phrases_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_sentiment_detection_job(
        self,
        InputDataConfig: InputDataConfigTypeDef,
        OutputDataConfig: OutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> StartSentimentDetectionJobResponseTypeDef:
        """
        [Client.start_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.start_sentiment_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_topics_detection_job(
        self,
        InputDataConfig: InputDataConfigTypeDef,
        OutputDataConfig: OutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        NumberOfTopics: int = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: VpcConfigTypeDef = None,
    ) -> StartTopicsDetectionJobResponseTypeDef:
        """
        [Client.start_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.start_topics_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_dominant_language_detection_job(
        self, JobId: str
    ) -> StopDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.stop_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.stop_dominant_language_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_entities_detection_job(self, JobId: str) -> StopEntitiesDetectionJobResponseTypeDef:
        """
        [Client.stop_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.stop_entities_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_key_phrases_detection_job(
        self, JobId: str
    ) -> StopKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.stop_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.stop_key_phrases_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_sentiment_detection_job(self, JobId: str) -> StopSentimentDetectionJobResponseTypeDef:
        """
        [Client.stop_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.stop_sentiment_detection_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_training_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Client.stop_training_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.stop_training_document_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_training_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Client.stop_training_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.stop_training_entity_recognizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_endpoint(self, EndpointArn: str, DesiredInferenceUnits: int) -> Dict[str, Any]:
        """
        [Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Client.update_endpoint)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_document_classification_jobs"]
    ) -> paginator_scope.ListDocumentClassificationJobsPaginator:
        """
        [Paginator.ListDocumentClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_document_classifiers"]
    ) -> paginator_scope.ListDocumentClassifiersPaginator:
        """
        [Paginator.ListDocumentClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dominant_language_detection_jobs"]
    ) -> paginator_scope.ListDominantLanguageDetectionJobsPaginator:
        """
        [Paginator.ListDominantLanguageDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_entities_detection_jobs"]
    ) -> paginator_scope.ListEntitiesDetectionJobsPaginator:
        """
        [Paginator.ListEntitiesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_entity_recognizers"]
    ) -> paginator_scope.ListEntityRecognizersPaginator:
        """
        [Paginator.ListEntityRecognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_key_phrases_detection_jobs"]
    ) -> paginator_scope.ListKeyPhrasesDetectionJobsPaginator:
        """
        [Paginator.ListKeyPhrasesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_sentiment_detection_jobs"]
    ) -> paginator_scope.ListSentimentDetectionJobsPaginator:
        """
        [Paginator.ListSentimentDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_topics_detection_jobs"]
    ) -> paginator_scope.ListTopicsDetectionJobsPaginator:
        """
        [Paginator.ListTopicsDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)
        """


class Exceptions:
    BatchSizeLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidFilterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    JobNotFoundException: Boto3ClientError
    KmsKeyValidationException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    TextSizeLimitExceededException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    TooManyTagKeysException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnsupportedLanguageException: Boto3ClientError
