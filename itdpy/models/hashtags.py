from pydantic import Field, model_validator
from typing import List, Any
from .base import ITDBaseModel
from .post import Post
from .pagination import Pagination


class Hashtag(ITDBaseModel):
    id: str
    name: str
    posts_count: int = Field(alias="postsCount")

class HashtagPosts(ITDBaseModel):
    hashtag: Hashtag
    posts: List[Post]
    pagination: Pagination | None = None

    @model_validator(mode="before")
    @classmethod
    def flatten_data(cls, payload: Any):
        if isinstance(payload, dict) and "data" in payload:
            return payload["data"]
        return payload

    def __iter__(self):
        return iter(self.posts)

    def __len__(self):
        return len(self.posts)

    def __getitem__(self, item):
        return self.posts[item]

    def __repr__(self):
        return f"<HashtagPosts #{self.hashtag.name} posts={len(self)}>"
    
class TrendingHashtagsResponse(ITDBaseModel):
    hashtags: list[Hashtag]

    def __iter__(self):
        return iter(self.hashtags)

    def __len__(self):
        return len(self.hashtags)

    def __getitem__(self, item):
        return self.hashtags[item]