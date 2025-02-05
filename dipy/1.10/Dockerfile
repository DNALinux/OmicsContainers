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

ARG TARGETARCH    
USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt-get install -y python3-pip python3-venv wget && apt clean && apt purge && rm -rf /var/lib/apt/lists/* /tmp/*

RUN if [ "$TARGETARCH" = "amd64" ]; then \
        echo "Building for x86_64" && \
        python3 -m venv dipy && . dipy/bin/activate && pip install dipy[all]==1.10 fury ; \
    elif [ "$TARGETARCH" = "arm64" ]; then \
        echo "Building for ARM64" && \
        python3 -m venv dipy && . dipy/bin/activate && pip install dipy==1.10 ;\
    else \
        echo "Unsupported architecture: $TARGETARCH" && exit 1; \
    fi

# How to run:
# docker run -it dnalinux/dipy:1.10 /dipy/bin/python
