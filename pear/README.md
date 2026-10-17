# PEAR

This directory contains Dockerfiles for **PEAR**, a fast and memory-efficient merger of Illumina paired-end reads.

## What is PEAR?

**PEAR** (Paired-End reAd mergeR) is an ultrafast, memory-efficient and highly accurate pair-end read merger. It is fully parallelized and can run with as low as just a few kilobytes of memory. It assembles Illumina paired-end reads if the DNA fragment sizes are smaller than twice the read length, and also works with multiplexed data sets where the true fragment size varies.

Every Dockerfile in this directory builds PEAR from source — `./configure && make && make install` — after copying a local `reader.c` into the extracted source tree.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/pear/general

- **`dnalinux/pear:latest`** — recommended; currently points to `0.9.6-src-gz`
- **`dnalinux/pear:0.9.6-src-gz`** — PEAR 0.9.6 built on `ubuntu:16.04` from `pear_0.9.6_src_all.tar.gz` (Galaxy depot). Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/pear:0.9.6-src`** — the same PEAR 0.9.6 source and build, without the compression libraries. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/pear:0.9.2`** — PEAR 0.9.2 built on `ubuntu:16.04` from `PEAR-master.zip`, downloaded from `https://github.com/hisplan/docker-PEAR`. Multi-arch (`linux/amd64`, `linux/arm64`).

How the four directories map to those tags:

- `0.9.6-src-gz` and `0.9.6-srcgz` hold byte-identical Dockerfiles: both install `zlib1g-dev` and `libbz2-dev` on top of `build-essential` and `wget`. PEAR's `configure` detects those headers and links zlib/bz2, which is what enables gzip- and bzip2-compressed FASTQ input. Only `0.9.6-src-gz` is published on Docker Hub; there is no `0.9.6-srcgz` tag.
- `0.9.6-src` is the same PEAR 0.9.6 build without `zlib1g-dev` and `libbz2-dev`.
- `0.92-src` is the directory that produces the `0.9.2` tag.

## Building the image

```bash
cd 0.9.6-src-gz
docker build -t dnalinux/pear:0.9.6-src-gz .
```

## Smoke test

`pear -h` prints the version banner followed by the help screen:

```bash
docker run -it --rm dnalinux/pear:0.9.6-src-gz pear -h
```

## License

PEAR 0.9.6 is released under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported license, as stated in the `README` and `LICENSE.txt` of the upstream source distribution. The Dockerfiles record the license as `other`.
