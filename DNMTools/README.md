# DNMTools

This directory contains a Dockerfile for **DNMTools**, a suite of tools for analyzing DNA methylation data from high-throughput sequencing.

## What is DNMTools?

**DNMTools** (https://github.com/smithlabcode/dnmtools) is a set of command-line tools for analyzing DNA methylation data, especially whole-genome bisulfite sequencing (WGBS) and reduced representation bisulfite sequencing (RRBS). Since version 1.5.0 it can also start from Nanopore BAM files with 5mC and 5hmC calls. The tools cover read mapping (`abismal`), methylation level estimation (`counts`, `levels`, `bsrate`), differentially methylated region analysis (`diff`, `radmeth`), and related statistics.

## Available images

The image is already published to Docker Hub:

- **`dnalinux/dnmtools:latest`** — currently points to `1.5.1-src`
- **`dnalinux/dnmtools:1.5.1-src`** — DNMTools 1.5.1 built from the upstream release source tarball, with HTSlib 1.21 also compiled from source, on `alpine:3.24`. Multi-arch (`linux/amd64`, `linux/arm64`).

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/dnmtools/general

## Building the image

If you prefer to build the image yourself instead of pulling it, give it a local tag of your choosing. The `dnalinux/` prefix identifies the images published by the DNALinux project and is not needed for a local build:

```bash
cd 1.5.1-src
docker build -t dnmtools:1.5.1-src .
```

For a multi-arch build use buildx with `--platform` and `--push`:

```bash
cd 1.5.1-src
docker buildx build --platform linux/amd64,linux/arm64 -t dnalinux/dnmtools:1.5.1-src --push .
```

The Dockerfile is based on the [upstream Dockerfile](https://github.com/smithlabcode/dnmtools/blob/master/Dockerfile), adapted to download the v1.5.1 release tarball instead of copying a git checkout, to skip the release-only `make distcheck`, and to build with `-ffp-contract=off` so `linux/arm64` produces the same floating-point rounding as `linux/amd64` (dnmtools' checksum-based test suite requires this). The build compiles HTSlib and samtools from source; samtools is used only by the test suite, and the final image contains just the HTSlib shared library and the `dnmtools` binary.

## Smoke test

Running the image with no arguments prints the version and command list:

```bash
docker run --rm dnalinux/dnmtools:1.5.1-src
```

To mount a data directory and run a command, pass the subcommand as the first argument:

```bash
docker run --rm -v "$(pwd):/data" dnalinux/dnmtools:1.5.1-src counts -n -c /data/genome.fa /data/reads.bam
```

The image sets `ENTRYPOINT ["dnmtools"]`, so the first argument is the DNMTools subcommand.

## License

DNMTools is distributed under the GNU General Public License v3.0 (https://github.com/smithlabcode/dnmtools/blob/master/LICENSE). The Dockerfile records `about.license="GPL-3.0"`. HTSlib, built during the image build, is distributed under the MIT/Expat license.
