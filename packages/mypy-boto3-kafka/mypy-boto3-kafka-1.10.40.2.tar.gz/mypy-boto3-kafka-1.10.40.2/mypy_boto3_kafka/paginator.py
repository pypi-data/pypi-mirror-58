"Main interface for kafka service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kafka.type_defs import (
    ListClusterOperationsResponseTypeDef,
    ListClustersResponseTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListNodesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListClusterOperationsPaginator",
    "ListClustersPaginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListNodesPaginator",
)


class ListClusterOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListClusterOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClusterOperationsResponseTypeDef, None, None]:
        """
        [ListClusterOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ClusterNameFilter: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClustersResponseTypeDef, None, None]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListClusters.paginate)
        """


class ListConfigurationRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConfigurationRevisionsResponseTypeDef, None, None]:
        """
        [ListConfigurationRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions.paginate)
        """


class ListConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConfigurationsResponseTypeDef, None, None]:
        """
        [ListConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListConfigurations.paginate)
        """


class ListNodesPaginator(Boto3Paginator):
    """
    [Paginator.ListNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListNodes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListNodesResponseTypeDef, None, None]:
        """
        [ListNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kafka.html#Kafka.Paginator.ListNodes.paginate)
        """
