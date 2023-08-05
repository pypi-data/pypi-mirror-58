"Main interface for migrationhub-config service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_migrationhub_config.client as client_scope
from mypy_boto3_migrationhub_config.type_defs import (
    CreateHomeRegionControlResultTypeDef,
    DescribeHomeRegionControlsResultTypeDef,
    GetHomeRegionResultTypeDef,
    TargetTypeDef,
)


__all__ = ("MigrationHubConfigClient",)


class MigrationHubConfigClient(BaseClient):
    """
    [MigrationHubConfig.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/migrationhub-config.html#MigrationHubConfig.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/migrationhub-config.html#MigrationHubConfig.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_home_region_control(
        self, HomeRegion: str, Target: TargetTypeDef, DryRun: bool = None
    ) -> CreateHomeRegionControlResultTypeDef:
        """
        [Client.create_home_region_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/migrationhub-config.html#MigrationHubConfig.Client.create_home_region_control)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_home_region_controls(
        self,
        ControlId: str = None,
        HomeRegion: str = None,
        Target: TargetTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeHomeRegionControlsResultTypeDef:
        """
        [Client.describe_home_region_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/migrationhub-config.html#MigrationHubConfig.Client.describe_home_region_controls)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/migrationhub-config.html#MigrationHubConfig.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_home_region(self) -> GetHomeRegionResultTypeDef:
        """
        [Client.get_home_region documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/migrationhub-config.html#MigrationHubConfig.Client.get_home_region)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    DryRunOperation: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
