import requests


def get_random_cat_image():
    search_url = "https://api.thecatapi.com/v1/images/search"

    try:
        response = requests.get(search_url)
        response.raise_for_status()

        cat_image = response.json()
        if cat_image:
            return cat_image[0]["url"]
        else:
            print("Не удалось получить изображение кошки")
            return None
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None


if __name__ == "__main__":
    cat_image_url = get_random_cat_image()
    if cat_image_url:
        print("Ссылка на изображение кошки:", cat_image_url)
