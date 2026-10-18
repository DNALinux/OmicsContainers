# DIAMOND

This directory contains Dockerfiles for **DIAMOND**, a sequence aligner for protein and translated DNA searches.

## What is DIAMOND?

**DIAMOND** is an accelerated BLAST-compatible local sequence aligner, designed for high-performance analysis of big sequence data. Upstream: https://github.com/bbuchfink/diamond (documentation at http://www.diamondsearch.org).

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/diamond/general

- **`dnalinux/diamond:latest`** — currently points to `2.1.10`
- **`dnalinux/diamond:2.1.10`** — DIAMOND **2.1.10** (upstream build 2.1.10.164), installed by unpacking the pre-compiled `diamond-linux64.tar.gz` release archive from GitHub on `debian:trixie-slim`. `linux/amd64` only, runs as `root`. Built from the `2.1.10-bin` directory.
- **`dnalinux/diamond:2.1.9`** — DIAMOND **2.1.9-1** (upstream build 2.1.9.163), installed from the Debian package `diamond-aligner=2.1.9-1` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`, working directory `/data`. Built from the `2.1.9-debian` directory.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 2.1.10-bin
docker build -t diamond:2.1.10 .
```

## Smoke test

In the `2.1.9` image the `diamond` binary comes from the Debian package and is on `PATH`:

```bash
docker run -it --rm dnalinux/diamond:2.1.9 diamond --version
```

The `2.1.10` Dockerfile unpacks the archive into the image's working directory and does not put it on `PATH`, so the binary has to be called by path (the Dockerfile's own trailing comment says "run with ./diamond CMD"):

```bash
docker run -it --rm dnalinux/diamond:2.1.10 /diamond --version
```

## License

DIAMOND is released under the GPL-3.0 license (Dockerfile `about.license` LABEL). The `2.1.9-debian` Dockerfile also points `about.license_file` at `/usr/share/doc/diamond/copyright`.
