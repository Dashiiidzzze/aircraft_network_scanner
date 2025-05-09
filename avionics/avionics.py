# """
# Модуль Avionics:
# Центральный вычислительный блок, реализующий концепцию Integrated Modular Avionics (IMA).
# Обрабатывает данные от сенсоров и контроллеров, публикует агрегированные данные по MQTT.
# """

# import socket  # Для работы с сетевыми соединениями
# import threading  # Для запуска параллельных потоков
# import time  # Для работы со временем
# import json  # Для работы с JSON-данными
# import paho.mqtt.client as mqtt  # MQTT-клиент для публикации данных

# # Настройки UDP-сервера для приёма данных от сенсоров и контроллеров
# UDP_IP = "0.0.0.0"  # Слушаем на всех интерфейсах
# UDP_PORT = 5005  # Порт для приёма данных

# # Настройки MQTT-брокера для публикации агрегированных данных
# MQTT_BROKER = "secure_gateway"  # Имя сервиса брокера в Docker-сети
# MQTT_PORT = 1883  # Стандартный порт MQTT
# MQTT_TOPIC = "avionics/data"  # Тема для публикации данных

# # Инициализация MQTT-клиента
# mqtt_client = mqtt.Client()

# def udp_listener():
#     """
#     Функция для приёма данных по UDP от сенсоров и контроллеров.
#     """
#     # Создаём UDP-сокет
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # Привязываем сокет к IP и порту
#     sock.bind((UDP_IP, UDP_PORT))
#     print(f"[avionics] Слушаем UDP на {UDP_IP}:{UDP_PORT}")

#     while True:
#         try:
#             # Принимаем данные и адрес отправителя
#             data, addr = sock.recvfrom(1024)
#             # Декодируем байты в строку
#             message = data.decode()
#             print(f"[avionics] Получено от {addr}: {message}")
#             # Обрабатываем полученные данные
#             process_data(message)
#         except Exception as e:
#             print(f"[avionics] Ошибка при приёме данных: {e}")

# def process_data(message):
#     """
#     Обработка полученных данных и публикация агрегированной информации по MQTT.
#     """
#     try:
#         # Предполагаем, что сообщение в формате JSON
#         data = json.loads(message)
#         # Добавляем метку времени
#         data['timestamp'] = time.time()
#         # Публикуем данные в MQTT
#         mqtt_client.publish(MQTT_TOPIC, json.dumps(data))
#         print(f"[avionics] Опубликовано в MQTT: {data}")
#     except json.JSONDecodeError:
#         print(f"[avionics] Неверный формат данных: {message}")
#     except Exception as e:
#         print(f"[avionics] Ошибка при обработке данных: {e}")

# def main():
#     """
#     Главная функция для запуска модуля Avionics.
#     """
#     try:
#         # Подключаемся к MQTT-брокеру
#         mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
#         print(f"[avionics] Подключено к MQTT-брокеру на {MQTT_BROKER}:{MQTT_PORT}")
#     except Exception as e:
#         print(f"[avionics] Не удалось подключиться к MQTT-брокеру: {e}")
#         return

#     # Запускаем поток для приёма UDP-данных
#     udp_thread = threading.Thread(target=udp_listener, daemon=True)
#     udp_thread.start()

#     # Основной цикл для поддержания работы модуля
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("[avionics] Завершение работы модуля.")

# if __name__ == "__main__":
#     main()


# # # import socket  # Для работы с сетевыми соединениями
# # # import threading  # Для запуска параллельных потоков
# # # import time  # Для работы со временем
# # # import json  # Для работы с JSON-данными
# # # import paho.mqtt.client as mqtt  # MQTT-клиент для публикации данных

# # # # Настройки UDP-сервера для приёма данных от сенсоров и контроллеров
# # # UDP_IP = "0.0.0.0"  # Слушаем на всех интерфейсах
# # # UDP_PORT = 5005  # Порт для приёма данных

# # # # Настройки MQTT-брокера для публикации агрегированных данных
# # # MQTT_BROKER = "secure_gateway"  # Имя сервиса брокера в Docker-сети
# # # MQTT_PORT = 1883  # Стандартный порт MQTT
# # # MQTT_TOPIC = "avionics/data"  # Тема для публикации данных

