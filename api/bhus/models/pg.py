from typing import List

from asyncpg import Record
from asyncpg.pool import Pool


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


async def get_operators_by_time_range(pool: Pool, from_: int, to: int) -> List[Record]:
    async with pool.acquire() as conn:
        return await conn.fetch(
            "SELECT DISTINCT(operator) FROM vehicle_state WHERE timestamp >= $1 AND timestamp <= $2",
            from_,
            to
        )


async def get_vehicles_by_time_range(pool: Pool, from_: int, to: int) -> List[Record]:
    pass


async def get_vehicles_by_operator_and_time_range(pool: Pool, operator_id: str, from_: int, to: int) -> List[Record]:
    pass


async def get_vehicle_by_time_range(pool: Pool, operator_id: str, from_: int, to: int) -> List[Record]:
    pass
