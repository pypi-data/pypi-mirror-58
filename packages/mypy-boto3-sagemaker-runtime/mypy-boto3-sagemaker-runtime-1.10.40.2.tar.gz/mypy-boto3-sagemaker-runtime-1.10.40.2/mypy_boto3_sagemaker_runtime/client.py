"Main interface for sagemaker-runtime service Client"
from __future__ import annotations

from typing import Any, Dict, IO, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sagemaker_runtime.client as client_scope
from mypy_boto3_sagemaker_runtime.type_defs import InvokeEndpointOutputTypeDef


__all__ = ("SageMakerRuntimeClient",)


class SageMakerRuntimeClient(BaseClient):
    """
    [SageMakerRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invoke_endpoint(
        self,
        EndpointName: str,
        Body: Union[bytes, IO],
        ContentType: str = None,
        Accept: str = None,
        CustomAttributes: str = None,
        TargetModel: str = None,
    ) -> InvokeEndpointOutputTypeDef:
        """
        [Client.invoke_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalFailure: Boto3ClientError
    ModelError: Boto3ClientError
    ServiceUnavailable: Boto3ClientError
    ValidationError: Boto3ClientError
