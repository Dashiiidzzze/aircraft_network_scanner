# Минимальный образ с Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем основной скрипт в контейнер
COPY . .

# Запуск при старте контейнера
CMD ["python", "controllers.py"]