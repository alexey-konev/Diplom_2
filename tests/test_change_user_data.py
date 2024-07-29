import pytest
import requests
import allure
import data, helpers


class TestChangeUserData:

    @allure.title("Проверка изменения данных пользователя с авторизацией по токену")
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_change_user_data_success(self, field):

        user_data, access_token = helpers.register_new_user_and_return_login_password_token()
        headers = {'Authorization': access_token}
        payload = {
            "email": user_data[0],
            "password": user_data[1],
            "name": user_data[2]
        }
        payload[field] = f'{payload[field]}asd'  # меняем эмейл, пароль или имя

        response = requests.patch(f'{data.BURGER_URL}/{data.UPDATE_USER_ENDPOINT}',
                                  json=payload, headers=headers)

        assert response.status_code == 200 and '"success":true' in response.text

        helpers.delete_user(access_token)  # удаляем тетстовые данные

    @allure.title("Проверка изменения данных пользователя без авторизации")
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_change_user_data_without_token_fail(self, field):

        user_data, access_token = helpers.register_new_user_and_return_login_password_token()

        payload = {
            "email": user_data[0],
            "password": user_data[1],
            "name": user_data[2]
        }
        payload[field] = f'{payload[field]}asd'  # меняем эмейл, пароль или имя

        response = requests.patch(f'{data.BURGER_URL}/{data.UPDATE_USER_ENDPOINT}',
                                  json=payload)

        assert response.status_code == 401 and response.text == data.UNAUTHORIZED_MESSAGE

        helpers.delete_user(access_token)  # удаляем тетстовые данные


    @allure.title("Проверка изменения эмейла, на тот, который уже используется")
    def test_change_user_data_email_already_exists_fail(self):

        user_data_1, access_token_1 = helpers.register_new_user_and_return_login_password_token()
        user_data_2, access_token_2 = helpers.register_new_user_and_return_login_password_token()

        headers = {'Authorization': access_token_1}
        payload = {
            "email": user_data_2[0],  # попробуем подставить эмейл пользователя 2
        }

        response = requests.patch(f'{data.BURGER_URL}/{data.UPDATE_USER_ENDPOINT}',
                                  json=payload, headers=headers)

        assert response.status_code == 403 and response.text == data.EMAIL_EXISTS_MESSAGE

        helpers.delete_user(access_token_1)  # удаляем тетстовые данные
        helpers.delete_user(access_token_2)
