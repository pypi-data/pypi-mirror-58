"Main interface for transcribe service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

MediaTypeDef = TypedDict("MediaTypeDef", {"MediaFileUri": str}, total=False)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
    },
    total=False,
)

TranscriptTypeDef = TypedDict("TranscriptTypeDef", {"TranscriptFileUri": str}, total=False)

TranscriptionJobTypeDef = TypedDict(
    "TranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "MediaSampleRateHertz": int,
        "MediaFormat": Literal["mp3", "mp4", "wav", "flac"],
        "Media": MediaTypeDef,
        "Transcript": TranscriptTypeDef,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": SettingsTypeDef,
    },
    total=False,
)

GetTranscriptionJobResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseTypeDef", {"TranscriptionJob": TranscriptionJobTypeDef}, total=False
)

GetVocabularyResponseTypeDef = TypedDict(
    "GetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

TranscriptionJobSummaryTypeDef = TypedDict(
    "TranscriptionJobSummaryTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "TranscriptionJobStatus": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "FailureReason": str,
        "OutputLocationType": Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"],
    },
    total=False,
)

ListTranscriptionJobsResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "TranscriptionJobSummaries": List[TranscriptionJobSummaryTypeDef],
    },
    total=False,
)

VocabularyInfoTypeDef = TypedDict(
    "VocabularyInfoTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)

ListVocabulariesResponseTypeDef = TypedDict(
    "ListVocabulariesResponseTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "Vocabularies": List[VocabularyInfoTypeDef],
    },
    total=False,
)

StartTranscriptionJobResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": TranscriptionJobTypeDef},
    total=False,
)

UpdateVocabularyResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)
