# This template can be used for debian and python programs
# Use bookworm-slim when possible

# Debian versions:
# trixie (testing)
# Debian 12 (bookworm) — current stable release
# Debian 11 (bullseye) — current oldstable release
# Debian 10 (buster) — archived release

FROM debian:bookworm-slim

LABEL    software="bcftools" \ 
    base_image="debian:bookworm-slim" \ 
    container="bcftools" \ 
    about.summary="Variant callilng and file manipulation" \ 
    about.home="https://samtools.github.io/bcftools/howtos/index.html" \ 
    software.version="1.20-deb" \ 
    upstream.version="1.20" \ 
    version="1" \ 
    about.copyright="Genome Research Ltd" \ 
    about.license="other" \ 
    about.license_file="/usr/share/doc/bcftools/copyright" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt-get install -y python3-pip python3-venv && apt clean && apt purge && rm -rf /var/lib/apt/lists/* /tmp/*

# Next line creates a venv and install a python module in this venv
RUN python3 -m venv bcftools && . bcftools/bin/activate && pip install bcftools==1.20
# Since this is installed in a venv, run with:
# docker run -it dnalinux/bcftools:1.20 /bcftools/bin/python
