"Main interface for shield service"
from mypy_boto3_shield.client import ShieldClient as Client, ShieldClient
from mypy_boto3_shield.paginator import ListAttacksPaginator, ListProtectionsPaginator


__all__ = ("Client", "ListAttacksPaginator", "ListProtectionsPaginator", "ShieldClient")
