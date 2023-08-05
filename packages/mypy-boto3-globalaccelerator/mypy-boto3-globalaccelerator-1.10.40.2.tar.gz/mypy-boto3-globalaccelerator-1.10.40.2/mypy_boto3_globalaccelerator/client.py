"Main interface for globalaccelerator service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_globalaccelerator.client as client_scope

# pylint: disable=import-self
import mypy_boto3_globalaccelerator.paginator as paginator_scope
from mypy_boto3_globalaccelerator.type_defs import (
    CreateAcceleratorResponseTypeDef,
    CreateEndpointGroupResponseTypeDef,
    CreateListenerResponseTypeDef,
    DescribeAcceleratorAttributesResponseTypeDef,
    DescribeAcceleratorResponseTypeDef,
    DescribeEndpointGroupResponseTypeDef,
    DescribeListenerResponseTypeDef,
    EndpointConfigurationTypeDef,
    ListAcceleratorsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    PortRangeTypeDef,
    UpdateAcceleratorAttributesResponseTypeDef,
    UpdateAcceleratorResponseTypeDef,
    UpdateEndpointGroupResponseTypeDef,
    UpdateListenerResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlobalAcceleratorClient",)


class GlobalAcceleratorClient(BaseClient):
    """
    [GlobalAccelerator.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_accelerator(
        self,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: Literal["IPV4"] = None,
        Enabled: bool = None,
    ) -> CreateAcceleratorResponseTypeDef:
        """
        [Client.create_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_endpoint_group(
        self,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> CreateEndpointGroupResponseTypeDef:
        """
        [Client.create_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_listener(
        self,
        AcceleratorArn: str,
        PortRanges: List[PortRangeTypeDef],
        Protocol: Literal["TCP", "UDP"],
        IdempotencyToken: str,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> CreateListenerResponseTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_accelerator(self, AcceleratorArn: str) -> None:
        """
        [Client.delete_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint_group(self, EndpointGroupArn: str) -> None:
        """
        [Client.delete_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_listener(self, ListenerArn: str) -> None:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_accelerator(self, AcceleratorArn: str) -> DescribeAcceleratorResponseTypeDef:
        """
        [Client.describe_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_accelerator_attributes(
        self, AcceleratorArn: str
    ) -> DescribeAcceleratorAttributesResponseTypeDef:
        """
        [Client.describe_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoint_group(
        self, EndpointGroupArn: str
    ) -> DescribeEndpointGroupResponseTypeDef:
        """
        [Client.describe_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_listener(self, ListenerArn: str) -> DescribeListenerResponseTypeDef:
        """
        [Client.describe_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accelerators(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListAcceleratorsResponseTypeDef:
        """
        [Client.list_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_endpoint_groups(
        self, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListEndpointGroupsResponseTypeDef:
        """
        [Client.list_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_listeners(
        self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListListenersResponseTypeDef:
        """
        [Client.list_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_accelerator(
        self,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: Literal["IPV4"] = None,
        Enabled: bool = None,
    ) -> UpdateAcceleratorResponseTypeDef:
        """
        [Client.update_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_accelerator_attributes(
        self,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None,
    ) -> UpdateAcceleratorAttributesResponseTypeDef:
        """
        [Client.update_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_endpoint_group(
        self,
        EndpointGroupArn: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> UpdateEndpointGroupResponseTypeDef:
        """
        [Client.update_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_listener(
        self,
        ListenerArn: str,
        PortRanges: List[PortRangeTypeDef] = None,
        Protocol: Literal["TCP", "UDP"] = None,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> UpdateListenerResponseTypeDef:
        """
        [Client.update_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accelerators"]
    ) -> paginator_scope.ListAcceleratorsPaginator:
        """
        [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_endpoint_groups"]
    ) -> paginator_scope.ListEndpointGroupsPaginator:
        """
        [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_listeners"]
    ) -> paginator_scope.ListListenersPaginator:
        """
        [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
        """


class Exceptions:
    AcceleratorNotDisabledException: Boto3ClientError
    AcceleratorNotFoundException: Boto3ClientError
    AccessDeniedException: Boto3ClientError
    AssociatedEndpointGroupFoundException: Boto3ClientError
    AssociatedListenerFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    EndpointGroupAlreadyExistsException: Boto3ClientError
    EndpointGroupNotFoundException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidPortRangeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError
