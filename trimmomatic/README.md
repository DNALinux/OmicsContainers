# Trimmomatic

This directory contains Dockerfiles for **Trimmomatic**, a flexible read trimming tool for Illumina NGS data.

## What is Trimmomatic?

**Trimmomatic** performs a variety of trimming tasks on Illumina paired-end and single-end reads. The Debian package used here provides the `TrimmomaticPE` and `TrimmomaticSE` commands.

Upstream: http://www.usadellab.org/cms/index.php?page=trimmomatic

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/trimmomatic/general

- **`dnalinux/trimmomatic:0.39`** — Trimmomatic **0.39+dfsg-2** installed from the Debian package `trimmomatic` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

```bash
cd 0.39dfsg-2-deb
docker build -t dnalinux/trimmomatic:0.39 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/trimmomatic:0.39 TrimmomaticPE -version
```

## Data files

The Debian package places its data files in `/usr/share/trimmomatic/`.

## License

Trimmomatic is released under the GPL-3+ license (the `about.license` field of the Dockerfile's LABEL block).
