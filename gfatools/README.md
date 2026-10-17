# gfatools

This directory contains a Dockerfile for **gfatools**, a toolkit for manipulating sequence graphs in the GFA and rGFA formats.

## What is gfatools?

**gfatools** (https://github.com/lh3/gfatools) is a set of tools for manipulating sequence graphs in the GFA format and in the rGFA variant used for pangenome graphs (https://github.com/lh3/gfatools/blob/master/doc/rGFA.md). It parses GFA files, extracts subgraphs, and converts between GFA, FASTA and BED. It is a small C program built with `make`, with a subcommand per operation (`view`, `stat`, `gfa2fa`, `gfa2bed`, `blacklist`, `bubble`, `asm`, `sql`).

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/gfatools/general

- **`dnalinux/gfatools:latest`** — recommended; currently points to `final-gt`
- **`dnalinux/gfatools:final-gt`** — gfatools built from source at the upstream tag `final-gt` on `debian:bookworm-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

```bash
cd final-gt
docker build -t dnalinux/gfatools:final-gt .
```

The build downloads `https://github.com/lh3/gfatools/archive/refs/tags/final-gt.tar.gz` and runs `make`. The version is fixed by the `VER` build argument in the Dockerfile.

## Smoke test

The build compiles gfatools under `/gfatools-final-gt` and does not install it on `PATH`, so the binary is called by its full path:

```bash
docker run -it --rm dnalinux/gfatools:final-gt /gfatools-final-gt/gfatools
docker run -it --rm dnalinux/gfatools:final-gt /gfatools-final-gt/gfatools version
```

Run with no arguments, gfatools prints its command list and exits.

## License

Neither the Dockerfile nor the upstream repository (https://github.com/lh3/gfatools) states a license — the repository ships no license file — so no license can be given here.
