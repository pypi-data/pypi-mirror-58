"Main interface for ec2-instance-connect service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ec2_instance_connect.client as client_scope
from mypy_boto3_ec2_instance_connect.type_defs import SendSSHPublicKeyResponseTypeDef


__all__ = ("EC2InstanceConnectClient",)


class EC2InstanceConnectClient(BaseClient):
    """
    [EC2InstanceConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_ssh_public_key(
        self, InstanceId: str, InstanceOSUser: str, SSHPublicKey: str, AvailabilityZone: str
    ) -> SendSSHPublicKeyResponseTypeDef:
        """
        [Client.send_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_ssh_public_key)
        """


class Exceptions:
    AuthException: Boto3ClientError
    ClientError: Boto3ClientError
    EC2InstanceNotFoundException: Boto3ClientError
    InvalidArgsException: Boto3ClientError
    ServiceException: Boto3ClientError
    ThrottlingException: Boto3ClientError
