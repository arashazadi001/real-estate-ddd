from uuid import uuid4

from app.application.commands.listing.create_listing_command import CreateListingCommand
from app.application.mediator.handlers import RequestHandler
from app.domain.entities.listing import Listing
from app.domain.value_objects.price import Price
from app.domain.value_objects.area import Area
from app.domain.value_objects.listing_title import ListingTitle
from app.domain.unit_of_work.unit_of_work import UnitOfWork


class CreateListingHandler(
    RequestHandler[CreateListingCommand, str]
):

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, command: CreateListingCommand):

        listing = Listing(
            id=uuid4(),
            title=ListingTitle(command.title),
            description=command.description,
            price=Price(command.price),
            area=Area(command.area),
            owner_id=command.owner_id
        )

        async with self.uow:
            await self.uow.listings.add(listing)

        return str(listing.id)
