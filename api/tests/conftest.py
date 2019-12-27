from contextlib import asynccontextmanager
from random import choice, random, randint
from time import time
import string

from aiohttp.test_utils import make_mocked_coro
import asyncpg
import pytest

from bhus.spec import Operator, Vehicle, VehicleState


_TIME = time()
_id = 0


class FakePool:
    def __init__(self, *args, **kwargs):
        self.conn = FakeConnection()

    @asynccontextmanager
    async def acquire(self):
        try:
            yield self.conn
        finally:
            pass

    async def close(self):
        pass


class FakeConnection:
    def __init__(self, *args, **kwargs):
        self.fetch_calls = []

    async def execute(self, statement: str, *args):
        """
	Echoes the statement sent to the conn.execute() method.
	"""
        return make_mocked_coro(statement)

    async def fetch(self, statement: str, *args, **kwargs):
        """
	Echoes the statement sent to the conn.fetch() method.
	"""
        self.fetch_calls.append({"statement": statement, "*args": args})
        return [_gen_record() for v in range(10)]


class FakeRecord:

    def __init__(self, field_values):
        self._field_values = field_values

    def __getitem__(self, key):
        return self._field_values[key]


def _gen_record():
    return FakeRecord(field_values={
        "id": _gen_id(),
        "timestamp": _gen_timestamp(),
        "operator_id": _gen_operator_id(),
        "vehicle_id": _gen_vehicle_id(),
        "latitude": _gen_latitude(),
        "longitude": _gen_longitude(),
        "at_stop": _gen_at_stop(),
    })


def _gen_id():
    """
    Non-thread safe, though we don't care much for colliding id's at this point, nor
    do we run test code in multiple threads.
    """
    global _id
    _id += 1
    return _id


def _gen_timestamp():
    return int(random()*_TIME)


def _gen_operator_id():
    return "".join(choice(string.ascii_uppercase) for _ in range(2))


def _gen_vehicle_id():
    return int(random()*100000)


def _gen_latitude():
    return randint(-90000, 90000) / 1000


def _gen_longitude():
    return randint(-180000, 180000) / 1000


def _gen_at_stop():
    return choice([True, False])


@pytest.fixture
async def app_client(aiohttp_client, m_pg):
    from bhus import factory

    client = await aiohttp_client(factory.make_app)
    return client


@pytest.fixture
async def m_pg(monkeypatch):
    fake_pool = make_mocked_coro(FakePool())
    monkeypatch.setattr(asyncpg, "create_pool", fake_pool)
    return fake_pool


@pytest.fixture
def records():
    return [_gen_record() for _ in range(10)]


@pytest.fixture
def operators():
    return [Operator(id=_gen_operator_id()) for _ in range(10)]


@pytest.fixture
def vehicles():
    return [Vehicle(id=_gen_operator_id()) for _ in range(10)]


@pytest.fixture
def vehicle_states():
    return [
        VehicleState(
            timestamp=_gen_timestamp(),
            latitude=_gen_latitude(),
            longitude=_gen_longitude(),
            at_stop=_gen_at_stop(),
        ) for _ in range(10)
    ]


@pytest.fixture
async def m_operators_by_time_range(monkeypatch, operators):
    from bhus import domain

    m_operators_by_time_range = make_mocked_coro(operators)
    monkeypatch.setattr(
        domain, "get_unique_operators_by_time_range", m_operators_by_time_range
    )
    return m_operators_by_time_range


@pytest.fixture
async def m_select_distinct_vehicles_by_operator_and_time_range(monkeypatch, operators):
    from bhus.models import pg

    m_records = make_mocked_coro(records)
    monkeypatch.setattr(
        pg, "select_distinct_vehicles_by_operator_and_time_range", m_records
    )
    return m_records


@pytest.fixture
async def m_select_distinct_vehicles_by_operator_at_stop_and_time_range(monkeypatch, operators):
    from bhus.models import pg

    m_records = make_mocked_coro(records)
    monkeypatch.setattr(
        pg, "select_distinct_vehicles_by_operator_at_stop_and_time_range", m_records
    )
    return m_records
