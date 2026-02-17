FROM debian:sid-slim
LABEL    software="samtools" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \   
    base_image="biocontainers/biocontainers:vdebian-buster-backports_cv1" \ 
    container="samtools" \ 
    about.summary="processing sequence alignments in SAM, BAM and CRAM formats" \ 
    about.home="http://www.htslib.org/" \ 
    software.version="1.23-sc" \ 
    upstream.version="1.23" \ 
    version="1.23" \ 
    extra.identifiers.biotools="samtools" \ 
    about.copyright=" 20082016, Genome Research Ltd. (GRL)" \ 
    about.license="MIT/Expat" \ 
    about.license_file="/usr/share/doc/samtools/copyright" \ 
    about.tags="field::biology, field::biology:bioinformatics, implemented-in::c,:commandline, network::client, protocol::ftp, protocol::http,:program, scope::utility, uitoolkit::ncurses, use::analysing,:calculating,:filtering, works-with::biological-sequence" 

USER root
ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y autoconf wget bzip2 automake make gcc perl zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev libncurses5-dev libdeflate-dev && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*

RUN wget https://github.com/samtools/samtools/releases/download/1.23/samtools-1.23.tar.bz2
RUN tar -xjf samtools-1.23.tar.bz2
WORKDIR /samtools-1.23
RUN ./configure --prefix=/usr/local
RUN make
RUN make install
