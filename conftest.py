import pytest
import requests

import data
import helpers


@pytest.fixture()
def register_new_user():

    # генерируем рандомные данные и отправляем запрос на регистарцию
    payload = helpers.generate_new_user_data()
    response = requests.post(f'{data.BURGER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)
    yield response
    access_token = response.json()["accessToken"]
    helpers.delete_user(access_token)  # удаляем тетстовые данные


@pytest.fixture()
def register_user_and_get_token():
    # генерируем рандомные данные и отправляем запрос на регистарцию
    payload = helpers.generate_new_user_data()
    response = requests.post(f'{data.BURGER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)
    access_token = response.json()["accessToken"]
    yield access_token
    helpers.delete_user(access_token)  # удаляем тетстовые данные

# @pytest.fixture()
# def login_new_user():
#
#     new_user = helpers.register_new_user_and_return_login_password()  # получаем список из логина, пароля и имени
#     payload = {
#         "login": new_user[0],  # 0 - индекс логина в списке new_user
#         "password": new_user[1]  # 1 - индекс пароля в списке new_user
#     }
#     response = requests.post(f'{data.BURGER_URL}/{data.LOGIN_ENDPOINT}', json=payload)
#     yield response
#
#     helpers.delete_courier(payload)
