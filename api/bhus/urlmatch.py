from aiohttp import web


def get_id_from_request(key: str, request: web.Request) -> int:
    try:
        return request.match_info[key]
    except KeyError, TypeError:
        raise web.HTTPBadRequest
