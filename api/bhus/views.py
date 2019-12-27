from aiohttp import web

from bhus import domain, querystring, urlmatch
from bhus.serializers import serialize_operators, serialize_vehicles, serialize_vehicle_states

routes = web.RouteTableDef()


@routes.get("/")
async def index(request: web.Request) -> web.Response:
    return web.Response(text=f"Hello!")


@routes.get("/healthz")
async def healthz(request: web.Request) -> web.Response:
    return web.json_response({"status": "OK"})


@routes.get("/api/operator")
async def operators(request: web.Request) -> web.Response:
    """
    TODO proper view level documentation.

    This returns a plain list of JSON dictionaries with an `id` field and value.
    """
    from_, to = querystring.get_time_range_from_request(request)
    operators = await domain.get_unique_operators_by_time_range(
        pool=request.app["pool"], from_=from_, to=to,
    )
    return web.json_response(
        serialize_operators(operators)
    )


@routes.get("/api/operator/{operator_id}/vehicle")
async def operator_vehicles(request: web.Request) -> web.Response:
    """
    TODO proper view level documentation.

    This returns a plain list of JSON dictionaries with an `id` field and value.
    """
    from_, to = querystring.get_time_range_from_request(request)
    at_stop = querystring.get_at_stop_from_request(request)
    operator_id = urlmatch.get_id_from_request('operator_id', request, str)
    vehicles = await domain.get_unique_vehicles_by_operator_and_time_range(
        pool=request.app["pool"], operator_id=operator_id, from_=from_, to=to, at_stop=at_stop
    )
    return web.json_response(
        serialize_vehicles(vehicles)
    )


@routes.get("/api/vehicle/{vehicle_id}/state")
async def vehicles(request: web.Request) -> web.Response:
    """
    TODO proper view level documentation.
    """
    from_, to = querystring.get_time_range_from_request(request)
    vehicle_id = urlmatch.get_id_from_request('vehicle_id', request, int)
    vehicle_states = await domain.get_vehicle_states_by_vehicle_and_time_range(
        pool=request.app["pool"], vehicle_id=vehicle_id, from_=from_, to=to
    )
    return web.json_response(
        serialize_vehicle_states(vehicle_states)
    )
