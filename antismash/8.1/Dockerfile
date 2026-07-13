FROM debian:trixie-slim
LABEL    software="antismash" \
    base_image="debian:trixie-slim" \
    about.summary="the antibiotics and Secondary Metabolite Analysis SHell" \
    about.home="https://antismash.secondarymetabolites.org/#!/about" \
    software.version="8.1" \
    upstream.version="8.1" \
    version="8.1" \
    about.copyright="" \
    about.license="GNU Affero General Public License version 3.0 or greater" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""
USER root
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y apt-transport-https pip wget gnupg2 && wget http://dl.secondarymetabolites.org/antismash-stretch.list -O /etc/apt/sources.list.d/antismash.list && wget -q -O- http://dl.secondarymetabolites.org/antismash.asc | apt-key add - && apt update
RUN apt install -y hmmer diamond-aligner fasttree prodigal ncbi-blast+ muscle5 glimmerhmm
RUN wget https://github.com/antismash/antismash/archive/refs/tags/8-1.tar.gz && tar -zxf 8-1.tar.gz && rm 8-1.tar.gz
RUN pip install ./antismash-8-1 --break-system-packages
RUN mkdir -p /data/databases/ && ln -s /mnt/disks/bucket/data/databases/ /data/databases/
