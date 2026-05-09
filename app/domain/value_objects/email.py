import re
from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class Email(ValueObject):

    EMAIL_REGEX = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    def __init__(self, value: str):
        if not value or not value.strip():
            raise DomainException("Email cannot be empty.")

        value = value.strip().lower()

        if not re.match(self.EMAIL_REGEX, value):
            raise DomainException("Invalid email format.")

        object.__setattr__(self, "value", value)

    def __str__(self):
        return self.value
