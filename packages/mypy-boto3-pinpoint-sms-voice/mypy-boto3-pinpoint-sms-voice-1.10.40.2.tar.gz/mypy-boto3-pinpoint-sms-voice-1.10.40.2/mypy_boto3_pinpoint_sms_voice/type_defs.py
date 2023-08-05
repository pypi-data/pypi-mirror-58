"Main interface for pinpoint-sms-voice service type defs"
from __future__ import annotations

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


CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef", {"IamRoleArn": str, "LogGroupArn": str}, total=False
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef", {"DeliveryStreamArn": str, "IamRoleArn": str}, total=False
)

SnsDestinationTypeDef = TypedDict("SnsDestinationTypeDef", {"TopicArn": str}, total=False)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "CloudWatchLogsDestination": CloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": KinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "SnsDestination": SnsDestinationTypeDef,
    },
    total=False,
)

EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": CloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": KinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "Name": str,
        "SnsDestination": SnsDestinationTypeDef,
    },
    total=False,
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {"EventDestinations": List[EventDestinationTypeDef]},
    total=False,
)

SendVoiceMessageResponseTypeDef = TypedDict(
    "SendVoiceMessageResponseTypeDef", {"MessageId": str}, total=False
)

CallInstructionsMessageTypeTypeDef = TypedDict(
    "CallInstructionsMessageTypeTypeDef", {"Text": str}, total=False
)

PlainTextMessageTypeTypeDef = TypedDict(
    "PlainTextMessageTypeTypeDef", {"LanguageCode": str, "Text": str, "VoiceId": str}, total=False
)

SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef", {"LanguageCode": str, "Text": str, "VoiceId": str}, total=False
)

VoiceMessageContentTypeDef = TypedDict(
    "VoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": CallInstructionsMessageTypeTypeDef,
        "PlainTextMessage": PlainTextMessageTypeTypeDef,
        "SSMLMessage": SSMLMessageTypeTypeDef,
    },
    total=False,
)
