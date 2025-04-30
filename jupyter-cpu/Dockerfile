FROM quay.io/jupyter/scipy-notebook:2025-04-30

USER root
# Generally, Dev Container Features assume that the non-root user (in this case jovyan)
# is in a group with the same name (in this case jovyan). So we must first make that so.

RUN apt-get update -y
RUN apt-get upgrade -y


RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.7.29/quarto-1.7.29-linux-amd64.deb
RUN dpkg -i quarto-1.7.29-linux-amd64.deb
RUN apt-get install -f
RUN rm quarto-1.7.29-linux-amd64.deb
RUN apt-get install lmodern -y
RUN apt-get install texlive-fonts-recommended texlive-fonts-extra -y


RUN quarto install tinytex 
run tlmgr init-usertree

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN groupadd jovyan \
    && usermod -g jovyan -a -G users jovyan

USER jovyan