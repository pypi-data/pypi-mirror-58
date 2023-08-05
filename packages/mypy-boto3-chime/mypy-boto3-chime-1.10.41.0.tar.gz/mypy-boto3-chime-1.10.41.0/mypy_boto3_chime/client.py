"Main interface for chime service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_chime.client as client_scope

# pylint: disable=import-self
import mypy_boto3_chime.paginator as paginator_scope
from mypy_boto3_chime.type_defs import (
    AccountSettingsTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef,
    BatchCreateAttendeeResponseTypeDef,
    BatchCreateRoomMembershipResponseTypeDef,
    BatchDeletePhoneNumberResponseTypeDef,
    BatchSuspendUserResponseTypeDef,
    BatchUnsuspendUserResponseTypeDef,
    BatchUpdatePhoneNumberResponseTypeDef,
    BatchUpdateUserResponseTypeDef,
    BusinessCallingSettingsTypeDef,
    CreateAccountResponseTypeDef,
    CreateAttendeeRequestItemTypeDef,
    CreateAttendeeResponseTypeDef,
    CreateBotResponseTypeDef,
    CreateMeetingResponseTypeDef,
    CreatePhoneNumberOrderResponseTypeDef,
    CreateRoomMembershipResponseTypeDef,
    CreateRoomResponseTypeDef,
    CreateVoiceConnectorGroupResponseTypeDef,
    CreateVoiceConnectorResponseTypeDef,
    CredentialTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef,
    GetAccountResponseTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetAttendeeResponseTypeDef,
    GetBotResponseTypeDef,
    GetEventsConfigurationResponseTypeDef,
    GetGlobalSettingsResponseTypeDef,
    GetMeetingResponseTypeDef,
    GetPhoneNumberOrderResponseTypeDef,
    GetPhoneNumberResponseTypeDef,
    GetPhoneNumberSettingsResponseTypeDef,
    GetRoomResponseTypeDef,
    GetUserResponseTypeDef,
    GetUserSettingsResponseTypeDef,
    GetVoiceConnectorGroupResponseTypeDef,
    GetVoiceConnectorLoggingConfigurationResponseTypeDef,
    GetVoiceConnectorOriginationResponseTypeDef,
    GetVoiceConnectorResponseTypeDef,
    GetVoiceConnectorStreamingConfigurationResponseTypeDef,
    GetVoiceConnectorTerminationHealthResponseTypeDef,
    GetVoiceConnectorTerminationResponseTypeDef,
    InviteUsersResponseTypeDef,
    ListAccountsResponseTypeDef,
    ListAttendeesResponseTypeDef,
    ListBotsResponseTypeDef,
    ListMeetingsResponseTypeDef,
    ListPhoneNumberOrdersResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListRoomMembershipsResponseTypeDef,
    ListRoomsResponseTypeDef,
    ListUsersResponseTypeDef,
    ListVoiceConnectorGroupsResponseTypeDef,
    ListVoiceConnectorTerminationCredentialsResponseTypeDef,
    ListVoiceConnectorsResponseTypeDef,
    LoggingConfigurationTypeDef,
    MeetingNotificationConfigurationTypeDef,
    MembershipItemTypeDef,
    OriginationTypeDef,
    PutEventsConfigurationResponseTypeDef,
    PutVoiceConnectorLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorOriginationResponseTypeDef,
    PutVoiceConnectorStreamingConfigurationResponseTypeDef,
    PutVoiceConnectorTerminationResponseTypeDef,
    RegenerateSecurityTokenResponseTypeDef,
    ResetPersonalPINResponseTypeDef,
    RestorePhoneNumberResponseTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    StreamingConfigurationTypeDef,
    TerminationTypeDef,
    UpdateAccountResponseTypeDef,
    UpdateBotResponseTypeDef,
    UpdatePhoneNumberRequestItemTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdateRoomMembershipResponseTypeDef,
    UpdateRoomResponseTypeDef,
    UpdateUserRequestItemTypeDef,
    UpdateUserResponseTypeDef,
    UpdateVoiceConnectorGroupResponseTypeDef,
    UpdateVoiceConnectorResponseTypeDef,
    UserSettingsTypeDef,
    VoiceConnectorItemTypeDef,
    VoiceConnectorSettingsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ChimeClient",)


class ChimeClient(BaseClient):
    """
    [Chime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_phone_number_with_user(
        self, AccountId: str, UserId: str, E164PhoneNumber: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_phone_number_with_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.associate_phone_number_with_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_phone_numbers_with_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[str] = None, ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
        """
        [Client.associate_phone_numbers_with_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_phone_numbers_with_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: List[str] = None,
        ForceAssociate: bool = None,
    ) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
        """
        [Client.associate_phone_numbers_with_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_create_attendee(
        self, MeetingId: str, Attendees: List[CreateAttendeeRequestItemTypeDef]
    ) -> BatchCreateAttendeeResponseTypeDef:
        """
        [Client.batch_create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.batch_create_attendee)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_create_room_membership(
        self, AccountId: str, RoomId: str, MembershipItemList: List[MembershipItemTypeDef]
    ) -> BatchCreateRoomMembershipResponseTypeDef:
        """
        [Client.batch_create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.batch_create_room_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_phone_number(
        self, PhoneNumberIds: List[str]
    ) -> BatchDeletePhoneNumberResponseTypeDef:
        """
        [Client.batch_delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.batch_delete_phone_number)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_suspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> BatchSuspendUserResponseTypeDef:
        """
        [Client.batch_suspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.batch_suspend_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_unsuspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> BatchUnsuspendUserResponseTypeDef:
        """
        [Client.batch_unsuspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.batch_unsuspend_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_update_phone_number(
        self, UpdatePhoneNumberRequestItems: List[UpdatePhoneNumberRequestItemTypeDef]
    ) -> BatchUpdatePhoneNumberResponseTypeDef:
        """
        [Client.batch_update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.batch_update_phone_number)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_update_user(
        self, AccountId: str, UpdateUserRequestItems: List[UpdateUserRequestItemTypeDef]
    ) -> BatchUpdateUserResponseTypeDef:
        """
        [Client.batch_update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.batch_update_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account(self, Name: str) -> CreateAccountResponseTypeDef:
        """
        [Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_attendee(self, MeetingId: str, ExternalUserId: str) -> CreateAttendeeResponseTypeDef:
        """
        [Client.create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_attendee)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_bot(
        self, AccountId: str, DisplayName: str, Domain: str = None
    ) -> CreateBotResponseTypeDef:
        """
        [Client.create_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_bot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_meeting(
        self,
        ClientRequestToken: str,
        MeetingHostId: str = None,
        MediaRegion: str = None,
        NotificationsConfiguration: MeetingNotificationConfigurationTypeDef = None,
    ) -> CreateMeetingResponseTypeDef:
        """
        [Client.create_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_meeting)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_phone_number_order(
        self, ProductType: Literal["BusinessCalling", "VoiceConnector"], E164PhoneNumbers: List[str]
    ) -> CreatePhoneNumberOrderResponseTypeDef:
        """
        [Client.create_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_phone_number_order)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_room(
        self, AccountId: str, Name: str, ClientRequestToken: str = None
    ) -> CreateRoomResponseTypeDef:
        """
        [Client.create_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_room)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MemberId: str,
        Role: Literal["Administrator", "Member"] = None,
    ) -> CreateRoomMembershipResponseTypeDef:
        """
        [Client.create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_room_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_voice_connector(
        self,
        Name: str,
        RequireEncryption: bool,
        AwsRegion: Literal["us-east-1", "us-west-2"] = None,
    ) -> CreateVoiceConnectorResponseTypeDef:
        """
        [Client.create_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_voice_connector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_voice_connector_group(
        self, Name: str, VoiceConnectorItems: List[VoiceConnectorItemTypeDef] = None
    ) -> CreateVoiceConnectorGroupResponseTypeDef:
        """
        [Client.create_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.create_voice_connector_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_account(self, AccountId: str) -> Dict[str, Any]:
        """
        [Client.delete_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_attendee(self, MeetingId: str, AttendeeId: str) -> None:
        """
        [Client.delete_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_attendee)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_events_configuration(self, AccountId: str, BotId: str) -> None:
        """
        [Client.delete_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_events_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_meeting(self, MeetingId: str) -> None:
        """
        [Client.delete_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_meeting)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_phone_number(self, PhoneNumberId: str) -> None:
        """
        [Client.delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_phone_number)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_room(self, AccountId: str, RoomId: str) -> None:
        """
        [Client.delete_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_room)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_room_membership(self, AccountId: str, RoomId: str, MemberId: str) -> None:
        """
        [Client.delete_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_room_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_voice_connector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_group(self, VoiceConnectorGroupId: str) -> None:
        """
        [Client.delete_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_voice_connector_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_origination(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_voice_connector_origination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_streaming_configuration(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_voice_connector_streaming_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_termination(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_voice_connector_termination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Usernames: List[str] = None
    ) -> None:
        """
        [Client.delete_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.delete_voice_connector_termination_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_phone_number_from_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_phone_number_from_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.disassociate_phone_number_from_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_phone_numbers_from_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[str] = None
    ) -> DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        [Client.disassociate_phone_numbers_from_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_phone_numbers_from_voice_connector_group(
        self, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str] = None
    ) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        [Client.disassociate_phone_numbers_from_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector_group)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account(self, AccountId: str) -> GetAccountResponseTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account_settings(self, AccountId: str) -> GetAccountSettingsResponseTypeDef:
        """
        [Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_account_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_attendee(self, MeetingId: str, AttendeeId: str) -> GetAttendeeResponseTypeDef:
        """
        [Client.get_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_attendee)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot(self, AccountId: str, BotId: str) -> GetBotResponseTypeDef:
        """
        [Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_bot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_events_configuration(
        self, AccountId: str, BotId: str
    ) -> GetEventsConfigurationResponseTypeDef:
        """
        [Client.get_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_events_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_global_settings(self) -> GetGlobalSettingsResponseTypeDef:
        """
        [Client.get_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_global_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_meeting(self, MeetingId: str) -> GetMeetingResponseTypeDef:
        """
        [Client.get_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_meeting)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_phone_number(self, PhoneNumberId: str) -> GetPhoneNumberResponseTypeDef:
        """
        [Client.get_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_phone_number)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_phone_number_order(self, PhoneNumberOrderId: str) -> GetPhoneNumberOrderResponseTypeDef:
        """
        [Client.get_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_phone_number_order)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseTypeDef:
        """
        [Client.get_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_phone_number_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_room(self, AccountId: str, RoomId: str) -> GetRoomResponseTypeDef:
        """
        [Client.get_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_room)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user(self, AccountId: str, UserId: str) -> GetUserResponseTypeDef:
        """
        [Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_settings(self, AccountId: str, UserId: str) -> GetUserSettingsResponseTypeDef:
        """
        [Client.get_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_user_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector(self, VoiceConnectorId: str) -> GetVoiceConnectorResponseTypeDef:
        """
        [Client.get_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_voice_connector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_group(
        self, VoiceConnectorGroupId: str
    ) -> GetVoiceConnectorGroupResponseTypeDef:
        """
        [Client.get_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_voice_connector_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_logging_configuration(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Client.get_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_voice_connector_logging_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_origination(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorOriginationResponseTypeDef:
        """
        [Client.get_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_voice_connector_origination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Client.get_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_voice_connector_streaming_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_termination(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationResponseTypeDef:
        """
        [Client.get_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_voice_connector_termination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_termination_health(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        [Client.get_voice_connector_termination_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.get_voice_connector_termination_health)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invite_users(self, AccountId: str, UserEmailList: List[str]) -> InviteUsersResponseTypeDef:
        """
        [Client.invite_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.invite_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accounts(
        self, Name: str = None, UserEmail: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_accounts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_attendees(
        self, MeetingId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAttendeesResponseTypeDef:
        """
        [Client.list_attendees documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_attendees)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bots(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListBotsResponseTypeDef:
        """
        [Client.list_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_bots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_meetings(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListMeetingsResponseTypeDef:
        """
        [Client.list_meetings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_meetings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_phone_number_orders(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListPhoneNumberOrdersResponseTypeDef:
        """
        [Client.list_phone_number_orders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_phone_number_orders)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_phone_numbers(
        self,
        Status: Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ] = None,
        ProductType: Literal["BusinessCalling", "VoiceConnector"] = None,
        FilterName: Literal[
            "AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"
        ] = None,
        FilterValue: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        [Client.list_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_phone_numbers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_room_memberships(
        self, AccountId: str, RoomId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomMembershipsResponseTypeDef:
        """
        [Client.list_room_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_room_memberships)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_rooms(
        self, AccountId: str, MemberId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomsResponseTypeDef:
        """
        [Client.list_rooms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_rooms)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self, AccountId: str, UserEmail: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_voice_connector_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorGroupsResponseTypeDef:
        """
        [Client.list_voice_connector_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_voice_connector_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_voice_connector_termination_credentials(
        self, VoiceConnectorId: str
    ) -> ListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        [Client.list_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_voice_connector_termination_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_voice_connectors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorsResponseTypeDef:
        """
        [Client.list_voice_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.list_voice_connectors)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def logout_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.logout_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.logout_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_events_configuration(
        self,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: str = None,
        LambdaFunctionArn: str = None,
    ) -> PutEventsConfigurationResponseTypeDef:
        """
        [Client.put_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.put_events_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_logging_configuration(
        self, VoiceConnectorId: str, LoggingConfiguration: LoggingConfigurationTypeDef
    ) -> PutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Client.put_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.put_voice_connector_logging_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_origination(
        self, VoiceConnectorId: str, Origination: OriginationTypeDef
    ) -> PutVoiceConnectorOriginationResponseTypeDef:
        """
        [Client.put_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.put_voice_connector_origination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str, StreamingConfiguration: StreamingConfigurationTypeDef
    ) -> PutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Client.put_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.put_voice_connector_streaming_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_termination(
        self, VoiceConnectorId: str, Termination: TerminationTypeDef
    ) -> PutVoiceConnectorTerminationResponseTypeDef:
        """
        [Client.put_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.put_voice_connector_termination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Credentials: List[CredentialTypeDef] = None
    ) -> None:
        """
        [Client.put_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.put_voice_connector_termination_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def regenerate_security_token(
        self, AccountId: str, BotId: str
    ) -> RegenerateSecurityTokenResponseTypeDef:
        """
        [Client.regenerate_security_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.regenerate_security_token)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_personal_pin(self, AccountId: str, UserId: str) -> ResetPersonalPINResponseTypeDef:
        """
        [Client.reset_personal_pin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.reset_personal_pin)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_phone_number(self, PhoneNumberId: str) -> RestorePhoneNumberResponseTypeDef:
        """
        [Client.restore_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.restore_phone_number)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_available_phone_numbers(
        self,
        AreaCode: str = None,
        City: str = None,
        Country: str = None,
        State: str = None,
        TollFreePrefix: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        [Client.search_available_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.search_available_phone_numbers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_account(self, AccountId: str, Name: str = None) -> UpdateAccountResponseTypeDef:
        """
        [Client.update_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_account_settings(
        self, AccountId: str, AccountSettings: AccountSettingsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_account_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_bot(
        self, AccountId: str, BotId: str, Disabled: bool = None
    ) -> UpdateBotResponseTypeDef:
        """
        [Client.update_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_bot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_global_settings(
        self,
        BusinessCalling: BusinessCallingSettingsTypeDef,
        VoiceConnector: VoiceConnectorSettingsTypeDef,
    ) -> None:
        """
        [Client.update_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_global_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_phone_number(
        self,
        PhoneNumberId: str,
        ProductType: Literal["BusinessCalling", "VoiceConnector"] = None,
        CallingName: str = None,
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        [Client.update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_phone_number)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_phone_number_settings(self, CallingName: str) -> None:
        """
        [Client.update_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_phone_number_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_room(
        self, AccountId: str, RoomId: str, Name: str = None
    ) -> UpdateRoomResponseTypeDef:
        """
        [Client.update_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_room)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MemberId: str,
        Role: Literal["Administrator", "Member"] = None,
    ) -> UpdateRoomMembershipResponseTypeDef:
        """
        [Client.update_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_room_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user(
        self,
        AccountId: str,
        UserId: str,
        LicenseType: Literal["Basic", "Plus", "Pro", "ProTrial"] = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_settings(
        self, AccountId: str, UserId: str, UserSettings: UserSettingsTypeDef
    ) -> None:
        """
        [Client.update_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_user_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_voice_connector(
        self, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> UpdateVoiceConnectorResponseTypeDef:
        """
        [Client.update_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_voice_connector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List[VoiceConnectorItemTypeDef],
    ) -> UpdateVoiceConnectorGroupResponseTypeDef:
        """
        [Client.update_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Client.update_voice_connector_group)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accounts"]
    ) -> paginator_scope.ListAccountsPaginator:
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Paginator.ListAccounts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> paginator_scope.ListUsersPaginator:
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Paginator.ListUsers)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServiceFailureException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottledClientException: Boto3ClientError
    UnauthorizedClientException: Boto3ClientError
    UnprocessableEntityException: Boto3ClientError
