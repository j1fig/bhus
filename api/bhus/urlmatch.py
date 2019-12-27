from typing import Any, Callable

from aiohttp import web


def get_id_from_request(key: str, request: web.Request, parser: Callable[[Any], Any]) -> int:
    try:
        return parser(request.match_info[key])
    except (KeyError, TypeError):
        raise web.HTTPBadRequest
