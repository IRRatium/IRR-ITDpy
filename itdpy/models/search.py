from __future__ import annotations
from typing import List
from pydantic import Field, model_validator
from .base import ITDBaseModel
from .who_to_follow import SuggestedUser
from .hashtags import Hashtag


class Search(ITDBaseModel):
    users: List[SuggestedUser] = Field(default_factory=list)
    hashtags: List[Hashtag] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def unwrap_data(cls, payload):
        if isinstance(payload, dict) and "data" in payload:
            return payload["data"]
        return payload

    def __repr__(self):
        return (
            f"<Search users={len(self.users)} "
            f"hashtags={len(self.hashtags)}>"
        )