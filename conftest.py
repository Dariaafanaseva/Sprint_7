import pytest
import random
import string
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods


@pytest.fixture()
def order_methods():
    return OrderMethods()

@pytest.fixture()
def courier_methods():
    return CourierMethods()

@pytest.fixture()
def courier_data(courier_methods):
    # Генерация случайных значений для логина, пароля и имени
    def generate_random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = courier_methods.post_create_courier(payload)
    print(f"Create courier response: {response.text}")  # Добавлено для отладки
    assert response.status_code == 201, "Не удалось создать курьера"

    login_payload = {
        "login": login,
        "password": password
    }

    login_response = courier_methods.post_courier_id(login_payload)
    print(f"Login response: {login_response.text}")  # Добавлено для отладки
    assert login_response.status_code == 200, "Не удалось выполнить вход"
    courier_id = login_response.json().get('id')
    yield response, payload, login_response, login
    if courier_id:
        courier_methods.delete_courier(courier_id)
    print('Курьер успешно удален')

