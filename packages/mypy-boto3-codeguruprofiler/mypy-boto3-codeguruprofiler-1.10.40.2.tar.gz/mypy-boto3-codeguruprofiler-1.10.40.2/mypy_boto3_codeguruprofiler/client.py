"Main interface for codeguruprofiler service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, IO, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_codeguruprofiler.client as client_scope
from mypy_boto3_codeguruprofiler.type_defs import (
    AgentOrchestrationConfigTypeDef,
    ConfigureAgentResponseTypeDef,
    CreateProfilingGroupResponseTypeDef,
    DescribeProfilingGroupResponseTypeDef,
    GetProfileResponseTypeDef,
    ListProfileTimesResponseTypeDef,
    ListProfilingGroupsResponseTypeDef,
    UpdateProfilingGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeGuruProfilerClient",)


class CodeGuruProfilerClient(BaseClient):
    """
    [CodeGuruProfiler.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def configure_agent(
        self, profilingGroupName: str, fleetInstanceId: str = None
    ) -> ConfigureAgentResponseTypeDef:
        """
        [Client.configure_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.configure_agent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_profiling_group(
        self,
        clientToken: str,
        profilingGroupName: str,
        agentOrchestrationConfig: AgentOrchestrationConfigTypeDef = None,
    ) -> CreateProfilingGroupResponseTypeDef:
        """
        [Client.create_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.create_profiling_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_profiling_group(self, profilingGroupName: str) -> Dict[str, Any]:
        """
        [Client.delete_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.delete_profiling_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_profiling_group(
        self, profilingGroupName: str
    ) -> DescribeProfilingGroupResponseTypeDef:
        """
        [Client.describe_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.describe_profiling_group)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_profile(
        self,
        profilingGroupName: str,
        accept: str = None,
        endTime: datetime = None,
        maxDepth: int = None,
        period: str = None,
        startTime: datetime = None,
    ) -> GetProfileResponseTypeDef:
        """
        [Client.get_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_profile_times(
        self,
        endTime: datetime,
        period: Literal["P1D", "PT1H", "PT5M"],
        profilingGroupName: str,
        startTime: datetime,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: Literal["TimestampAscending", "TimestampDescending"] = None,
    ) -> ListProfileTimesResponseTypeDef:
        """
        [Client.list_profile_times documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profile_times)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_profiling_groups(
        self, includeDescription: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ListProfilingGroupsResponseTypeDef:
        """
        [Client.list_profiling_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profiling_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_agent_profile(
        self,
        agentProfile: Union[bytes, IO],
        contentType: str,
        profilingGroupName: str,
        profileToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.post_agent_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.post_agent_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_profiling_group(
        self, agentOrchestrationConfig: AgentOrchestrationConfigTypeDef, profilingGroupName: str
    ) -> UpdateProfilingGroupResponseTypeDef:
        """
        [Client.update_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.update_profiling_group)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
