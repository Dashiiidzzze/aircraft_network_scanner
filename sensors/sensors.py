"""
Модуль SENSORS: Имитирует отправку телеметрических данных в формате CAN-like по UDP.
Данные передаются в модуль CONTROLLERS.
"""

import socket
import time
import json
import random
from datetime import datetime

# Конфигурация адреса контроллера (куда будут отправляться данные)
CONTROLLER_HOST = "controllers"  # DNS-имя контейнера контроллера (указано в docker-compose)
CONTROLLER_PORT = 9000          # Порт, на который контроллер слушает

# Создаём UDP сокет для передачи сообщений
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def generate_sensor_data():
    """
    Генерирует случайные значения телеметрии для температуры, давления и вибрации.
    Значения выбираются в пределах допустимого диапазона.
    """
    return {
        "sensor_id": "TEMP-001",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "temperature": round(random.uniform(22.0, 100.0), 2),   # °C
        "pressure": round(random.uniform(950.0, 1050.0), 2),    # hPa
        "vibration": round(random.uniform(0.0, 5.0), 2)         # m/s²
    }

def send_telemetry():
    """
    Формирует телеметрию, сериализует в JSON и отправляет через UDP.
    """
    data = generate_sensor_data()
    try:
        payload = json.dumps(data).encode('utf-8')
        sock.sendto(payload, (CONTROLLER_HOST, CONTROLLER_PORT))
        print(f"[sensors] -> Sent telemetry: {data}")
    except Exception as e:
        print(f"[sensors] !! Error sending data: {e}")

def main_loop():
    """
    Основной цикл: отправка телеметрии каждую секунду.
    """
    print("[sensors] Telemetry sensor started.")
    while True:
        send_telemetry()
        time.sleep(1)  # интервал между отправками

if __name__ == "__main__":
    main_loop()