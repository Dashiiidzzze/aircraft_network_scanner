# Импортируем библиотеку Flask для создания HTTP сервера
from flask import Flask, jsonify

# Создаём приложение Flask
app = Flask(__name__)

# Имитация текущих параметров полёта (здесь данные получаются "от avionics")
flight_data = {
    "altitude": 11500,  # Высота в метрах
    "speed": 850,       # Скорость в км/ч
    "heading": 270      # Курс (направление) в градусах
}

# Роут: возвращает параметры полёта в формате JSON
@app.route("/telemetry", methods=["GET"])
def get_telemetry():
    return jsonify(flight_data)

# Роут: отправка команд от пилота (на самом деле просто логируем)
@app.route("/command/<action>", methods=["POST"])
def send_command(action):
    # В реальности команды шли бы через avionics → controllers
    print(f"[PILOT INTERFACE] Command sent: {action}")
    return jsonify({"status": "command received", "action": action})

# Запуск сервера на порту 80
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
