FROM debian:trixie-slim

LABEL software="bakta" \
    base_image="debian:trixie-slim" \
    container="bakta" \
    about.summary="Rapid and standardized annotation of bacterial genomes, MAGs and plasmids" \
    about.home="https://github.com/oschwengers/bakta" \
    software.version="1.12.2-conda" \
    upstream.version="1.12.2" \
    version="2" \
    about.license="GPL-3.0" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="genomics,annotation,bacteria,prokaryotes"

ARG software_version=1.12.2
# NCBI BLAST+ release used on aarch64, where bioconda has no BLAST+ >= 2.17.0.
ARG blast_version=2.17.0
ENV PATH="/opt/miniconda3/envs/bakta/bin:/opt/miniconda3/bin:${PATH}"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates libgomp1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    useradd --create-home --shell /bin/bash dnalinux

RUN if [ $(uname -m) = x86_64 ] ; then arch=x86_64; \
    elif [ $(uname -m) = aarch64 ] ; then arch=aarch64; \
    else echo "Architecture $(uname -m) is not supported" >&2; exit 1; \
    fi && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-${arch}.sh \
    && bash Miniconda3-latest-Linux-${arch}.sh -b -p /opt/miniconda3 \
    && rm -f Miniconda3-latest-Linux-${arch}.sh

# On x86_64 the whole environment, including BLAST+ >= 2.17.0, is solved by
# conda. Bioconda publishes no linux-aarch64 BLAST+ newer than 2.16.0, so on
# aarch64 a minimal conda package named "blast" is built from NCBI's prebuilt
# BLAST+ binaries and passed to the solver, which then sees BLAST+ 2.17.0 for
# aarch64 and resolves the rest of the environment normally. The binaries are
# installed into the environment by conda, so nothing is added to PATH by hand.
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r && \
    conda config --remove channels defaults || true && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    conda install --yes mamba && \
    if [ $(uname -m) = x86_64 ] ; then \
        mamba create --yes -n bakta bakta=${software_version} ; \
    else \
        set -eu ; \
        base=https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blast_version} ; \
        tarball=ncbi-blast-${blast_version}+-aarch64-linux.tar.gz ; \
        cd /tmp && \
        wget -q ${base}/${tarball} ${base}/${tarball}.md5 && \
        md5sum -c ${tarball}.md5 && \
        mkdir -p /tmp/blast-src /tmp/blast-pkg/info && \
        tar xzf ${tarball} -C /tmp/blast-src --strip-components=1 && \
        mv /tmp/blast-src/bin /tmp/blast-pkg/bin && \
        printf '{"name":"blast","version":"%s","build":"ncbi_0","build_number":0,"subdir":"linux-aarch64","platform":"linux","arch":"aarch64","depends":[],"license":"Public Domain","summary":"NCBI BLAST+ prebuilt binaries"}' "${blast_version}" \
            > /tmp/blast-pkg/info/index.json && \
        ( cd /tmp/blast-pkg && find bin \( -type f -o -type l \) | sort > info/files ) && \
        ( cd /tmp/blast-pkg && tar cjf /tmp/blast-${blast_version}-ncbi_0.tar.bz2 info bin ) && \
        mamba create --yes -n bakta /tmp/blast-${blast_version}-ncbi_0.tar.bz2 bakta=${software_version} && \
        rm -rf /tmp/blast-src /tmp/blast-pkg /tmp/blast-${blast_version}-ncbi_0.tar.bz2 ${tarball} ${tarball}.md5 ; \
    fi && \
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
