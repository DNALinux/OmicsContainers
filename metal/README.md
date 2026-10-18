# METAL

This directory contains a Dockerfile for **METAL**, a program for the meta-analysis of large datasets such as several whole-genome association scans.

## What is METAL?

**METAL** (Meta Analysis) combines the results of multiple genome-wide association studies. It can combine test statistics and standard errors, or p-values and direction of effect, across studies, and reports per-marker summary statistics and between-study heterogeneity. It is driven interactively or by a script file of commands (`PROCESS`, `ANALYZE`, `QUIT`).

- Project page: https://csg.sph.umich.edu/abecasis/Metal/index.html

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/metal/general

- **`dnalinux/metal:latest`** — currently points to `2011-03-25`
- **`dnalinux/metal:2011-03-25`** — METAL 2011-03-25, compiled with `make` from the `generic-metal-2011-03-25` source tarball distributed by the University of Michigan on `debian:bullseye-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 2011-03-25
docker build -t metal:2011-03-25 .
```

## Smoke test

METAL has no version or help command-line flag; it is driven interactively or by a script file, and the `HELP` command lists its available commands, for example:

```bash
docker run --rm -i dnalinux/metal:2011-03-25 bash -c 'echo HELP | metal'
```

## License

GPL-3 (per the image `LABEL` metadata).
