FROM debian:trixie-slim

LABEL version="1.21"
LABEL about.summary="generic indexer for TAB-delimited genome position files"
LABEL software="tabix"
LABEL software.version="1.21+ds-1"
LABEL maintainer="Sebastian Bassi <sebastian@toyoko.io>"
LABEL about.tags="Genomics"
LABEL about.home="https://www.htslib.org/doc/tabix.html"
LABEL about.license="GPL-3.0"
LABEL about.author=" Heng Li."


ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tabix=1.21+ds-1 && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
