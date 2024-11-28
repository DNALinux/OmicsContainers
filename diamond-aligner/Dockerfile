FROM debian:trixie

LABEL \
    software="diamond" \
    base_image="debian:trixie" \
    container="diamond-aligner" \
    about.summary="DIAMOND is a sequence aligner for protein and translated DNA searches,\
    designed for high performance analysis of big sequence data" \
    about.home="https://github.com/bbuchfink/diamond/" \
    software.version="2.1.9-1" \
    upstream.version="2.1.10" \
    version="2.1.9-1" \
    about.copyright="DIAMOND authors" \
    about.license="GPL-3.0" \
    about.license_file="/usr/share/doc/diamond/copyright" \
    maintainer="Facundo Mercado <facu.mercado1224@gmail.com>" \
    about.tags="bioinformatics, sequence alignment, protein clustering"

USER root

# 1 warning found LegacyKeyValueFormat: "ENV key=value" should be used instead of legacy "ENV key value" format (line 21)
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt-get install -y \
    diamond-aligner=2.1.9-1 \
    && apt clean && apt purge \
    && rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /data

ENTRYPOINT ["diamond"]

CMD ["--help"]