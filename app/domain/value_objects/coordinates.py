from app.shared.base.value_object import ValueObject
from app.shared.base.domain_exception import DomainException


class Coordinates(ValueObject):

    def __init__(self, latitude: float, longitude: float):

        if latitude < -90 or latitude > 90:
            raise DomainException("Latitude must be between -90 and 90.")

        if longitude < -180 or longitude > 180:
            raise DomainException("Longitude must be between -180 and 180.")

        object.__setattr__(self, "latitude", latitude)
        object.__setattr__(self, "longitude", longitude)

    def __str__(self):
        return f"{self.latitude},{self.longitude}"
