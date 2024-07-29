# ИНГРЕДИЕНТЫ

VALID_INGREDIENTS_1 = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]

VALID_INGREDIENTS_2 = ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa72"]

INVALID_INGREDIENT = ["60d3b41abdacab0026a733c6asd"]

# ЭНДПОИНТЫ

BURGER_URL = 'https://stellarburgers.nomoreparties.site/'

REGISTRATION_ENDPOINT = 'api/auth/register'

LOGIN_ENDPOINT = 'api/auth/login'

DELETE_ENDPOINT = 'api/auth/user'

UPDATE_USER_ENDPOINT = 'api/auth/user'

ORDER_ENDPOINT = 'api/orders'

GET_ORDERS_ENDPOINT = 'api/orders'

# ТЕЛО ОТВЕТА

MISSING_FILED_MESSAGE = '{"success":false,"message":"Email, password and name are required fields"}'

LOGIN_EXISTS_MESSAGE = '{"success":false,"message":"User already exists"}'

INCORRECT_LOGIN_DATA_MESSAGE = '{"success":false,"message":"email or password are incorrect"}'

UNAUTHORIZED_MESSAGE = '{"success":false,"message":"You should be authorised"}'

EMAIL_EXISTS_MESSAGE = '{"success":false,"message":"User with such email already exists"}'

NO_INGREDIENTS_MESSAGE = '{"success":false,"message":"Ingredient ids must be provided"}'
