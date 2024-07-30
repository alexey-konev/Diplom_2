import pytest
import requests
import allure
import data, helpers


class TestRegistration:

    @allure.title("Проверка регистрации пользователя")
    def test_registration_success(self, register_new_user):
        # через фикстуру генерируем данные и отправляем запрос на регистрацию
        response = register_new_user  # записываем ответ в response

        assert response.status_code == 200 and '"success":true' in response.text
        # после asserta тестовые данные удаляются фикстуре

    @allure.title("Проверка регистрации пользователя без одного из полей")
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_registration_without_field_fail(self, field):

        payload = helpers.generate_new_user_data()
        payload.pop(field)  # убираем одно из полей
        response = requests.post(f'{data.BURGER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)

        assert response.status_code == 403 and response.text == data.MISSING_FILED_MESSAGE

    @allure.title("Проверка создания двух одинаковых пользователей")
    def test_registration_twice_fail(self):
        # генерируем рандомные данные и отправляем запрос на регистарцию
        payload = helpers.generate_new_user_data()
        response_1 = requests.post(f'{data.BURGER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)
        access_token = response_1.json()["accessToken"]
        response_2 = requests.post(f'{data.BURGER_URL}/{data.REGISTRATION_ENDPOINT}',
                                 json=payload)  # дублируем запрос на регистарцию

        assert response_2.status_code == 403 and response_2.text == data.LOGIN_EXISTS_MESSAGE

        helpers.delete_user(access_token)  # удаляем тетстовые данные




