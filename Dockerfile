FROM python:3.12.1-bullseye

RUN apt-get clean && \
    apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing \
    && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender1 \
        build-essential binutils \
        ca-certificates cmake cmake-qt-gui curl \
        dbus-x11 \
        ffmpeg \
        gdb gcc g++ gfortran git \
        tar \
        lsb-release \
        procps \
        manpages-dev \
        unzip \
        zip \
        wget \
        xauth \
        swig \
        libboost-python-dev libboost-thread-dev libatlas-base-dev libavcodec-dev \
        libavformat-dev libavutil-dev libcanberra-gtk3-module libeigen3-dev \
        libglew-dev libgl1-mesa-dev libgtk2.0-dev \
        libgtk-3-dev libjpeg-dev liblapack-dev \
        liblapacke-dev libopenblas-dev libopencv-dev libpng-dev libpostproc-dev \
        libpq-dev libswscale-dev libtbb-dev libtbb2 libtesseract-dev \
        libtiff-dev libtiff5-dev libv4l-dev libx11-dev libxine2-dev \
        libxrender-dev libxvidcore-dev libx264-dev libgtkglext1 libgtkglext1-dev \
        libvtk9-dev libdc1394-dev libgstreamer-plugins-base1.0-dev \
        libgstreamer1.0-dev libopenexr-dev \
        openexr \
        pkg-config \
        qv4l2 \
        v4l-utils \
        zlib1g-dev \
        locales \
        && locale-gen en_US.UTF-8 \
        && LC_ALL=en_US.UTF-8 \
        && rm -rf /var/lib/apt/lists/* \
        && apt-get clean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV QT_QPA_PLATFORM minimal
# ENV QT_PLUGIN_PATH .
# ENV QT_QPA_PLATFORM_PLUGIN_PATH ""

WORKDIR /app

COPY requirements.txt ./app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./app/requirements.txt

COPY . /app/

# RUN python manage.py collectstatic --noinput
