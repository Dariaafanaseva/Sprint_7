from data import BASE_URL, ORDERS_URL
import requests
import allure


class OrderMethods:

    def post_order(self, params):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=params)
        print(response.text)
        return response.status_code, response.json()
