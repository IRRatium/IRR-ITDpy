from typing import Optional
from pydantic import Field
from .base import ITDBaseModel


class Pin(ITDBaseModel):
    slug: str
    name: str
    description: Optional[str] = None
    granted_at: Optional[str] = Field(None, alias="grantedAt")

    def __repr__(self) -> str:
        return f"<Pin {self.slug}>"
