# syntax=docker/dockerfile:1

# Stage 1: Build environment
FROM rust:1.90-slim-trixie AS builder

ARG MODKIT_VERSION=0.6.4

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    cmake \
    libbz2-dev \
    libclang-dev \
    libcurl4-openssl-dev \
    liblzma-dev \
    libssl-dev \
    pkg-config \
    wget \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

# Source tarball for the v0.6.4 tag
RUN wget -nv https://github.com/nanoporetech/modkit/archive/refs/tags/v${MODKIT_VERSION}.tar.gz \
    && echo "0197d49c0313551c1bb4fd6399a6ee4e44abb2233c9704bed2019389bee2fd61  v${MODKIT_VERSION}.tar.gz" | sha256sum -c - \
    && tar -xzf v${MODKIT_VERSION}.tar.gz

WORKDIR /build/modkit-${MODKIT_VERSION}

# Cargo.lock pins dependency versions compatible with the Rust 1.90 toolchain
# pinned upstream; newer releases of some crates require a newer compiler.
COPY Cargo.lock /build/modkit-${MODKIT_VERSION}/Cargo.lock

RUN cargo build --release --package modkit --locked

# Stage 2: Final runtime image
FROM debian:trixie-slim

ARG MODKIT_VERSION=0.6.4

LABEL software="modkit" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      base_image="debian:trixie-slim" \
      container="modkit" \
      about.summary="A bioinformatics tool for working with modified bases in Oxford Nanopore sequencing data" \
      about.home="https://github.com/nanoporetech/modkit" \
      software.version="0.6.4-src" \
      upstream.version="0.6.4" \
      version="1" \
      about.copyright="(c) 2023 Oxford Nanopore Technologies Plc." \
      about.license="other" \
      extra.binaries="/usr/local/bin/modkit"

COPY --from=builder /build/modkit-${MODKIT_VERSION}/target/release/modkit /usr/local/bin/modkit

# Runtime dependency of the bundled HTSlib
RUN apt-get update && apt-get install -y --no-install-recommends \
    libbz2-1.0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["modkit"]
CMD ["--help"]
