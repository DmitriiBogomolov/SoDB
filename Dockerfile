FROM python:3.8.5

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["sh", "-c", "python manage.py migrate & \
                  gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000"]
