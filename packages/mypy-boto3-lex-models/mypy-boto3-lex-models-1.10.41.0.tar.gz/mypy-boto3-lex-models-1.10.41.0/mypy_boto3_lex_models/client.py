"Main interface for lex-models service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_lex_models.client as client_scope

# pylint: disable=import-self
import mypy_boto3_lex_models.paginator as paginator_scope
from mypy_boto3_lex_models.type_defs import (
    CodeHookTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateIntentVersionResponseTypeDef,
    CreateSlotTypeVersionResponseTypeDef,
    EnumerationValueTypeDef,
    FollowUpPromptTypeDef,
    FulfillmentActivityTypeDef,
    GetBotAliasResponseTypeDef,
    GetBotAliasesResponseTypeDef,
    GetBotChannelAssociationResponseTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotResponseTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBotsResponseTypeDef,
    GetBuiltinIntentResponseTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetExportResponseTypeDef,
    GetImportResponseTypeDef,
    GetIntentResponseTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetIntentsResponseTypeDef,
    GetSlotTypeResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    GetUtterancesViewResponseTypeDef,
    IntentTypeDef,
    PromptTypeDef,
    PutBotAliasResponseTypeDef,
    PutBotResponseTypeDef,
    PutIntentResponseTypeDef,
    PutSlotTypeResponseTypeDef,
    SlotTypeDef,
    StartImportResponseTypeDef,
    StatementTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LexModelBuildingServiceClient",)


class LexModelBuildingServiceClient(BaseClient):
    """
    [LexModelBuildingService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_bot_version(
        self, name: str, checksum: str = None
    ) -> CreateBotVersionResponseTypeDef:
        """
        [Client.create_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.create_bot_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_intent_version(
        self, name: str, checksum: str = None
    ) -> CreateIntentVersionResponseTypeDef:
        """
        [Client.create_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.create_intent_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_slot_type_version(
        self, name: str, checksum: str = None
    ) -> CreateSlotTypeVersionResponseTypeDef:
        """
        [Client.create_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.create_slot_type_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bot(self, name: str) -> None:
        """
        [Client.delete_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bot_alias(self, name: str, botName: str) -> None:
        """
        [Client.delete_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bot_channel_association(self, name: str, botName: str, botAlias: str) -> None:
        """
        [Client.delete_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_channel_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bot_version(self, name: str, version: str) -> None:
        """
        [Client.delete_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_intent(self, name: str) -> None:
        """
        [Client.delete_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_intent_version(self, name: str, version: str) -> None:
        """
        [Client.delete_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_slot_type(self, name: str) -> None:
        """
        [Client.delete_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_slot_type_version(self, name: str, version: str) -> None:
        """
        [Client.delete_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_utterances(self, botName: str, userId: str) -> None:
        """
        [Client.delete_utterances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.delete_utterances)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot(self, name: str, versionOrAlias: str) -> GetBotResponseTypeDef:
        """
        [Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot_alias(self, name: str, botName: str) -> GetBotAliasResponseTypeDef:
        """
        [Client.get_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot_aliases(
        self, botName: str, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetBotAliasesResponseTypeDef:
        """
        [Client.get_bot_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_aliases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot_channel_association(
        self, name: str, botName: str, botAlias: str
    ) -> GetBotChannelAssociationResponseTypeDef:
        """
        [Client.get_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot_channel_associations(
        self,
        botName: str,
        botAlias: str,
        nextToken: str = None,
        maxResults: int = None,
        nameContains: str = None,
    ) -> GetBotChannelAssociationsResponseTypeDef:
        """
        [Client.get_bot_channel_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetBotVersionsResponseTypeDef:
        """
        [Client.get_bot_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bots(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetBotsResponseTypeDef:
        """
        [Client.get_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_bots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_builtin_intent(self, signature: str) -> GetBuiltinIntentResponseTypeDef:
        """
        [Client.get_builtin_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_builtin_intents(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetBuiltinIntentsResponseTypeDef:
        """
        [Client.get_builtin_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_builtin_slot_types(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetBuiltinSlotTypesResponseTypeDef:
        """
        [Client.get_builtin_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_slot_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_export(
        self,
        name: str,
        version: str,
        resourceType: Literal["BOT", "INTENT", "SLOT_TYPE"],
        exportType: Literal["ALEXA_SKILLS_KIT", "LEX"],
    ) -> GetExportResponseTypeDef:
        """
        [Client.get_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_export)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_import(self, importId: str) -> GetImportResponseTypeDef:
        """
        [Client.get_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_import)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_intent(self, name: str, version: str) -> GetIntentResponseTypeDef:
        """
        [Client.get_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_intent_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetIntentVersionsResponseTypeDef:
        """
        [Client.get_intent_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_intents(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetIntentsResponseTypeDef:
        """
        [Client.get_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_intents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_slot_type(self, name: str, version: str) -> GetSlotTypeResponseTypeDef:
        """
        [Client.get_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_slot_type_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetSlotTypeVersionsResponseTypeDef:
        """
        [Client.get_slot_type_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_slot_types(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetSlotTypesResponseTypeDef:
        """
        [Client.get_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_utterances_view(
        self, botName: str, botVersions: List[str], statusType: Literal["Detected", "Missed"]
    ) -> GetUtterancesViewResponseTypeDef:
        """
        [Client.get_utterances_view documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.get_utterances_view)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bot(
        self,
        name: str,
        locale: Literal["en-US", "en-GB", "de-DE"],
        childDirected: bool,
        description: str = None,
        intents: List[IntentTypeDef] = None,
        clarificationPrompt: PromptTypeDef = None,
        abortStatement: StatementTypeDef = None,
        idleSessionTTLInSeconds: int = None,
        voiceId: str = None,
        checksum: str = None,
        processBehavior: Literal["SAVE", "BUILD"] = None,
        detectSentiment: bool = None,
        createVersion: bool = None,
    ) -> PutBotResponseTypeDef:
        """
        [Client.put_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bot_alias(
        self,
        name: str,
        botVersion: str,
        botName: str,
        description: str = None,
        checksum: str = None,
    ) -> PutBotAliasResponseTypeDef:
        """
        [Client.put_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_intent(
        self,
        name: str,
        description: str = None,
        slots: List[SlotTypeDef] = None,
        sampleUtterances: List[str] = None,
        confirmationPrompt: PromptTypeDef = None,
        rejectionStatement: StatementTypeDef = None,
        followUpPrompt: FollowUpPromptTypeDef = None,
        conclusionStatement: StatementTypeDef = None,
        dialogCodeHook: CodeHookTypeDef = None,
        fulfillmentActivity: FulfillmentActivityTypeDef = None,
        parentIntentSignature: str = None,
        checksum: str = None,
        createVersion: bool = None,
    ) -> PutIntentResponseTypeDef:
        """
        [Client.put_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.put_intent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_slot_type(
        self,
        name: str,
        description: str = None,
        enumerationValues: List[EnumerationValueTypeDef] = None,
        checksum: str = None,
        valueSelectionStrategy: Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"] = None,
        createVersion: bool = None,
    ) -> PutSlotTypeResponseTypeDef:
        """
        [Client.put_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.put_slot_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_import(
        self,
        payload: Union[bytes, IO],
        resourceType: Literal["BOT", "INTENT", "SLOT_TYPE"],
        mergeStrategy: Literal["OVERWRITE_LATEST", "FAIL_ON_CONFLICT"],
    ) -> StartImportResponseTypeDef:
        """
        [Client.start_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Client.start_import)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_bot_aliases"]
    ) -> paginator_scope.GetBotAliasesPaginator:
        """
        [Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_bot_channel_associations"]
    ) -> paginator_scope.GetBotChannelAssociationsPaginator:
        """
        [Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_bot_versions"]
    ) -> paginator_scope.GetBotVersionsPaginator:
        """
        [Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_bots"]
    ) -> paginator_scope.GetBotsPaginator:
        """
        [Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_builtin_intents"]
    ) -> paginator_scope.GetBuiltinIntentsPaginator:
        """
        [Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_builtin_slot_types"]
    ) -> paginator_scope.GetBuiltinSlotTypesPaginator:
        """
        [Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_intent_versions"]
    ) -> paginator_scope.GetIntentVersionsPaginator:
        """
        [Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_intents"]
    ) -> paginator_scope.GetIntentsPaginator:
        """
        [Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_slot_type_versions"]
    ) -> paginator_scope.GetSlotTypeVersionsPaginator:
        """
        [Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_slot_types"]
    ) -> paginator_scope.GetSlotTypesPaginator:
        """
        [Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    PreconditionFailedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
