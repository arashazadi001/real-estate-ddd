from enum import Enum


class ListingStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    SOLD = "sold"
    RENTED = "rented"
    ARCHIVED = "archived"
