FROM debian:bookworm-slim

LABEL    software="Quast" \
    base_image="debian:bookworm-slim" \
    about.summary="QUAST stands for QUality ASsessment Tool. The tool evaluates genome assemblies by computing various metrics." \
    about.home="https://quast.sourceforge.net/" \
    software.version="5.3.0" \
    upstream.version="5.3.0" \
    version="5.3.0" \
    about.copyright="" \
    about.license="GPL v2" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

# Setup a base system
RUN apt update && \
    apt install -y curl wget g++ make libboost-all-dev git \
        tar gzip bzip2 build-essential \
        python3-dev python3-setuptools python3-pip python3-venv \
        zlib1g-dev default-jdk perl && \
    apt upgrade -y libstdc++6

# Matplotlib dependencies
RUN apt update && apt install -y pkg-config libfreetype6-dev \
    libpng-dev python3-matplotlib

# QUAST installation
RUN wget https://github.com/ablab/quast/releases/download/quast_5.3.0/quast-5.3.0.tar.gz && \
    tar -xzf quast-5.3.0.tar.gz && rm quast-5.3.0.tar.gz 

WORKDIR /quast-5.3.0

RUN pip3 install --upgrade --break-system-packages setuptools pip && \
    python3 setup.py install_full