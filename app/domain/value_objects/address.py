from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class Address(ValueObject):

    def __init__(
        self,
        city: str,
        district: str,
        street: str,
        building_number: str,
        unit: str | None = None,
        postal_code: str | None = None,
    ):

        if not city or not city.strip():
            raise DomainException("City cannot be empty.")

        if not district or not district.strip():
            raise DomainException("District cannot be empty.")

        if not street or not street.strip():
            raise DomainException("Street cannot be empty.")

        if not building_number or not building_number.strip():
            raise DomainException("Building number cannot be empty.")

        object.__setattr__(self, "city", city.strip())
        object.__setattr__(self, "district", district.strip())
        object.__setattr__(self, "street", street.strip())
        object.__setattr__(self, "building_number", building_number.strip())
        object.__setattr__(self, "unit", unit)
        object.__setattr__(self, "postal_code", postal_code)

    def __str__(self):
        base = f"{self.city}, {self.district}, {self.street}, {self.building_number}"
        if self.unit:
            base += f", Unit {self.unit}"
        return base
