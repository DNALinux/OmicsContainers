FROM debian:trixie-slim

LABEL    software="kofamscan" \
    base_image="debian:trixie-slim" \
    about.summary="" \
    about.home="" \
    software.version="" \
    upstream.version="" \
    version="1" \
    about.copyright="" \
    about.license="" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y git ruby hmmer=3.4+dfsg-2 parallel && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/takaram/kofam_scan.git

