"Main interface for secretsmanager service"
from mypy_boto3_secretsmanager.client import SecretsManagerClient, SecretsManagerClient as Client
from mypy_boto3_secretsmanager.paginator import ListSecretsPaginator


__all__ = ("Client", "ListSecretsPaginator", "SecretsManagerClient")
