FROM pytorch/pytorch:2.2.2-cuda11.8-cudnn8-runtime

USER root

# Install required tools for Coder
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y curl sudo \
    && rm -rf /var/lib/apt/lists/*

# Create jovyan user or rename ubuntu user to jovyan if it exists
RUN if id -u ubuntu >/dev/null 2>&1; then \
        usermod -l jovyan -d /home/jovyan -m ubuntu && groupmod -n jovyan ubuntu; \
    else \
        useradd -m -s /bin/bash -u 1000 jovyan; \
    fi \
    && echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && chown -R jovyan:users /opt/conda || true

USER jovyan
ENV HOME=/home/jovyan
WORKDIR /home/jovyan

# Install 'uv' for lightning-fast python package management
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/jovyan/.local/bin:/home/jovyan/.cargo/bin:${PATH}"