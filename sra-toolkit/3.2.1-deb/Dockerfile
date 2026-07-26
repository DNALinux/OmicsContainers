FROM debian:trixie-slim
 
LABEL software="sra-toolkit" \
      base_image="debian:trixie-slim" \
      container="sra-toolkit" \
      about.summary="utilities for the NCBI Sequence Read Archive" \
      about.home="https://github.com/ncbi/sra-tools" \
      software.version="3.2.1+dfsg-4" \
      upstream.version="3.2.1" \
      version="1" \
      about.license="public-domain" \
      about.license_file="/usr/share/doc/sra-toolkit/copyright" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      about.tags="genomics,sequencing,ncbi,sra"
 
ENV DEBIAN_FRONTEND noninteractive
 
RUN apt-get update && \
    apt-get install -y sra-toolkit=3.2.1+dfsg-4 && \
    apt-get clean && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    useradd --create-home --shell /bin/bash dnalinux
 
USER dnalinux
WORKDIR /home/dnalinux
