FROM debian:trixie-slim

LABEL    software="muscle" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    container="muscle" \ 
    about.summary="Multiple alignment program of protein sequences" \ 
    about.home="http://www.drive5.com/muscle/" \ 
    software.version="1:5.1.0-1" \ 
    version="1" \ 
    extra.identifiers.biotools="muscle" \ 
    about.copyright=" Robert C. Edgar "Bob" <muscle@drive5.com>" \ 
    about.license="PD-dedication" \ 
    about.license_file="/usr/share/doc/muscle/copyright" \ 
    extra.binaries="/usr/bin/muscle" \ 
    extra.identifiers.conda="muscle" \ 
    about.tags="biology::format:aln, biology::peptidic, field::biology,:biology:bioinformatics, implemented-in::c++,:commandline, role::program, scope::utility, use::comparing,:plaintext, works-with::TODO" 

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y muscle=1:5.1.0-1 && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
