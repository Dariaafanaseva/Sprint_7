import pytest
from data import ORDER_DATA_BLACK_COLOR, ORDER_DATA_BLACK_AND_GREY_COLOR, ORDER_DATA_NO_COLOR
from methods import order_methods

class TestCreateOrder:
    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_DATA_BLACK_COLOR,
            ORDER_DATA_BLACK_AND_GREY_COLOR,
            ORDER_DATA_NO_COLOR
        ]
    )
    def test_create_order(self, order_data, order_methods):
        status_code, response_context = order_methods.post_order(order_data)
        assert status_code == 201 and  'track' in response_context