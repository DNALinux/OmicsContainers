FROM debian:trixie-slim

LABEL \
    software="diamond" \
    base_image="debian:trixie" \
    container="diamond-aligner" \
    about.summary="DIAMOND is a sequence aligner for protein and translated DNA searches,\
    designed for high performance analysis of big sequence data" \
    about.home="https://github.com/bbuchfink/diamond/" \
    software.version="2.1.10" \
    upstream.version="2.1.10" \
    version="2.1.10" \
    about.copyright="DIAMOND authors" \
    about.license="GPL-3.0" \
    about.license_file="/usr/share/doc/diamond/copyright" \
    maintainer="Facundo Mercado <facu.mercado1224@gmail.com>" \
    about.tags="bioinformatics, sequence alignment, protein clustering"

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt-get install -y \
    g++ \
    automake \
    cmake \
    zlib1g-dev \
    git \ 
    libzstd-dev \
    wget \
    tar \
    && apt clean && apt purge \
    && rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /opt/diamond

RUN wget https://github.com/bbuchfink/diamond/archive/refs/tags/v2.1.10.tar.gz \
    && tar -xzf v2.1.10.tar.gz \
    && rm v2.1.10.tar.gz

WORKDIR /opt/diamond/diamond-2.1.10

RUN mkdir build \
    && cd build \
    && cmake .. \
    && make -j$(nproc)

ENV PATH="/opt/diamond/diamond-2.1.10/build:${PATH}"