# Используем легкий образ Python как базу
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY . .

# Открываем порт 80 для HTTP
EXPOSE 80

# Запускаем сервер
CMD ["python", "pilot_interface.py"]
