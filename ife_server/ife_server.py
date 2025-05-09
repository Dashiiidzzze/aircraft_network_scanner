# Импортируем Flask — веб-фреймворк для создания API
from flask import Flask, jsonify

# Создаём экземпляр Flask-приложения
app = Flask(__name__)

# Имитированный каталог фильмов (в реальности тянулось бы с NAS)
media_catalog = [
    {"id": 1, "title": "Top Gun", "genre": "Action"},
    {"id": 2, "title": "The Martian", "genre": "Sci-Fi"},
    {"id": 3, "title": "Coco", "genre": "Animation"}
]

# Маршрут API для получения списка фильмов
@app.route("/media", methods=["GET"])
def get_media():
    # Возвращаем список фильмов в формате JSON
    return jsonify({"catalog": media_catalog})

# Роут для "воспроизведения" контента — в реальности поток шел бы через AV-модуль
@app.route("/play/<int:media_id>", methods=["POST"])
def play_media(media_id):
    # Псевдологика воспроизведения
    print(f"[IFE] Playing media ID {media_id}")
    return jsonify({"status": "playing", "media_id": media_id})

# Запуск сервера на адресе 0.0.0.0, порт 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
