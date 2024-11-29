FROM debian:bookworm-slim

###################################### METADATA ##############################
LABEL base_image="biocontainers:latest" \
  software="hsfiasm" \
  software.version="0.20.0" \
  about.summary="Hifiasm is a haplotype-resolved de novo assembler designed for HiFi reads." \
  about.home="https://github.com/chhylp123/hifiasm" \
  about.documentation="https://github.com/chhylp123/hifiasm/blob/master/LICENSE" \
  about.license="MIT" \
  about.tags="bioinformatics, genomics, pacbio"
  
ENV DEBIAN_FRONTEND=noninteractive
################## BEGIN INSTALLATION #######################
USER root

RUN apt-get update -qq && \
    apt-get install -y -q --fix-missing \
      libncurses5-dev  \
      libncursesw5-dev \
      build-essential \
      wget \
      zlib1g-dev && \
    apt-get clean && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir /data /config

ARG URL=https://github.com/chhylp123/hifiasm/archive/refs/tags/
ARG VER=0.20.0
# https://github.com/chhylp123/hifiasm/archive/refs/tags/0.20.0.tar.gz
RUN wget ${URL}${VER}.tar.gz && \
    tar xvfz ${VER}.tar.gz && \
    rm ${VER}.tar.gz && \
    cd hifiasm-${VER} && \
    make && cd .. && mv hifiasm-${VER}/hifiasm /usr/local/bin/ && \
    rm -rf hifiasm-${VER}
