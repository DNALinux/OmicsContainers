# bedGraphToBigWig

This directory contains Dockerfiles for **bedGraphToBigWig**, a UCSC utility that converts a bedGraph file into a bigWig file.

## What is bedGraphToBigWig?

**bedGraphToBigWig** is one of the UCSC Genome Browser command-line utilities (https://hgdownload.soe.ucsc.edu/downloads.html). It converts a bedGraph file — four-column chrom/start/end/value coverage data — into the indexed bigWig format.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bedgraphtobigwig/general

- **`dnalinux/bedgraphtobigwig:latest`** — currently points to `2.10-bin`
- **`dnalinux/bedgraphtobigwig:2.10-bin`** — the pre-compiled `linux.x86_64` binary from UCSC, placed in `/usr/local/bin` on `debian:bookworm-slim`. `linux/amd64` only.
- **`dnalinux/bedgraphtobigwig:2.10`** — an earlier build of the same UCSC 2.10 binary. `linux/amd64` only.

## Building the image

```bash
cd 2.10-bin
docker build -t dnalinux/bedgraphtobigwig:2.10-bin .
```

## Smoke test

`bedGraphToBigWig` has no `--version` or `-h` flag; running it with no arguments prints its usage message:

```bash
docker run -it --rm dnalinux/bedgraphtobigwig:2.10-bin bedGraphToBigWig
```

## License

The UCSC command-line utilities, `bedGraphToBigWig` included, are covered by the MIT license on the UCSC license page (https://genome.ucsc.edu/license/). The Dockerfile records `about.license="MIT"` and `about.copyright="https://genome.ucsc.edu/license/"`.