# # # # Инициализация MQTT-клиента
# # # mqtt_client = mqtt.Client()

# # # def on_connect(client, userdata, flags, rc):
# # #     """
# # #     Обработчик события подключения к MQTT-брокеру.
# # #     """
# # #     if rc == 0:
# # #         print(f"[avionics] Успешное подключение к MQTT-брокеру: {MQTT_BROKER}")
# # #     else:
# # #         print(f"[avionics] Ошибка подключения к MQTT-брокеру. Код: {rc}")

# # # def on_disconnect(client, userdata, rc):
# # #     """
# # #     Обработчик события отключения от MQTT-брокера.
# # #     """
# # #     if rc != 0:
# # #         print(f"[avionics] Отключение от MQTT-брокера. Код ошибки: {rc}")
# # #     else:
# # #         print("[avionics] Отключение от MQTT-брокера выполнено.")

# # # # Инициализация MQTT-клиента
# # # mqtt_client.on_connect = on_connect
# # # mqtt_client.on_disconnect = on_disconnect

# # # def udp_listener():
# # #     """
# # #     Функция для приёма данных по UDP от сенсоров и контроллеров.
# # #     """
# # #     # Создаём UDP-сокет
# # #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # #     # Привязываем сокет к IP и порту
# # #     sock.bind((UDP_IP, UDP_PORT))
# # #     print(f"[avionics] Слушаем UDP на {UDP_IP}:{UDP_PORT}")

# # #     while True:
# # #         try:
# # #             # Принимаем данные и адрес отправителя
# # #             data, addr = sock.recvfrom(1024)
# # #             # Декодируем байты в строку
# # #             message = data.decode()
# # #             print(f"[avionics] Получено от {addr}: {message}")
# # #             # Обрабатываем полученные данные
# # #             process_data(message)
# # #         except Exception as e:
# # #             print(f"[avionics] Ошибка при приёме данных: {e}")
# # #         finally:
# # #             sock.close()

# # # def process_data(message):
# # #     """
# # #     Обработка полученных данных и публикация агрегированной информации по MQTT.
# # #     """
# # #     try:
# # #         # Предполагаем, что сообщение в формате JSON
# # #         data = json.loads(message)
# # #         # Добавляем метку времени
# # #         data['timestamp'] = time.time()
# # #         # Публикуем данные в MQTT
# # #         mqtt_client.publish(MQTT_TOPIC, json.dumps(data))
# # #         print(f"[avionics] Опубликовано в MQTT: {data}")
# # #     except json.JSONDecodeError:
# # #         print(f"[avionics] Неверный формат данных: {message}")
# # #     except Exception as e:
# # #         print(f"[avionics] Ошибка при обработке данных: {e}")

# # # def main():
# # #     """
# # #     Главная функция для запуска модуля Avionics.
# # #     """
# # #     try:
# # #         # Подключаемся к MQTT-брокеру
# # #         mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
# # #         print(f"[avionics] Подключено к MQTT-брокеру на {MQTT_BROKER}:{MQTT_PORT}")
# # #     except Exception as e:
# # #         print(f"[avionics] Не удалось подключиться к MQTT-брокеру: {e}")
# # #         return

# # #     # Запускаем поток для приёма UDP-данных
# # #     udp_thread = threading.Thread(target=udp_listener, daemon=True)
# # #     udp_thread.start()

# # #     # Запускаем MQTT-клиент в отдельном потоке, чтобы он не блокировал основной поток
# # #     mqtt_thread = threading.Thread(target=mqtt_client.loop_forever, daemon=True)
# # #     mqtt_thread.start()

# # #     # Основной цикл для поддержания работы модуля
# # #     try:
# # #         while True:
# # #             time.sleep(1)
# # #     except KeyboardInterrupt:
# # #         print("[avionics] Завершение работы модуля.")
# # #     finally:
# # #         mqtt_client.disconnect()

# # # if __name__ == "__main__":
# # #     main()

# import paho.mqtt.client as mqtt  # MQTT-клиент для публикации данных

