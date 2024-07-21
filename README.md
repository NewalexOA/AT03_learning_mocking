### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание
Этот учебный проект посвящен использованию mock-тестов с библиотекой `pytest` для тестирования HTTP-запросов. Цель проекта - показать, как можно имитировать ответы от API для тестирования функций, которые делают HTTP-запросы.

### Задание
1. Написать функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки.
2. Написать тест, который проверяет успешный запрос и возвращает правильный URL.
3. Написать тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает `None`.

### Выполнение
1. Функция `get_random_cat_image` отправляет запрос к TheCatAPI и возвращает URL случайного изображения кошки, если запрос успешен. В случае ошибки запроса функция возвращает `None`.
2. Тесты написаны с использованием библиотеки `pytest` и `mocker` для имитации ответов на HTTP-запросы.
3. Один тест проверяет успешный запрос, имитируя ответ с кодом 200 и ожидаемым JSON-ответом.
4. Другой тест проверяет неуспешный запрос, имитируя ответ с кодом 404 и возвращая `None`.

### Установка
Для запуска проекта необходимо установить следующие библиотеки:
- requests
- pytest
- pytest-mock

Установить их можно с помощью команды:
```bash
pip install requests pytest pytest-mock
```

---

## <a name="english"></a>Description in English

### Description
This educational project focuses on using mock tests with the `pytest` library to test HTTP requests. The goal of the project is to demonstrate how to mock API responses for testing functions that make HTTP requests.

### Task
1. Write a function that makes a request to TheCatAPI to get a random cat image.
2. Write a test that verifies a successful request and returns the correct URL.
3. Write a test that verifies an unsuccessful request (e.g., status code 404) and returns `None`.

### Implementation
1. The `get_random_cat_image` function sends a request to TheCatAPI and returns the URL of a random cat image if the request is successful. In case of a request error, the function returns `None`.
2. Tests are written using the `pytest` library and `mocker` to mock the responses to HTTP requests.
3. One test checks a successful request by mocking a response with a 200 status code and the expected JSON response.
4. Another test checks an unsuccessful request by mocking a response with a 404 status code and returning `None`.

### Installation
To run the project, you need to install the following libraries:
- requests
- pytest
- pytest-mock

You can install them using the following command:
```bash
pip install requests pytest pytest-mock
```