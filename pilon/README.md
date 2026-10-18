# Pilon

This directory contains a Dockerfile for **Pilon**, an automated genome assembly improvement and variant detection tool.

## What is Pilon?

**Pilon** automatically improves draft genome assemblies and finds variation among strains, including large event detection. It takes a FASTA file of the genome together with one or more BAM files of reads aligned to that FASTA, identifies inconsistencies between the input genome and the evidence in the reads, and writes an improved FASTA plus an optional VCF file describing the variation.

- Home page and documentation: https://github.com/broadinstitute/pilon/wiki
- Copyright 2012-2017 Broad Institute, Inc.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/pilon/general

- **`dnalinux/pilon:latest`** — recommended; currently points to `1.24-3-deb`
- **`dnalinux/pilon:1.24-3-deb`** — the Debian package `pilon=1.24-3` (upstream Pilon 1.24) installed on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

The image is a plain Debian install, so the command is `/usr/bin/pilon`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 1.24-3-deb
docker build -t pilon:1.24-3-deb .
```

## Smoke test

```bash
docker run -it --rm dnalinux/pilon:1.24-3-deb pilon --version
docker run -it --rm dnalinux/pilon:1.24-3-deb pilon --help
```

## License

GPL-2. The Dockerfile `LABEL` records `about.license="GPL-2"`, copyright 2012-2017 Broad Institute, Inc.
