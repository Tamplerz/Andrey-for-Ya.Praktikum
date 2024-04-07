# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


# эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body


# Функция для позитивной проверки
def negative_assert(first_name):
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(first_name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    user_response = sender_stand_request.post_new_user(user_body)

    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400
    # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == ("Имя пользователя введено некорректно. " \
                                               "Имя может содержать только русские или " \
                                               "латинские буквы, длина должна быть не менее " \
                                               "2 и не более 15 символов")


# для теста 10-11
def negative_assert10_11(user_body):
    # В переменную user_body сохраняется обновлённое тело запроса
 #   user_body = get_user_body(first_name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    response = sender_stand_request.post_new_user(user_body)

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400
    # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


def negative_assert12(first_name):
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(first_name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    user_response12 = sender_stand_request.post_new_user(user_body)

    # Проверяется, что код ответа равен 400
    assert user_response12.status_code == 400


# Тест 3. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test3_create_user_2_letter_in_first_name_get_success_response():
    negative_assert("A")


# Тест 4. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test4_create_user_2_letter_in_first_name_get_success_response():
    negative_assert("Aaaaaaaaaaaaaaaa")


# Тест 7. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test7_create_user_2_letter_in_first_name_get_success_response():
    negative_assert("Человек и Ко")


# Тест 8. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test8_create_user_2_letter_in_first_name_get_success_response():
    negative_assert("№%@")


# Тест 9. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test9_create_user_2_letter_in_first_name_get_success_response():
    negative_assert("123")


# тест 10
def test10_create_user_no_first_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    user_body = data.user_body.copy()
    # Удаление параметра firstName из запроса
    user_body.pop("firstName")
    # Проверка полученного ответа
    negative_assert10_11(user_body)


# Тест 11. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test11_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("")
    # Проверка полученного ответа
    negative_assert10_11(user_body)


# Тест 12. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test12_create_user_2_letter_in_first_name_get_success_response():
    negative_assert12(12)
