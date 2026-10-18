# AllHiC

This directory contains Dockerfiles for **AllHiC**, a pipeline for Hi-C scaffolding of contigs.

## What is AllHiC?

**AllHiC** (https://github.com/tanghaibao/allhic) uses Hi-C data to order and orient genomic contigs into scaffolds. It is designed with auto-polyploid and heterozygous diploid genomes in mind (Allele-aware scaffolding), and it is intended to be driven from a scripted workflow.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/allhic/general

- **`dnalinux/allhic:latest`** — currently points to `0.9.14`
- **`dnalinux/allhic:0.9.14`** — AllHiC 0.9.14, compiled from the upstream source tarball with the Go toolchain on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/allhic:0.9.13`** — AllHiC 0.9.13, same build method. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 0.9.14
docker build -t allhic:0.9.14 .
```

## Smoke test

Both images set `ENTRYPOINT ["allhic"]`, so the first argument after the image name is passed to `allhic`:

```bash
docker run -it --rm dnalinux/allhic:0.9.14 --version
docker run -it --rm dnalinux/allhic:0.9.14 --help
```

## Note on the 0.9.14 build

`base.go` in the upstream 0.9.14 tarball still reports the version as `0.9.13`; the Dockerfile patches that string to `0.9.14` during the build.

## License

AllHiC is released under the BSD 3-Clause license, per `LICENSE` in the upstream repository.
