# MitoHiFi

This directory contains Dockerfiles for **MitoHiFi**, a Python pipeline for assembling mitochondrial genomes from PacBio HiFi reads. The two directories build two images that are published to two Docker Hub repositories.

## What is MitoHiFi?

**MitoHiFi** assembles mitochondrial genomes from PacBio HiFi reads. Given reads (`-r`) it extracts and assembles the mitochondrial reads with hifiasm; given assembled contigs (`-c`) it searches them for the mitogenome. It separates NUMTS from true mitogenome contigs and produces circularized, annotated mitochondrial sequences and coverage/annotation plots. It requires a closely related mitochondrial reference sequence in FASTA and GenBank format (`-f`, `-g`), which the bundled `findMitoReference.py` can locate and download from NCBI.

- Source code: https://github.com/marcelauliano/MitoHiFi

## Available images

Docker Hub repositories:
- https://hub.docker.com/repository/docker/dnalinux/mitohifi-base/general
- https://hub.docker.com/repository/docker/dnalinux/mitohifi-code/general

Base image — `dnalinux/mitohifi-base`:

- **`dnalinux/mitohifi-base:3.2.2`** — the runtime layer, built from `ubuntu:18.04`. Installs the pipeline dependencies (MitoFinder, MITOS in its own conda environment, hifiasm 0.16.1, minimap2 2.24, CD-HIT, MAFFT, BLAST+, bedtools, samtools, Infernal) and downloads the `refseq89m` and `refseq89f` reference databases from Zenodo into `/opt/databases`. `linux/amd64` only.

Code image — `dnalinux/mitohifi-code`, built `FROM dnalinux/mitohifi-base:3.2.2`:

- **`dnalinux/mitohifi-code:latest`** — currently points to `3.2.2.p4`
- **`dnalinux/mitohifi-code:3.2.2.p4`**, **`3.2.2.p3`**, **`3.2.2.p2`**, **`3.2.2.p1`**, **`3.2.2`** — the MitoHiFi scripts and wrapper scripts added on top of the base image, together with the Python dependencies (Biopython, pandas, Pillow, matplotlib, entrezpy, dna_features_viewer, bcbio-gff). `linux/amd64` only.

`dnalinux/mitohifibase:3.2.2` is a legacy alias of `dnalinux/mitohifi-base:3.2.2`.

## Building the images

The base image is built first; the code image is built from it:

```bash
cd 3.2.2
docker build -t dnalinux/mitohifi-base:3.2.2 .

cd ../3.2.2-code
docker build -t dnalinux/mitohifi-code:3.2.2 .
```

## Smoke test

The code image puts the MitoHiFi scripts on `PATH`; `-h` prints the usage:

```bash
docker run -it --rm dnalinux/mitohifi-code:3.2.2 mitohifi.py -h
```

The base image carries the dependencies (`hifiasm`, `minimap2`, MitoFinder, MITOS) but not the MitoHiFi scripts.

## License

MitoHiFi is released under the MIT license, as stated in its upstream repository.
