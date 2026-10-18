# GATK

This directory contains Dockerfiles for **GATK**, the Broad Institute's toolkit for variant discovery in high-throughput sequencing data.

## What is GATK?

**GATK** (the Genome Analysis Toolkit) is a software package developed at the Broad Institute to analyse high-throughput sequencing data. Its main use is variant discovery: local re-assembly of haplotypes, genotyping, and the filtering and evaluation of variant calls. The command-line program is `gatk`.

- Source code: https://github.com/broadinstitute/gatk

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/gatk/general

- **`dnalinux/gatk:latest`** — recommended; currently points to `4.6.1.0`
- **`dnalinux/gatk:4.6.1.0`** — GATK 4.6.1.0 installed from bioconda (`gatk4=4.6.1.0`) with Miniconda on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/gatk:4.5.0.0`** — GATK 4.5.0.0 installed from bioconda (`gatk4=4.5.0.0`) with Miniconda on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Note on the 4.6.0.0 directory

`4.6.0.0` is a from-source build rather than a conda install: it starts from the upstream GATK build image (`broadinstitute/gatk:gatkbase-3.3.0`), builds the toolkit with Gradle, and copies the resulting bundle into the final image. It is **not** published on Docker Hub — the two conda images above are the ones to use.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 4.6.1.0
docker build -t gatk:4.6.1.0 .
```

Both conda Dockerfiles take the version as a build argument (`software_version`), and download the Miniconda installer matching the build machine's architecture (`x86_64` or `aarch64`); any other architecture aborts the build.

## Smoke test

```bash
docker run -it --rm dnalinux/gatk:4.6.1.0 gatk --version
docker run -it --rm dnalinux/gatk:4.6.1.0 gatk --help
```

## License

GATK is licensed under the Apache License 2.0 — Copyright 2021 Broad Institute, Inc. (upstream `LICENSE.TXT`).
