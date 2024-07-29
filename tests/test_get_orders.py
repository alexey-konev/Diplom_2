import pytest
import requests
import allure
import data


class TestGetOrders:

    @allure.title("Проверка успешного получения заказов пользователя")
    def test_get_orders_success(self, register_user_and_get_token):
        access_token = register_user_and_get_token  # регистрируем нового пользователя и получаем токен
        headers = {'Authorization': access_token}

        response = requests.get(f'{data.BURGER_URL}/{data.GET_ORDERS_ENDPOINT}', headers=headers)

        assert response.status_code == 200 and '"success":true' in response.text
        # ручка не возвращает заказы конкретного пользователя, в постман тоже. Хотел проверить через кол-во заказов
        # у пользователя - "total" , но total возвращается равный примерно 102 тысячи - видимо всех пользователей

    @allure.title("Проверка получения заказов без авторизации")
    def test_get_orders_unauthorized_fail(self):

        response = requests.get(f'{data.BURGER_URL}/{data.GET_ORDERS_ENDPOINT}')

        assert response.status_code == 401 and data.UNAUTHORIZED_MESSAGE
