from typing import Optional, Union
from pydantic import Field

from .base import ITDBaseModel


class Pagination(ITDBaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 20
    total: Optional[int] = 0
    next_cursor: str | int | None = Field(default=None, alias="nextCursor")
    has_more: Optional[bool] = Field(False, alias="hasMore")

    def __repr__(self) -> str:
        return (
            f"<Pagination page={self.page} "
            f"limit={self.limit} total={self.total} "
            f"has_more={self.has_more}>"
        )
