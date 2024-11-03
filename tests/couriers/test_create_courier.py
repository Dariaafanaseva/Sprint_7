import pytest
#from data import COURIER_DATA

class TestCreateCourier:

    #проверки что курьера (со всеми обязательными полями) можно создать
    def test_create_courier(self, courier_methods, courier):
        status_code, response_context = courier_methods.post_create_courier(courier)
        assert status_code == 201 and response_context == {'ok': True}

    #нельзя создать курьера с дублирующими данными
    def test_create_dublicate_courier(self, courier_methods, courier):
        status_code, response_context = courier_methods.post_create_courier(courier)
        assert status_code == 201
        status_code_dup, response_context_dup = courier_methods.post_create_courier(courier)
        assert status_code_dup == 409, f"Ожидался код 409, получен: {status_code_dup}. Ответ: {response_context_dup.get('message', 'Нет сообщения')}"


    #нельзя создать курьера без логина:
    def test_create_courier_without_firstname(self, courier_methods, courier_without_firstname):
        status_code, response_context = courier_methods.post_create_courier(courier_without_firstname)
        assert status_code == 400

    #нельзя создать курьера с существующим логином
    def test_create_existing_courier(self, courier_methods, existing_courier):
        status_code, response_context = courier_methods.post_create_courier(existing_courier)
        assert status_code == 409 and response_context == {"message": "Этот логин уже используется"}

    #определение id созданного курьера
    def test_id_courier(self, courier_methods, courier, courier_id):
        status_code, response_context = courier_methods.post_create_courier(courier)
        assert status_code == 201



