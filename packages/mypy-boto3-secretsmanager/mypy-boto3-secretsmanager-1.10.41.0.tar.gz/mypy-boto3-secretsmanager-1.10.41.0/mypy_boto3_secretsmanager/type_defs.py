"Main interface for secretsmanager service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, IO, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CancelRotateSecretResponseTypeDef = TypedDict(
    "CancelRotateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)

CreateSecretResponseTypeDef = TypedDict(
    "CreateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)

DeleteResourcePolicyResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)

DeleteSecretResponseTypeDef = TypedDict(
    "DeleteSecretResponseTypeDef", {"ARN": str, "Name": str, "DeletionDate": datetime}, total=False
)

RotationRulesTypeTypeDef = TypedDict(
    "RotationRulesTypeTypeDef", {"AutomaticallyAfterDays": int}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

DescribeSecretResponseTypeDef = TypedDict(
    "DescribeSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": RotationRulesTypeTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[TagTypeDef],
        "VersionIdsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)

GetRandomPasswordResponseTypeDef = TypedDict(
    "GetRandomPasswordResponseTypeDef", {"RandomPassword": str}, total=False
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {"ARN": str, "Name": str, "ResourcePolicy": str},
    total=False,
)

GetSecretValueResponseTypeDef = TypedDict(
    "GetSecretValueResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "SecretBinary": Union[bytes, IO],
        "SecretString": str,
        "VersionStages": List[str],
        "CreatedDate": datetime,
    },
    total=False,
)

SecretVersionsListEntryTypeDef = TypedDict(
    "SecretVersionsListEntryTypeDef",
    {
        "VersionId": str,
        "VersionStages": List[str],
        "LastAccessedDate": datetime,
        "CreatedDate": datetime,
    },
    total=False,
)

ListSecretVersionIdsResponseTypeDef = TypedDict(
    "ListSecretVersionIdsResponseTypeDef",
    {"Versions": List[SecretVersionsListEntryTypeDef], "NextToken": str, "ARN": str, "Name": str},
    total=False,
)

SecretListEntryTypeDef = TypedDict(
    "SecretListEntryTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": RotationRulesTypeTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[TagTypeDef],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)

ListSecretsResponseTypeDef = TypedDict(
    "ListSecretsResponseTypeDef",
    {"SecretList": List[SecretListEntryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)

PutSecretValueResponseTypeDef = TypedDict(
    "PutSecretValueResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str, "VersionStages": List[str]},
    total=False,
)

RestoreSecretResponseTypeDef = TypedDict(
    "RestoreSecretResponseTypeDef", {"ARN": str, "Name": str}, total=False
)

RotateSecretResponseTypeDef = TypedDict(
    "RotateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)

UpdateSecretResponseTypeDef = TypedDict(
    "UpdateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)

UpdateSecretVersionStageResponseTypeDef = TypedDict(
    "UpdateSecretVersionStageResponseTypeDef", {"ARN": str, "Name": str}, total=False
)
