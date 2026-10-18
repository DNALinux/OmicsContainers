# SRA Toolkit

This directory contains Dockerfiles for the **NCBI SRA Toolkit**, the utilities for the NCBI Sequence Read Archive.

## What is the SRA Toolkit?

The **SRA Toolkit** provides NCBI's command-line utilities for the Sequence Read Archive (SRA).

Upstream: https://github.com/ncbi/sra-tools

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/sra-toolkit/general

- **`dnalinux/sra-toolkit:latest`** — points to `3.4.1-bin`
- **`dnalinux/sra-toolkit:3.4.1-bin`** — SRA Toolkit **3.4.1** from NCBI's pre-compiled `sratoolkit.3.4.1-ubuntu64` tarball, unpacked under `/opt/sratoolkit` and added to `PATH`, on `debian:trixie-slim`. `linux/amd64` only.
- **`dnalinux/sra-toolkit:3.2.1-deb`** — SRA Toolkit **3.2.1+dfsg-4** installed from the Debian package `sra-toolkit` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

Both images run as the unprivileged user `dnalinux`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 3.4.1-bin
docker build -t sra-toolkit:3.4.1-bin .
```

## Smoke test

```bash
docker run -it --rm dnalinux/sra-toolkit:3.4.1-bin fastq-dump --version
docker run -it --rm dnalinux/sra-toolkit:3.2.1-deb fastq-dump --version
```

## License

The SRA Toolkit is in the public domain (the `about.license` field of the Dockerfile's LABEL block). The Debian package's copyright file is installed at `/usr/share/doc/sra-toolkit/copyright`.
