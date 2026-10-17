# bcftools

This directory contains Dockerfiles for **bcftools**, a program for variant calling and for manipulating VCF and BCF files.

## What is bcftools?

**bcftools** (https://samtools.github.io/bcftools/howtos/index.html) is a set of utilities for variant calling and for manipulating variant files in the VCF and BCF formats. It belongs to the samtools/htslib project and is normally used together with `samtools`.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bcftools/general

- **`dnalinux/bcftools:latest`** — currently points to `1.23.1`
- **`dnalinux/bcftools:1.23.1`** — bcftools 1.23.1 built from the upstream source tarball on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/bcftools:1.21`** — bcftools 1.21 built from the upstream source tarball on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/bcftools:1.20`** — bcftools 1.20 installed from the Debian package (`bcftools=1.20-2` on amd64, `1.20-2+b1` on arm64) on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

```bash
cd 1.23.1
docker build -t dnalinux/bcftools:1.23.1 .
```

## Smoke test

Every image sets `ENTRYPOINT ["bcftools"]`, so the first argument after the image name is passed to `bcftools`:

```bash
docker run -it --rm dnalinux/bcftools:1.23.1 --version
docker run -it --rm dnalinux/bcftools:1.23.1 --help
```

## License

bcftools is dual-licensed: it is available under either the MIT/Expat license or the GNU General Public License, as stated in the LICENSE file of the upstream repository. The Dockerfile records `about.license="other"` and points to `/usr/share/doc/bcftools/copyright` for the full text.
