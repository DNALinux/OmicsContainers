FROM debian:bookworm-slim

LABEL    software="biopython" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    base_image="debian:bookworm-slim" \ 
    container="biopython" \ 
    about.summary="Python library for bioinformatics (implemented in Python 3)" \ 
    about.home="http://biopython.org" \ 
    software.version="1.85-pip" \ 
    upstream.version="1.85" \ 
    version="1" \ 
    about.copyright=" 2002-2009 Biopython contributors" \ 
    about.license="other" \ 
    about.license_file="/usr/share/doc/biopython/copyright" \ 
    about.tags=""

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt-get install -y python3-pip python3-venv && apt clean && apt purge && rm -rf /var/lib/apt/lists/* /tmp/*
RUN python3 -m venv biopython && . biopython/bin/activate && pip install biopython==1.85

# Since this is installed in a venv, run with:
# docker run -it dnalinux/biopython:1.85-pip /biopython/bin/python
