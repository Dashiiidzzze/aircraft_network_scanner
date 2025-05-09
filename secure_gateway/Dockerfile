# Минимальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем скрипт шлюза и SSL-сертификаты
COPY gateway.py .
COPY server.crt .
COPY server.key .

# Устанавливаем зависимости
RUN pip install --no-cache-dir paho-mqtt

# Открываем HTTPS-порт
EXPOSE 443

# Запускаем шлюз
CMD ["python", "gateway.py"]
