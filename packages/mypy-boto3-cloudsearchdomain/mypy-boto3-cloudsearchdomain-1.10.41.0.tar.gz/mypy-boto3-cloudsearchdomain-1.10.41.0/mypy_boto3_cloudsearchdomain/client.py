"Main interface for cloudsearchdomain service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_cloudsearchdomain.client as client_scope
from mypy_boto3_cloudsearchdomain.type_defs import (
    SearchResponseTypeDef,
    SuggestResponseTypeDef,
    UploadDocumentsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudSearchDomainClient",)


class CloudSearchDomainClient(BaseClient):
    """
    [CloudSearchDomain.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search(
        self,
        query: str,
        cursor: str = None,
        expr: str = None,
        facet: str = None,
        filterQuery: str = None,
        highlight: str = None,
        partial: bool = None,
        queryOptions: str = None,
        queryParser: Literal["simple", "structured", "lucene", "dismax"] = None,
        returnFields: str = None,
        size: int = None,
        sort: str = None,
        start: int = None,
        stats: str = None,
    ) -> SearchResponseTypeDef:
        """
        [Client.search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.search)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def suggest(self, query: str, suggester: str, size: int = None) -> SuggestResponseTypeDef:
        """
        [Client.suggest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.suggest)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_documents(
        self,
        documents: Union[bytes, IO],
        contentType: Literal["application/json", "application/xml"],
    ) -> UploadDocumentsResponseTypeDef:
        """
        [Client.upload_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.upload_documents)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DocumentServiceException: Boto3ClientError
    SearchException: Boto3ClientError
