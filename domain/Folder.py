import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar
from uuid import UUID


@dataclass
class Folder:
    MAX_NAME_LENGTH: ClassVar[int] = 100

    _id: UUID
    _name: str
    _created_at: datetime

    def __post_init__(self):
        self._validate_name(self._name)

    @classmethod
    def create(cls, name: str) -> "Folder":
        return cls(
            _id=uuid.uuid4(),
            _name=name,
            _created_at=datetime.now()
        )

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def rename(self, new_name:str) -> None:
        self._validate_name(new_name)
        self._name = new_name

    def _validate_name(self, name: str):
        if name.strip() == "":
            raise ValueError("Folder name cannot be empty")
        if len(name) > self.MAX_NAME_LENGTH:
            raise ValueError(f"Folder name cannot be longer than {self.MAX_NAME_LENGTH} characters")