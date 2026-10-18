# SPAdes

This directory contains Dockerfiles for **SPAdes**, a genome assembler for single-cell and isolate data sets.

## What is SPAdes?

**SPAdes** (St. Petersburg genome assembler) is a genome assembler for single-cell and isolate sequencing data sets. Its command-line entry point is `spades.py`.

- Upstream: https://ablab.github.io/spades/
- Citation: Prjibelski A, Antipov D, Meleshko D, Lapidus A, Korobeynikov A (2020) *Using SPAdes de novo assembler*. Current Protocols in Bioinformatics 70(1): e102. https://doi.org/10.1002/cpbi.102

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/spades/general

- **`dnalinux/spades:latest`** — points to `4.2.0-src`
- **`dnalinux/spades:4.2.0-src`** — SPAdes 4.2.0 compiled from the release tarball with CMake on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/spades:4.0.0`** — SPAdes 4.0.0 compiled from the release tarball with CMake on `python:3.10.14-slim-bullseye`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 4.2.0-src
docker build -t spades:4.2.0-src .
```

Both Dockerfiles configure the build with `-DSPADES_USE_NCBISDK=ON -DSPADES_ENABLE_PROJECTS=all`. The `4.2.0-src` image additionally installs OpenMPI, Python 3 and `python3-dev`.

## Smoke test

```bash
docker run -it --rm dnalinux/spades:4.2.0-src spades.py --version
```

## License

SPAdes is released under the GPL-2+ license (the `about.license` field of the Dockerfile's LABEL block).
