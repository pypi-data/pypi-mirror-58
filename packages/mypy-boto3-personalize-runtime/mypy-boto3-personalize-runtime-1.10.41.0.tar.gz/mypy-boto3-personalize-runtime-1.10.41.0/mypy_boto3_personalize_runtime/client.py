"Main interface for personalize-runtime service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_personalize_runtime.client as client_scope
from mypy_boto3_personalize_runtime.type_defs import (
    GetPersonalizedRankingResponseTypeDef,
    GetRecommendationsResponseTypeDef,
)


__all__ = ("PersonalizeRuntimeClient",)


class PersonalizeRuntimeClient(BaseClient):
    """
    [PersonalizeRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-runtime.html#PersonalizeRuntime.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_personalized_ranking(
        self, campaignArn: str, inputList: List[str], userId: str
    ) -> GetPersonalizedRankingResponseTypeDef:
        """
        [Client.get_personalized_ranking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_personalized_ranking)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_recommendations(
        self, campaignArn: str, itemId: str = None, userId: str = None, numResults: int = None
    ) -> GetRecommendationsResponseTypeDef:
        """
        [Client.get_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_recommendations)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
