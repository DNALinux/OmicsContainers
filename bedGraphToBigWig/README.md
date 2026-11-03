# bedGraphToBigWig

This directory contains Dockerfiles for **bedGraphToBigWig**, a UCSC utility that converts a bedGraph file into a bigWig file.

## What is bedGraphToBigWig?

**bedGraphToBigWig** is one of the UCSC Genome Browser command-line utilities (https://hgdownload.soe.ucsc.edu/downloads.html). It converts a bedGraph file — four-column chrom/start/end/value coverage data — into the indexed bigWig format.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bedgraphtobigwig/general

- **`dnalinux/bedgraphtobigwig:latest`** — currently points to `2.10-bin`
- **`dnalinux/bedgraphtobigwig:2.10-bin`** — the pre-compiled UCSC 2.10 binary for the build platform (`linux.x86_64` or `linux.aarch64`, both stored locally in `2.10-bin/`), placed in `/usr/local/bin` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/bedgraphtobigwig:2.10`** — an earlier build of the same UCSC 2.10 binary. `linux/amd64` only.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing. The pre-compiled binaries for both architectures are committed in `2.10-bin/`, so the build works offline. For a multi-arch build use buildx with `--platform` and `--push`:

```bash
cd 2.10-bin
docker build -t bedgraphtobigwig:2.10-bin .
```

```bash
cd 2.10-bin
docker buildx build --platform linux/amd64,linux/arm64 -t dnalinux/bedgraphtobigwig:2.10-bin --push .
```

## Smoke test

`bedGraphToBigWig` has no `--version` or `-h` flag; running it with no arguments prints its usage message:

```bash
docker run -it --rm dnalinux/bedgraphtobigwig:2.10-bin bedGraphToBigWig
```

## License

The UCSC command-line utilities, `bedGraphToBigWig` included, are covered by the MIT license on the UCSC license page (https://genome.ucsc.edu/license/). The Dockerfile records `about.license="MIT"` and `about.copyright="https://genome.ucsc.edu/license/"`.
