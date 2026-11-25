# syntax=docker/dockerfile:1
# Based on the upstream Dockerfile:
# https://github.com/voutcn/megahit/blob/v1.2.9/Dockerfile
# Differences: builds from the v1.2.9 release tarball on debian:trixie-slim
# instead of ubuntu:18.04, uses a multi-stage build to keep the compiler out
# of the final image, and points the Python driver script at python3 (trixie
# has no "python" executable).
#
# The v1.2.9 source only compiles on x86-64 (its CPU dispatch header uses
# inline cpuid assembler unconditionally). The image applies the upstream
# fix for other architectures, commit 4687e4f72844 ("Add support for
# non-x86_64 architectures", 2024-03-27, fixes voutcn/megahit#320), from
# megahit-1.2.9-non-x86.patch in this directory, so the image builds for
# both linux/amd64 and linux/arm64.

FROM debian:trixie-slim AS builder

ARG MEGAHIT_VERSION=1.2.9

COPY megahit-1.2.9-non-x86.patch /build/megahit-1.2.9-non-x86.patch

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        patch \
        wget \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
RUN wget -nv -O megahit.tar.gz \
        https://github.com/voutcn/megahit/archive/refs/tags/v${MEGAHIT_VERSION}.tar.gz \
    && tar -xzf megahit.tar.gz

WORKDIR /build/megahit-${MEGAHIT_VERSION}

# v1.2.9 uses "#!/usr/bin/env python" but is compatible with Python 2 and 3;
# Debian trixie only ships python3. local_assemble.h uses uint32_t without
# including <cstdint>, which GCC 14 (trixie) no longer provides transitively.
RUN patch -p1 < /build/megahit-1.2.9-non-x86.patch \
    && sed -i '1s|^#!/usr/bin/env python$|#!/usr/bin/env python3|' src/megahit \
    && sed -i 's|#include <string>|#include <cstdint>\n#include <string>|' src/localasm/local_assemble.h \
    && mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. \
    && make -j"$(nproc)" \
    && make install DESTDIR=/opt/megahit

FROM debian:trixie-slim

ARG MEGAHIT_VERSION=1.2.9

LABEL software="megahit" \
    base_image="debian:trixie-slim" \
    container="megahit" \
    about.summary="Ultra-fast and memory-efficient NGS assembler for metagenomes and single genomes" \
    about.home="https://github.com/voutcn/megahit" \
    software.version="1.2.9-src" \
    upstream.version="1.2.9" \
    version="1" \
    about.copyright="2014-2015 The University of Hong Kong & L3 Bioinformatics Limited" \
    about.license="GPL-3.0" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="assembly,metagenomics,genomics"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        bzip2 \
        gzip \
        libgomp1 \
        python3 \
        zlib1g \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/megahit/usr/local/ /usr/local/

WORKDIR /data

ENTRYPOINT ["megahit"]
CMD ["--help"]

# Usage examples:
# docker run --rm -v $(pwd):/data dnalinux/megahit:1.2.9-src \
#     -1 /data/reads_1.fq.gz -2 /data/reads_2.fq.gz -t 8 -o /data/megahit_out
#
# Single-end reads:
# docker run --rm -v $(pwd):/data dnalinux/megahit:1.2.9-src \
#     -r /data/reads.fq.gz -t 8 -o /data/megahit_out
