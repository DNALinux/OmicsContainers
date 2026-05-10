FROM debian:trixie-slim

LABEL software="fastp" \
    base_image="debian:trixie-slim" \
    container="fastp" \
    about.summary="An ultra-fast all-in-one FASTQ preprocessor" \
    about.home="https://github.com/OpenGene/fastp" \
    software.version="1.3.3" \
    upstream.version="1.3.3" \
    version="1" \
    about.license="MIT" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="genomics,qc,trimming,fastq"

ARG software_version=1.3.3
ENV PATH="/opt/miniconda3/bin:${PATH}"
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
    conda install --yes fastp=${software_version} && \
    conda clean --all --yes && \
    chmod -R a+rX /opt/miniconda3

USER dnalinux
WORKDIR /home/dnalinux

CMD ["/bin/bash"]

# Usage examples:
# docker run -it dnalinux/fastp:1.3.3-conda fastp --in1 input.fastq --out1 output.fastq
# docker run -it -v $(pwd):/home/dnalinux dnalinux/fastp:1.3.3-conda fastp --in1 input.fastq --out1 output.fastq
