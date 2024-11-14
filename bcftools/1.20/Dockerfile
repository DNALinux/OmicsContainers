FROM debian:trixie-slim

LABEL    software="bcftools" \ 
    base_image="debian:trixie-slim" \ 
    container="bcftools" \ 
    about.summary="Variant callilng and file manipulation" \ 
    about.home="https://samtools.github.io/bcftools/howtos/index.html" \ 
    software.version="1.20-src" \ 
    upstream.version="1.20" \ 
    version="1" \ 
    about.copyright="Genome Research Ltd" \ 
    about.license="other" \ 
    about.license_file="/usr/share/doc/bcftools/copyright" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y wget make gcc bzip2 libbz2-dev liblzma-dev zlib1g-dev libcurl4-openssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN wget https://github.com/samtools/bcftools/releases/download/1.20/bcftools-1.20.tar.bz2 && \
    tar -xvjf bcftools-1.20.tar.bz2 && \
    cd bcftools-1.20 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf bcftools-1.20 bcftools-1.20.tar.bz2
ENTRYPOINT ["bcftools"]

