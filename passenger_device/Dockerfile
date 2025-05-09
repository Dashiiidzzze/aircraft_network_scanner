# Образ с Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем их
RUN pip install --no-cache-dir -r requirements.txt

# Копируем клиентский код
COPY . .

# Запускаем клиентскую симуляцию
CMD ["python", "ife_client.py"]
