from dataclasses import dataclass, field
from typing import List


__all__ = [
    'Mapping',
    'Tag',
    'Task',
]


@dataclass
class Mapping:
    name: str


@dataclass
class Tag:
    name: str


@dataclass
class Task:
    name: str
    tags: List[Tag] = field(default_factory=list)
