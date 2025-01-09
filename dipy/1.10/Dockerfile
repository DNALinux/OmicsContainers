# This template can be used for debian and python programs
# Use bookworm-slim when possible, trixie only is needed and never sid

# Debian versions:
# Debian 13 (trixie) - current testing
# Debian 12 (bookworm) — current stable release
# Debian 11 (bullseye) — current oldstable release
# Debian 10 (buster) — archived release

FROM debian:bookworm-slim

LABEL    software="dipy" \ 
    base_image="biocontainers/biocontainers:vdebian-buster-backports_cv1" \ 
    container="dipy" \ 
    about.summary="a python package for analyzing diffusion MRI data" \ 
    about.home="https://dipy.org/" \ 
    software.version="1.10.0-pip" \ 
    upstream.version="1.10" \ 
    version="1" \ 
    about.copyright="Copyright 2008-2024,DIPY developers" \ 
    about.license="other" \ 
    about.license_file="/usr/share/doc/dipy/copyright" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt-get install -y python3-pip python3-venv && apt clean && apt purge && rm -rf /var/lib/apt/lists/* /tmp/*

# Next line creates a venv and install a python module in this venv
RUN python3 -m venv dipy && . dipy/bin/activate && pip install dipy==1.10
# Since this is installed in a venv, run with:
# docker run -it dnalinux/dipy:1.10 /dipy/bin/python
# To install a Python package outside a environment, use --break-system-packages
