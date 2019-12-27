from unittest.mock import ANY

from bhus import domain


def test_get_unique_vehicles_by_operator_and_time_range(
    app_client,
    m_select_distinct_vehicles_by_operator_and_time_range,
    m_select_distinct_vehicles_by_operator_at_stop_and_time_range
    ):
    pool = app_client.app["pool"]
    print('passed tests')
    print(domain.get_unique_vehicles_by_operator_and_time_range)
    domain.get_unique_vehicles_by_operator_and_time_range(
        pool=pool,
        operator_id='ANY',
        from_=100,
        to=101,
    )
    m_select_distinct_vehicles_by_operator_and_time_range.assert_called_once_with(
        pool=ANY, operator_id='ANY', from_=100, to=100
    )
    m_select_distinct_vehicles_by_operator_at_stop_and_time_range.assert_not_called()
