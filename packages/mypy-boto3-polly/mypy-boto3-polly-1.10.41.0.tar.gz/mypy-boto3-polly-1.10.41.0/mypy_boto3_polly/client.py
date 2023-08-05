"Main interface for polly service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_polly.client as client_scope

# pylint: disable=import-self
import mypy_boto3_polly.paginator as paginator_scope
from mypy_boto3_polly.type_defs import (
    DescribeVoicesOutputTypeDef,
    GetLexiconOutputTypeDef,
    GetSpeechSynthesisTaskOutputTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
    StartSpeechSynthesisTaskOutputTypeDef,
    SynthesizeSpeechOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PollyClient",)


class PollyClient(BaseClient):
    """
    [Polly.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_lexicon(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.delete_lexicon)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_voices(
        self,
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        IncludeAdditionalLanguageCodes: bool = None,
        NextToken: str = None,
    ) -> DescribeVoicesOutputTypeDef:
        """
        [Client.describe_voices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.describe_voices)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_lexicon(self, Name: str) -> GetLexiconOutputTypeDef:
        """
        [Client.get_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.get_lexicon)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_speech_synthesis_task(self, TaskId: str) -> GetSpeechSynthesisTaskOutputTypeDef:
        """
        [Client.get_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.get_speech_synthesis_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_lexicons(self, NextToken: str = None) -> ListLexiconsOutputTypeDef:
        """
        [Client.list_lexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.list_lexicons)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_speech_synthesis_tasks(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Status: Literal["scheduled", "inProgress", "completed", "failed"] = None,
    ) -> ListSpeechSynthesisTasksOutputTypeDef:
        """
        [Client.list_speech_synthesis_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.list_speech_synthesis_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_lexicon(self, Name: str, Content: str) -> Dict[str, Any]:
        """
        [Client.put_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.put_lexicon)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_speech_synthesis_task(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        OutputS3BucketName: str,
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        OutputS3KeyPrefix: str = None,
        SampleRate: str = None,
        SnsTopicArn: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> StartSpeechSynthesisTaskOutputTypeDef:
        """
        [Client.start_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.start_speech_synthesis_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def synthesize_speech(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        SampleRate: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> SynthesizeSpeechOutputTypeDef:
        """
        [Client.synthesize_speech documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Client.synthesize_speech)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_voices"]
    ) -> paginator_scope.DescribeVoicesPaginator:
        """
        [Paginator.DescribeVoices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Paginator.DescribeVoices)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_lexicons"]
    ) -> paginator_scope.ListLexiconsPaginator:
        """
        [Paginator.ListLexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Paginator.ListLexicons)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_speech_synthesis_tasks"]
    ) -> paginator_scope.ListSpeechSynthesisTasksPaginator:
        """
        [Paginator.ListSpeechSynthesisTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)
        """


class Exceptions:
    ClientError: Boto3ClientError
    EngineNotSupportedException: Boto3ClientError
    InvalidLexiconException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidS3BucketException: Boto3ClientError
    InvalidS3KeyException: Boto3ClientError
    InvalidSampleRateException: Boto3ClientError
    InvalidSnsTopicArnException: Boto3ClientError
    InvalidSsmlException: Boto3ClientError
    InvalidTaskIdException: Boto3ClientError
    LanguageNotSupportedException: Boto3ClientError
    LexiconNotFoundException: Boto3ClientError
    LexiconSizeExceededException: Boto3ClientError
    MarksNotSupportedForFormatException: Boto3ClientError
    MaxLexemeLengthExceededException: Boto3ClientError
    MaxLexiconsNumberExceededException: Boto3ClientError
    ServiceFailureException: Boto3ClientError
    SsmlMarksNotSupportedForTextTypeException: Boto3ClientError
    SynthesisTaskNotFoundException: Boto3ClientError
    TextLengthExceededException: Boto3ClientError
    UnsupportedPlsAlphabetException: Boto3ClientError
    UnsupportedPlsLanguageException: Boto3ClientError
