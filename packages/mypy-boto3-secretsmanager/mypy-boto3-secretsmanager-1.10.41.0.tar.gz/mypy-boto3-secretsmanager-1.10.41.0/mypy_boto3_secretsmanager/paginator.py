"Main interface for secretsmanager service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_secretsmanager.type_defs import ListSecretsResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListSecretsPaginator",)


class ListSecretsPaginator(Boto3Paginator):
    """
    [Paginator.ListSecrets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSecretsResponseTypeDef, None, None]:
        """
        [ListSecrets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets.paginate)
        """
