"""
Модуль ACTUATORS: Получает команды от controller'а по UDP и имитирует выполнение действий.
"""

import socket
import json
from datetime import datetime

# Настройки прослушивания команд
LISTEN_HOST = "0.0.0.0"
LISTEN_PORT = 9100  # Порт, на который controller отправляет команды

# Инициализация UDP-сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_HOST, LISTEN_PORT))

def perform_action(command):
    """
    Имитация выполнения команды. В реальности — здесь управление механизмами.
    """
    try:
        print(f"[actuator] -> Executing command: {command['action']}")
        print(f"[actuator]    Reason: {command.get('reason')}")
        print(f"[actuator]    Details: {command.get('details')}")
        print(f"[actuator]    Time: {command.get('timestamp')}")
        print(f"[actuator] -- Action completed.\n")
    except Exception as e:
        print(f"[actuator] !! Failed to execute action: {e}")

def main_loop():
    """
    Цикл ожидания управляющих команд от controller'а.
    """
    print("[actuator] Actuator is running and waiting for commands...")
    while True:
        try:
            message, _ = sock.recvfrom(4096)
            data = json.loads(message.decode('utf-8'))
            perform_action(data)
        except Exception as e:
            print(f"[actuator] !! Error receiving/processing command: {e}")

if __name__ == "__main__":
    main_loop()
