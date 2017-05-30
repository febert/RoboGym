FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

# Prevent keyboard-configuration from requiring input
RUN echo "XKBMODEL=\"pc104\"" >> /etc/default/keyboard
RUN echo "XKBLAYOUT=\"us\"" >> /etc/default/keyboard

RUN apt-get update -q \
    && apt-get install -y \
    curl \
    git \
    meshlab \
    vim \
    xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN echo 'Xvfb :100 & && export DISPLAY=:100.0' > /etc/profile.d/.bash.sh
RUN Xvfb :100 &
RUN export DISPLAY=:100.0

RUN git clone https://github.com/kmammou/v-hacd.git /opt/v-hacd
RUN mkdir -p /opt/v-hacd/bin/ubuntu && \
    cd /opt/v-hacd/bin/ubuntu && \
    git checkout bb547c87190a92c73287988801256624fca7c6f5 testVHACD && \
    cd -
ENV VHACD_PATH=/opt/v-hacd/bin/ubuntu/testVHACD


ENV PATH $PATH:/gpr/bin

WORKDIR /meshes
COPY . /meshes