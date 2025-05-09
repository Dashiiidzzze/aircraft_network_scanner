# Используем минимальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем библиотеки Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Открываем порт 8080 — на нем будет доступен контент
EXPOSE 8080

# Запускаем основной скрипт
CMD ["python", "ife_server.py"]