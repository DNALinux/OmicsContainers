FROM debian:trixie-slim

LABEL software="checkm2" \
    base_image="debian:trixie-slim" \
    container="checkm2" \
    about.summary="Rapid assessment of genome bin quality using machine learning" \
    about.home="https://github.com/chklovski/CheckM2" \
    software.version="1.1.0-conda" \
    upstream.version="1.1.0" \
    version="1" \
    about.license="GPL-3.0" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="genomics,metagenomics,binning,qc"

ARG software_version=1.1.0
ENV PATH="/opt/miniconda3/envs/checkm2/bin:/opt/miniconda3/bin:${PATH}"
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
    mamba create --yes -n checkm2 checkm2=${software_version} && \
    conda clean --all --yes && \
    mamba clean --all --yes && \
    chmod -R a+rX /opt/miniconda3

USER dnalinux
WORKDIR /home/dnalinux

CMD ["/bin/bash"]

# Usage examples:
# The DIAMOND database is NOT included in this image. Download it first
# (~1.7 GB download, several GB on disk):
# docker run -it -v $(pwd)/db:/home/dnalinux/db dnalinux/checkm2:1.1.0-conda \
#     checkm2 database --download --path /home/dnalinux/db
# Then run predictions, mounting both the DB and your input genomes:
# docker run -it -v $(pwd)/db:/home/dnalinux/db -v $(pwd)/genomes:/home/dnalinux/genomes \
#     dnalinux/checkm2:1.1.0-conda \
#     checkm2 predict --input /home/dnalinux/genomes --output-directory /home/dnalinux/out \
#         --database_path /home/dnalinux/db/uniref100.KO.1.dmnd
# (Alternatively set CHECKM2DB=/home/dnalinux/db inside the container and omit --database_path.)
