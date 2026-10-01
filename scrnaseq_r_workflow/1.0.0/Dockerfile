# Dockerfile
# OmicsContainers layout: <software>/<version>/Dockerfile
# Workflow: scRNA-seq Radiation Skin Analysis (Control vs Irradiated)
# Content: R + Seurat + Matrix + igraph + bnlearn

# rocker/r-ver: fixed R version, Posit Package Manager (P3M) as CRAN mirror,
# frozen CRAN snapshot on version tags -> reproducible builds
FROM rocker/r-ver:4.5

LABEL base_image="rocker/r-ver:4.5" \
      software="scrnaseq-r-workflow" \
      software.version="1.0.0" \
      about.summary="R environment for scRNA-seq workflow (Seurat + Matrix + igraph + bnlearn). Covers QC, normalization, RPCA integration, clustering, annotation, condition-specific DE, and NR4A1 co-expression/Bayesian networks." \
      about.home="https://github.com/DNALinux/OmicsContainers" \
      about.license="Apache-2.0" \
      about.tags="field::biology:bioinformatics, single-cell, scRNA-seq, Seurat, R, networks" \
      maintainer="DNALinux <dnalinux@toyoko.io>"

# ---- System libraries ---------------------------------------------------
# Only apt for system libs, never r-cran-* (rocker convention).
# libglpk/gmp      -> igraph
# plotting stack   -> Seurat QC plots (png, ragg, systemfonts, textshaping)
# hdf5             -> optional 10x HDF5 input support (SeuratDisk/hdf5r)
RUN apt-get update && apt-get install -y --no-install-recommends \
      libglpk-dev \
      libgmp-dev \
      libfontconfig1-dev \
      libharfbuzz-dev \
      libfribidi-dev \
      libfreetype6-dev \
      libpng-dev \
      libtiff5-dev \
      libjpeg-dev \
      libhdf5-dev \
      libxml2-dev \
      libcurl4-openssl-dev \
      libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# ---- R packages (binary from P3M on amd64) ------------------------------
# install2.r is the idiomatic rocker/littler installer.
# Non-latest r-ver tags resolve against a frozen CRAN snapshot ->
# same Seurat/Matrix/igraph/bnlearn versions on every rebuild.
RUN install2.r --error --skipinstalled --ncpus -1 \
      Seurat \
      Matrix \
      igraph \
      bnlearn \
    && rm -rf /tmp/downloaded_packages \
    && (strip /usr/local/lib/R/site-library/*/libs/*.so 2>/dev/null || true)

# ---- Validation ----------------------------------------------------------
RUN R -q -e "library(Seurat); library(Matrix); library(igraph); library(bnlearn); sessionInfo()"

WORKDIR /data

CMD ["R"]

