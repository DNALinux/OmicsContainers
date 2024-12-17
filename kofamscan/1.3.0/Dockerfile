FROM debian:trixie-slim

LABEL    software="kofamscan" \
    base_image="debian:trixie-slim" \
    about.summary="KofamScan is a gene function annotation tool based on KEGG Orthology and hidden Markov model. You need KOfam database to use this tool" \
    about.home="https://www.genome.jp/tools/kofamkoala/" \
    software.version="1.3.0" \
    upstream.version="1.3.0" \
    version="1" \
    about.copyright="Aramaki T., Blanc-Mathieu R., Endo H., Ohkubo K., Kanehisa M., Goto S., Ogata H." \
    about.license="MIT" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND=noninteractive

# Variable for architectures
ARG TARGETARCH
RUN echo $TARGETARCH

RUN if [ "$TARGETARCH" = "arm64" ]; then \
        echo "Building for ARM64 architecture"; \
        export VERSION="3.4+dfsg-2+b1"; \
    elif [ "$TARGETARCH" = "amd64" ]; then \
        echo "Building for AMD64 architecture"; \
        export VERSION="3.4+dfsg-2"; \
    fi && \
    apt update && \
    apt install -y wget ruby hmmer=$VERSION parallel && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/takaram/kofam_scan/archive/refs/tags/v1.3.0.tar.gz && tar xvfz v1.3.0.tar.gz && rm v1.3.0.tar.gz

# run: ./kofam_scan-1.3.0/exec_annotation
