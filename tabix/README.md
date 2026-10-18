# Tabix

This directory contains Dockerfiles for **Tabix**, a generic indexer for TAB-delimited genome position files.

## What is Tabix?

**Tabix** is a generic indexer for TAB-delimited genome position files. It is part of the HTSlib project, by Heng Li.

Upstream documentation: https://www.htslib.org/doc/tabix.html

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/tabix/general

- **`dnalinux/tabix:latest`** — points to `1.21-deb`
- **`dnalinux/tabix:1.21-deb`** — Tabix **1.21** installed from the Debian package `tabix=1.21+ds-1` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 1.21-deb
docker build -t tabix:1.21-deb .
```

## Smoke test

```bash
docker run -it --rm dnalinux/tabix:1.21-deb tabix --version
```

## License

Tabix is released under the GNU General Public License version 3 (GPL-3.0) (the `about.license` field of the Dockerfile's LABEL block).
