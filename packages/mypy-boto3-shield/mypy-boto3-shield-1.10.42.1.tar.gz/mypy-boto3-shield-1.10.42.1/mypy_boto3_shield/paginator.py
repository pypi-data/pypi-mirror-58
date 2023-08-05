"Main interface for shield service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_shield.type_defs import (
    ListAttacksResponseTypeDef,
    ListProtectionsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimeRangeTypeDef,
)


__all__ = ("ListAttacksPaginator", "ListProtectionsPaginator")


class ListAttacksPaginator(Boto3Paginator):
    """
    [Paginator.ListAttacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/shield.html#Shield.Paginator.ListAttacks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceArns: List[str] = None,
        StartTime: TimeRangeTypeDef = None,
        EndTime: TimeRangeTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAttacksResponseTypeDef, None, None]:
        """
        [ListAttacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/shield.html#Shield.Paginator.ListAttacks.paginate)
        """


class ListProtectionsPaginator(Boto3Paginator):
    """
    [Paginator.ListProtections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/shield.html#Shield.Paginator.ListProtections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProtectionsResponseTypeDef, None, None]:
        """
        [ListProtections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/shield.html#Shield.Paginator.ListProtections.paginate)
        """
