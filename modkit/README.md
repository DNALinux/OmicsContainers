# modkit

This directory contains a Dockerfile for **modkit**, a toolkit for working with modified bases in Oxford Nanopore sequencing data.

## What is modkit?

**modkit** (https://github.com/nanoporetech/modkit) is a set of tools from Oxford Nanopore Technologies for manipulating and summarizing modified-base data stored in BAM files. Modified-base calls are carried in the `MM` and `ML` tags of the SAM/BAM specification, and modkit can create bedMethyl tables (`pileup`), summarize modification calls (`summary`, `sample-proportions`), extract read-level modification information (`extract`), and perform motif- and region-level analyses (`motif`, `dmr`, `refmod`). It also includes experimental `open-chromatin` commands.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/modkit/general

- **`dnalinux/modkit:latest`** — currently points to `0.6.4-src`
- **`dnalinux/modkit:0.6.4-src`** — modkit 0.6.4 compiled with `cargo` from the v0.6.4 source tarball in a build stage on `rust:1.90-slim-trixie`, with the binary placed in `/usr/local/bin` on `debian:trixie-slim`. The Rust version matches the upstream `rust-toolchain.toml`. Multi-arch (`linux/amd64`, `linux/arm64`).

The image sets `ENTRYPOINT ["modkit"]` and `CMD ["--help"]`, so the first argument after the image name is the modkit subcommand.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 0.6.4-src
docker build -t modkit:0.6.4-src .
```

For a multi-arch build use buildx with `--platform` and `--push`:

```bash
cd 0.6.4-src
docker buildx build --platform linux/amd64,linux/arm64 -t dnalinux/modkit:0.6.4-src --push .
```

The build downloads the source tarball from `https://github.com/nanoporetech/modkit/archive/refs/tags/v0.6.4.tar.gz` (SHA-256 verified) and its Rust dependencies from crates.io, so it needs network access. HTSlib is compiled as part of the `rust-htslib` dependency.

The upstream source archive does not ship a `Cargo.lock`, so this directory contains one (generated with the Rust 1.90 toolchain from the upstream `rust-toolchain.toml`) that pins the dependency versions that toolchain supports. It is copied into the build tree and `cargo build --locked` is used; without it, newer releases of some transitive crates no longer build: for example `parking_lot` 0.13 requires Rust 1.95, and `hts-sys` 2.2.x changes the generated HTSlib bindings in a way `rust-htslib` 0.46 cannot compile against (it is pinned to 2.1.4).

## Smoke test

Running the image with no arguments prints the help screen and version:

```bash
docker run --rm dnalinux/modkit:0.6.4-src
```

To mount data and run a command, pass the subcommand as the first argument:

```bash
docker run --rm -v "$(pwd):/data" dnalinux/modkit:0.6.4-src \
    pileup /data/reads.bam /data/output.bed.gz --modified-bases 5mC
```

## License

modkit is distributed under the Oxford Nanopore Technologies Public License, v. 1.0 (see the upstream `README.md`). This is a source-available licence, not an OSI-approved open-source licence. The Dockerfile records `about.license="other"`.
