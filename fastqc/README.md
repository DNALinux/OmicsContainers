# FastQC

This directory contains a Dockerfile for **FastQC**, a quality control tool for high throughput sequence data.

## What is FastQC?

**FastQC** provides quality control for high throughput sequence data: it reads one or more sequence files and writes a report on the quality of the raw reads. Upstream: http://www.bioinformatics.babraham.ac.uk/projects/fastqc/

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/fastqc/general

- **`dnalinux/fastqc:latest`** — currently points to `0.12.1-deb`
- **`dnalinux/fastqc:0.12.1-deb`** — FastQC **0.12.1** (Debian package version `0.12.1+dfsg-4`), installed from the Debian package `fastqc` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`. Built from the `0.12.1+dfsg-3-deb` directory.
- **`dnalinux/fastqc:0.12.1`** — an older FastQC 0.12.1 image (2024-08-30) that has no matching directory in this repository.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 0.12.1+dfsg-3-deb
docker build -t fastqc:0.12.1-deb .
```

## Smoke test

```bash
docker run -it --rm dnalinux/fastqc:0.12.1-deb fastqc --version
```

## Notes on the version names

The names of the directory, the Debian package and the Docker Hub tag do not agree:

- the directory is `0.12.1+dfsg-3-deb`, but the Dockerfile installs `fastqc=0.12.1+dfsg-4` (the package version currently in the Debian repositories);
- the Dockerfile's `software.version` LABEL says `0.12.1dfsg-4-deb`;
- the published tag is `0.12.1-deb`.

## License

FastQC is released under the GPL-3.0-or-later license (Dockerfile `about.license` LABEL, written as `GPL-3.0+`), with `about.license_file` at `/usr/share/doc/fastqc/copyright`.
