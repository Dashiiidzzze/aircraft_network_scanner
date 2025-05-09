# Базовый образ Python с необходимыми утилитами
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY . .

# Открываем порт 5000 для HTTP API
EXPOSE 5000

# Запускаем сервер
CMD ["python", "maintenance_api.py"]
