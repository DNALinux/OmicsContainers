###################################### METADATA ##############################
FROM debian:bookworm-slim

LABEL base_image="debian:bookworm-slim" \
      software="AllHiC" \
      software.version="0.9.14" \
      about.summary="AllHiC is a pipeline for Hi-C scaffolding of contigs" \
      about.home="https://github.com/tanghaibao/allhic" \
      upstream.version="0.9.14" \
      about.copyright="MIT" \
      about.license="other" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      about.tags="field::biology:bioinformatics"

USER root

ENV DEBIAN_FRONTEND=noninteractive

################################ INSTALL DEPENDENCIES ##############################
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    make \
    gcc \
    bzip2 \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev \
    libcurl4-openssl-dev \
    golang-go && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates

################################ INSTALL ALLHIC ##############################
# Note: There is a version with incorrectly reports as 0.9.13, so I manually 
# change it to 0.9.14
RUN wget https://github.com/tanghaibao/allhic/archive/refs/tags/v0.9.14.tar.gz && \
    tar xvfz v0.9.14.tar.gz && \
    cd allhic-0.9.14 && \
    sed 's/0.9.13/0.9.14/g' base.go > temp && mv temp base.go && \
    go build -o allhic ./cmd/main.go && \
    mv allhic /usr/local/bin/ && \
    chmod +x /usr/local/bin/allhic && \
    cd .. && \
    rm -rf v0.9.14.tar.gz allhic-0.9.14

################################ SET ENTRYPOINT ##############################
ENTRYPOINT ["allhic"]

