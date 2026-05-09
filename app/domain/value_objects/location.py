from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class Location(ValueObject):
    def __init__(self, city: str, district: str):

        if not city or not city.strip():
            raise DomainException("City cannot be empty.")

        if not district or not district.strip():
            raise DomainException("District cannot be empty.")

        object.__setattr__(self, "city", city.strip())
        object.__setattr__(self, "district", district.strip())

    def __str__(self):
        return f"{self.city} - {self.district}"
