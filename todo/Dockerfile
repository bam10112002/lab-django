# Используйте образ Python
FROM python:3.10

# Установите рабочую директорию в /app
WORKDIR /app

# Скопируйте файл requirements.txt в рабочую директорию контейнера
COPY requirements.txt /app/

# Установите зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте текущий каталог (включая файлы) в контейнер в /app
COPY . /app/

EXPOSE 8000
# Выполните миграции при создании контейнера
# RUN python3 manage.py makemigrations && python3 manage.py migrate

# Запустите Gunicorn при запуске контейнера
# CMD ["gunicorn", "todo.wsgi", "--bind", "0.0.0.0:8000", "--workers", "3"]
