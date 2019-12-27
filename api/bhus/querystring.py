from typing import Optional

from aiohttp import web


def get_time_range_from_request(request: web.Request) -> (int, int):
    q = request.query
    # Right now both from/to are required parameters.
    if any([p not in q for p in ("from", "to")]):
        raise web.HTTPBadRequest

    try:
        from_ = int(q["from"])
        to = int(q["to"])
    except TypeError:
        raise web.HTTPBadRequest

    validate_time_range(from_, to)
    return from_, to


def get_at_stop_from_request(request: web.Request) -> Optional[bool]:
    q = request.query
    # at_stop is *not* a required parameter.
    if "at_stop" not in q:
        return None

    try:
        at_stop = bool(q["at_stop"])
    except TypeError:
        raise web.HTTPBadRequest

    return at_stop


def validate_time_range(from_: int, to: int) -> None:
    valid_from = validate_timestamp(from_)
    valid_to = validate_timestamp(to)
    valid_range = from_ <= to
    if not valid_range:
        raise web.HTTPBadRequest


def validate_timestamp(ts: int) -> None:
    valid = ts > 0
    if not valid:
        raise web.HTTPBadRequest
