# takollama

This directory contains Dockerfiles for **takollama**, a Python application packaged with `uv`.

## What is takollama?

The Dockerfile does not state what the application does, so this section describes only what the image contains. It is built on `debian:bookworm-slim` with:

- `curl`, `ca-certificates`, `bzip2`, Python 3, `python3-venv`, `python3-pip` and `build-essential`
- `uv`, installed from `https://astral.sh/uv/install.sh` into `/root/.local/bin`
- the application source, downloaded as `takollama.tar.bz2` and unpacked into `/app`
- `uv sync --locked`, run in `/app/ai` to install the application's dependencies

Source of the application tarball: https://github.com/DNALinux/ai

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/takollama/general

- **`dnalinux/takollama:0.1-uv`** — the image described above. `linux/amd64` only.

## Building the image

```bash
cd 0.1-uv
docker build -t dnalinux/takollama:0.1-uv .
```

The build downloads `takollama.tar.bz2` from the `FILE_URL` build argument (default `https://github.com/DNALinux/ai/releases/download/demo/takollama.tar.bz2`), so it needs network access.

## Smoke test

The Dockerfile declares no entry point and no version or help command, so there is no tool-specific version invocation to run. A container can be started to inspect the environment it builds:

```bash
docker run -it --rm dnalinux/takollama:0.1-uv bash -c 'uv --version && ls /app/ai'
```

## License

The Dockerfile declares no license.
