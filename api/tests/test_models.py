from bhus import models
from unittest.mock import ANY

import pytest


@pytest.mark.parametrize('kwargs,statement', [
    (
        {
            'from_': 100,
            'to': 150,
        },
        "SELECT DISTINCT(operator) FROM vehicle_state WHERE timestamp > $1 AND timestamp < $2"
    ),
])
async def test_get_operators_by_time_range(kwargs, statement, app_client, mocker):
    # pool = app_client.app['pool']
    # mocker.patch(
    # assert await models.get_operators_by_time_range(pool=pool, **kwargs) == statement
    # TODO rewrite so as to mock fetch called with correct args.
    pass
