FROM debian:trixie-slim

LABEL    software="spades" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    base_image="debian:trixie-slim" \
    container="spades" \
    about.summary="genome assembler for single-cell and isolates data sets" \
    about.home="https://ablab.github.io/spades/" \
    software.version="4.2.0" \
    extra.identifiers.biotools="spades" \
    about.paper="Prjibelski A, Antipov D, Meleshko D, Lapidus A, Korobeynikov A (2020) Using SPAdes de novo assembler. Current Protocols in Bioinformatics 70(1): e102. https://doi.org/10.1002/cpbi.102" \
    about.license="GPL-2+" \
    about.tags="biology::nucleic-acids, field::biology, field::biology:bioinformatics,:c++,:python, interface::commandline,:program, scope::utility, works-with::biological-sequence,:file"

USER root

RUN apt-get update && apt-get install -y \
        build-essential \
        cmake \
        wget \
        libbz2-dev \
        git \
        libopenmpi-dev \
        openmpi-bin \
        python3 \
        python3-pip \
        python3-dev \
        python3-setuptools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN wget https://github.com/ablab/spades/releases/download/v4.2.0/SPAdes-4.2.0.tar.gz

RUN tar xfz SPAdes-4.2.0.tar.gz && rm SPAdes-4.2.0.tar.gz && cd SPAdes-4.2.0/ && \
    cmake -B build/ -S src/ -DSPADES_USE_NCBISDK=ON -DSPADES_ENABLE_PROJECTS=all && \
    cmake --build build/ -j4 && cmake --install build/ && cd .. && rm -rf SPAdes-4.2.0/

CMD ["/bin/bash"]

# spades.py --test
