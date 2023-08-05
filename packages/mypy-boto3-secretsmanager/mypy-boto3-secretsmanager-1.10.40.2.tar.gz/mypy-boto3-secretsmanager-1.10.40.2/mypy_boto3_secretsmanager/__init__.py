"Main interface for secretsmanager service"
from mypy_boto3_secretsmanager.client import SecretsManagerClient as Client, SecretsManagerClient
from mypy_boto3_secretsmanager.paginator import ListSecretsPaginator


__all__ = ("Client", "ListSecretsPaginator", "SecretsManagerClient")
