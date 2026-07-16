FROM python:3.11-slim-bookworm
LABEL    software="antismash" \
    base_image="python:3.11-slim-bookworm" \
    about.summary="the antibiotics and Secondary Metabolite Analysis SHell" \
    about.home="https://antismash.secondarymetabolites.org/#!/about" \
    software.version="8.0.4" \
    upstream.version="8.0.4" \
    version="8.0.4" \
    about.copyright="" \
    about.license="GNU Affero General Public License version 3.0 or greater" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""
USER root
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y apt-transport-https pip wget gnupg2 && \
    apt update
RUN apt install -y hmmer2 diamond-aligner fasttree prodigal ncbi-blast+
RUN wget https://github.com/antismash/antismash/archive/refs/tags/8-0-4.tar.gz && tar -zxf 8-0-4.tar.gz && rm 8-0-4.tar.gz
RUN pip install ./antismash-8-0-4 --break-system-packages
RUN mkdir -p /data/databases/ && ln -s /mnt/disks/bucket/data/databases/ /data/databases/
