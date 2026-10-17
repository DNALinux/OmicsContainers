# fastp

This directory contains Dockerfiles for **fastp**, an ultra-fast all-in-one FASTQ preprocessor.

## What is fastp?

**fastp** is a preprocessor for FASTQ files: it performs quality control and read filtering in a single pass and writes an HTML/JSON report alongside the processed reads. Upstream: https://github.com/OpenGene/fastp

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/fastp/general

- **`dnalinux/fastp:latest`** — currently points to `1.3.3-conda`
- **`dnalinux/fastp:1.3.3-conda`** — fastp **1.3.3** installed from bioconda into a Miniconda installation at `/opt/miniconda3` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as the unprivileged user `dnalinux`, working directory `/home/dnalinux`.
- **`dnalinux/fastp:0.23.4`** — fastp **0.23.4** installed with conda from a Miniconda installation at `/root/miniconda3` on `debian:bookworm-slim`. Multi-arch, runs as `root`, working directory `/data`.

Notes:

- The `0.23.4` tag is built from the `0.23.4-conda` directory; the published tag drops the `-conda` suffix.
- Both Dockerfiles download the Miniconda installer for the machine's architecture (`x86_64` or `aarch64`) and fail the build on anything else, which is what makes the images work on both `linux/amd64` and `linux/arm64`.

## Building the image

```bash
cd 1.3.3-conda
docker build -t dnalinux/fastp:1.3.3-conda .
```

## Smoke test

```bash
docker run -it --rm dnalinux/fastp:1.3.3-conda fastp --version
docker run -it --rm dnalinux/fastp:0.23.4 fastp --version
```

## Usage

```bash
docker run -it --rm -v $(pwd):/home/dnalinux dnalinux/fastp:1.3.3-conda \
    fastp --in1 input.fastq --out1 output.fastq
```

## License

fastp is released under the MIT license (Dockerfile `about.license` LABEL in `1.3.3-conda`). The `0.23.4-conda` Dockerfile records only the software name and maintainer, with no license field.
