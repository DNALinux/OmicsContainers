# RepeatMasker

This directory contains Dockerfiles for **RepeatMasker**, a program that screens DNA sequences for interspersed repeats and low-complexity DNA sequences.

## What is RepeatMasker?

**RepeatMasker** screens DNA sequences for interspersed repeats and low-complexity DNA sequences. The image builds RepeatMasker 4.1.6 from the upstream tarball and adds the external search programs it uses:

- **TRF 4.09.1** — the `trf409.linux64` binary from the Benson-Genomics-Lab TRF release, placed at `/usr/local/trf409.linux64`
- **RMBlast 2.14.1+** — the pre-built `rmblast-2.14.1+-x64-linux` binaries, unpacked under `/usr/local/rmblast-2.14.1/`
- **RepeatMasker 4.1.6** — unpacked under `/usr/local/RepeatMasker/`

Upstream: https://www.repeatmasker.org/

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/repeatmasker/general

- **`dnalinux/repeatmasker:latest`** — closest in size to the RepeatMasker **4.1.7** build (see the note on tags below)
- **`dnalinux/repeatmasker:4.1.6`** — built from `4.1.6/`, on `python:3.10.14-slim-bookworm`. `linux/amd64` only.

## Note on tags

This repository holds a single `4.1.6/` directory, but the Docker Hub repository carries more tags:

- `4.1.7` was built from a `4.1.7/` directory that was later removed from this repository; the image is still on Docker Hub. `latest` (382,997,996 bytes) is almost the same size as `4.1.7` (382,997,468 bytes) and differs from `4.1.6` (382,640,757 bytes) by about 350 kB, so `latest` corresponds to the 4.1.7 build.
- `4.1.6-configured`, `4.1.6-configured-p0p5` and `debug3` are further tags on the Hub that no Dockerfile currently in this repository builds. `4.1.6-configured` and `debug3` have the same size (407,359,917 bytes).

## Building the image

```bash
cd 4.1.6
docker build -t dnalinux/repeatmasker:4.1.6 .
```

## Smoke test

The image ships RepeatMasker **unconfigured**: `perl configure` still has to be run inside a container, and a repeat library installed, before the `RepeatMasker` program can be used.

## License

The Dockerfile's LABEL block declares no license: its `about.license` line is commented out. See the upstream RepeatMasker distribution for its licensing terms.
