# syntax=docker/dockerfile:1

# eggNOG-mapper calls esl-reformat (from Easel) for Pfam realignment and for
# custom HMMER sequence databases. Debian ships HMMER but has no easel
# package, so build Easel from the HMMER source release.
FROM debian:trixie-slim AS easel

ARG HMMER_VERSION=3.4

RUN apt-get update && apt-get install -y --no-install-recommends \
        autoconf \
        build-essential \
        ca-certificates \
        wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
RUN wget -nv https://eddylab.org/software/hmmer/hmmer-${HMMER_VERSION}.tar.gz \
    && tar -xzf hmmer-${HMMER_VERSION}.tar.gz

WORKDIR /build/hmmer-${HMMER_VERSION}/easel
RUN autoconf \
    && ./configure --prefix=/usr/local \
    && make -j"$(nproc)" \
    && make install

FROM debian:trixie-slim

ARG EGGNOG_VERSION=2.1.15

LABEL software="eggnog-mapper" \
    base_image="debian:trixie-slim" \
    container="eggnog-mapper" \
    about.summary="Fast functional annotation of novel sequences using eggNOG orthology assignments" \
    about.home="https://github.com/eggnogdb/eggnog-mapper" \
    software.version="2.1.15-src" \
    upstream.version="2.1.15" \
    version="1" \
    about.copyright="eggNOG-mapper authors" \
    about.license="AGPL-3.0-only" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="annotation,orthology,functional-genomics,metagenomics"

ENV DEBIAN_FRONTEND=noninteractive

# eggNOG-mapper, DIAMOND, HMMER, MMseqs2 and Prodigal from Debian, plus the
# Python modules listed in upstream requirements.txt. python3-setuptools is
# needed because eggnog-mapper imports distutils, which Python 3.13 no longer
# ships in the standard library.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        diamond-aligner \
        hmmer \
        mmseqs2 \
        prodigal \
        python3 \
        python3-biopython \
        python3-psutil \
        python3-setuptools \
        python3-xlsxwriter \
        wget \
    && rm -rf /var/lib/apt/lists/*

COPY --from=easel /usr/local/bin/esl-* /usr/local/bin/

# The source tarball ships pre-compiled x86-64 copies of DIAMOND, MMseqs2,
# Prodigal and HMMER in eggnogmapper/bin/. Remove them so the tools found on
# PATH are used and the image works on every architecture.
RUN wget -nv -O /tmp/eggnog-mapper.tar.gz \
        https://github.com/eggnogdb/eggnog-mapper/archive/refs/tags/v${EGGNOG_VERSION}.tar.gz \
    && tar -xzf /tmp/eggnog-mapper.tar.gz -C /opt \
    && mv /opt/eggnog-mapper-${EGGNOG_VERSION} /opt/eggnog-mapper \
    && rm /tmp/eggnog-mapper.tar.gz \
    && find /opt/eggnog-mapper/eggnogmapper/bin -type f ! -name '__init__.py' -delete

# 2.1.15 uses invalid escape sequences in several regexes; Python 3.13 warns
# about each of them on every run.
ENV PATH="/opt/eggnog-mapper:${PATH}" \
    PYTHONPATH="/opt/eggnog-mapper" \
    PYTHONWARNINGS="ignore::SyntaxWarning"

WORKDIR /data

CMD ["emapper.py", "--help"]

# The eggNOG database is not included in the image: download it to a mounted
# directory once (about 4 GB for the DIAMOND database alone), then point
# emapper.py at it with --data_dir (or the EGGNOG_DATA_DIR variable).
#
# docker run --rm -v $(pwd)/emapperdb:/db dnalinux/eggnog-mapper:2.1.15-src \
#     download_eggnog_data.py --data_dir /db -y
#
# docker run --rm -v $(pwd):/data -v $(pwd)/emapperdb:/db \
#     dnalinux/eggnog-mapper:2.1.15-src \
#     emapper.py -i /data/proteins.fa --data_dir /db -o /data/annotation --cpu 8
