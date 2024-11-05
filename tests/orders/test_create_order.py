import pytest
import allure
from data import ORDER_DATA_BLACK_COLOR, ORDER_DATA_BLACK_AND_GREY_COLOR, ORDER_DATA_NO_COLOR

class TestCreateOrder:
    @allure.title("Успешное создание заказа с разными данными")
    @allure.description("Проверка создания заказа с разными наборами данных: без выбранного цвета самоката, с одним выбранным цветом, с двумя выбранными цветами")
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

    @allure.title("Получение списка заказов")
    @allure.description(
        "Проверка получения списка заказов")
    def test_get_orders(self, order_methods):
        status_code, response_json = order_methods.get_orders()
        assert status_code == 200 and 'orders' in response_json