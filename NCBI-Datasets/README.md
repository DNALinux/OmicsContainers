# NCBI Datasets

This directory contains a Dockerfile for the **NCBI Datasets** command-line tool, which gathers sequence, annotation and metadata from across NCBI databases.

## What is NCBI Datasets?

**NCBI Datasets** is a resource that lets you easily gather data from across NCBI databases (https://www.ncbi.nlm.nih.gov/datasets/docs/v2/getting_started/). The `datasets` command-line tool downloads gene, genome, taxonomy and virus data as data packages. The comment at the end of the Dockerfile gives this example:

```bash
datasets download genome taxon "Escherichia coli" --filename /ftmp/ecoli_dataset.zip
```

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/ncbi-datasets/general

- **`dnalinux/ncbi-datasets:latest`** — recommended; currently points to `18.18.0`
- **`dnalinux/ncbi-datasets:18.18.0`** — the `datasets` 18.18.0 executable downloaded from the NCBI FTP server at build time on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd datasets/18.18.0
docker build -t ncbi-datasets:18.18.0 .
```

The Dockerfile picks the pre-compiled binary with `uname -m`: `linux-amd64` on x86_64 and `linux-arm64` on aarch64 (a 32-bit `linux-arm` build is also handled, for armv7l and armv6l).

## Smoke test

```bash
docker run -it --rm dnalinux/ncbi-datasets:18.18.0 /datasets --version
```

The `datasets` executable is downloaded into `/`, so it has to be called by its full path.

## License

Public domain. The Dockerfile `LABEL` records `about.license="PD"`, copyright NCBI.
