from typing import List

from asyncpg.pool import Pool

from bhus.spec import Vehicle, Operator


class VehicleState:
    TABLE = 'vehicle_state'

    COLUMNS = (
        'id',
        'timestamp',
        'operator',
        'longitude',
        'latitude',
        'vehicle_id',
        'at_stop',
    )


async def get_operators_by_time_range(pool: Pool, from_: int, to: int) -> List[dict]:
    async with pool.acquire() as conn:
        records =  await conn.fetch(
            "SELECT DISTINCT(operator) FROM vehicle_state WHERE timestamp > $1 AND timestamp < $2",
            from_,
            to
        )
        return [dict(r) for r in records]


async def get_vehicles_by_time_range(pool: Pool, from_: int, to: int) -> List[dict]:
    pass


async def get_vehicles_by_operator_and_time_range(pool: Pool, operator_id: str, from_: int, to: int) -> List[dict]:
    pass


async def get_vehicle_by_time_range(pool: Pool, operator_id: str, from_: int, to: int) -> List[dict]:
    pass
