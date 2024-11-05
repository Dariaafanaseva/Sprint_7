BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'
COURIER_ID_URL = 'courier/login'


DUBLICATE_LOGIN_MESSAGE = 'Этот логин уже используется. Попробуйте другой.'
CREATE_REQUEST_WITHOUT_LOGIN = 'Недостаточно данных для создания учетной записи'
EXISTING_LOGIN_MASSAGE = 'Этот логин уже используется. Попробуйте другой.'
LOGIN_REQUEST_WITHOUT_PASSWORD = 'Недостаточно данных для входа'
NOT_EXISTING_DATA = 'Учетная запись не найдена'

ORDER_DATA_BLACK_COLOR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-11-11",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
ORDER_DATA_BLACK_AND_GREY_COLOR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-11-11",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK",
        "GRAY"
    ]
}
ORDER_DATA_NO_COLOR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-11-11",
    "comment": "Saske, come back to Konoha",
    "color": []
}

COURIER_DATA = {
    "login": "niTnja",
    "password": "1234",
    "firstName": "Tsaske"
}

EXISTING_COURIER = {
        "login": "existing_login159",
        "password": "password",
        "firstName": "Name"}

COURIER_DATA_NO_LOGIN = {
    "password": "1234",
    "firstName": "Tsaske"
}

