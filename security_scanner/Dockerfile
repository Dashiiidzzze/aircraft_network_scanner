# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /scanner

# Копируем файл зависимостей
#COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код сканера
COPY . .

# Запускаем сканер
CMD ["python", "scanner.py"]
