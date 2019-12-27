from typing import NamedTuple


class Vehicle(NamedTuple):
    id: int
    latitude: float
    longitude: float
    at_stop: bool
    timestamp: int


class Operator(NamedTuple):
    id: str

    def to_dict(self):
        return {"id": self.id}
