"""
Модуль CONTROLLERS: Принимает телеметрию от сенсоров по UDP, анализирует и решает, отправлять ли команду actuator'у.
"""

import socket
import json
from datetime import datetime

# Настройки сервера
LISTEN_HOST = "0.0.0.0"  # слушаем на всех интерфейсах контейнера
LISTEN_PORT = 9000       # порт, на который сенсоры отправляют данные

# Адрес исполнительного модуля
ACTUATOR_HOST = "actuators"
ACTUATOR_PORT = 9100

# Пороговые значения — если превышены, отправляется команда
TEMP_THRESHOLD = 80.0      # °C
VIBRATION_THRESHOLD = 4.0  # m/s²

# Инициализация UDP-сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_HOST, LISTEN_PORT))

def parse_and_decide(message):
    """
    Обрабатывает полученное сообщение. Если данные превышают допустимые значения — формирует команду.
    """
    try:
        data = json.loads(message.decode('utf-8'))
        print(f"[controller] <- Received: {data}")
        
        temperature = data.get("temperature", 0)
        vibration = data.get("vibration", 0)

        # Проверка превышения допустимых значений
        if temperature > TEMP_THRESHOLD or vibration > VIBRATION_THRESHOLD:
            command = {
                "action": "SHUTDOWN_ENGINE",
                "reason": "Telemetry threshold exceeded",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "details": {
                    "temperature": temperature,
                    "vibration": vibration
                }
            }
            send_command_to_actuator(command)
        else:
            print("[controller] -- Normal telemetry. No action required.")
    except Exception as e:
        print(f"[controller] !! Error processing telemetry: {e}")

def send_command_to_actuator(command):
    """
    Отправляет управляющую команду actuator'у.
    """
    try:
        payload = json.dumps(command).encode('utf-8')
        sock.sendto(payload, (ACTUATOR_HOST, ACTUATOR_PORT))
        print(f"[controller] -> Sent command to actuator: {command}")
    except Exception as e:
        print(f"[controller] !! Failed to send command: {e}")

def main_loop():
    """
    Цикл приёма сообщений от сенсоров.
    """
    print("[controller] Controller is running and waiting for telemetry...")
    while True:
        try:
            message, _ = sock.recvfrom(4096)  # получение UDP-пакета
            parse_and_decide(message)
        except Exception as e:
            print(f"[controller] !! UDP receive error: {e}")

if __name__ == "__main__":
    main_loop()
