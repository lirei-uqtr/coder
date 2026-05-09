###############################################################################
# Base image: Jupyter SciPy Notebook (highly optimized for Data Science)
FROM quay.io/jupyter/scipy-notebook:2025-04-30

###############################################################################
# ---- 1. OS packages & User Setup --------------------------------------------
USER root

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
      wget curl xz-utils sudo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Coder/DevContainers often assume the user has a primary group with their name.
# Jupyter default sets primary group to `users` (100). We fix that and give sudo.
RUN groupadd jovyan || true \
    && usermod -g jovyan -a -G users jovyan \
    && echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

###############################################################################
# ---- 2. Quarto for Data Science Publishing ----------------------------------
RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.7.29/quarto-1.7.29-linux-amd64.deb && \
    dpkg -i quarto-1.7.29-linux-amd64.deb || true && \
    apt-get -fy install && \
    rm quarto-1.7.29-linux-amd64.deb

###############################################################################
# ---- 3. User Tools (uv) -----------------------------------------------------
USER jovyan

# Install 'uv' for lightning-fast python package management
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/jovyan/.local/bin:/home/jovyan/.cargo/bin:${PATH}"

###############################################################################
# ---- 4. Done ----------------------------------------------------------------
WORKDIR /home/jovyan
