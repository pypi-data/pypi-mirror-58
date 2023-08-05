"Main interface for route53resolver service"
from mypy_boto3_route53resolver.client import Route53ResolverClient as Client, Route53ResolverClient
from mypy_boto3_route53resolver.paginator import ListTagsForResourcePaginator


__all__ = ("Client", "ListTagsForResourcePaginator", "Route53ResolverClient")
