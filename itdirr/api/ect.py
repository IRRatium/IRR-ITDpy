from __future__ import annotations

from ..models import WhoToFollow, HashtagPosts, Search, TrendingHashtagsResponse

def who_to_follow(client) -> WhoToFollow:
    response = client.get("/api/users/suggestions/who-to-follow")
    response.raise_for_status()
    return WhoToFollow.model_validate(response.json())

def search_hashtags(client, name, limit=20) -> HashtagPosts:
    response = client.get(f"/api/hashtags/{name}/posts?limit={limit}")
    response.raise_for_status()
    return HashtagPosts.model_validate(response.json())

def search(client, query, user_limit = 5, hashtag_limit = 5):
    response = client.get(f"/api/search/?q={query}&userLimit={user_limit}&hashtagLimit={hashtag_limit}")
    response.raise_for_status()
    return Search.model_validate(response.json())

def get_trending_hashtags(client, limit: int = 10) -> TrendingHashtagsResponse:

    response = client.get(
        "/api/hashtags/trending",
        params={"limit": limit},
    )

    response.raise_for_status()

    data = response.json()["data"]
    hashtags = data["hashtags"]

    return TrendingHashtagsResponse.model_validate(response.json()["data"])