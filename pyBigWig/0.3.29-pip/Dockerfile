FROM debian:trixie-slim
LABEL software="pyBigWig" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    base_image="debian:trixie-slim" \
    container="pyBigWig" \
    about.summary="Python library for reading and writing bigWig files" \
    about.home="https://github.com/deeptools/pyBigWig" \
    software.version="0.3.29-pip" \
    upstream.version="0.3.29" \
    version="0.3.29" \
    about.copyright="2014-2024, the deepTools team" \
    about.license="MIT" \
    about.license_file="/usr/share/doc/pybigwig/copyright" \
    about.tags=""
USER root
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt-get install -y python3-pip python3-venv && apt clean && rm -rf /var/lib/apt/lists/* /tmp/*
RUN python3 -m venv pyBigWig && . pyBigWig/bin/activate && pip install pyBigWig==0.3.29 numpy
# Since this is installed in a venv, run with:
# docker run -it dnalinux/pybigwig:0.3.29-pip /pyBigWig/bin/python
