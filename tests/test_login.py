import pytest
import allure
import requests
import helpers, data


class TestLogin:
    @allure.title("Проверка успешной авторизации пользователя")
    def test_login_success(self):

        user_data, access_token = helpers.register_new_user_and_return_login_password_token()
        payload = {
            "email": user_data[0],
            "password": user_data[1]
        }
        response = requests.post(f'{data.BURGER_URL}/{data.LOGIN_ENDPOINT}', json=payload)

        assert response.status_code == 200 and access_token  # проверяем код ответа, и что получен токен

        helpers.delete_user(access_token)  # удаляем тетстовые данные

    @allure.title("Проверка авторизации пользователя  неправильным эмейлом")
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_login_incorrect_email_fail(self, field):

        user_data, access_token = helpers.register_new_user_and_return_login_password_token()
        payload = {
            "email": user_data[0],
            "password": user_data[1]
        }
        payload[field] = f'{payload[field]}asd'  # "портим" эмейл или пароль
        response = requests.post(f'{data.BURGER_URL}/{data.LOGIN_ENDPOINT}', json=payload)

        assert response.status_code == 401 and response.text == data.INCORRECT_LOGIN_DATA_MESSAGE  # проверяем код ответа, и что получен токен

        helpers.delete_user(access_token)  # удаляем тетстовые данные
