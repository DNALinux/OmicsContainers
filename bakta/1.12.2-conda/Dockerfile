FROM debian:trixie-slim

LABEL software="bakta" \
    base_image="debian:trixie-slim" \
    container="bakta" \
    about.summary="Rapid and standardized annotation of bacterial genomes, MAGs and plasmids" \
    about.home="https://github.com/oschwengers/bakta" \
    software.version="1.12.2-conda" \
    upstream.version="1.12.2" \
    version="1" \
    about.license="GPL-3.0" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="genomics,annotation,bacteria,prokaryotes"

ARG software_version=1.12.2
ENV PATH="/opt/miniconda3/envs/bakta/bin:/opt/miniconda3/bin:${PATH}"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    useradd --create-home --shell /bin/bash dnalinux

# Bakta 1.12.x requires BLAST+ >= 2.17.0, but bioconda publishes no
# linux-aarch64 build of BLAST+ newer than 2.16.0. The conda solve therefore
# only resolves on x86_64, so fail early with that reason instead of letting
# the solver fail with a message about an unsatisfiable dependency.
RUN if [ $(uname -m) = x86_64 ] ; then arch=x86_64; \
    else echo "Bakta 1.12.2 is only available for linux/amd64: bioconda has no linux-aarch64 BLAST+ >= 2.17.0" >&2; exit 1; \
    fi && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-${arch}.sh \
    && bash Miniconda3-latest-Linux-${arch}.sh -b -p /opt/miniconda3 \
    && rm -f Miniconda3-latest-Linux-${arch}.sh

RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r && \
    conda config --remove channels defaults || true && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    conda install --yes mamba && \
    mamba create --yes -n bakta bakta=${software_version} && \
    conda clean --all --yes && \
    mamba clean --all --yes && \
    chmod -R a+rX /opt/miniconda3

USER dnalinux
WORKDIR /home/dnalinux

CMD ["/bin/bash"]

# Usage examples:
# The Bakta database is NOT included in this image: ~1.3 GB compressed
# (~3.9 GB unpacked) for the light build and ~30 GB (~84 GB unpacked) for the
# full one. Download it once onto the host, with the output directory mounted,
# so it survives the container:
# docker run -it --rm -v $(pwd)/bakta_db:/home/dnalinux/db \
#     dnalinux/bakta:1.12.2-conda \
#     bakta_db download --output /home/dnalinux/db --type light
# That creates /home/dnalinux/db/db-light (the full build is unpacked as
# /home/dnalinux/db/db). Then annotate a genome:
# docker run -it --rm -v $(pwd)/bakta_db:/home/dnalinux/db \
#     -v $(pwd)/data:/home/dnalinux/data \
#     dnalinux/bakta:1.12.2-conda \
#     bakta --db /home/dnalinux/db/db-light --output /home/dnalinux/data/out \
#         --prefix mygenome --threads 8 /home/dnalinux/data/genome.fasta
# (Alternatively set BAKTA_DB=/home/dnalinux/db/db-light and omit --db.)
