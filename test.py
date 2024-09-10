from main import get_random_cat_image


def test_successful_request(mocker):
    # Создание имитации успешного ответа
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/example.jpg'}
    ]

    # Вызов функции и проверка результата
    result = get_random_cat_image()

    assert result == "https://cdn2.thecatapi.com/images/example.jpg"


def test_unsuccessful_request(mocker):
    # Создание имитации неуспешного ответа
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = None

    # Вызов функции и проверка результата
    result = get_random_cat_image()

    assert result is None
