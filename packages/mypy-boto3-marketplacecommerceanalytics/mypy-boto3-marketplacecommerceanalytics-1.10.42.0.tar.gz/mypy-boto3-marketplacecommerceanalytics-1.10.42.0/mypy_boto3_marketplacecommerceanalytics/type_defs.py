"Main interface for marketplacecommerceanalytics service type defs"
from __future__ import annotations

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


GenerateDataSetResultTypeDef = TypedDict(
    "GenerateDataSetResultTypeDef", {"dataSetRequestId": str}, total=False
)

StartSupportDataExportResultTypeDef = TypedDict(
    "StartSupportDataExportResultTypeDef", {"dataSetRequestId": str}, total=False
)
