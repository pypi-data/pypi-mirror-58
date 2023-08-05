"Main interface for lex-models service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lex_models.type_defs import (
    GetBotAliasesResponseTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBotsResponseTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetIntentsResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetBotAliasesPaginator",
    "GetBotChannelAssociationsPaginator",
    "GetBotVersionsPaginator",
    "GetBotsPaginator",
    "GetBuiltinIntentsPaginator",
    "GetBuiltinSlotTypesPaginator",
    "GetIntentVersionsPaginator",
    "GetIntentsPaginator",
    "GetSlotTypeVersionsPaginator",
    "GetSlotTypesPaginator",
)


class GetBotAliasesPaginator(Boto3Paginator):
    """
    [Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        botName: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBotAliasesResponseTypeDef, None, None]:
        """
        [GetBotAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases.paginate)
        """


class GetBotChannelAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        botName: str,
        botAlias: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBotChannelAssociationsResponseTypeDef, None, None]:
        """
        [GetBotChannelAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations.paginate)
        """


class GetBotVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetBotVersionsResponseTypeDef, None, None]:
        """
        [GetBotVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions.paginate)
        """


class GetBotsPaginator(Boto3Paginator):
    """
    [Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetBotsResponseTypeDef, None, None]:
        """
        [GetBots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots.paginate)
        """


class GetBuiltinIntentsPaginator(Boto3Paginator):
    """
    [Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBuiltinIntentsResponseTypeDef, None, None]:
        """
        [GetBuiltinIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents.paginate)
        """


class GetBuiltinSlotTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBuiltinSlotTypesResponseTypeDef, None, None]:
        """
        [GetBuiltinSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes.paginate)
        """


class GetIntentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetIntentVersionsResponseTypeDef, None, None]:
        """
        [GetIntentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions.paginate)
        """


class GetIntentsPaginator(Boto3Paginator):
    """
    [Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetIntentsResponseTypeDef, None, None]:
        """
        [GetIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents.paginate)
        """


class GetSlotTypeVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSlotTypeVersionsResponseTypeDef, None, None]:
        """
        [GetSlotTypeVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions.paginate)
        """


class GetSlotTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSlotTypesResponseTypeDef, None, None]:
        """
        [GetSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes.paginate)
        """
