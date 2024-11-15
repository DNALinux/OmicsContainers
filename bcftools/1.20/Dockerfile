FROM debian:trixie-slim

ARG TARGETARCH

LABEL    software="bcftools" \
    base_image="debian:bookworm-slim" \
    container="bcftools" \
    about.summary="Variant callilng and file manipulation" \
    about.home="https://samtools.github.io/bcftools/howtos/index.html" \
    software.version="1.20" \
    upstream.version="1.20" \
    version="1" \
    about.copyright="Genome Research Ltd" \
    about.license="other" \
    about.license_file="/usr/share/doc/bcftools/copyright" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND noninteractive

RUN echo $TARGETARCH

RUN if [ "$TARGETARCH" = "arm64" ]; then \
        echo "Building for ARM64 architecture"; \
        export VERSION="1.20-2+b1"; \
    elif [ "$TARGETARCH" = "amd64" ]; then \
        echo "Building for AMD64 architecture"; \
        export VERSION="1.20-2"; \
    fi && \
    apt-get update && \
    apt-get install -y bcftools=$VERSION && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["bcftools"]
