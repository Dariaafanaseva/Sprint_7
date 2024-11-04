from data import BASE_URL, COURIERS_URL, COURIER_ID_URL, COURIERS_DELETE_URL
import requests
import allure

class CourierMethods:

    def post_create_courier(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=params)
        return response

    def post_courier_id(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_ID_URL}', json=params)
        return response

    def delete_courier(self, id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{id}')
        return response


