from aiohttp import web
from aiohttp.test_utils import make_mocked_request
import pytest

from bhus import querystring


@pytest.mark.parametrize('ts', [
    0,
    1,
    128371.00123,
    12739187239,
])
def test_validate_timestamp(ts):
    querystring.validate_timestamp(ts)  # will raise if invalid.


@pytest.mark.parametrize('ts', [
    -1,
    -1231566345,
])
def test_validate_timestamp_bad(ts):
    with pytest.raises(web.HTTPBadRequest):
        querystring.validate_timestamp(ts)


@pytest.mark.parametrize('from_,to', [
    (0, 2),
    (1, 1),
    (0, 0),
    (1, 10),
    (999999, 1000000),
])
def test_validate_time_range(from_, to):
    querystring.validate_time_range(from_, to)  # will raise if invalid.


@pytest.mark.parametrize('from_,to', [
    (-1, 2),
    (1, -1),
    (999999, -1000000),
])
def test_validate_time_range_bad(from_, to):
    with pytest.raises(web.HTTPBadRequest):
        querystring.validate_time_range(from_, to)


@pytest.mark.parametrize('path,time_range', [
    ('/api/some/url?from=10&to=15', (10, 15)),
    ('/api/some/url?from=10&to=15', (10, 15)),
    ('/api/some/url?from=123456&to=123457', (123456, 123457)),
])
def test_validate_time_range(path, time_range):
    req = make_mocked_request('GET', path)
    assert querystring.get_time_range_from_request(req) == time_range


@pytest.mark.parametrize('path', [
    '/api/some/url?from=10.0&to=15',
    '/api/some/url?from=10&to=ha',
    '/api/some/url?from=10&to=9',
    '/api/some/url?from=1&to=-1',
    '/api/some/url?from=1&tod=2',
    '/api/some/url?from=1',
    '/api/some/url?from_=1&to=2',
    '/api/some/url?to=2',
    '/api/some/url',
])
def test_validate_time_range_bad(path):
    req = make_mocked_request('GET', path)
    with pytest.raises(web.HTTPBadRequest):
        querystring.get_time_range_from_request(req)
