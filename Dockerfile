FROM python:3.12.2-bookworm

RUN apt-get update \
    && apt-get install -y \
        libgl1-mesa-glx \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        libqt5widgets5 \
        bzip2 \
        g++ \
        git \
        graphviz \
        libhdf5-dev \
        openmpi-bin \
        wget \
        python3-tk \
    && rm -rf /var/lib/apt/lists/*


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ENV QT_QPA_PLATFORM minimal

ENV QT_QPA_PLATFORM_PLUGIN_PATH=/app/venv/lib/python3.12/site-packages/cv2/qt/plugins/platforms


WORKDIR /app
COPY . /app/
COPY requirements.txt ./app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./app/requirements.txt


ENV QT_X11_NO_MITSHM=1
