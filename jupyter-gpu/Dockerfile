FROM pytorch/pytorch:2.2.2-cuda11.8-cudnn8-runtime

USER root

# Install required tools for Coder
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y curl sudo \
    && rm -rf /var/lib/apt/lists/*

# Rename ubuntu user to jovyan and change home directory
RUN usermod -l jovyan -d /home/jovyan -m ubuntu \
    && groupmod -n jovyan ubuntu \
    && echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER jovyan
WORKDIR /home/jovyan