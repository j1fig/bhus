from contextlib import asynccontextmanager
from random import choice
import string

from aiohttp.test_utils import make_mocked_coro
import asyncpg
import pytest

from bhus.spec import Operator, Vehicle


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
        self.fetch_calls.append({'statement': statement, '*args': args})
        return [{'id': v} for v in range(10)]


@pytest.fixture
async def app_client(aiohttp_client, m_pg):
    from bhus import factory
    client = await aiohttp_client(factory.make_app)
    return client


@pytest.fixture
async def m_pg(monkeypatch):
    fake_pool = make_mocked_coro(FakePool())
    monkeypatch.setattr(asyncpg, 'create_pool', fake_pool)
    return fake_pool


@pytest.fixture
def operators():
    operators = []
    for _ in range(10):
        id_ = ''.join(choice(string.ascii_uppercase) for _ in range(2))
        operators.append({'operator': id_})
    return operators


@pytest.fixture
async def m_operators_by_time_range(monkeypatch, operators):
    from bhus import domain
    m_operators_by_time_range = make_mocked_coro(operators)
    monkeypatch.setattr(domain, 'get_operators_by_time_range', m_operators_by_time_range)
    return m_operators_by_time_range
