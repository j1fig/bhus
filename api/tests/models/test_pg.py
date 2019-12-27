from bhus.models import pg
from unittest.mock import ANY

import pytest


@pytest.mark.parametrize(
    "kwargs,statement",
    [
        (
            {"from_": 100, "to": 150,},
            "SELECT DISTINCT(operator_id) FROM vehicle_state WHERE timestamp >= $1 AND timestamp <= $2",
        ),
    ],
)
async def test_select_distinct_operators_by_time_range(kwargs, statement, app_client):
    pool = app_client.app["pool"]
    await pg.select_distinct_operators_by_time_range(pool=pool, **kwargs)
    assert app_client.app["pool"].conn.fetch_calls == [
        {"statement": statement, "*args": (kwargs["from_"], kwargs["to"]),}
    ]


@pytest.mark.parametrize(
    "kwargs,statement",
    [
        (
            {"operator_id": "D2", "from_": 100, "to": 150,},
            "SELECT DISTINCT(vehicle_id) FROM vehicle_state WHERE operator_id = $1 AND timestamp >= $2 AND timestamp <= $3",
        ),
    ],
)
async def test_select_distinct_vehicles_by_operator_and_time_range(kwargs, statement, app_client):
    pool = app_client.app["pool"]
    await pg.select_distinct_vehicles_by_operator_and_time_range(pool=pool, **kwargs)
    assert app_client.app["pool"].conn.fetch_calls == [
        {"statement": statement, "*args": (kwargs['operator_id'], kwargs["from_"], kwargs["to"]),}
    ]


@pytest.mark.parametrize(
    "kwargs,statement",
    [
        (
            {"operator_id": "D2", "at_stop": True, "from_": 100, "to": 150,},
            "SELECT DISTINCT(vehicle_id) FROM vehicle_state WHERE operator_id = $1 AND at_stop = $2 AND timestamp >= $3 AND timestamp <= $4",
        ),
    ],
)
async def test_select_distinct_vehicles_by_operator_at_stop_and_time_range(kwargs, statement, app_client):
    pool = app_client.app["pool"]
    await pg.select_distinct_vehicles_by_operator_at_stop_and_time_range(pool=pool, **kwargs)
    assert app_client.app["pool"].conn.fetch_calls == [
        {"statement": statement, "*args": (kwargs['operator_id'], kwargs['at_stop'], kwargs["from_"], kwargs["to"]),}
    ]


@pytest.mark.parametrize(
    "kwargs,statement",
    [
        (
            {"vehicle_id": "33325", "from_": 100, "to": 150,},
            "SELECT timestamp, latitude, longitude, at_stop FROM vehicle_state WHERE vehicle_id = $1 AND timestamp >= $2 AND timestamp <= $3 ORDER BY timestamp",
        ),
    ],
)
async def test_select_vehicle_state_by_vehicle_and_time_range_order_by_timestamp(kwargs, statement, app_client):
    pool = app_client.app["pool"]
    await pg.select_vehicle_state_by_vehicle_and_time_range_order_by_timestamp(pool=pool, **kwargs)
    assert app_client.app["pool"].conn.fetch_calls == [
        {"statement": statement, "*args": (kwargs['vehicle_id'], kwargs["from_"], kwargs["to"]),}
    ]
