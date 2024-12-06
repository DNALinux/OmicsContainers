FROM debian:trixie-slim

LABEL    software="diamond" \
    base_image="debian:trixie-slim" \
    about.summary="Accelerated BLAST compatible local sequence aligner." \
    about.home="https://github.com/bbuchfink/diamond" \
    about.documentation="http://www.diamondsearch.org" \
    software.version="2.1.10" \
    upstream.version="2.1.10.164" \
    about.copyright="Benjamin Buchfink" \
    about.license="GPL 3.0" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget

RUN wget https://github.com/bbuchfink/diamond/releases/download/v2.1.10/diamond-linux64.tar.gz && \
  tar xvfz diamond-linux64.tar.gz && rm diamond-linux64.tar.gz

# run with ./diamond CMD
