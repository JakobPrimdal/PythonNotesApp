from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Tag:
    MAX_LENGTH: ClassVar[int] = 30

    name: str

    def __post_init__(self):
        cleaned = self.name.strip().lower()
        if cleaned == "":
            raise ValueError("Tag name cannot be empty")
        if len(cleaned) > self.MAX_LENGTH:
            raise ValueError(f"Tag name cannot be longer than {self.MAX_LENGTH}")
        object.__setattr__(self, "name", cleaned)