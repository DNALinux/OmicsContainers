# PHYLIP

This directory contains Dockerfiles for **PHYLIP**, a package of programs for inferring phylogenies.

## What is PHYLIP?

**PHYLIP** (the PHYLogeny Inference Package) is a package of programs for inferring phylogenies (evolutionary trees). It covers distance matrix methods, parsimony and likelihood analysis and tree drawing; the Debian package installs programs such as `dnapars`, `dnaml`, `neighbor`, `protdist`, `protpars`, `seqboot`, `consense`, `drawgram` and `drawtree`.

- Project home page: http://evolution.genetics.washington.edu/phylip.html
- Copyright 1980-2014 Joe Felsenstein

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/phylip/general

- **`dnalinux/phylip:latest`** — recommended; currently points to `1-3.697dfsg-2-deb`
- **`dnalinux/phylip:1-3.697dfsg-2-deb`** — the Debian package pinned to `phylip=1:3.697+dfsg-2`, installed on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/phylip:1-3.697dfsg-1-deb`** — installs the `phylip` package without pinning a version. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 1-3.697dfsg-2-deb
docker build -t phylip:1-3.697dfsg-2-deb .
```

## Smoke test

The package installs the PHYLIP programs together with a `/usr/bin/phylip` wrapper, invoked as `phylip program [arguments]`, which runs the program named in the first argument; the wrapper itself takes no options. There is no version or help flag, so the image has no non-interactive smoke test. The `phylip(1)` manual page gives this example:

```bash
docker run -it --rm dnalinux/phylip:1-3.697dfsg-2-deb phylip dnapenny
```

## License

BSD 2-clause. The Dockerfile `LABEL` records `about.license="BSD-2-clause"` and points at `/usr/share/doc/phylip/copyright`.
