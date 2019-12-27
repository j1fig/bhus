from typing import List, Optional

# Yes, `models` are a leaky abstraction because of PG-specific types leaking
# all the way up to the views in this case.
# This will be fixed in the eventuality of adding a separate/replacement datastore
# by abstracting the asyncpg.Pool into a new spec.Engine abstract type which will conform
# to a common interface.
from asyncpg.pool import Pool

from bhus.models import pg
from bhus.spec import Vehicle, Operator, VehicleState


async def get_unique_operators_by_time_range(
    pool: Pool, from_: int, to: int
) -> List[Operator]:
    records = await pg.select_distinct_operators_by_time_range(pool=pool, from_=from_, to=to)
    return [Operator(id=r['operator_id']) for r in records]


async def get_unique_vehicles_by_operator_and_time_range(
    pool: Pool, operator_id: str, from_: int, to: int, at_stop: Optional[bool] = None
) -> List[Vehicle]:
    print('passed 0')
    if at_stop is not None:
        records = await pg.select_distinct_vehicles_by_operator_at_stop_and_time_range(
            pool=pool, operator_id=operator_id, from_=from_, to=to, at_stop=at_stop
        )
    else:
        print('passed')
        records = await pg.select_distinct_vehicles_by_operator_and_time_range(
            pool=pool, operator_id=operator_id, from_=from_, to=to
        )
    return [Vehicle(id=r['vehicle_id']) for r in records]


async def get_vehicle_states_by_vehicle_and_time_range(
    pool: Pool, vehicle_id: str, from_: int, to: int
) -> List[Vehicle]:
    records = await pg.select_vehicle_state_by_vehicle_and_time_range_order_by_timestamp(pool=pool, vehicle_id=vehicle_id, from_=from_, to=to)
    return [
        VehicleState(
            timestamp=r['timestamp'],
            latitude=r['latitude'],
            longitude=r['longitude'],
            at_stop=r['at_stop'],
        )
        for r in records
    ]
