#!/bin/bash

# Allow X Server connections
xhost +local:docker

# Set X Server socket and Xauth file paths
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth

# Create Xauth file
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

# Start your Django application
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Revert X Server permissions
xhost -local:docker
