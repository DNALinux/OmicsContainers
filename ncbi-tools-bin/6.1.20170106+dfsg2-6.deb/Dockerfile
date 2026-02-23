FROM debian:trixie-slim

LABEL    software="ncbi-tools-bin" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.summary="NCBI libraries for biology applications (text-based utilities)" \ 
    about.home="" \ 
    software.version="6.1.20170106+dfsg2-6" \ 
    about.copyright=" NCBI" \ 
    about.license="PD" \ 
    about.tags="field::biology,:biology:bioinformatics, implemented-in::c++,:commandline, role::program, scope::utility, use::comparing,:plaintext, works-with::TODO" 

ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y ncbi-tools-bin=6.1.20170106+dfsg2-6 && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
