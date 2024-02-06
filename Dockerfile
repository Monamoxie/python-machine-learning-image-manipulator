FROM python:3.12.1-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./app/

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r ./app/requirements.txt
RUN pip install python-decouple

COPY . /app/

# RUN python manage.py collectstatic --noinput
