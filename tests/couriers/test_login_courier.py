import allure
from faker import Faker
class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    @allure.description("Проверка авторизации с зарегистрированным раннее логином и паролем, используя все обязательные поля")
    def test_login_user(self, courier_methods, courier_data):
        login = courier_data[0]
        password = courier_data[1]
        payload = {
            'login': login,
            'password': password
        }
        response = courier_methods.login_courier(payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title("Авторизация с отсутствующим полем пароль")
    @allure.description("Проверка авторизации с отстутствующим паролем")
    def test_login_without_password(self, courier_methods, courier_data):
        login = courier_data[0]
        payload = {
            'password': login
        }
        response = courier_methods.post_courier_id(payload)
        assert response.status_code == 400

    @allure.title("Авторизация с существующим логином и неправильным паролем")
    @allure.description("Проверка авторизации с существующим логином и неправильным паролем к нему")
    def test_login_with_incorrect_password(self, courier_methods, courier_data):
        login = courier_data[0]
        payload = {
            'login': login,
            'password': 123456
        }
        response = courier_methods.post_courier_id(payload)
        assert response.status_code == 404


    @allure.title("Авторизация под несуществующим пользователем")
    @allure.description("Проверка логина курьера с несуществующими данными.")
    def test_login_with_wrong_data(self, courier_methods):
        fake = Faker()
        payload = {
            'login': fake.user_name(),
            'password': fake.password()
        }
        response = courier_methods.post_courier_id(payload)
        assert response.status_code == 404