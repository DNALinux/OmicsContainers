# DIPY

This directory contains a Dockerfile for **DIPY**, a Python package for analyzing diffusion MRI data.

## What is DIPY?

**DIPY** is a Python package for analyzing diffusion MRI data. Upstream: https://dipy.org/

It is a library rather than a command-line program: the image installs it into a Python virtual environment, and it is used through that interpreter.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/dipy/general

- **`dnalinux/dipy:latest`** — currently points to `1.10.0`
- **`dnalinux/dipy:1.10.0`** — DIPY **1.10** installed with pip into a virtual environment at `/dipy` on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`. Built from the `1.10` directory.

The install differs per architecture, because the Dockerfile branches on the BuildKit `TARGETARCH` argument:

| Architecture | Install command |
|---|---|
| `amd64` | `pip install dipy[all]==1.10 fury` |
| `arm64` | `pip install dipy==1.10` |

The build exits with an error for any other `TARGETARCH`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

The Dockerfile branches on `TARGETARCH`, so the build needs BuildKit (the default in current Docker) or Buildx:

```bash
cd 1.10
docker build -t dipy:1.10.0 .
```

To build and push both architectures at once with Buildx:

```bash
cd 1.10
docker buildx build --platform linux/amd64,linux/arm64 \
    -t dnalinux/dipy:1.10.0 --push .
```

## Smoke test

The Dockerfile sets no `CMD` or `ENTRYPOINT`; DIPY is reached through the virtual environment's interpreter:

```bash
docker run -it --rm dnalinux/dipy:1.10.0 /dipy/bin/python -c "import dipy; print(dipy.__version__)"
```

## License

The Dockerfile LABEL records the license as `other`, with `about.license_file` at `/usr/share/doc/dipy/copyright`. DIPY itself is released under the BSD 3-Clause license (the DIPY `LICENSE` file).
