import allure
from data import COURIER_DATA_NO_LOGIN, EXISTING_COURIER

class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Проверка успешного создания курьера")
    def test_create_courier(self, courier_methods, courier_data):
        response = courier_data[3]
        assert response.status_code == 201 and response.json() == {'ok': True}


    @allure.title("Создание дубликата курьера")
    @allure.description("Проверка невозможности создания двух курьеров с одинаковой парой логин/пароль")
    def test_create_dublicate_courier(self, courier_methods, courier_data):
        login = courier_data[0]
        password = courier_data[1]
        firstName = courier_data[2]
        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        response = courier_methods.post_create_courier(payload)
        assert response.status_code == 409


    @allure.title("Создание курьера, заполняя не все обязательные поля")
    @allure.description("Проверка невозможности создания курьера, если не передать в запрос логин")
    def test_create_courier_without_firstname(self, courier_methods):
        response = courier_methods.post_create_courier(COURIER_DATA_NO_LOGIN)
        assert response.status_code == 400

    #нельзя создать курьера с существующим логином
    @allure.title("Создание курьера с существующим логином")
    @allure.description("Проверка невозможности создания курьера с логином, который уже существует в системе")
    def test_create_existing_courier(self, courier_methods):
        response = courier_methods.post_create_courier(EXISTING_COURIER)
        assert response.status_code == 409





