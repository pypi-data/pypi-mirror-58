"Main interface for forecastquery service type defs"
from __future__ import annotations

import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


DataPointTypeDef = TypedDict("DataPointTypeDef", {"Timestamp": str, "Value": float}, total=False)

ForecastTypeDef = TypedDict(
    "ForecastTypeDef", {"Predictions": Dict[str, List[DataPointTypeDef]]}, total=False
)

QueryForecastResponseTypeDef = TypedDict(
    "QueryForecastResponseTypeDef", {"Forecast": ForecastTypeDef}, total=False
)
