# Redundans

This directory contains Dockerfiles for **Redundans**, a pipeline that scaffolds heterozygous genome assemblies.

## What is Redundans?

**Redundans** assists the assembly of heterozygous genomes. It takes assembled contigs, sequencing libraries and/or a reference sequence as input and returns a scaffolded homozygous genome assembly. The final assembly is expected to be less fragmented and smaller than the input contigs, and Redundans also closes the gaps left by genome assembly or scaffolding.

Upstream repository: https://github.com/Gabaldonlab/redundans

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/redundans/general

- **`dnalinux/redundans:latest`** — points to `2.0`
- **`dnalinux/redundans:2.0`** — Redundans 2.0 compiled from the Gabaldonlab repository on `python:3.9.1`. `linux/amd64` only.

## Building the image

```bash
cd 2.0
docker build -t dnalinux/redundans:2.0 .
```

The build also compiles R 4.1.0 from source and installs the R packages `ggplot2`, `scales` and `argparse`, so it takes considerably longer than a typical image build.

## Smoke test

```bash
docker run -it --rm dnalinux/redundans:2.0 bash -c 'cd /root/src/redundans && ./redundans.py -h'
```

## License

Redundans is released under the GNU General Public License (the `license` field of the Dockerfile's LABEL block).