# # Настройки MQTT-брокера для публикации агрегированных данных
# MQTT_BROKER = "secure_gateway"  # Имя сервиса брокера в Docker-сети
# MQTT_PORT = 1883  # Стандартный порт MQTT
# MQTT_TOPIC = "avionics/data"  # Тема для публикации данных

# # Инициализация MQTT-клиента с использованием MQTTv5
# mqtt_client = mqtt.Client(protocol=mqtt.MQTTv5)

# def on_connect(client, userdata, flags, rc):
#     """
#     Обработчик события подключения к MQTT-брокеру.
#     """
#     if rc == 0:
#         print(f"[avionics] Успешное подключение к MQTT-брокеру: {MQTT_BROKER}")
#         client.subscribe(MQTT_TOPIC)  # Подписка на нужную тему
#     else:
#         print(f"[avionics] Ошибка подключения к MQTT-брокеру. Код: {rc}")

# def on_disconnect(client, userdata, rc):
#     """
#     Обработчик события отключения от MQTT-брокера.
#     """
#     if rc != 0:
#         print(f"[avionics] Отключение от MQTT-брокера. Код ошибки: {rc}")
#     else:
#         print("[avionics] Отключение от MQTT-брокера выполнено.")

# # Инициализация MQTT-клиента
# mqtt_client.on_connect = on_connect
# mqtt_client.on_disconnect = on_disconnect

"""
Модуль Avionics:
Центральный вычислительный блок, реализующий концепцию Integrated Modular Avionics (IMA).
Обрабатывает данные от сенсоров и контроллеров, публикует агрегированные данные по MQTT.
"""

import socket
import threading
import time
import json
import paho.mqtt.client as mqtt

# Настройки UDP-сервера
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

# Настройки MQTT-брокера
MQTT_BROKER = "mosquitto-broker"
MQTT_PORT = 1883
MQTT_TOPIC = "avionics/data/#"

# Инициализация MQTT-клиента с новым API
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def on_connect(client, userdata, flags, reason_code, properties=None):
    """
    Обработчик подключения к MQTT-брокеру (новый API).
    """
    if reason_code == 0:
        print(f"[avionics] Успешное подключение к MQTT-брокеру: {MQTT_BROKER}")
    else:
        print(f"[avionics] Ошибка подключения. Код: {reason_code}")

def on_disconnect(client, userdata, flags, reason_code, properties=None):
    """
    Обработчик отключения от MQTT-брокера (новый API).
    """
    print(f"[avionics] Отключение от брокера. Код: {reason_code}")

# Назначаем обработчики
mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect

def udp_listener():
    """Функция для приёма данных по UDP."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"[avionics] Слушаем UDP на {UDP_IP}:{UDP_PORT}")

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            message = data.decode()
            print(f"[avionics] Получено от {addr}: {message}")
            process_data(message)
        except Exception as e:
            print(f"[avionics] Ошибка при приёме данных: {e}")

def process_data(message):
    """Обработка данных и публикация в MQTT."""
    try:
        data = json.loads(message)
        data['timestamp'] = time.time()
        mqtt_client.publish(MQTT_TOPIC, json.dumps(data))
        print(f"[avionics] Опубликовано в MQTT: {data}")
    except json.JSONDecodeError:
        print(f"[avionics] Неверный формат данных: {message}")
    except Exception as e:
        print(f"[avionics] Ошибка обработки: {e}")

def main():
    """Главная функция модуля."""
    try:
        # Подключение с таймаутом и обработкой ошибок
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print(f"[avionics] Попытка подключения к {MQTT_BROKER}:{MQTT_PORT}")
        
        # Запуск MQTT-клиента в отдельном потоке
        mqtt_thread = threading.Thread(target=mqtt_client.loop_start)
        mqtt_thread.daemon = True
        mqtt_thread.start()
        
        # Даем время на подключение
        time.sleep(2)
        
        if not mqtt_client.is_connected():
            print("[avionics] Предупреждение: подключение к MQTT не установлено")
        
    except Exception as e:
        print(f"[avionics] Критическая ошибка подключения: {e}")
        return

    # Запуск UDP-листенера
    udp_thread = threading.Thread(target=udp_listener)
    udp_thread.daemon = True
    udp_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[avionics] Завершение работы.")
    finally:
        mqtt_client.disconnect()

if __name__ == "__main__":
    main()
