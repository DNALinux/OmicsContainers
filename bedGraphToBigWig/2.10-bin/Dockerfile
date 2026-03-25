###################################### METADATA ##############################
FROM debian:bookworm-slim

LABEL base_image="debian:bookworm-slim" \
      software="bedGraphToBigWig" \
      software.version="2.10" \
      about.summary="Convert bedGraph to bigWig file" \
      about.home="https://hgdownload.soe.ucsc.edu/downloads.html" \
      upstream.version="2.10" \
      about.copyright="https://genome.ucsc.edu/license/" \
      about.license="MIT" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      about.tags="field::biology:bioinformatics"

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y ca-certificates wget && update-ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig && \
    mv bedGraphToBigWig /usr/local/bin/ && \
    chmod +x /usr/local/bin/bedGraphToBigWig

