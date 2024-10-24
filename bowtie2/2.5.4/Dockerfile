FROM continuumio/miniconda3

LABEL    software="bowtie2" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>"

ARG software_version=2.5.4

RUN conda config --add channels bioconda
RUN conda install conda-forge::libgcc-ng
RUN conda install ncurses bowtie2=$software_version

CMD ["/bin/sh"]



