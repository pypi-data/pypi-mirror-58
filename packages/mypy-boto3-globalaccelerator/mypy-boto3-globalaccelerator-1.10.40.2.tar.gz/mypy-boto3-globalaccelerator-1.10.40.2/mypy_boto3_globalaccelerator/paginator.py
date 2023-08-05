"Main interface for globalaccelerator service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_globalaccelerator.type_defs import (
    ListAcceleratorsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListAcceleratorsPaginator", "ListEndpointGroupsPaginator", "ListListenersPaginator")


class ListAcceleratorsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAcceleratorsResponseTypeDef, None, None]:
        """
        [ListAccelerators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators.paginate)
        """


class ListEndpointGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ListenerArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListEndpointGroupsResponseTypeDef, None, None]:
        """
        [ListEndpointGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups.paginate)
        """


class ListListenersPaginator(Boto3Paginator):
    """
    [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AcceleratorArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListListenersResponseTypeDef, None, None]:
        """
        [ListListeners.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners.paginate)
        """
