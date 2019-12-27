from unittest.mock import ANY

from bhus.serializers import serialize_operators, serialize_vehicles, serialize_vehicle_states


def test_serialize_operators(operators):
    assert serialize_operators(operators) == [{'id': ANY} for _ in range(len(operators))]


def test_serialize_vehicles(vehicles):
    assert serialize_vehicles(vehicles) == [{'id': ANY} for _ in range(len(vehicles))]


def test_serialize_vehicle_states(vehicle_states):
    assert serialize_vehicle_states(vehicle_states) == [{
        'timestamp': ANY,
        'latitude': ANY,
        'longitude': ANY,
        'at_stop': ANY
    } for _ in range(len(vehicle_states))]
