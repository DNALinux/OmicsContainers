# syntax=docker/dockerfile:1
###################################### METADATA ##############################
FROM debian:trixie-slim AS binaries
COPY bedGraphToBigWig.x86_64 bedGraphToBigWig.aarch64 /binaries/

FROM debian:trixie-slim

ARG TARGETPLATFORM

LABEL base_image="debian:trixie-slim" \
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

# debian:trixie-slim provides glibc >= 2.38, needed by the aarch64 binary.
# Copy only the binary matching the build platform into the final image.
RUN --mount=type=bind,from=binaries,source=/binaries,target=/binaries \
    if [ "$TARGETPLATFORM" = "linux/amd64" ]; then \
        cp /binaries/bedGraphToBigWig.x86_64 /usr/local/bin/bedGraphToBigWig; \
    elif [ "$TARGETPLATFORM" = "linux/arm64" ]; then \
        cp /binaries/bedGraphToBigWig.aarch64 /usr/local/bin/bedGraphToBigWig; \
    else \
        echo "Unsupported platform: $TARGETPLATFORM" >&2 && exit 1; \
    fi && chmod +x /usr/local/bin/bedGraphToBigWig
