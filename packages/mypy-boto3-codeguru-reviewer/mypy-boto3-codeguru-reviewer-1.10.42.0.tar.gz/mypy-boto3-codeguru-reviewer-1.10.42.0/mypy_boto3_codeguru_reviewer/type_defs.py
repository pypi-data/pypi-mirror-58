"Main interface for codeguru-reviewer service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


RepositoryAssociationTypeDef = TypedDict(
    "RepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

AssociateRepositoryResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": RepositoryAssociationTypeDef},
    total=False,
)

DescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "DescribeRepositoryAssociationResponseTypeDef",
    {"RepositoryAssociation": RepositoryAssociationTypeDef},
    total=False,
)

DisassociateRepositoryResponseTypeDef = TypedDict(
    "DisassociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": RepositoryAssociationTypeDef},
    total=False,
)

RepositoryAssociationSummaryTypeDef = TypedDict(
    "RepositoryAssociationSummaryTypeDef",
    {
        "AssociationArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
    },
    total=False,
)

ListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseTypeDef",
    {"RepositoryAssociationSummaries": List[RepositoryAssociationSummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

CodeCommitRepositoryTypeDef = TypedDict("CodeCommitRepositoryTypeDef", {"Name": str})

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef", {"CodeCommit": CodeCommitRepositoryTypeDef}, total=False
)
