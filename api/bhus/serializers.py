from typing import List

from bhus.spec import Operator, Vehicle, VehicleState


def serialize_operators(operators: List[Operator]) -> List[dict]:
    return [o.to_dict() for o in operators]


def serialize_vehicles(vehicles: List[Vehicle]) -> List[dict]:
    return [v.to_dict() for v in vehicles]


def serialize_vehicle_states(vehicle_states: List[VehicleState]) -> List[dict]:
    return [s.to_dict() for s in vehicle_states]
