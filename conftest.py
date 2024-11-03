import pytest
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
def existing_courier():
    return {
        "login": "existing_login159",
        "password": "password",
        "firstName": "Name"}

@pytest.fixture
def courier_id():
    courier_instance = CreateRandomCourier()
    response = courier_instance.register_new_courier_and_return_login_password()
    return response

