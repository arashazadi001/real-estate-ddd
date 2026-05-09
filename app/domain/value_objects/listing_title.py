from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class ListingTitle(ValueObject):

    MIN_LENGTH = 5
    MAX_LENGTH = 120

    def __init__(self, value: str):
        if not value or not value.strip():
            raise DomainException("Title cannot be empty.")

        value = value.strip()

        if len(value) < self.MIN_LENGTH:
            raise DomainException("Title is too short.")

        if len(value) > self.MAX_LENGTH:
            raise DomainException("Title is too long.")

        object.__setattr__(self, "value", value)

    def __str__(self):
        return self.value
