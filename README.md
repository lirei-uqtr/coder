# Lirei Coder Docker Images

This repository contains custom Docker images optimized for Data Science and Machine Learning workflows, designed specifically to be used as remote workspaces within [Coder](https://coder.com/).

These images are built and published automatically to the GitHub Container Registry (`ghcr.io`) via GitHub Actions.

## Available Images

### 1. PyTorch GPU (`jupyter-gpu/`)
An image highly optimized for Machine Learning and Deep Learning workloads with GPU acceleration.

- **Base Image:** `pytorch/pytorch:2.2.2-cuda11.8-cudnn8-runtime`
- **Features:**
  - Native CUDA support for older architectures like **Tesla P40** (compute capability `sm_61`) via CUDA 11.8.
  - Pre-configured `jovyan` user with passwordless `sudo` for Coder compatibility.
  - Ultra-fast Python package management with [`uv`](https://astral.sh/uv/).
- **Registry Tag:** `ghcr.io/lirei-uqtr/coder-pytorch:main`

### 2. SciPy CPU (`jupyter-cpu/`)
A lightweight, blazing-fast image tailored for pure Data Science, statistical analysis, and publishing.

- **Base Image:** `quay.io/jupyter/scipy-notebook:2025-04-30`
- **Features:**
  - Pre-loaded with the SciPy stack (Pandas, NumPy, SciPy, Scikit-Learn, and Matplotlib).
  - Includes [Quarto](https://quarto.org/) for interactive scientific reporting.
  - Stripped of heavy LaTeX dependencies for faster boot times and reduced image size.
  - Ultra-fast Python package management with [`uv`](https://astral.sh/uv/).
  - Pre-configured `jovyan` user with passwordless `sudo` for Coder compatibility.
- **Registry Tag:** `ghcr.io/lirei-uqtr/coder-scipy:main`

## Coder Integration (`jupyter-gpu/main.tf`)

The repository includes a Terraform template (`main.tf`) ready to be imported into Coder. It allows users to dynamically provision Kubernetes workspaces using these images, featuring:
- CPU allocation options from 2 up to **32 Cores**.
- Memory allocation options from 2 GB up to **256 GB RAM**.
- Dynamic GPU allocation (0 to 2 GPUs).

## CI/CD Pipeline

The images are automatically built and pushed to the GitHub Container Registry whenever a change is merged into the `main` branch. 
The GitHub Actions workflows are defined in the `.github/workflows/` directory:
- `build-pytorch.yml`
- `build-scipy.yml`

## Usage / Local Testing

You can build and test any of the images locally using Docker:

```bash
# Build the CPU image locally
cd jupyter-cpu
docker build -t local-jupyter-cpu .

# Test uv package manager inside the container
docker run --rm local-jupyter-cpu bash -c "uv pip install --system rich"
```
