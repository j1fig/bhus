from typing import List, Optional

# Yes, `models` are a leaky abstraction because of PG-specific types leaking
# all the way up to the views in this case.
# This will be fixed in the eventuality of adding a separate/replacement datastore
# by abstracting the asyncpg.Pool into a new spec.Engine abstract type which will conform
# to a given common interface.
from asyncpg.pool import Pool

from bhus.spec import Vehicle, Operator


async def get_operators_by_time_range(
    pool: Pool, from_: int, to: int
) -> List[Operator]:
    records = await pg.get_operators_by_time_range(pool=pool, from_=from_, to=to)
    return [dict(r) for r in records]


async def get_vehicles_by_operator_and_time_range(
    pool: Pool, operator_id: str, from_: int, to: int, at_stop: Optional[bool] = None
) -> List[Vehicle]:
    if at_stop is not None:
        records = await pg.get_vehicles_by_operator_and_time_range(
            pool=pool, from_=from_, to=to, at_stop=at_stop
        )
    else:
        records = await pg.get_vehicles_by_operator_and_time_range(
            pool=pool, from_=from_, to=to
        )
    return [dict(r) for r in records]


# TODO I think this is a different endpoint and resource... like /api/vehicle/{id}/state and returns a list of VehicleState's
# which actually contain the lat/lon, at_stop, etc.
async def get_vehicle_by_time_range(
    pool: Pool, operator_id: str, from_: int, to: int
) -> List[Vehicle]:
    return await pg.get_vehicle_by_time_range(pool=pool, from_=from_, to=to)
