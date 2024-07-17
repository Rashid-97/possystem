# Dockerfile
FROM python:3.9-slim

# Установка зависимостей
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev

# Установка рабочего каталога
WORKDIR /app

# Копирование файлов проекта
COPY . .

# Установка зависимостей через pip
RUN pip install --no-cache-dir -r requirements.txt

# Сборка статических файлов
RUN python manage.py collectstatic --noinput

# Запуск Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "possystem.wsgi:application"]
