import pytest
import requests
import allure
import data


class TestCreateOrder:

    @allure.title("Проверка создания заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_success(self, register_user_and_get_token):
        access_token = register_user_and_get_token  # регистрируем нового пользователя и получаем токен

        headers = {'Authorization': access_token}
        payload = {
            "ingredients": data.VALID_INGREDIENTS_1
        }
        response = requests.post(f'{data.BURGER_URL}/{data.ORDER_ENDPOINT}',
                                 json=payload, headers=headers)

        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title("Проверка создания заказа без авторизации")
    def test_create_order_no_auth_success(self):

        payload = {
            "ingredients": data.VALID_INGREDIENTS_1
        }
        response = requests.post(f'{data.BURGER_URL}/{data.ORDER_ENDPOINT}',
                                 json=payload)

        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_no_ingredients_fail(self, register_user_and_get_token):
        access_token = register_user_and_get_token  # регистрируем нового пользователя и получаем токен

        headers = {'Authorization': access_token}
        payload = {
            "ingredients": ""
        }
        response = requests.post(f'{data.BURGER_URL}/{data.ORDER_ENDPOINT}',
                                 json=payload, headers=headers)

        assert response.status_code == 400 and response.text == data.NO_INGREDIENTS_MESSAGE

    @allure.title("Проверка создания заказа c неправильным хэшем ингредиентов")
    def test_create_order_wrong_ids_fail(self, register_user_and_get_token):
        access_token = register_user_and_get_token  # регистрируем нового пользователя и получаем токен

        headers = {'Authorization': access_token}
        payload = {
            "ingredients": data.INVALID_INGREDIENT
        }
        response = requests.post(f'{data.BURGER_URL}/{data.ORDER_ENDPOINT}',
                                 json=payload, headers=headers)

        assert response.status_code == 500

