"Main interface for translate service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_translate.type_defs import ListTerminologiesResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListTerminologiesPaginator",)


class ListTerminologiesPaginator(Boto3Paginator):
    """
    [Paginator.ListTerminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/translate.html#Translate.Paginator.ListTerminologies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTerminologiesResponseTypeDef, None, None]:
        """
        [ListTerminologies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/translate.html#Translate.Paginator.ListTerminologies.paginate)
        """
