from __future__ import annotations

from typing import List, Optional
from pydantic import Field
from .base import ITDBaseModel


class PollOption(ITDBaseModel):
    id: Optional[str] = None
    text: str
    position: Optional[int] = None
    votes_count: int = Field(0, alias="votesCount")


class Poll(ITDBaseModel):
    
    id: Optional[str] = None
    post_id: Optional[str] = Field(None, alias="postId")

    question: str
    options: List[PollOption]

    multiple_choice: bool = Field(False, alias="multipleChoice")

    total_votes: int = Field(0, alias="totalVotes")
    has_voted: bool = Field(False, alias="hasVoted")
    voted_option_ids: List[str] = Field(default_factory=list, alias="votedOptionIds")
    created_at: str = Field(..., alias="createdAt")

    @classmethod
    def from_simple(
        cls,
        question: str,
        options: list[str],
        multiple_choice: bool = False,
    ) -> "Poll":

        if len(options) < 2:
            raise ValueError("Poll must contain at least 2 options")

        if len(options) > 10:
            raise ValueError("Poll cannot contain more than 10 options")

        return cls(
            question=question,
            options=[PollOption(text=o) for o in options],
            multipleChoice=multiple_choice,
        )
