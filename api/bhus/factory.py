from aiohttp import web

from bhus import views


def make_app(loop=None):
    app = web.Application()
    app.add_routes(views.routes)

    return app
