import http.server  # Для создания HTTP(S) сервера
import ssl  # Для поддержки SSL-сертификатов
import threading  # Для параллельного запуска MQTT и HTTPS
import paho.mqtt.client as mqtt  # Клиент для подключения к Mosquitto
import time  # Для добавления паузы в основной поток
import os

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Обработчик HTTP(S) запросов — может отдавать заглушку или статус.
    """
    def do_GET(self):
        # Простой ответ на любой GET-запрос
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Secure Gateway Operational")

def start_https_server():
    """
    Запускает HTTPS-сервер на порту 443.
    """
    httpd = http.server.HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)

    if not os.path.exists('/app/server.crt') or not os.path.exists('/app/server.key'):
        print("[ERROR] SSL certificate files not found!")
        exit(1111)
    
    # Оборачиваем в SSL — используем локальные сертификаты
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='/app/server.crt', keyfile='/app/server.key')

    # Применяем SSL-контекст
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print("[gateway] HTTPS-сервер запущен на порту 443")
    httpd.serve_forever()

def on_message(client, userdata, msg):
    """
    Обработка входящих MQTT-сообщений.
    """
    print(f"[mqtt] Сообщение получено: {msg.topic} => {msg.payload.decode()}")

def on_connect(client, userdata, flags, rc, properties=None):
    """
    Обработка события подключения к MQTT брокеру.
    """
    if rc == mqtt.CONNACK_ACCEPTED:
        print("[mqtt] Успешное подключение к брокеру")
        client.subscribe("avionics/data/#")
    else:
        print(f"[mqtt] Ошибка подключения, код: {rc}")

def start_mqtt_client():
    """
    Подключение к внешнему Mosquitto-брокеру (в контейнере).
    """
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.on_connect = on_connect

    # Подключение к брокеру
    try:
        client.connect("mosquitto-broker", 1883)  # имя контейнера, если внутри Docker-сети
    except Exception as e:
        print(f"[mqtt] Ошибка подключения: {e}")
        return

    print("[mqtt] Подключено к Mosquitto, подписка на gateway/#")
    client.loop_forever()

def main():
    """
    Главная точка входа в шлюз.
    """
    print("[gateway] Запуск Secure Gateway")

    # HTTPS-сервер — отдельный поток
    threading.Thread(target=start_https_server, daemon=True).start()

    # MQTT-клиент — отдельный поток
    threading.Thread(target=start_mqtt_client, daemon=True).start()

    # Основной цикл с паузой, чтобы не завершался главный поток
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()