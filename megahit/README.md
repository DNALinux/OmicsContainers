# MEGAHIT

This directory contains a Dockerfile for **MEGAHIT**, an ultra-fast and memory-efficient assembler for metagenomes and single genomes.

## What is MEGAHIT?

**MEGAHIT** assembles short-read sequencing data using a succinct de Bruijn graph (SdBG), which keeps memory use low enough to assemble large and complex metagenomes on a single server. It accepts paired-end, interleaved paired-end and single-end reads, supports gzip/bzip2 input, and ships a `megahit_toolkit` for contig statistics and format conversion.

- Source code and releases: https://github.com/voutcn/megahit
- Citation: Li D, Liu CM, Luo R, Sadakane K, Lam TW. *MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph.* Bioinformatics 31(10):1674–1676, 2015. https://doi.org/10.1093/bioinformatics/btv033

## Available image

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/megahit/general

- **`dnalinux/megahit:latest`** — currently points to `1.2.9-src`
- **`dnalinux/megahit:1.2.9-src`** — MEGAHIT **1.2.9** built from the upstream v1.2.9 release tarball on `debian:trixie-slim`, following the upstream Dockerfile but with a multi-stage build instead of the end-of-life Ubuntu 18.04 environment. The v1.2.9 driver script is compatible with both Python 2 and Python 3; the image runs it with `python3` because `debian:trixie-slim` has no `python` executable. `linux/amd64` only, runs as `root`.

MEGAHIT 1.2.9 does not build on ARM: its CPU-dispatch header uses x86 `cpuid` inline assembly unconditionally. Upstream added a non-x86 guard after the 1.2.9 release, but there is no newer release, so this image remains `linux/amd64` only (as do the upstream image and the official precompiled release).

The image sets `ENTRYPOINT ["megahit"]` and `CMD ["--help"]`, so arguments after the image name are passed straight to MEGAHIT:

```bash
docker run --rm dnalinux/megahit:1.2.9-src --version
```

The `megahit_toolkit` binary (contig statistics and FASTG conversion) is installed next to `megahit` in `/usr/local/bin`, together with the test dataset in `/usr/local/share/megahit/test_data`. Because the image entry point is `megahit`, run the toolkit with `--entrypoint megahit_toolkit`:

```bash
docker run --rm --entrypoint megahit_toolkit dnalinux/megahit:1.2.9-src --help
```

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available image**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 1.2.9-src
docker build --platform linux/amd64 -t megahit:1.2.9-src .
```

The `--platform linux/amd64` is required on ARM hosts (including Apple silicon); on an x86-64 host it can be omitted. There is no arm64 build because of the 1.2.9 source limitation described above.

## Smoke test

MEGAHIT ships a small test dataset, so the image can be checked without any input data:

```bash
docker run --rm dnalinux/megahit:1.2.9-src --test
docker run --rm dnalinux/megahit:1.2.9-src --test --kmin-1pass
docker run --rm dnalinux/megahit:1.2.9-src --version
```

On ARM hosts Docker runs the `linux/amd64` image through emulation; add `--platform linux/amd64` to `docker run` if you want to silence the platform warning.

## Usage

Assemble paired-end reads (mount the directory holding the reads at `/data`; `-o` must be inside a writable mount):

```bash
docker run --rm -v "$PWD:/data" dnalinux/megahit:1.2.9-src \
    -1 /data/reads_1.fq.gz -2 /data/reads_2.fq.gz -t 8 -o /data/megahit_out
```

Single-end or interleaved reads:

```bash
docker run --rm -v "$PWD:/data" dnalinux/megahit:1.2.9-src \
    -r /data/reads.fq.gz -t 8 -o /data/megahit_out

docker run --rm -v "$PWD:/data" dnalinux/megahit:1.2.9-src \
    --12 /data/reads.fq.gz -t 8 -o /data/megahit_out
```

The final assembly is written to `megahit_out/final.contigs.fa`. Use `-t/--num-cpu-threads` for the thread count, `--k-list` to set the k-mer sizes and `--mem-flag` to trade memory for speed. Run the image without arguments (or with `--help`) for the full option list.

## License

MEGAHIT is released under the GNU General Public License, version 3 (upstream `LICENSE`). The Dockerfile records `about.license="GPL-3.0"`.
