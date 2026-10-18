# funannotate

This directory contains Dockerfiles for **funannotate**, a eukaryotic genome annotation pipeline.

## What is funannotate?

**funannotate** (https://github.com/nextgenusfs/funannotate) is a genome prediction, annotation and comparison pipeline, originally written for fungal genomes. It runs gene prediction from ab initio predictors or from RNA-seq/EST and protein evidence, and then annotates the predicted genes with functional domains and protein signatures.

Citation: Palmer, J.M., Stajich, J.E. (2020). *Funannotate v1.8.1: Eukaryotic genome annotation* (v1.8). Zenodo. https://doi.org/10.5281/zenodo.1134477

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/funannotate/general

- **`dnalinux/funannotate:latest`** — funannotate installed from source into a conda environment that is packed into a Debian image; `linux/amd64` only. This is the only tag in the repository, and it corresponds to the `Dockerfile` in this directory.

## The two Dockerfiles here

- **`Dockerfile`** — a two-stage build. A `condaforge/mambaforge` stage creates the `funannotate` environment from bioconda, installs funannotate itself with `pip install git+https://github.com/nextgenusfs/funannotate.git`, and packs the environment with `conda-pack`. The runtime stage, on `debian:buster`, unpacks it into `/venv`, adds the Debian `snap`, `augustus`, `augustus-data`, `locales`, `libgl1` and `procps` packages, and unpacks the `gmes.tar.gz` archive kept in this directory (GeneMark-ES), setting `GENEMARK_PATH=/root/gmes`. Because funannotate is installed from the repository rather than a release, its exact version depends on when the image was built.
- **`Dockerfile2`** — a database layer built on the upstream `nextgenusfs/funannotate-slim` image. Its only build step is `funannotate setup -i all --wget -b dikarya microsporidia embryophyta metazoa arthropoda vertebrata protists tetrapoda`, which downloads the annotation datasets into `/opt/databases` (the `FUNANNOTATE_DB` path set by `Dockerfile`).

Docker Hub also holds separate repositories for images that bundle those datasets — `dnalinux/funannotate-dikarya`, `dnalinux/funannotate-gmes`, `dnalinux/funannotate-dikarya-gmes` and `dnalinux/funannotate-gmes-ascomycota`. Each has a single `latest` tag (`linux/amd64` only) and there is no Dockerfile for them in this repository.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd funannotate
docker build -t funannotate:latest .
```

The database layer has no published tag. It is built explicitly, as `Dockerfile` is the default build file, and tagged locally:

```bash
cd funannotate
docker build -f Dockerfile2 -t funannotate-db:local .
```

## Smoke test

```bash
docker run -it --rm dnalinux/funannotate:latest funannotate --version
```

## License

funannotate is released under the BSD 2-Clause license (upstream repository `LICENSE`).
