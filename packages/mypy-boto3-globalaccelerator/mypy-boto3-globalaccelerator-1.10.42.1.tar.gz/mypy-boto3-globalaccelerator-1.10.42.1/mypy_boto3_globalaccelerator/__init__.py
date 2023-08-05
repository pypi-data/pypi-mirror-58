"Main interface for globalaccelerator service"
from mypy_boto3_globalaccelerator.client import (
    GlobalAcceleratorClient,
    GlobalAcceleratorClient as Client,
)
from mypy_boto3_globalaccelerator.paginator import (
    ListAcceleratorsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)


__all__ = (
    "Client",
    "GlobalAcceleratorClient",
    "ListAcceleratorsPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)
