# CheckM2

This directory contains Dockerfiles for **CheckM2**, a tool for rapid assessment of genome bin quality using machine learning.

## What is CheckM2?

**CheckM2** (https://github.com/chklovski/CheckM2) predicts the completeness and contamination of metagenome-assembled genomes (MAGs) and isolate genomes. It is the successor to CheckM and uses machine learning models (neural networks and gradient boosting) trained on GTDB, combined with DIAMOND annotation against UniRef100 KO signatures. CheckM2 1.1.0 is built on GTDB release 202 and handles low-quality, low-completeness and novel-lineage genomes much better than CheckM.

## Available images

- **`dnalinux/checkm2:1.1.0-conda`** — CheckM2 1.1.0 installed from bioconda into its own mamba environment on `debian:trixie-slim`

## Building the image

```bash
cd 1.1.0-conda
docker build -t dnalinux/checkm2:1.1.0-conda .
```

## Smoke test (no database needed)

The DIAMOND database is only needed by `predict`/`testrun`/`database`, so the image can be verified without it:

```bash
docker run -it --rm dnalinux/checkm2:1.1.0-conda checkm2 --version
docker run -it --rm dnalinux/checkm2:1.1.0-conda checkm2 --help
docker run -it --rm dnalinux/checkm2:1.1.0-conda bash -c \
  'python -c "import tensorflow, keras; print(tensorflow.__version__)" && diamond --version && prodigal -v'
```

## Downloading the DIAMOND database

The database is **not** included in the image. Download it manually from Zenodo (DIAMOND database v3, ~1.7 GB compressed, for CheckM2 >= 1.1.0):

```bash
mkdir -p checkm2_db && cd checkm2_db
curl -LO https://zenodo.org/records/14897628/files/checkm2_database.tar.gz
tar xzf checkm2_database.tar.gz
```

Extraction produces several GB of data, including `uniref100.KO.1.dmnd`. The tarball can be deleted afterwards. Do not reuse an older CheckM2 1.0.x database: v1.1.0 models are built on GTDB release 202 and the v3 database requires DIAMOND 2.1.11 (already in this image).

Alternatively, let the container itself download it (mount first so it persists on the host):

```bash
docker run -it -v $(pwd)/checkm2_db:/home/dnalinux/db dnalinux/checkm2:1.1.0-conda \
    checkm2 database --download --path /home/dnalinux/db
```

## Telling CheckM2 where the database is

Either pass `--database_path` on every run, or set the `CHECKM2DB` environment variable when starting the container:

```bash
docker run -it -v /full/path/to/checkm2_db:/home/dnalinux/db \
    -e CHECKM2DB=/home/dnalinux/db/uniref100.KO.1.dmnd \
    dnalinux/checkm2:1.1.0-conda checkm2 testrun
```

## Running predictions

Mount the database, your genomes and an output directory, e.g.:

```bash
docker run -it -v /full/path/to/checkm2_db:/home/dnalinux/db \
    -v $(pwd)/genomes:/home/dnalinux/genomes \
    -v $(pwd)/out:/home/dnalinux/out \
    dnalinux/checkm2:1.1.0-conda \
    checkm2 predict --input /home/dnalinux/genomes \
        --output-directory /home/dnalinux/out \
        --database_path /home/dnalinux/db/uniref100.KO.1.dmnd
```

Notes:

- Give the container enough RAM for DIAMOND; use the `--lowmem` flag if you hit memory limits.
- `checkm2 testrun` takes under 5 minutes on an average desktop once the database is in place.

## License

CheckM2 is released under the GPL-3.0 license.
