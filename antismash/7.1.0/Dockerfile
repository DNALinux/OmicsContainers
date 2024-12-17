
FROM debian:bookworm-slim

LABEL    software="antismash" \
    base_image="debian:bookworm-slim" \
    about.summary="the antibiotics and Secondary Metabolite Analysis SHell" \
    about.home="https://antismash.secondarymetabolites.org/#!/about" \
    software.version="7.1.0" \
    upstream.version="7.1.0" \
    version="7.1.0" \
    about.copyright="" \
    about.license="GNU Affero General Public License version 3.0 or greater" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y apt-transport-https pip wget gnupg2 && wget http://dl.secondarymetabolites.org/antismash-stretch.list -O /etc/apt/sources.list.d/antismash.list && wget -q -O- http://dl.secondarymetabolites.org/antismash.asc | apt-key add - && apt update

RUN apt install -y hmmer2 hmmer diamond-aligner fasttree prodigal ncbi-blast+ muscle glimmerhmm

RUN wget https://dl.secondarymetabolites.org/releases/7.1.0/antismash-7.1.0.tar.gz && tar -zxf antismash-7.1.0.tar.gz && rm antismash-7.1.0.tar.gz

RUN pip install ./antismash-7.1.0 --break-system-packages

RUN mkdir -p /data/databases/ && ln -s /mnt/disks/bucket/data/databases/ /data/databases/
