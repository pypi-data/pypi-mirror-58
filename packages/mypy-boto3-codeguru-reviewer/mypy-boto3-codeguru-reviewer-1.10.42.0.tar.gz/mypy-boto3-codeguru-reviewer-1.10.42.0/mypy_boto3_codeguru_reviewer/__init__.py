"Main interface for codeguru-reviewer service"
from mypy_boto3_codeguru_reviewer.client import (
    CodeGuruReviewerClient,
    CodeGuruReviewerClient as Client,
)
from mypy_boto3_codeguru_reviewer.paginator import ListRepositoryAssociationsPaginator


__all__ = ("Client", "CodeGuruReviewerClient", "ListRepositoryAssociationsPaginator")
