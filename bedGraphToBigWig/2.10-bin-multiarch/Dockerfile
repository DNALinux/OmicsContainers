###################################### METADATA ##############################
FROM debian:trixie-slim

ARG TARGETPLATFORM

LABEL base_image="debian:trixie-slim" \
      software="bedGraphToBigWig" \
      software.version="2.10-multiarch" \
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

# UCSC ships pre-compiled binaries per architecture; the aarch64 build requires
# glibc >= 2.38, hence the debian:trixie-slim base.
RUN if [ "$TARGETPLATFORM" = "linux/amd64" ]; then \
        wget -q https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig -O /usr/local/bin/bedGraphToBigWig; \
    elif [ "$TARGETPLATFORM" = "linux/arm64" ]; then \
        wget -q https://hgdownload.soe.ucsc.edu/admin/exe/linux.aarch64/bedGraphToBigWig -O /usr/local/bin/bedGraphToBigWig; \
    else \
        echo "Unsupported platform: $TARGETPLATFORM" >&2 && exit 1; \
    fi && chmod +x /usr/local/bin/bedGraphToBigWig
