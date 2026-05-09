from dataclasses import dataclass
from uuid import UUID

from app.application.mediator.requests import Command


@dataclass
class CreateListingCommand(Command[UUID]):
    title: str
    description: str
    price: float
    area: float
    owner_id: str
