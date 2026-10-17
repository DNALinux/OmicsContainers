# Bowtie 2

This directory contains a Dockerfile for **Bowtie 2**, an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.

## What is Bowtie 2?

**Bowtie 2** aligns sequencing reads of roughly 50 to hundreds or thousands of bases against long reference sequences, including mammalian genomes. It uses an FM Index to keep memory use low (about 3.2 GB for the human genome) and supports gapped, local and paired-end alignment modes. Upstream: https://bowtie-bio.sourceforge.net/bowtie2/index.shtml

Please cite: Langmead B, Salzberg S. *Fast gapped-read alignment with Bowtie 2*. Nature Methods. 2012, 9:357-359.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bowtie2/general

- **`dnalinux/bowtie2:latest`** — currently points to `2.5.4`
- **`dnalinux/bowtie2:2.5.4`** — Bowtie 2 **2.5.4**, installed from the bioconda `bowtie2` package with `conda install` on top of `continuumio/miniconda3`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`.

## Building the image

```bash
cd 2.5.4
docker build -t dnalinux/bowtie2:2.5.4 .
```

The version is passed to the conda solver through the `software_version` build argument, which defaults to `2.5.4`.

## Smoke test

```bash
docker run -it --rm dnalinux/bowtie2:2.5.4 bowtie2 --version
```

The image's `CMD` is `/bin/sh`, so the binary name has to be given explicitly.

## License

Bowtie 2 is distributed under the GPLv3 license (stated in the Bowtie 2 manual). The Dockerfile records only the software name and maintainer, with no license field.
