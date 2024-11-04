import pytest
import random
import string
import allure
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods
from tests.couriers.create_courier_data import CreateRandomCourier

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

    if response.status_code == 201:
        print(login, password, first_name, response)
        yield [login, password, first_name, response]
    else:
        raise Exception(f"Не удалось создать курьера: {response.text}")

@pytest.fixture()
def courier(courier_methods):
    courier_instance = CreateRandomCourier()
    response = courier_instance.register_new_courier_and_return_login_password_firstname()
    return response

@pytest.fixture
def courier_without_firstname():
    courier_instance = CreateRandomCourier()
    login_pass = courier_instance.register_new_courier_without_firstname()
    return login_pass


@pytest.fixture
def courier_id():
    courier_instance = CreateRandomCourier()
    response = courier_instance.register_new_courier_and_return_login_password()
    return response

