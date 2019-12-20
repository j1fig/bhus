from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    name = request.match_info.get('name', 'Visitor')
    return web.Response(text=f"Hello, {name}!")


@routes.get('/healthz')
async def healthz(request):
    return web.json_response({'status': 'OK'})


@routes.get('/api/operator')
async def operators(request):
    return web.Response(text="OK")


@routes.get('/api/operator/{operator_id}/vehicle')
async def operator_vehicles(request):
    return web.Response(text="OK")


@routes.get('/api/vehicle')
async def operators(request):
    return web.Response(text="OK")


@routes.get('/api/vehicle/{vehicle_id}')
async def vehicles(request):
    return web.Response(text="OK")
