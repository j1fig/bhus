import asyncpg


def init_app(app):
    app.on_startup.append(init)
    app.on_cleanup.append(close)


async def init(app):
    app['pool'] = await asyncpg.create_pool(dsn=app['config']['db_dsn'])


async def close(app):
    app['pool'].close()
