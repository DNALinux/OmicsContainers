FROM debian:bookworm-slim

MAINTAINER Sebastian Bassi <sebastian@toyoko.io>
LABEL software="bcftools" \ 
    base_image="debian:bookworm-slim" \ 
    container="bcftools" \ 
    about.summary="Variant callilng and file manipulation" \ 
    about.home="https://samtools.github.io/bcftools/howtos/index.html" \ 
    software.version="1.21-src" \ 
    upstream.version="1.21" \ 
    version="1" \ 
    about.copyright="Genome Research Ltd" \ 
    about.license="other" \ 
    about.license_file="/usr/share/doc/bcftools/copyright" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="field::biology:bioinformatics"

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y \
    wget \
    make \
    gcc \
    bzip2 \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev \
    libcurl4-openssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN wget https://github.com/samtools/bcftools/releases/download/1.21/bcftools-1.21.tar.bz2 && \
    tar -xvjf bcftools-1.21.tar.bz2 && \
    cd bcftools-1.21 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf bcftools-1.21 bcftools-1.21.tar.bz2
ENTRYPOINT ["bcftools"]

