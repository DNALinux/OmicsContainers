FROM debian:trixie-slim

LABEL    software="hmmer" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    base_image="debian:trixie-slim" \ 
    container="hmmer" \ 
    about.summary="profile hidden Markov models for protein sequence analysis" \ 
    about.home="http://hmmer.org/" \ 
    software.version="3.4+dfsg-2-deb" \ 
    upstream.version="3.4" \ 
    version="1" \ 
    about.copyright="1992-2010 Sean R. Eddy <eddy@genetics.wustl.edu>" \ 
    about.license="GPL-3" \ 
    about.license_file="/usr/share/doc/hmmer/copyright" \ 
    extra.binaries="/usr/bin/alimask,/usr/bin/hmmalign,/usr/bin/hmmbuild,/usr/bin/hmmconvert,/usr/bin/hmmemit,/usr/bin/hmmfetch,/usr/bin/hmmlogo,/usr/bin/hmmpgmd,/usr/bin/hmmpress,/usr/bin/hmmscan,/usr/bin/hmmsearch,/usr/bin/hmmsim,/usr/bin/hmmstat,/usr/bin/jackhmmer,/usr/bin/makehmmerdb,/usr/bin/nhmmer,/usr/bin/nhmmscan,/usr/bin/phmmer" \ 
    about.tags="biology::format:aln, biology::peptidic, field::biology,:biology:bioinformatics, implemented-in::c,:commandline, role::program, scope::utility, use::searching,:plaintext, works-with::db" 

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y hmmer=3.4+dfsg-2 && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
