ARG PARSNP_VER="2.1.5"

FROM condaforge/mambaforge:latest AS app

ARG PARSNP_VER

LABEL base.image="condaforge/mambaforge:latest"
LABEL dockerfile.version="1"
LABEL software="Parsnp"
LABEL software.version="${PARSNP_VER}"
LABEL description="Efficient microbial core genome alignment, SNP detection, and phylogeny for bacterial genomes"
LABEL website="https://github.com/marbl/parsnp"
LABEL license="https://github.com/marbl/parsnp/blob/master/LICENSE"
LABEL maintainer="Diya Nair"
LABEL maintainer.email="diyasnair30@gmail.com"

# install via Bioconda (parsnp's own README recommends this over building from source,
# which additionally requires a custom Muscle library build)
RUN mamba install -y -c bioconda -c conda-forge "parsnp=${PARSNP_VER}" wget ca-certificates && \
    mamba clean -afy

CMD ["parsnp", "--help"]

WORKDIR /data

## Test ##
FROM app AS test
ARG PARSNP_VER
RUN parsnp --version
# pull down the real mers_virus example bundled in the parsnp repo and run an actual alignment
RUN wget -q https://github.com/marbl/parsnp/archive/refs/tags/v${PARSNP_VER}.tar.gz &&\
    tar -xzf v${PARSNP_VER}.tar.gz && rm v${PARSNP_VER}.tar.gz
RUN parsnp -r parsnp-${PARSNP_VER}/examples/mers_virus/ref/England1.fna \
    -d parsnp-${PARSNP_VER}/examples/mers_virus/genomes/*.fna \
    -o /data/test-out --no-partition
