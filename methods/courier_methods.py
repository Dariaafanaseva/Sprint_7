from data import BASE_URL, COURIERS_URL, COURIER_ID_URL, COURIERS_DELETE_URL
import requests
import json

class CourierMethods:

    def post_create_courier(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=params)
        return response.status_code, response.json()

    def post_courier_id(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_ID_URL}', json=params)
        return response.status_code, response.json()

@allure.step("Удаление курьера по ID")
    def delete_courier(self, id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{id}')
        return response

    @allure.step("Аутентификация курьера с параметрами")
    def login_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', json=payload)
        return response

