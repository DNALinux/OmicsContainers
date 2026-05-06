# This template can be used for debian and python programs
# Use trixie-slim when possible, and never sid
# Debian versions:
# Debian 13 (trixie) - current testing
# Debian 12 (bookworm) — current stable release
# Debian 11 (bullseye) — current oldstable release
# Debian 10 (buster) — archived release

FROM debian:trixie-slim
LABEL    software="biopython" \ 
    base_image="debian:trixie-slim" \ 
    container="biopython" \ 
    about.summary="Python library for bioinformatics (implemented in Python 3)" \ 
    about.home="http://biopython.org" \ 
    software.version="1.84-pip" \ 
    upstream.version="1.84" \ 
    version="1" \ 
    about.copyright=" 2002-2009 Biopython contributors" \ 
    about.license="other" \ 
    about.license_file="/usr/share/doc/biopython/copyright" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
    apt-get install -y python3-pip python3-venv && \
    apt clean && \
    apt purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    useradd --create-home --shell /bin/bash dnalinux

USER dnalinux
WORKDIR /home/dnalinux

# Next line creates a venv and installs a python module in this venv
RUN python3 -m venv biopython && . biopython/bin/activate && pip install biopython==1.84

# Since this is installed in a venv, run with:
# docker run -it dnalinux/biopython:1.84 /home/dnalinux/biopython/bin/python
# To install a Python package outside an environment, use --break-system-packages
