FROM debian:trixie

LABEL \
    software="diamond" \
    base_image="debian:trixie" \
    container="diamond-aligner" \
    about.summary="DIAMOND is a sequence aligner for protein and translated DNA searches,\
    designed for high performance analysis of big sequence data" \
    about.home="https://github.com/bbuchfink/diamond/" \
    software.version="2.1.9-1" \
    upstream.version="2.1.9.163" \
    version="2.1.9-1" \
    about.copyright="DIAMOND authors" \
    about.license="GPL-3.0" \
    about.license_file="/usr/share/doc/diamond/copyright" \
    maintainer="Facundo Mercado <facu.mercado1224@gmail.com>" \
    about.tags="bioinformatics, sequence alignment, protein clustering"

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt-get install -y \
    diamond-aligner=2.1.9-1 \
    && apt clean && apt purge \
    && rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /data