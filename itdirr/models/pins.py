from __future__ import annotations

from typing import Any
from pydantic import Field, model_validator
from typing import Optional
from .base import ITDBaseModel
from .pin import Pin


class Pins(ITDBaseModel):
    pins: list[Pin] = Field(default_factory=list)
    active_pin: Optional[str] = Field(None, alias="activePin")

    @model_validator(mode="before")
    @classmethod
    def parse_structure(cls, data: Any) -> Any:

        if isinstance(data, dict) and "data" in data:
            data = data["data"]

        if isinstance(data, dict):
            return {
                "pins": data.get("pins", []),
                "activePin": data.get("activePin")
            }

        return {"pins": [], "activePin": None}

    def __iter__(self):
        return iter(self.pins)

    def __getitem__(self, item):
        return self.pins[item]

    def __len__(self):
        return len(self.pins)

    def __repr__(self) -> str:
        return f"<Pins count={len(self)} active={self.active_pin}>"
