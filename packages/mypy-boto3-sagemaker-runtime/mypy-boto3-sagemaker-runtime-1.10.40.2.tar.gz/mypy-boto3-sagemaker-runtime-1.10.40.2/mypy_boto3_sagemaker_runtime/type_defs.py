"Main interface for sagemaker-runtime service type defs"
from __future__ import annotations

import sys
from typing import IO, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


_RequiredInvokeEndpointOutputTypeDef = TypedDict(
    "_RequiredInvokeEndpointOutputTypeDef", {"Body": Union[bytes, IO]}
)
_OptionalInvokeEndpointOutputTypeDef = TypedDict(
    "_OptionalInvokeEndpointOutputTypeDef",
    {"ContentType": str, "InvokedProductionVariant": str, "CustomAttributes": str},
    total=False,
)


class InvokeEndpointOutputTypeDef(
    _RequiredInvokeEndpointOutputTypeDef, _OptionalInvokeEndpointOutputTypeDef
):
    pass
