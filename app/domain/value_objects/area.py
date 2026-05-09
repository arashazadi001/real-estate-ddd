from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class Area(ValueObject):
    def __init__(self, square_meters: float):
        if square_meters <= 0:
            raise DomainException("Area must be greater than zero.")

        if square_meters > 100000:
            raise DomainException("Area value is unrealistically large.")

        object.__setattr__(self, "square_meters", square_meters)

    def __str__(self):
        return f"{self.square_meters} m²"
