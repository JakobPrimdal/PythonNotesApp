import uuid
from dataclasses import dataclass
from typing import ClassVar
from uuid import UUID


@dataclass(eq=False)
class Tag:
    MAX_LENGTH: ClassVar[int] = 30

    _id: UUID
    _name: str

    def __post_init__(self) -> None:
        self._validate_name(self._name)
        self._name = self._normalize(self._name)

    @classmethod
    def create(cls, name: str) -> "Tag":
        return cls(
            _id=uuid.uuid4(),
            _name=name
        )

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def rename(self, new_name: str) -> None:
        self._validate_name(new_name)
        self._name = self._normalize(new_name)

    def _validate_name(self, name: str) -> None:
        cleaned = self._normalize(name)
        if cleaned == "":
            raise ValueError("Tag name cannot be empty")
        if len(cleaned) > self.MAX_LENGTH:
            raise ValueError(f"Tag name cannot be longer than {self.MAX_LENGTH} characters")

    @staticmethod
    def _normalize(name: str) -> str:
        return name.strip().lower()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented
        return self._id == other.id

    def __hash__(self) -> int:
        return hash(self._id)