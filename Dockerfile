#getting base image ubuntu 
FROM tensorflow/tensorflow:latest-gpu

#suppress user input when downloading required packages
ARG DEBIAN_FRONTEND=noninteractive

#set the working directory
WORKDIR '<your directory goes here>'
#commands
RUN apt-get update && apt-get install -y \
    libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev \
    libjpeg-dev libpng-dev libtiff-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev \
    libopenblas-dev libatlas-base-dev liblapack-dev gfortran \
    libhdf5-serial-dev \
    python3-dev python3-tk python-imaging-tk \
    libgtk-3-dev wget\
    vim
RUN apt-get update 
RUN pip install opencv-contrib-python \
    scikit-image \
    pillow \
    imutils \
    scikit-learn \
    matplotlib \
    progressbar2 \
    beautifulsoup4 \
    pandas \
    pyyaml h5py
