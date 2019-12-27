from aiohttp import web
from aiohttp.test_utils import make_mocked_request
import pytest

from bhus import urlmatch


@pytest.mark.parametrize('path,match_info,id_', [
    ('/any/url', {'resource_id': 4}, 4),
    ('/any/url', {'sid': 666}, 666),
    ('/any/url', {'sid': "7"}, "7"),
    ('/any/url', {'o_id': "D2"}, "D2"),
])
def test_get_id_from_request(path, match_info, id_):
    req = make_mocked_request('GET', path, match_info=match_info)
    for k in match_info.keys():
        assert urlmatch.get_id_from_request(k, req) == id_
