# Используем минимальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем скрипт модуля в контейнер
COPY avionics.py .

# Устанавливаем необходимые зависимости
RUN pip install --no-cache-dir paho-mqtt

# Устанавливаем команду запуска контейнера
CMD ["python", "avionics.py"]
