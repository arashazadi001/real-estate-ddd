from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    async def add(self, entity: T) -> None:
        ...

    @abstractmethod
    async def get_by_id(self, entity_id: UUID) -> T | None:
        ...

    @abstractmethod
    async def update(self, entity: T) -> None:
        ...

    @abstractmethod
    async def delete(self, entity_id: UUID) -> None:
        ...
