FROM debian:trixie-slim
 
LABEL software="sra-toolkit" \
      base_image="debian:trixie-slim" \
      container="sra-toolkit" \
      about.summary="utilities for the NCBI Sequence Read Archive" \
      about.home="https://github.com/ncbi/sra-tools" \
      software.version="3.4.1" \
      upstream.version="3.4.1" \
      version="1" \
      about.license="public-domain" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      about.tags="genomics,sequencing,ncbi,sra"
 
ENV DEBIAN_FRONTEND=noninteractive
ENV SRA_VERSION=3.4.1
ENV SRA_URL=https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/${SRA_VERSION}/sratoolkit.${SRA_VERSION}-ubuntu64.tar.gz
 
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    wget -q "${SRA_URL}" -O /tmp/sratoolkit.tar.gz && \
    tar -xzf /tmp/sratoolkit.tar.gz -C /opt && \
    mv /opt/sratoolkit.${SRA_VERSION}-ubuntu64 /opt/sratoolkit && \
    rm /tmp/sratoolkit.tar.gz && \
    apt-get purge -y --auto-remove wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    useradd --create-home --shell /bin/bash dnalinux
 
ENV PATH="/opt/sratoolkit/bin:${PATH}"
 
USER dnalinux
WORKDIR /home/dnalinux
