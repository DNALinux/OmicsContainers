FROM debian:trixie-slim

LABEL version="1.2.4"
LABEL about.summary="Making accurate alignments of many protein sequences"
LABEL software="Clustal Omega"
LABEL software.version="1.2.4"
LABEL maintainer="Sebastian Bassi <sebastian@toyoko.io>"
LABEL about.tags="Genomics"
LABEL about.home="http://www.clustal.org/omega/"
LABEL about.license="GPL-3.0"
LABEL about.author="Wang, Liguo"


ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y clustalo=1.2.4-8 && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
