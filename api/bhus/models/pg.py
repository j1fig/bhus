from typing import List

from asyncpg import Record
from asyncpg.pool import Pool


class VehicleState:
    TABLE = "vehicle_state"

    COLUMNS = (
        "id",
        "timestamp",
        "operator_id",
        "vehicle_id",
        "latitude",
        "longitude",
        "at_stop",
    )


async def select_distinct_operators_by_time_range(pool: Pool, from_: int, to: int) -> List[Record]:
    async with pool.acquire() as conn:
        return await conn.fetch(
            "SELECT DISTINCT(operator_id) FROM vehicle_state WHERE timestamp >= $1 AND timestamp <= $2",
            from_,
            to,
        )


async def select_distinct_vehicles_by_operator_and_time_range(
    pool: Pool, operator_id: str, from_: int, to: int
) -> List[Record]:
    async with pool.acquire() as conn:
        return await conn.fetch(
            "SELECT DISTINCT(vehicle_id) FROM vehicle_state WHERE operator_id = $1 AND timestamp >= $2 AND timestamp <= $3",
            operator_id,
            from_,
            to,
        )


async def select_distinct_vehicles_by_operator_at_stop_and_time_range(
    pool: Pool, operator_id: str, from_: int, to: int, at_stop: bool
) -> List[Record]:
    async with pool.acquire() as conn:
        return await conn.fetch(
            "SELECT DISTINCT(vehicle_id) FROM vehicle_state WHERE operator_id = $1 AND at_stop = $2 AND timestamp >= $3 AND timestamp <= $4",
            operator_id,
            at_stop,
            from_,
            to,
        )


async def select_vehicle_state_by_vehicle_and_time_range_order_by_timestamp(
    pool: Pool, vehicle_id: int, from_: int, to: int
) -> List[Record]:
    async with pool.acquire() as conn:
        return await conn.fetch(
            "SELECT timestamp, latitude, longitude, at_stop FROM vehicle_state WHERE vehicle_id = $1 AND timestamp >= $2 AND timestamp <= $3 ORDER BY timestamp",
            vehicle_id,
            from_,
            to,
        )
