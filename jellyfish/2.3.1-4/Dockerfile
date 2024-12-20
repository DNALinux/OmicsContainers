FROM debian:trixie-slim

LABEL software="Jellyfish" \
    base_image="debian:bookworm-slim" \
    container="Jellyfish" \
    about.summary="JELLYFISH is a tool for fast, memory-efficient counting of k-mers in DNA" \
    about.home="https://github.com/gmarcais/Jellyfish" \
    software.version="2.3.1-4" \
    version="1" \
    about.copyright="Guillaume Marcais and Carl Kingsford" \
    about.license="Dual-licensed (3-Clause BSD or GPL 3.0)" \
    about.license_file="/usr/share/doc/jellyfish/copyright" \
    maintainer="Facundo Mercado <facu.mercado1224@gmail.com>" \
    about.tags="k-mers counting, dna sequences"

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
apt-get install -y  jellyfish=2.3.1-4 && \
apt clean && apt purge && \
rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /data