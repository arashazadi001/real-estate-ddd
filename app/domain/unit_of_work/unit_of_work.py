from abc import ABC, abstractmethod

from app.domain.repositories.listing_repository import ListingRepository


class UnitOfWork(ABC):

    listings: ListingRepository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def rollback(self) -> None:
        ...
