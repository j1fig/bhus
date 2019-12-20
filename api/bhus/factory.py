from aiohttp import web

from bhus import views
from bhus import db
from bhus import config


def make_app(loop=None):
    app = web.Application()
    app.add_routes(views.routes)

    config.init_app(app)
    db.init_app(app)

    return app
