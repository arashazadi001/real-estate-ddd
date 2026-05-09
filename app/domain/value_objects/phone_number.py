import re
from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class PhoneNumber(ValueObject):

    PHONE_REGEX = r"^\+?\d{10,15}$"

    def __init__(self, value: str):

        if not value:
            raise DomainException("Phone number cannot be empty.")

        value = value.replace(" ", "").replace("-", "")

        if not re.match(self.PHONE_REGEX, value):
            raise DomainException("Invalid phone number.")

        object.__setattr__(self, "value", value)

    def __str__(self):
        return self.value
