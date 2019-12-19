from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    name = request.match_info.get('name', 'Anonymous')
    text = "Hello, " + name
    return web.Response(text=text)


@routes.get('/healthz')
async def healthz(request):
    return web.Response(text="OK")
