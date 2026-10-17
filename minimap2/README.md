# minimap2

This directory contains Dockerfiles for **minimap2**, a versatile pairwise aligner for genomic and spliced nucleotide sequences.

## What is minimap2?

**minimap2** is a pairwise aligner for nucleotide sequences. It maps long reads (PacBio and Oxford Nanopore) to a reference and supports spliced alignment of cDNA/RNA to a genome, among other presets.

- Source code: https://github.com/lh3/minimap2

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/minimap2/general

- **`dnalinux/minimap2:latest`** — currently points to `2.30-src`
- **`dnalinux/minimap2:2.30-src`** — minimap2 2.30 compiled from the v2.30 source tarball in a build stage on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/minimap2:2.27-deb`** — minimap2 2.27 installed from the Debian package on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

Both images set `ENTRYPOINT ["minimap2"]`, so the first argument after the image name is passed to minimap2.

## Building the image

```bash
cd 2.30-src
docker build -t dnalinux/minimap2:2.30-src .
```

## Smoke test

```bash
docker run -it --rm dnalinux/minimap2:2.30-src --version
```

## License

minimap2 is released under the MIT license (per the image `LABEL` metadata).
