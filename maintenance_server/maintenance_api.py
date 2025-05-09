# Импортируем Flask для создания HTTP API
from flask import Flask, request, jsonify

# Создаём Flask приложение
app = Flask(__name__)

# УЯЗВИМОСТЬ: включён DEBUG — может позволить удалённое выполнение кода!
app.config["DEBUG"] = True

# Список логов (в реальности логируются события с avionics и sensors)
logs = [
    "Sensor T1: OK",
    "Sensor P2: ERROR",
    "Flap actuator test: OK",
    "Temperature anomaly in zone 3"
]

# Роут для получения логов
@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify({"logs": logs})

# Роут для симуляции обновлений ПО
@app.route("/update_firmware", methods=["POST"])
def update_firmware():
    # Псевдообработка запроса
    data = request.get_json()
    print(f"[MAINTENANCE] Firmware update command received for module: {data.get('module')}")
    return jsonify({"status": "firmware update started", "module": data.get("module")})

# Запуск API-сервера на порту 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
