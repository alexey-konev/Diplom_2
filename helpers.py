import json
import allure
import requests
import random
import string
import data


@allure.step('Генерируем строку из букв нижнего регистра указанной длины')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерируем логин, пароль и имя пользователя')
def generate_new_user_data():

    # генерируем логин, пароль и имя курьера
    login = f'{generate_random_string(5)}@yayaya.com'
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": login,
        "password": password,
        "name": first_name
    }

    return payload


# метод регистрации нового пользователя возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Регистрируем сгенерированного пользоватлея')
def register_new_user_and_return_login_password_token():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []
    access_token = ''

    payload = generate_new_user_data()
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{data.BURGER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль курьера, записываем токен
    if response.status_code == 200:
        login_pass.append(payload['email'])
        login_pass.append(payload['password'])
        login_pass.append(payload['name'])

        access_token = response.json()["accessToken"]

    # возвращаем список и токен
    return login_pass, access_token

@allure.step('Удаляем сгенерированного тестового пользователя по токену')
def delete_user(user_token):

    headers = {'Authorization': user_token}
    requests.delete(f'{data.BURGER_URL}/{data.DELETE_ENDPOINT}', headers=headers)

