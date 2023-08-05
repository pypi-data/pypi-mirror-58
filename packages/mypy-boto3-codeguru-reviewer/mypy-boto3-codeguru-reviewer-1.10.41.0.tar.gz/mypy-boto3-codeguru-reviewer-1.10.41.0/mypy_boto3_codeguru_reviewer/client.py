"Main interface for codeguru-reviewer service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_codeguru_reviewer.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codeguru_reviewer.paginator as paginator_scope
from mypy_boto3_codeguru_reviewer.type_defs import (
    AssociateRepositoryResponseTypeDef,
    DescribeRepositoryAssociationResponseTypeDef,
    DisassociateRepositoryResponseTypeDef,
    ListRepositoryAssociationsResponseTypeDef,
    RepositoryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeGuruReviewerClient",)


class CodeGuruReviewerClient(BaseClient):
    """
    [CodeGuruReviewer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_repository(
        self, Repository: RepositoryTypeDef, ClientRequestToken: str = None
    ) -> AssociateRepositoryResponseTypeDef:
        """
        [Client.associate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.associate_repository)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_repository_association(
        self, AssociationArn: str
    ) -> DescribeRepositoryAssociationResponseTypeDef:
        """
        [Client.describe_repository_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_repository(self, AssociationArn: str) -> DisassociateRepositoryResponseTypeDef:
        """
        [Client.disassociate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.disassociate_repository)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_repository_associations(
        self,
        ProviderTypes: List[Literal["CodeCommit", "GitHub"]] = None,
        States: List[Literal["Associated", "Associating", "Failed", "Disassociating"]] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListRepositoryAssociationsResponseTypeDef:
        """
        [Client.list_repository_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_repository_associations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_repository_associations"]
    ) -> paginator_scope.ListRepositoryAssociationsPaginator:
        """
        [Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
