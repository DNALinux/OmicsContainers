FROM ubuntu:22.04
ARG version=2.15.0

LABEL software="blast2" \
      base_image="ubuntu:22.04" \
      about.summary="NCBI BLAST+ executable for searching nucleotide and protein databases" \
      about.home="https://blast.ncbi.nlm.nih.gov/Blast.cgi" \
      software.version="2.15.0-bin" \
      upstream.version="2.15.0" \
      version="1" \
      about.copyright="" \
      about.license="Public Domain" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      about.tags="field::biology:bioinformatics, ncbi, blast, sequence-alignment"

USER root

RUN apt-get -y -m update && apt-get install -y wget curl libidn-dev libnet-perl liblist-moreutils-perl perl-doc libgomp1 libxml2 libsqlite3-dev

RUN mkdir -p /blast/blastdb /blast/blastdb_custom
WORKDIR /blast

RUN if [ $(uname -m) = x86_64 ] ; then arch=x64; \
    elif [ $(uname -m) = aarch64 ] ; then arch=aarch64; \
    else echo "Architecture $(uname -m) is not supported" >&2; exit 1; \
    fi && \
    wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${version}/ncbi-blast-${version}+-${arch}-linux.tar.gz && \
    tar xzf ncbi-blast-${version}+-${arch}-linux.tar.gz --strip-components=1 && \
    rm ncbi-blast-${version}+-${arch}-linux.tar.gz

# Needed for 2.13.0 Linux amd64 release
RUN if [ -d "ncbi-blast-${version}+" ] ; then \
       cp -R "ncbi-blast-${version}+/bin" . ; \
       rm -R "ncbi-blast-${version}+"; \
    fi

RUN sed -i '$ a BLASTDB=/blast/blastdb:/blast/blastdb_custom' /etc/environment
ENV BLASTDB=/blast/blastdb:/blast/blastdb_custom
ENV BLAST_DOCKER=true
ENV PATH="/blast/bin:${PATH}"

CMD ["/bin/sh"]
