"Main interface for personalize-runtime service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


PredictedItemTypeDef = TypedDict("PredictedItemTypeDef", {"itemId": str}, total=False)

GetPersonalizedRankingResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseTypeDef",
    {"personalizedRanking": List[PredictedItemTypeDef]},
    total=False,
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef", {"itemList": List[PredictedItemTypeDef]}, total=False
)
