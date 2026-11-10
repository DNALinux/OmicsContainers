# syntax=docker/dockerfile:1
# Based on the upstream Dockerfile:
# https://github.com/smithlabcode/dnmtools/blob/master/Dockerfile
# Differences: builds from the v1.5.1 release tarball (instead of a git
# checkout), pins Alpine, and skips the release-only `make distcheck`.
# Alpine is used because it supports both linux/amd64 and linux/arm64.

# Define a base to inherit from so ARGs can be collected here
FROM alpine:3.24 AS base
ARG NUM_JOBS=4
ARG HTSLIB_VERSION=1.21
ARG SAMTOOLS_VERSION=1.21
ARG DNMTOOLS_VERSION=1.5.1

# Build htslib from source, installed to its own directory so the
# essential files can be retrieved separately as needed.
FROM base AS build_htslib
RUN apk add --no-cache \
    build-base \
    autoconf \
    automake \
    zlib-dev \
    bzip2-dev \
    xz-dev \
    ncurses-dev \
    wget
ENV HTSLIB=htslib-${HTSLIB_VERSION}
WORKDIR /build
RUN wget -nv https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/${HTSLIB}.tar.bz2 \
    && tar -xf ${HTSLIB}.tar.bz2 \
    && cd ${HTSLIB} \
    && autoreconf -i \
    && ./configure --prefix=$(pwd) \
    && make -j${NUM_JOBS} \
    && make install

# Build samtools from source, linked against the htslib built above.
# Only the binary is used, by dnmtools' test suite.
FROM base AS build_samtools
RUN apk add --no-cache \
    build-base \
    zlib-dev \
    bzip2-dev \
    xz-dev \
    ncurses-dev \
    wget
ENV HTSLIB=htslib-${HTSLIB_VERSION}
ENV SAMTOOLS=samtools-${SAMTOOLS_VERSION}
COPY --from=build_htslib /build/${HTSLIB}/lib /usr/lib
COPY --from=build_htslib /build/${HTSLIB}/include /usr/include
WORKDIR /build
RUN wget -nv https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/${SAMTOOLS}.tar.bz2 \
    && tar -xf ${SAMTOOLS}.tar.bz2 \
    && cd ${SAMTOOLS} \
    && ./configure --prefix=$(pwd) --with-htslib=/usr \
    && make -j${NUM_JOBS} \
    && make install

# Build dnmtools from the release tarball
FROM base AS build_dnmtools
RUN apk add --no-cache \
    build-base \
    gsl-dev \
    zlib-dev \
    bzip2-dev \
    xz-dev \
    wget \
    gzip \
    bash
ENV HTSLIB=htslib-${HTSLIB_VERSION}
ENV SAMTOOLS=samtools-${SAMTOOLS_VERSION}
# Copying the install from within the build tree keeps the build stage
# smaller than installing htslib system-wide first.
COPY --from=build_htslib /build/${HTSLIB}/lib /usr/lib
COPY --from=build_htslib /build/${HTSLIB}/include /usr/include
COPY --from=build_samtools /build/${SAMTOOLS}/bin/samtools /usr/bin/samtools

WORKDIR /build
RUN wget -nv https://github.com/smithlabcode/dnmtools/releases/download/v${DNMTOOLS_VERSION}/dnmtools-${DNMTOOLS_VERSION}.tar.gz \
    && echo "685f195db2b240dbf58ce9f3d024fc66a0eea85cfd0eabf870e2369e8725481b  dnmtools-${DNMTOOLS_VERSION}.tar.gz" | sha256sum -c - \
    && tar -xzf dnmtools-${DNMTOOLS_VERSION}.tar.gz

# Disable floating-point contraction so aarch64 (which has FMA) produces
# the same rounding as amd64; dnmtools' checksum-based tests depend on it.
RUN cd /build/dnmtools-${DNMTOOLS_VERSION} \
    && ./configure --prefix=$(pwd) \
        CXXFLAGS_set=set CXXFLAGS="-O3 -DNDEBUG -ffp-contract=off" \
    && make -j${NUM_JOBS} \
    && make -j${NUM_JOBS} check \
    && make install

# Build a light-weight image with just the binaries
FROM base
LABEL base_image="alpine:3.24" \
      software="DNMTools" \
      software.version="1.5.1-src" \
      about.summary="Tools for analyzing DNA methylation data from high-throughput sequencing experiments (WGBS, RRBS and Nanopore)" \
      about.home="https://github.com/smithlabcode/dnmtools" \
      upstream.version="1.5.1" \
      about.copyright="2008-2025 Cold Spring Harbor Laboratory, University of Southern California and Andrew D. Smith" \
      about.license="GPL-3.0" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      about.tags="field::biology:bioinformatics"
ENV HTSLIB=htslib-${HTSLIB_VERSION}
RUN apk add --no-cache \
    gsl \
    zlib \
    libbz2 \
    xz-libs \
    libstdc++ \
    libgomp
COPY --from=build_htslib /build/${HTSLIB}/lib /usr/lib
COPY --from=build_dnmtools /build/dnmtools-${DNMTOOLS_VERSION}/dnmtools /usr/bin

ENTRYPOINT ["dnmtools"]
