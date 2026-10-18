# Biopython

This directory contains Dockerfiles for **Biopython**, a Python library for bioinformatics.

## What is Biopython?

**Biopython** (https://biopython.org/) is a set of freely available Python tools for biological computation: sequence parsing and manipulation, access to online biological databases, alignment handling, phylogenetics, structural biology and more.

## Available images

The images are already published to Docker Hub, so in most cases you can simply pull the one you need:

```bash
docker pull dnalinux/biopython:1.88-pip
```

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/biopython/general

- **`dnalinux/biopython:latest`** — currently points to `1.88-pip`
- **`dnalinux/biopython:1.88-pip`** — Biopython 1.88 installed with `pip` into a virtual environment at `/biopython` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/biopython:1.87-pip`** — Biopython 1.87 installed with `pip` into a virtual environment at `/biopython` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/biopython:1.85-pip`** — Biopython 1.85 in a virtual environment at `/biopython` on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/biopython:1.84-pip`** — Biopython 1.84 in a virtual environment at `/biopython` on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

If you prefer to build the image yourself instead of pulling it, give it a local tag of your choosing. The `dnalinux/` prefix identifies the images published by the DNALinux project and is not needed for a local build:

```bash
cd 1.88-pip
docker build -t biopython:1.88-pip .
```

## Smoke test

Biopython is a library rather than a command, and it is installed in a virtual environment, so call that environment's interpreter. Use the image name you have locally, either the pulled `dnalinux/biopython:1.88-pip` or your own `biopython:1.88-pip`:

```bash
docker run -it --rm biopython:1.88-pip /biopython/bin/python -c 'import Bio; print(Bio.__version__)'
```

## License

Biopython is distributed under the Biopython License Agreement. The Dockerfile records `about.license="other"` and points to `/usr/share/doc/biopython/copyright`.
