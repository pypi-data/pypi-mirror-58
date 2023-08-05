"Main interface for translate service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_translate.client as client_scope

# pylint: disable=import-self
import mypy_boto3_translate.paginator as paginator_scope
from mypy_boto3_translate.type_defs import (
    EncryptionKeyTypeDef,
    GetTerminologyResponseTypeDef,
    ImportTerminologyResponseTypeDef,
    ListTerminologiesResponseTypeDef,
    TerminologyDataTypeDef,
    TranslateTextResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TranslateClient",)


class TranslateClient(BaseClient):
    """
    [Translate.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_terminology(self, Name: str) -> None:
        """
        [Client.delete_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client.delete_terminology)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_terminology(
        self, Name: str, TerminologyDataFormat: Literal["CSV", "TMX"]
    ) -> GetTerminologyResponseTypeDef:
        """
        [Client.get_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client.get_terminology)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_terminology(
        self,
        Name: str,
        MergeStrategy: Literal["OVERWRITE"],
        TerminologyData: TerminologyDataTypeDef,
        Description: str = None,
        EncryptionKey: EncryptionKeyTypeDef = None,
    ) -> ImportTerminologyResponseTypeDef:
        """
        [Client.import_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client.import_terminology)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_terminologies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListTerminologiesResponseTypeDef:
        """
        [Client.list_terminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client.list_terminologies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def translate_text(
        self,
        Text: str,
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: List[str] = None,
    ) -> TranslateTextResponseTypeDef:
        """
        [Client.translate_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Client.translate_text)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_terminologies"]
    ) -> paginator_scope.ListTerminologiesPaginator:
        """
        [Paginator.ListTerminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/translate.html#Translate.Paginator.ListTerminologies)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DetectedLanguageLowConfidenceException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TextSizeLimitExceededException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnsupportedLanguagePairException: Boto3ClientError
