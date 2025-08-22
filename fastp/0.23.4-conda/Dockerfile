FROM debian:bookworm-slim

LABEL    software="fastp" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>"

ARG software_version=0.23.4

ENV PATH="/root/miniconda3/bin:${PATH}"
RUN apt update && apt install -y wget && rm -rf /var/lib/apt/lists/*

RUN if [ $(uname -m) = x86_64 ] ; then arch=x86_64; \
    elif [ $(uname -m) = aarch64 ] ; then arch=aarch64; \
    else echo "Architecture $(uname -m) is not supported" >&2; exit 1; \
    fi && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-${arch}.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-${arch}.sh -b \
    && rm -f Miniconda3-latest-Linux-${arch}.sh

RUN conda config --add channels bioconda conda-forge
RUN conda install fastp=$software_version

CMD ["/bin/sh"]
WORKDIR /data/
