from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class Description(ValueObject):

    MAX_LENGTH = 2000

    def __init__(self, value: str):

        if value is None:
            value = ""

        value = value.strip()

        if len(value) > self.MAX_LENGTH:
            raise DomainException("Description is too long.")

        object.__setattr__(self, "value", value)

    def __str__(self):
        return self.value
