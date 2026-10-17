# Jellyfish

This directory contains Dockerfiles for **Jellyfish**, a tool for fast, memory-efficient counting of k-mers in DNA.

## What is Jellyfish?

**Jellyfish** is a command-line program for counting k-mers in DNA sequences. It reads FASTA and multi-FASTA files and writes the k-mer counts in a binary format, which is read back with `jellyfish dump` and queried with `jellyfish query`.

- Source code: https://github.com/gmarcais/Jellyfish

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/jellyfish/general

- **`dnalinux/jellyfish:latest`** — currently points to `2.3.1-4`
- **`dnalinux/jellyfish:2.3.1-4`** — Jellyfish 2.3.1 installed from the Debian package `jellyfish=2.3.1-4` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

```bash
cd 2.3.1-4
docker build -t dnalinux/jellyfish:2.3.1-4 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/jellyfish:2.3.1-4 jellyfish --version
```

## License

Jellyfish is dual-licensed: 3-Clause BSD or GPL 3.0 (per the image `LABEL` metadata and `/usr/share/doc/jellyfish/copyright`).
