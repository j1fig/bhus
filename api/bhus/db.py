from time import sleep

from aiohttp.web import Application
import asyncpg


def init_app(app: Application):
    app.on_startup.append(init)
    app.on_cleanup.append(close)


async def init(app: Application, retries: int = 10, retry_period=2.0):
    while retries > 0:
        try:
            app["pool"] = await asyncpg.create_pool(dsn=app["config"]["db_dsn"])
            return
        except OSError:
            # TODO log warning here.
            sleep(retry_period)
            retries -= 1


async def close(app: Application):
    await app["pool"].close()
