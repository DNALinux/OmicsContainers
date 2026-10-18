# bedtools

This directory contains Dockerfiles for **bedtools**, a suite of utilities for comparing genomic features.

## What is bedtools?

**bedtools** (https://github.com/arq5x/bedtools2) is a suite of command-line utilities for genome arithmetic: intersecting, merging, complementing, subtracting, grouping and otherwise comparing genomic intervals and the annotated features that overlap them. The suite is available both through the `bedtools <subcommand>` front end and as the individual `*Bed` commands.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bedtools/general

- **`dnalinux/bedtools:latest`** — currently points to `2.31.1-dfsg-2-deb`
- **`dnalinux/bedtools:2.31.1-dfsg-2-deb`** — bedtools 2.31.1 installed from the Debian package (`bedtools=2.31.1+dfsg-2`) on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

The directory `2.31.1+dfsg-2-deb` builds the Docker Hub tag `2.31.1-dfsg-2-deb`; Docker Hub normalises the `+` out of tag names.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 2.31.1+dfsg-2-deb
docker build -t bedtools:2.31.1-dfsg-2-deb .
```

## Smoke test

```bash
docker run -it --rm dnalinux/bedtools:2.31.1-dfsg-2-deb bedtools --version
docker run -it --rm dnalinux/bedtools:2.31.1-dfsg-2-deb bedtools --help
```

## License

bedtools is released under the MIT license (the Dockerfile records `about.license="MIT"` and points to `/usr/share/doc/bedtools/copyright`).
