# Python (free-threaded, no GIL)

This directory contains a Dockerfile for a **free-threaded CPython 3.13.1** build, published as `dnalinux/pythonnogil`.

## What is this image?

This image is a plain **CPython interpreter**, not a bioinformatics tool. It is the free-threaded ("no GIL") build of Python 3.13.1, in which the Global Interpreter Lock can be disabled so that threads run truly in parallel. The interpreter comes from the pre-compiled standalone builds published by `astral-sh`:

https://github.com/astral-sh/python-build-standalone

The Dockerfile compiles nothing: it downloads the `freethreaded+pgo+lto` release dated `20250115`, unpacks it under `/opt/python/install`, and adds `/opt/python/install/bin` to `PATH`. The build context is copied into `/scripts`, which is also the working directory.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/pythonnogil/general

- **`dnalinux/pythonnogil:latest`** — recommended; currently points to `3.13.1`
- **`dnalinux/pythonnogil:3.13.1`** — free-threaded CPython 3.13.1 on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`); the Dockerfile picks the `x86_64` or `aarch64` asset from `uname -m` and fails the build on any other architecture.

## Building the image

```bash
cd 3.13.1-no_GIL
docker build -t dnalinux/pythonnogil:3.13.1 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/pythonnogil:3.13.1 python3 --version
```

## License

Python is released under the Python Software Foundation License (PSL). The Dockerfile `LABEL` records `about.license="PSL"`.
