
import random
import string
import allure

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
class CreateRandomCourier:
    def register_new_courier_and_return_login_password_firstname(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Печатаем значения для проверки
        print("Сформированный payload для курьера:", payload)

        return payload

    def register_new_courier_without_firstname(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "password": password,
            "firstName": first_name
        }
        # Печатаем значения для проверки
        print("Сформированный payload для курьера:", payload)
        return payload

    def register_new_courier_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass
