"Main interface for translate service"
from mypy_boto3_translate.client import TranslateClient, TranslateClient as Client
from mypy_boto3_translate.paginator import ListTerminologiesPaginator


__all__ = ("Client", "ListTerminologiesPaginator", "TranslateClient")
