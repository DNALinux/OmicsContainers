# QUAST

This directory contains a Dockerfile for **QUAST**, a tool that evaluates genome assemblies by computing various metrics.

## What is QUAST?

**QUAST** stands for QUality ASsessment Tool. The tool evaluates genome assemblies by computing various metrics.

- Home page and documentation: https://quast.sourceforge.net/

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/quast/general

- **`dnalinux/quast:latest`** — recommended; currently points to `5.3.0`
- **`dnalinux/quast:5.3.0`** — QUAST 5.3.0 built from the upstream source release `quast-5.3.0.tar.gz` on `debian:bookworm-slim`. `linux/amd64` only.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 5.3.0-source
docker build -t quast:5.3.0 .
```

The Dockerfile installs the build and runtime dependencies from Debian (`g++`, `make`, `libboost-all-dev`, Python 3 with `pip` and `venv`, `python3-matplotlib` with the freetype and libpng headers, a JDK and Perl), unpacks the source into `/quast-5.3.0`, and runs `python3 setup.py install_full` there.

## Smoke test

```bash
docker run -it --rm dnalinux/quast:5.3.0 quast.py --version
docker run -it --rm dnalinux/quast:5.3.0 quast.py --help
```

## License

GPL v2. The Dockerfile `LABEL` records `about.license="GPL v2"`.
