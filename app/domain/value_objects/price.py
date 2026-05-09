from decimal import Decimal
from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class Price(ValueObject):
    def __init__(self, amount: Decimal):
        if amount <= 0:
            raise DomainException("Price must be greater than zero.")

        if amount > Decimal("100000000000"):
            raise DomainException("Price is unrealistically large.")

        object.__setattr__(self, "amount", amount)

    def __str__(self):
        return f"{self.amount}"
