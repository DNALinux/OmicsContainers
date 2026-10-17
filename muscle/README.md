# MUSCLE

This directory contains a Dockerfile for **MUSCLE**, a multiple alignment program for protein sequences.

## What is MUSCLE?

**MUSCLE** produces multiple sequence alignments of protein (amino-acid) sequences.

- Project page: http://www.drive5.com/muscle/

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/muscle/general

- **`dnalinux/muscle:latest`** — MUSCLE 5.1.0 installed from the Debian package `muscle=1:5.1.0-1` on `debian:trixie-slim`. `linux/amd64` only.

The version directory in this repository is `5.1.0-1-deb`. No version tag is published for it — the only tag on Docker Hub is `latest`.

## Building the image

```bash
cd 5.1.0-1-deb
docker build -t dnalinux/muscle:latest .
```

## Smoke test

```bash
docker run -it --rm dnalinux/muscle:latest muscle -version
```

## License

MUSCLE is dedicated to the public domain (PD-dedication), as stated in the image `LABEL` metadata and `/usr/share/doc/muscle/copyright`.
