from unittest.mock import ANY

from aiohttp.test_utils import make_mocked_coro
import pytest


async def test_healthz(app_client):
    resp = await app_client.get("/healthz")
    assert resp.status == 200
    json = await resp.json()
    assert json["status"] == "OK"


async def test_index(app_client):
    resp = await app_client.get("/")
    assert resp.status == 200


async def test_operators(app_client, m_operators_by_time_range):
    resp = await app_client.get("/api/operator?from=100&to=150")
    m_operators_by_time_range.assert_called_once_with(pool=ANY, from_=100, to=150)
    assert resp.status == 200
    data = await resp.json()
    assert all(isinstance(o["id"], str) for o in data)


async def test_operator_vehicles(app_client):
    operator_id = "MEH"
    resp = await app_client.get(f"/api/operator/{operator_id}/vehicle?from=100&to=150")
    assert resp.status == 200


async def test_operator_vehicles_at_stop(app_client):
    operator_id = "MEH"
    resp = await app_client.get(f"/api/operator/{operator_id}/vehicle?from=100&to=150")
    assert resp.status == 200


async def test_vehicle_state(app_client):
    vehicle_id = 98234
    resp = await app_client.get(f"/api/vehicle/{vehicle_id}/state?from=100&to=150")
    assert resp.status == 200
