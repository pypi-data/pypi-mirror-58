"Main interface for sms-voice service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sms_voice.client as client_scope
from mypy_boto3_sms_voice.type_defs import (
    EventDestinationDefinitionTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    SendVoiceMessageResponseTypeDef,
    VoiceMessageContentTypeDef,
)


__all__ = ("SMSVoiceClient",)


class SMSVoiceClient(BaseClient):
    """
    [SMSVoice.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set(self, ConfigurationSetName: str = None) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: EventDestinationDefinitionTypeDef = None,
        EventDestinationName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set_event_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set_event_destination)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.get_configuration_set_event_destinations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configuration_sets(
        self, NextToken: str = None, PageSize: str = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.list_configuration_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_voice_message(
        self,
        CallerId: str = None,
        ConfigurationSetName: str = None,
        Content: VoiceMessageContentTypeDef = None,
        DestinationPhoneNumber: str = None,
        OriginationPhoneNumber: str = None,
    ) -> SendVoiceMessageResponseTypeDef:
        """
        [Client.send_voice_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.send_voice_message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sms-voice.html#SMSVoice.Client.update_configuration_set_event_destination)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
