# BWA-MEM2

This directory contains a Dockerfile for **BWA-MEM2**, the next generation of the BWA-MEM algorithm.

## What is BWA-MEM2?

**BWA-MEM2** is a sequence aligner for mapping sequencing reads against a reference genome, and is the next generation of the BWA-MEM algorithm. It uses the BWA-MEM index and command-line interface (`index`, `mem`). Upstream: https://github.com/bwa-mem2/bwa-mem2

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bwa-mem2/general

- **`dnalinux/bwa-mem2:2.3-src`** — BWA-MEM2 **2.3**, built from source. The `Source_code_including_submodules.zip` archive of the v2.3 GitHub release is compiled with `make` in a `debian:trixie-slim` builder stage, and the resulting binaries are copied into a clean `debian:trixie-slim` runtime stage. `linux/amd64` only. The image sets `ENTRYPOINT ["bwa-mem2"]` and `WORKDIR /data`.

There is no `latest` tag for this repository.

## Notes

- The version directory is named `2.30-src`, the upstream version is `2.3`, and the published Docker Hub tag is `2.3-src`.
- The Dockerfile patches the vendored `safestringlib` sources before compiling (it prepends `#include <stdlib.h>` and `#include <ctype.h>` to the `.c` files) to fix implicit declarations, and installs only `zlib1g` in the runtime stage.
- The published tag is `amd64`-only: there is no ARM image for BWA-MEM2 in this repository.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 2.30-src
docker build -t bwa-mem2:2.3-src .
```

## Smoke test

`bwa-mem2` is the image's `ENTRYPOINT`, and it prints its available commands when it is run with no arguments:

```bash
docker run -it --rm dnalinux/bwa-mem2:2.3-src
```

## License

BWA-MEM2 is released under the MIT license (Dockerfile `about.license` LABEL).
