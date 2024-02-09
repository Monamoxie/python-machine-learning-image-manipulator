FROM python:3.12.1-bullseye

RUN apt-get clean && \
    apt-get update \
    && apt-get clean install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV QT_QPA_PLATFORM minimal
ENV QT_PLUGIN_PATH .
ENV QT_QPA_PLATFORM_PLUGIN_PATH ""

WORKDIR /app

COPY requirements.txt ./app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./app/requirements.txt

COPY . /app/

# RUN python manage.py collectstatic --noinput
