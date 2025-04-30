###############################################################################
# Base image
FROM quay.io/jupyter/scipy-notebook:2025-04-30

###############################################################################
# ---- 0. Versions & PATH -----------------------------------------------------
ARG TL_YEAR=2025
ENV PATH=/usr/local/texlive/${TL_YEAR}/bin/x86_64-linux:$PATH

###############################################################################
# ---- 1. OS packages (one layer) --------------------------------------------
USER root
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
      wget curl perl xz-utils fontconfig lmodern \
      # extra fonts that LaTeX docs often need
      texlive-fonts-recommended texlive-fonts-extra && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

###############################################################################
# ---- 2. TeX Live 2025 (vanilla) --------------------------------------------
RUN wget -qO- https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
    | tar -xz -C /tmp && \
    /tmp/install-tl-*/install-tl \
        --scheme=small \
        --texdir=/usr/local/texlive/${TL_YEAR} \
        --no-interaction && \
    rm -rf /tmp/install-tl-*

# essential LaTeX packages you usually miss
RUN tlmgr install \
        latexmk      \
        biblatex     \
        biber        \
        makeindex    \
        # optional but handy
        pdfcrop      \
        collection-fontsrecommended

###############################################################################
# ---- 3. Quarto (optional) ---------------------------------------------------
RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.7.29/quarto-1.7.29-linux-amd64.deb && \
    dpkg -i quarto-1.7.29-linux-amd64.deb || true && \
    apt-get -fy install && \
    rm quarto-1.7.29-linux-amd64.deb

# If you **do** want TinyTeX for Quarto’s caching, install it under jovyan:
RUN chown -R jovyan:users /usr/local/texlive/2025
USER jovyan
# comment these two lines out if you’re happy with TeX Live 2025 only
RUN quarto install tinytex --no-prompt --quiet
RUN tlmgr init-usertree   # MUST be capitals: RUN, not run

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

###############################################################################
# ---- 4. Back to default, done ----------------------------------------------
USER jovyan
