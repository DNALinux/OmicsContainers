# 3D-DNA

This directory contains Dockerfiles for **3D-DNA**, a pipeline for 3D de novo genome assembly from Hi-C data.

## What is 3D-DNA?

**3D-DNA** (https://github.com/aidenlab/3d-dna) orders and orients scaffolds, corrects misjoins, and produces chromosome-length scaffolds from a draft genome assembly together with Hi-C data. It is developed in the Aiden lab alongside the Juicer pipeline.

Citation: Dudchenko, O., Batra, S.S., Omer, A.D., Nyquist, S.K., Hoeger, M., Durand, N.C., Shamim, M.S., Machol, I., Lander, E.S., Aiden, A.P., et al. *De novo assembly of the Aedes aegypti genome using Hi-C yields chromosome-length scaffolds*. Science 356(6333):92-95 (2017). https://doi.org/10.1126/science.aal3327

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/3ddna/general

- **`dnalinux/3ddna:latest`** — currently points to `201008.1`
- **`dnalinux/3ddna:201008.1`** — 3D-DNA release `201008` plus the `201008.1` security-only update, built on `debian:trixie-slim` from the upstream source tarball. `linux/amd64` only.
- **`dnalinux/3ddna:201008`** — the original `201008` build. Multi-arch (`linux/amd64`, `linux/arm64`).

The single Dockerfile lives in the `201008/` directory; its labels record `software.version="201008"` and `oc_version="201008.1"`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 201008
docker build -t 3ddna:201008.1 .
```

## Smoke test

3D-DNA ships shell scripts (`run-asm-pipeline.sh` and related) rather than a single binary with a `--version` flag. The image sets no entrypoint, so confirm it by listing the unpacked upstream source tree:

```bash
docker run -it --rm dnalinux/3ddna:201008.1 ls /3d-dna-201008
```

## License

3D-DNA is released under the MIT License, per `LICENSE` in the upstream repository and the Dockerfile's `about.license="MIT"` label.
