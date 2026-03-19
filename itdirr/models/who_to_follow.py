from pydantic import Field
from typing import List
from .base import ITDBaseModel


class SuggestedUser(ITDBaseModel):
    id: str
    username: str
    display_name: str = Field(alias="displayName")
    avatar: str
    verified: bool
    followers_count: int = Field(alias="followersCount")

class WhoToFollow(ITDBaseModel):
    users: List[SuggestedUser] = Field(default_factory=list)

    def __iter__(self):
        return iter(self.users)

    def __getitem__(self, item):
        return self.users[item]

    def __len__(self):
        return len(self.users)

    def __repr__(self):
        return f"<WhoToFollow count={len(self)}>"
