from unittest.mock import ANY

from bhus import domain


async def test_get_unique_vehicles_by_operator_and_time_range(
    app_client,
    m_select_distinct_vehicles_by_operator_and_time_range,
    m_select_distinct_vehicles_by_operator_at_stop_and_time_range
    ):
    pool = app_client.app["pool"]
    await domain.get_unique_vehicles_by_operator_and_time_range(
        pool=pool,
        operator_id='ANY',
        from_=100,
        to=101,
    )
    m_select_distinct_vehicles_by_operator_and_time_range.assert_called_once_with(
        pool=ANY, operator_id='ANY', from_=100, to=101
    )
    m_select_distinct_vehicles_by_operator_at_stop_and_time_range.assert_not_called()


async def test_get_unique_vehicles_by_operator_and_time_range_with_at_stop(
    app_client,
    m_select_distinct_vehicles_by_operator_and_time_range,
    m_select_distinct_vehicles_by_operator_at_stop_and_time_range
    ):
    pool = app_client.app["pool"]
    await domain.get_unique_vehicles_by_operator_and_time_range(
        pool=pool,
        operator_id='ANY',
        from_=100,
        to=101,
        at_stop=False,
    )
    m_select_distinct_vehicles_by_operator_and_time_range.assert_not_called()
    m_select_distinct_vehicles_by_operator_at_stop_and_time_range.assert_called_once_with(
        pool=ANY, operator_id='ANY', from_=100, to=101, at_stop=False
    )
