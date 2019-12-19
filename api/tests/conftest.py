import pytest

from bhus import factory


@pytest.fixture
async def app_client(aiohttp_client):
    client = await aiohttp_client(factory.make_app)
    return client
