FROM quay.io/jupyter/scipy-notebook:latest

USER root
# Generally, Dev Container Features assume that the non-root user (in this case jovyan)
# is in a group with the same name (in this case jovyan). So we must first make that so.

RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.6.40/quarto-1.6.40-linux-amd64.deb

RUN dpkg -i quarto-1.6.40-linux-amd64.deb
RUN apt-get install -f
RUN rm quarto-1.6.40-linux-amd64.deb
RUN apt-get install lmodern -y

RUN groupadd jovyan \
    && usermod -g jovyan -a -G users jovyan

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

USER jovyan