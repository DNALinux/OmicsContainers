FROM debian:trixie-slim

LABEL    software="ncbi-dataset" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.summary="resource that lets you easily gather data from across NCBI databases" \ 
    about.home="https://www.ncbi.nlm.nih.gov/datasets/docs/v2/getting_started/" \ 
    software.version="18.18.0" \ 
    about.copyright=" NCBI" \ 
    about.license="PD" \ 
    about.tags="field::biology,:biology:bioinformatics, implemented-in::c++,:commandline, role::program, scope::utility, use::comparing,:plaintext, works-with::TODO" 

ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y curl && apt clean && apt purge && rm -rf /var/lib/apt/lists/* /tmp/*

RUN case "$(uname -m)" in \
    x86_64) curl -o datasets 'https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets' ;; \
    aarch64) curl -o datasets 'https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-arm64/datasets' ;; \
    armv7l|armv6l) curl -o datasets 'https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-arm/datasets' ;; \
    *) echo "Unsupported architecture: $(uname -m)" && exit 1 ;; \
    esac

RUN chmod +x datasets

# HOW TO USE:
#
# docker run -it -v $(pwd):/ftmp dnalinux/ncbi-datasets:18.18.0 /bin/bash
# /datasets download genome taxon "Escherichia coli" --filename /ftmp/ecoli_dataset.zip