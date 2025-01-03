###################################### METADATA ##############################
FROM debian:bookworm-slim

LABEL base_image="debian:bookworm-slim" \
      software="AllHiC" \
      software.version="0.9.13" \
      about.summary="AllHiC is a pipeline for Hi-C scaffolding of contigs" \
      about.home="https://github.com/tanghaibao/allhic" \
      upstream.version="0.9.13" \
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
RUN wget https://github.com/tanghaibao/allhic/archive/refs/tags/v0.9.13.tar.gz && \
    tar -xvzf v0.9.13.tar.gz && \
    cd allhic-0.9.13 && \
    go mod init github.com/tanghaibao/allhic && \
    go get ./... && \
    go build -o allhic ./cmd/main.go && \
    mv allhic /usr/local/bin/ && \
    chmod +x /usr/local/bin/allhic && \
    cd .. && \
    rm -rf v0.9.13.tar.gz allhic-0.9.13

################################ SET ENTRYPOINT ##############################
ENTRYPOINT ["allhic"]

