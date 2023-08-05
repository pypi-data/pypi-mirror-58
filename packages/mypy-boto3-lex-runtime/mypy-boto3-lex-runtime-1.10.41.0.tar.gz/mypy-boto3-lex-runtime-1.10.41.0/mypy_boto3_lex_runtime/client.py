"Main interface for lex-runtime service Client"
from __future__ import annotations

from typing import Any, Dict, IO, List, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_lex_runtime.client as client_scope
from mypy_boto3_lex_runtime.type_defs import (
    DeleteSessionResponseTypeDef,
    DialogActionTypeDef,
    GetSessionResponseTypeDef,
    IntentSummaryTypeDef,
    PostContentResponseTypeDef,
    PostTextResponseTypeDef,
    PutSessionResponseTypeDef,
)


__all__ = ("LexRuntimeServiceClient",)


class LexRuntimeServiceClient(BaseClient):
    """
    [LexRuntimeService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_session(
        self, botName: str, botAlias: str, userId: str
    ) -> DeleteSessionResponseTypeDef:
        """
        [Client.delete_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client.delete_session)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_session(
        self, botName: str, botAlias: str, userId: str, checkpointLabelFilter: str = None
    ) -> GetSessionResponseTypeDef:
        """
        [Client.get_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client.get_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_content(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO],
        sessionAttributes: str = None,
        requestAttributes: str = None,
        accept: str = None,
    ) -> PostContentResponseTypeDef:
        """
        [Client.post_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client.post_content)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_text(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Dict[str, str] = None,
        requestAttributes: Dict[str, str] = None,
    ) -> PostTextResponseTypeDef:
        """
        [Client.post_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client.post_text)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Dict[str, str] = None,
        dialogAction: DialogActionTypeDef = None,
        recentIntentSummaryView: List[IntentSummaryTypeDef] = None,
        accept: str = None,
    ) -> PutSessionResponseTypeDef:
        """
        [Client.put_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lex-runtime.html#LexRuntimeService.Client.put_session)
        """


class Exceptions:
    BadGatewayException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    DependencyFailedException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    LoopDetectedException: Boto3ClientError
    NotAcceptableException: Boto3ClientError
    NotFoundException: Boto3ClientError
    RequestTimeoutException: Boto3ClientError
    UnsupportedMediaTypeException: Boto3ClientError
