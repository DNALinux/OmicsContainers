FROM debian:trixie-slim
LABEL    software="antismash" \
    base_image="debian:trixie-slim" \
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

# 1. Install build utilities, Python environment, and Debian's native bioinformatic binaries
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    build-essential \
    ca-certificates \
    python3-pip \
    python3-venv \
    python3-dev \
    wget \
    hmmer \
    diamond-aligner \
    fasttree \
    prodigal \
    ncbi-blast+ \
    muscle \
    tigr-glimmer \
    && rm -rf /var/lib/apt/lists/*



# 2. Download, compile, and install GlimmerHMM to /usr/local/bin/
RUN wget https://ccb.jhu.edu/software/glimmerhmm/dl/GlimmerHMM-3.0.4.tar.gz \
    && tar -xzf GlimmerHMM-3.0.4.tar.gz \
    && cd GlimmerHMM/sources \
    && make \
    && cp glimmerhmm /usr/local/bin/ \
    && cd ../.. \
    && rm -rf GlimmerHMM GlimmerHMM-3.0.4.tar.gz

# 3. Download, extract and install antiSMASH
RUN wget https://github.com/antismash/antismash/archive/refs/tags/8-0-4.tar.gz \
    && tar -zxf 8-0-4.tar.gz \
    && rm 8-0-4.tar.gz


RUN pip install "biopython>=1.86" --break-system-packages

#RUN sed -i 's/"biopython == 1.81"/"biopython>=1.86"/' ./antismash-8-0-4/setup.py
RUN find ./antismash-8-0-4 -type f -exec sed -i 's/biopython\s*==\s*1.81/biopython>=1.86/g' {} +


RUN pip install ./antismash-8-0-4 --break-system-packages



RUN mkdir -p /data/databases/ && ln -s /mnt/disks/bucket/data/databases/ /data/databases/
