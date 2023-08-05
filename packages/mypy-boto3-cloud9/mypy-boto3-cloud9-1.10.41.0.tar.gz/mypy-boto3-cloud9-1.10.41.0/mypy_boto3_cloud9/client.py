"Main interface for cloud9 service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_cloud9.client as client_scope

# pylint: disable=import-self
import mypy_boto3_cloud9.paginator as paginator_scope
from mypy_boto3_cloud9.type_defs import (
    CreateEnvironmentEC2ResultTypeDef,
    CreateEnvironmentMembershipResultTypeDef,
    DescribeEnvironmentMembershipsResultTypeDef,
    DescribeEnvironmentStatusResultTypeDef,
    DescribeEnvironmentsResultTypeDef,
    ListEnvironmentsResultTypeDef,
    UpdateEnvironmentMembershipResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Cloud9Client",)


class Cloud9Client(BaseClient):
    """
    [Cloud9.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_environment_ec2(
        self,
        name: str,
        instanceType: str,
        description: str = None,
        clientRequestToken: str = None,
        subnetId: str = None,
        automaticStopTimeMinutes: int = None,
        ownerArn: str = None,
    ) -> CreateEnvironmentEC2ResultTypeDef:
        """
        [Client.create_environment_ec2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_environment_membership(
        self, environmentId: str, userArn: str, permissions: Literal["read-write", "read-only"]
    ) -> CreateEnvironmentMembershipResultTypeDef:
        """
        [Client.create_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.create_environment_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_environment(self, environmentId: str) -> Dict[str, Any]:
        """
        [Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.delete_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_environment_membership(self, environmentId: str, userArn: str) -> Dict[str, Any]:
        """
        [Client.delete_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_environment_memberships(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[Literal["owner", "read-write", "read-only"]] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeEnvironmentMembershipsResultTypeDef:
        """
        [Client.describe_environment_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.describe_environment_memberships)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_environment_status(
        self, environmentId: str
    ) -> DescribeEnvironmentStatusResultTypeDef:
        """
        [Client.describe_environment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.describe_environment_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_environments(self, environmentIds: List[str]) -> DescribeEnvironmentsResultTypeDef:
        """
        [Client.describe_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.describe_environments)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_environments(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListEnvironmentsResultTypeDef:
        """
        [Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.list_environments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_environment(
        self, environmentId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.update_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_environment_membership(
        self, environmentId: str, userArn: str, permissions: Literal["read-write", "read-only"]
    ) -> UpdateEnvironmentMembershipResultTypeDef:
        """
        [Client.update_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Client.update_environment_membership)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_environment_memberships"]
    ) -> paginator_scope.DescribeEnvironmentMembershipsPaginator:
        """
        [Paginator.DescribeEnvironmentMemberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> paginator_scope.ListEnvironmentsPaginator:
        """
        [Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
