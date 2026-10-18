# Clustal Omega

This directory contains Dockerfiles for **Clustal Omega**, a tool for making accurate alignments of many protein sequences.

## What is Clustal Omega?

**Clustal Omega** is a multiple sequence alignment program that makes accurate alignments of many protein sequences. Upstream: http://www.clustal.org/omega/

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/clustalo/general

- **`dnalinux/clustalo:latest`** — currently points to `1.2.4-8-deb`
- **`dnalinux/clustalo:1.2.4-8-deb`** — Clustal Omega **1.2.4**, installed from the Debian package `clustalo=1.2.4-8` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`. Built from the `1.2.4-deb` directory.

Only the Debian build is published: there is no tag on Docker Hub for the conda build.

## The two version directories

- **`1.2.4-deb`** — the published one. Uses the Debian binary package, so the image contains Clustal Omega plus its Debian dependencies.
- **`1.2.4-conda`** — installs `clustalo==1.2.4` from the conda-forge and bioconda channels on `continuumio/miniconda3`. It has no Docker Hub tag. The Dockerfile comment notes that the conda build has binaries for AMD64 and ARM v8, while the Debian build also carries ARM v7 (Raspberry Pi).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 1.2.4-deb
docker build -t clustalo:1.2.4-8-deb .
```

## Smoke test

```bash
docker run -it --rm dnalinux/clustalo:1.2.4-8-deb clustalo --version
```

## License

Clustal Omega is released under the GPL-3.0 license (Dockerfile `about.license` LABEL).
