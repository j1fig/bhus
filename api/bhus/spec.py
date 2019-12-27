from typing import NamedTuple


class Vehicle(NamedTuple):
    id: int

    def to_dict(self):
        return {"id": self.id}


class Operator(NamedTuple):
    id: str

    def to_dict(self):
        return {"id": self.id}


class VehicleState(NamedTuple):
    timestamp: int
    latitude: float
    longitude: float
    at_stop: bool

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "at_stop": self.at_stop,
        }
