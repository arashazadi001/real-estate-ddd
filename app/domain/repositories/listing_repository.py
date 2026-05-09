from abc import abstractmethod
from typing import List

from app.domain.entities.listing import Listing
from app.domain.repositories.base_repository import BaseRepository


class ListingRepository(BaseRepository[Listing]):

    @abstractmethod
    async def get_by_title(self, title: str) -> Listing | None:
        ...

    @abstractmethod
    async def get_active(self) -> List[Listing]:
        ...

    @abstractmethod
    async def get_by_owner(self, owner_id: str) -> List[Listing]:
        ...
