# pull base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Iet work directory ls
WORKDIR /app
RUN apt-get update && apt-get install -y netcat

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD gunicorn --bind 0.0.0.0:8080 --workers 5 --timeout 60 dj_backend.wsgi
