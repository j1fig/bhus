from bhus.models import pg
from unittest.mock import ANY

import pytest


@pytest.mark.parametrize(
    "kwargs,statement",
    [
        (
            {"from_": 100, "to": 150,},
            "SELECT DISTINCT(operator) FROM vehicle_state WHERE timestamp >= $1 AND timestamp <= $2",
        ),
    ],
)
async def test_select_distinct_operators_by_time_range(kwargs, statement, app_client, mocker):
    pool = app_client.app["pool"]
    await pg.select_distinct_operators_by_time_range(pool=pool, **kwargs)
    assert app_client.app["pool"].conn.fetch_calls == [
        {"statement": statement, "*args": (kwargs["from_"], kwargs["to"]),}
    ]
