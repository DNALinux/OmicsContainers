FROM debian:trixie-slim

LABEL software="orthofinder" \
    base_image="debian:trixie-slim" \
    container="orthofinder" \
    about.summary="Accurate inference of orthogroups, orthologues, gene trees and rooted species tree" \
    about.home="https://github.com/davidemms/OrthoFinder" \
    software.version="3.0.1b1-conda" \
    upstream.version="3.0.1b1" \
    version="1" \
    about.license="GPL-3.0" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="genomics,phylogenetics,orthology,orthogroups"

ARG software_version=3.0.1b1
ENV PATH="/opt/miniconda3/envs/orthofinder/bin:/opt/miniconda3/bin:${PATH}"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    useradd --create-home --shell /bin/bash dnalinux

RUN if [ $(uname -m) = x86_64 ] ; then arch=x86_64; \
    elif [ $(uname -m) = aarch64 ] ; then arch=aarch64; \
    else echo "Architecture $(uname -m) is not supported" >&2; exit 1; \
    fi && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-${arch}.sh \
    && bash Miniconda3-latest-Linux-${arch}.sh -b -p /opt/miniconda3 \
    && rm -f Miniconda3-latest-Linux-${arch}.sh

RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r && \
    conda config --remove channels defaults || true && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    conda install --yes mamba && \
    mamba create --yes -n orthofinder orthofinder=${software_version} && \
    conda clean --all --yes && \
    mamba clean --all --yes && \
    chmod -R a+rX /opt/miniconda3

USER dnalinux
WORKDIR /home/dnalinux

CMD ["/bin/bash"]

# Usage examples:
# OrthoFinder 3.0.1b1 is a beta release of the 3.x series: the pre-packaged
# executable was dropped upstream, so this image installs the bioconda package,
# which also pulls every runtime dependency (DIAMOND, MMseqs2, MCL, FastME,
# MAFFT, FastTree, IQ-TREE, RAxML, ASTRAL-Pro3/aster, ...) for the target
# architecture. ASTRAL-Pro3 (conda package "aster") is required by --assign.
#
# ExampleData (four Mycoplasma proteomes) ships inside the image. Note that
# OrthoFinder writes its results next to the input directory, which is inside
# the read-only conda environment, so results must be sent elsewhere with -o:
# docker run -it --rm dnalinux/orthofinder:3.0.1b1-conda \
#     orthofinder -f /opt/miniconda3/envs/orthofinder/share/orthofinder/ExampleData \
#         -o /home/dnalinux/example_out -og
#
# To analyse your own data, mount a directory holding one protein FASTA per
# species and give OrthoFinder enough open files:
# docker run -it --rm --ulimit nofile=1000000:1000000 -v $(pwd)/fastas:/home/dnalinux/fastas \
#     dnalinux/orthofinder:3.0.1b1-conda orthofinder -f /home/dnalinux/fastas -t 8
#
# Version 3 workflow with --core/--assign (adding species to existing orthogroups):
# docker run -it --rm -v $(pwd)/data:/home/dnalinux/data \
#     dnalinux/orthofinder:3.0.1b1-conda \
#     orthofinder --core /home/dnalinux/data/OrthoFinder/Results_Core --assign /home/dnalinux/data/AdditionalSpecies
