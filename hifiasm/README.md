# hifiasm

This directory contains Dockerfiles for **hifiasm**, a haplotype-resolved de novo assembler for PacBio HiFi reads.

## What is hifiasm?

**hifiasm** (https://github.com/chhylp123/hifiasm) is a fast haplotype-resolved de novo assembler initially designed for PacBio HiFi reads. Its later releases also use ultralong Oxford Nanopore reads together with Hi-C or parental short reads, and produce telomere-to-telomere assemblies for human-sized genomes.

Citation: Cheng, H., Concepcion, G.T., Feng, X., Zhang, H., Li, H. (2021) *Haplotype-resolved de novo assembly using phased assembly graphs with hifiasm*. Nature Methods 18:170-175. https://doi.org/10.1038/s41592-020-01056-5

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/hifiasm/general

- **`dnalinux/hifiasm:latest`** — recommended; currently points to `0.20.0`
- **`dnalinux/hifiasm:0.20.0`** — hifiasm 0.20.0 compiled from source on `debian:bookworm-slim`, with the binary moved to `/usr/local/bin`. `linux/amd64` only.
- **`dnalinux/hifiasm:0.19.9`** — hifiasm 0.19.9 compiled from source on `debian:bookworm-slim`. `linux/amd64` only.

Both images download the upstream source tarball for their tag (`https://github.com/chhylp123/hifiasm/archive/refs/tags/<version>.tar.gz`) and run `make`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 0.20.0
docker build -t hifiasm:0.20.0 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/hifiasm:0.20.0 hifiasm -h
```

The `0.19.9` build never moves the binary out of its build directory, so it is not on `PATH` and has to be called by its full path:

```bash
docker run -it --rm dnalinux/hifiasm:0.19.9 /hifiasm-0.19.9/hifiasm -h
```

## Note on the Dockerfile metadata

Both Dockerfiles carry a `base_image` label reading `biocontainers:latest`, but the images are built `FROM debian:bookworm-slim`. Both also set the `software` label to `hsfiasm`, which is a misspelling of hifiasm.

## License

hifiasm is released under the MIT license (`about.license` label of the 0.20.0 Dockerfile, and the upstream repository `LICENSE`).
