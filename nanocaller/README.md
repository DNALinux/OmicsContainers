# NanoCaller

This directory contains Dockerfiles for **NanoCaller**, a variant calling tool for long-read sequencing data.

## What is NanoCaller?

**NanoCaller** calls single-nucleotide variants and insertions/deletions from long-read sequencing data. It uses a deep convolutional neural network together with read phasing and local realignment, and takes an aligned BAM/CRAM file and a reference genome as input, writing VCF output.

- Source code: https://github.com/WGLab/NanoCaller

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/nanocaller/general

- **`dnalinux/nanocaller:latest`** — currently points to `3.6.1`
- **`dnalinux/nanocaller:3.6.1`** — NanoCaller 3.6.1, installed into a conda environment created from the NanoCaller `environment.yml` on `continuumio/miniconda3`. `linux/amd64` only.
- **`dnalinux/nanocaller:3.6.0`** — NanoCaller 3.6.0, installed the same way. `linux/amd64` only.

## Building the image

```bash
cd 3.6.1
docker build -t dnalinux/nanocaller:3.6.1 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/nanocaller:3.6.1 NanoCaller --help
```

## License

NanoCaller is released under the MIT license, as stated in its upstream repository.
