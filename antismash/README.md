# antiSMASH

This directory contains Dockerfiles for **antiSMASH**, the antibiotics and Secondary Metabolite Analysis SHell.

## What is antiSMASH?

**antiSMASH** (https://antismash.secondarymetabolites.org/) detects and annotates biosynthetic gene clusters — the gene sets behind secondary metabolites such as antibiotics — in genome sequences. It runs a series of HMMER-based and other analysis modules and produces an annotated, browsable result page.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/antismash/general

- **`dnalinux/antismash:latest`** — currently points to `8.0.4`
- **`dnalinux/antismash:8.0.4`** — antiSMASH 8.0.4 installed with `pip` from the upstream GitHub source on `python:3.11-slim-bookworm`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/antismash:7.1.0.1`** — antiSMASH 7.1.0.1 installed with `pip` from the upstream GitHub source on `debian:bookworm-slim`. `linux/amd64` only.
- **`dnalinux/antismash:7.1.0`** — antiSMASH 7.1.0 installed with `pip` from the release tarball at `dl.secondarymetabolites.org` on `debian:bookworm-slim`. `linux/amd64` only.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 8.0.4
docker build -t antismash:8.0.4 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/antismash:8.0.4 antismash --version
docker run -it --rm dnalinux/antismash:8.0.4 antismash --help
```

## Notes

- The 7.1.0 and 7.1.0.1 images add the antiSMASH Debian repository and install HMMER2, HMMER, DIAMOND, FastTree, Prodigal, NCBI BLAST+, MUSCLE and GlimmerHMM as system packages. 8.0.4 installs HMMER2, DIAMOND, FastTree, Prodigal and NCBI BLAST+.
- Every image creates a `/data/databases` symlink pointing at `/mnt/disks/bucket/data/databases/`, a path from the maintainer's build environment.

## License

antiSMASH is released under the GNU Affero General Public License version 3.0 or later (the Dockerfile records `about.license="GNU Affero General Public License version 3.0 or greater"`).
