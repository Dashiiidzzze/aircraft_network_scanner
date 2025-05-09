# Импортируем библиотеку requests для HTTP-запросов
import requests
import time

# Адрес сервера развлекательной системы
IFE_SERVER_URL = "http://ife_server:8080"

# Получаем список доступных фильмов
def get_available_media():
    response = requests.get(f"{IFE_SERVER_URL}/media")
    if response.status_code == 200:
        return response.json()["catalog"]
    return []

# Отправляем запрос на воспроизведение контента
def play_media(media_id):
    response = requests.post(f"{IFE_SERVER_URL}/play/{media_id}")
    if response.status_code == 200:
        print(f"[PASSENGER DEVICE] Media {media_id} is now playing")
    else:
        print("[PASSENGER DEVICE] Failed to play media")

# Основная функция клиента
if __name__ == "__main__":
    print("[PASSENGER DEVICE] Connecting to IFE...")
    
    # Пауза, чтобы сервер успел запуститься
    time.sleep(2)

    # Получаем каталог и запускаем первый доступный фильм
    catalog = get_available_media()
    if catalog:
        first_media = catalog[0]
        print(f"[PASSENGER DEVICE] Available: {first_media['title']}")
        play_media(first_media["id"])
    else:
        print("[PASSENGER DEVICE] No media available")
