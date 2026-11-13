# syntax=docker/dockerfile:1

# eggNOG-mapper calls esl-reformat (from Easel) for Pfam realignment.
# Debian ships HMMER but has no easel package, so build Easel from the
# HMMER source release.
FROM debian:trixie-slim AS easel

ARG HMMER_VERSION=3.4

RUN apt-get update && apt-get install -y --no-install-recommends \
        autoconf \
        build-essential \
        ca-certificates \
        wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
RUN wget -nv https://eddylab.org/software/hmmer/hmmer-${HMMER_VERSION}.tar.gz \
    && tar -xzf hmmer-${HMMER_VERSION}.tar.gz

WORKDIR /build/hmmer-${HMMER_VERSION}/easel
RUN autoconf \
    && ./configure --prefix=/usr/local \
    && make -j"$(nproc)" \
    && make install

# Build eggNOG-mapper v3 and its Cython extensions into a virtual environment.
FROM python:3.12-slim-trixie AS builder

ARG EGGNOG_VERSION=3.0.0-beta6

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
RUN wget -nv -O emapper.tar.gz \
        https://github.com/eggnogdb/eggnog-mapper/archive/refs/tags/v${EGGNOG_VERSION}.tar.gz \
    && tar -xzf emapper.tar.gz \
    && python -m venv /opt/eggnog-mapper \
    && /opt/eggnog-mapper/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/eggnog-mapper/bin/pip install --no-cache-dir ./eggnog-mapper-${EGGNOG_VERSION}

FROM python:3.12-slim-trixie

ARG EGGNOG_VERSION=3.0.0-beta6

LABEL software="eggnog-mapper" \
    base_image="python:3.12-slim-trixie" \
    container="eggnog-mapper" \
    about.summary="Fast functional annotation of novel sequences using eggNOG orthology assignments" \
    about.home="https://github.com/eggnogdb/eggnog-mapper" \
    software.version="3.0.0-beta6-src" \
    upstream.version="3.0.0-beta6" \
    version="1" \
    about.copyright="eggNOG-mapper authors" \
    about.license="AGPL-3.0-only" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="annotation,orthology,functional-genomics,metagenomics"

ENV DEBIAN_FRONTEND=noninteractive

# Search and gene-prediction tools from Debian. v3 does not bundle them:
# it resolves diamond, mmseqs, prodigal, hmmer and esl-reformat from PATH.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        diamond-aligner \
        hmmer \
        mmseqs2 \
        prodigal \
        wget \
    && rm -rf /var/lib/apt/lists/*

COPY --from=easel /usr/local/bin/esl-* /usr/local/bin/

# The venv keeps the Cython-accelerated extensions and the Python
# dependencies (biopython, psutil, xlsxwriter) isolated from the system
# interpreter. The same base image is used in both stages, so the copied
# venv keeps its absolute paths and scripts.
COPY --from=builder /opt/eggnog-mapper /opt/eggnog-mapper

ENV PATH="/opt/eggnog-mapper/bin:${PATH}"

WORKDIR /data

CMD ["emapper.py", "--help"]

# The eggNOG 7 database is not included in the image (~45 GB for the core
# download). v3 cannot use eggNOG 5 data from the 2.1.x image.
#
# docker run --rm -v $(pwd)/emapperdb-v7:/db dnalinux/eggnog-mapper:3.0.0-beta6-src \
#     download_eggnog_data.py --data_dir /db -y
#
# docker run --rm -v $(pwd):/data -v $(pwd)/emapperdb-v7:/db \
#     dnalinux/eggnog-mapper:3.0.0-beta6-src \
#     emapper.py -i /data/proteins.fa --data_dir /db -o /data/annotation --cpu 8
