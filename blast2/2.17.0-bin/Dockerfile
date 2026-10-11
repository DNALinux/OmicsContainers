FROM ubuntu:26.04
ARG version=2.17.0

LABEL maintainer="Sebastian Bassi <sebastian@toyoko.io>"

USER root

RUN mkdir -p /blast/blastdb /blast/blastdb_custom
WORKDIR /blast

RUN if [ $(uname -m) = x86_64 ] ; then arch=x64; \
    elif [ $(uname -m) = aarch64 ] ; then arch=aarch64; \
    fi; \
    apt-get -y -m update && apt-get install -y wget curl libidn-dev perl liblist-moreutils-perl perl-doc libgomp1 libxml2-16 libsqlite3-dev; \
    wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-${version}+-${arch}-linux.tar.gz && \
    tar xzf ncbi-blast-${version}+-${arch}-linux.tar.gz --strip-components=1 && rm ncbi-blast-${version}+-${arch}-linux.tar.gz

RUN sed -i '$ a BLASTDB=/blast/blastdb:/blast/blastdb_custom' /etc/environment
ENV BLASTDB=/blast/blastdb:/blast/blastdb_custom
ENV BLAST_DOCKER=true
ENV PATH="/blast/bin:${PATH}"

CMD ["/bin/sh"]
