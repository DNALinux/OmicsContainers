# Python (free-threaded, no GIL)

This directory contains Dockerfiles for **free-threaded CPython** builds, published as `dnalinux/pythonnogil`.

## What are these images?

These images are plain **CPython interpreters**, not bioinformatics tools. They are the free-threaded ("no GIL") builds of Python, in which the Global Interpreter Lock can be disabled so that threads run truly in parallel. The interpreters come from the pre-compiled standalone builds published by `astral-sh`:

https://github.com/astral-sh/python-build-standalone

The Dockerfiles compile nothing: each downloads the `freethreaded+pgo+lto` release for the target architecture, unpacks it under `/opt/python/install`, and adds `/opt/python/install/bin` to `PATH`. The build context is copied into `/scripts`, which is also the working directory.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/pythonnogil/general

- **`dnalinux/pythonnogil:latest`** — recommended; currently points to `3.14.8`
- **`dnalinux/pythonnogil:3.14.8`** — free-threaded CPython **3.14.8** (standalone release `20261013`) on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`); the Dockerfile fails the build on any other architecture.
- **`dnalinux/pythonnogil:3.13.1`** — free-threaded CPython **3.13.1** (standalone release `20250115`) on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`); the Dockerfile fails the build on any other architecture.

## Building an image

```bash
cd 3.14.8-no_GIL
docker build -t dnalinux/pythonnogil:3.14.8 .
```

Or, for the previous release:

```bash
cd 3.13.1-no_GIL
docker build -t dnalinux/pythonnogil:3.13.1 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/pythonnogil:3.14.8 python3 --version
```

The included test script checks that the interpreter can run threads without the GIL:

```bash
docker run -it --rm dnalinux/pythonnogil:3.14.8 python3 -X gil=0 /scripts/test_disablegil.py
```

## License

Python is released under the Python Software Foundation License (PSL). The Dockerfile `LABEL` records `about.license="PSL"`.
