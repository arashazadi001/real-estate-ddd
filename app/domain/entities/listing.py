from datetime import datetime
from uuid import UUID, uuid4

from app.shared.base.entity import Entity

from app.domain.value_objects.price import Price
from app.domain.value_objects.area import Area
from app.domain.value_objects.listing_title import ListingTitle
from app.domain.value_objects.description import Description
from app.domain.value_objects.address import Address
from app.domain.value_objects.coordinates import Coordinates

from app.domain.enums.listing_status import ListingStatus


class Listing(Entity):

    def __init__(
        self,
        owner_id: UUID,
        title: ListingTitle,
        description: Description,
        price: Price,
        area: Area,
        address: Address,
        coordinates: Coordinates,
        id: UUID | None = None,
    ):
        super().__init__(id or uuid4())

        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price = price
        self.area = area
        self.address = address
        self.coordinates = coordinates

        self.status = ListingStatus.DRAFT
        self.created_at = datetime.utcnow()

    def publish(self):

        if self.status != ListingStatus.DRAFT:
            raise Exception("Only draft listings can be published.")

        self.status = ListingStatus.ACTIVE

    def mark_sold(self):

        if self.status != ListingStatus.ACTIVE:
            raise Exception("Listing must be active to mark as sold.")

        self.status = ListingStatus.SOLD

    def archive(self):

        self.status = ListingStatus.ARCHIVED

    def update_price(self, price: Price):

        self.price = price

    def update_description(self, description: Description):

        self.description = description
