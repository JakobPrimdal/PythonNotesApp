from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class Note:
    _id: UUID
    _title: str
    _content: str
    _created_at: datetime
    _folder_id: Optional[UUID] = None
    _tags: list[str] = field(default_factory=list)
    _is_favorite: bool = False
    _is_archived: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if self._title.strip() == "" and self._content.strip() == "":
            raise ValueError("Empty title and empty content is not allowed for any note")

    @classmethod
    def create(cls, title: str, content: str) -> "Note":
        return cls(
            _id=uuid4(),
            _title=title,
            _content=content,
            _created_at=datetime.now(),
        )

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    def update_title(self, new_title: str) -> None:
        if self._is_archived:
            raise ValueError("Cannot change title of an archived note")
        if new_title.strip() == "" and self._content.strip() == "":
            raise ValueError("Empty title and empty content is not allowed")
        self._title = new_title

    @property
    def content(self) -> str:
        return self._content

    def update_content(self, new_content: str) -> None:
        if self._is_archived:
            raise ValueError("Cannot change content of an archived note")
        if new_content.strip() == "" and self._title.strip() == "":
            raise ValueError("Empty content and empty title is not allowed of an archived note")
        self._content = new_content

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def folder_id(self) -> Optional[UUID]:
        return self._folder_id

    def set_folder_id(self, folder_id: UUID) -> None:
        if self._is_archived:
            raise ValueError("Cannot change folder of an archived note")
        self._folder_id = folder_id

    @property
    def tags(self) -> list[str]:
        return self._tags

    def add_tag(self, tag: str) -> None:
        if self._is_archived:
            raise ValueError("Cannot add tag to an archived note")
        cleaned = tag.strip()
        if cleaned != "" and cleaned not in self._tags:
            self._tags.append(cleaned)

    def remove_tag(self, tag: str) -> None:
        if self._is_archived:
            raise ValueError("Cannot remove tag from an archived note")
        if tag in self._tags:
            self._tags.remove(tag)

    @property
    def is_favorite(self) -> bool:
        return self._is_favorite

    def mark_as_favorite(self) -> None:
        if self._is_archived:
            raise ValueError("Cannot mark an archived note as favorite")
        self._is_favorite = True

    def unmark_as_favorite(self) -> None:
        if self._is_archived:
            raise ValueError("Cannot unmark an archived note as favorite")
        self._is_favorite = False

    @property
    def is_archived(self) -> bool:
        return self._is_archived

    def archive(self) -> None:
        if self._is_archived:
            raise ValueError("Note already archived")
        self._is_archived = True

    def unarchive(self) -> None:
        if not self._is_archived:
            raise ValueError("Note not archived")
        self._is_archived = False