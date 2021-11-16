FROM python:3.8

WORKDIR /todoList
COPY requirements.txt /todoList//requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000