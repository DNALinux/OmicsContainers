# OrthoFinder

This directory contains Dockerfiles for **OrthoFinder**, a tool for accurate inference of orthogroups, orthologues, gene trees and rooted species trees from a set of protein FASTA files.

## What is OrthoFinder?

**OrthoFinder** takes one protein FASTA file per species and infers **orthogroups** — groups of genes descended from a single gene in the last common ancestor of the analysed species — using an all-vs-all sequence search followed by MCL graph clustering. On top of the orthogroups it infers gene trees, a **rooted species tree**, and uses the gene trees to separate orthologues from paralogues and to place gene duplication events on the species tree. It is a standard tool for comparative genomics, scaling from a handful of proteomes to thousands.

- Source code, manual and releases: https://github.com/davidemms/OrthoFinder
- Tutorials: https://davidemms.github.io/
- Citation: Emms, D.M., Kelly, S. *OrthoFinder: phylogenetic orthology inference for comparative genomics*. Genome Biology 20, 238 (2019). https://doi.org/10.1186/s13059-019-1832-0

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/orthofinder/general

- **`dnalinux/orthofinder:3.0.1b1-conda`** — OrthoFinder **3.0.1b1** installed from bioconda into its own mamba environment on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as the unprivileged user `dnalinux`.
- **`dnalinux/orthofinder:2.5.5`** — OrthoFinder **2.5.5** built on `python:3.10-slim-bullseye` with helper binaries downloaded at build time. `linux/amd64` only, runs as `root`. The `latest` tag currently points to this image.

## Differences between the two images

| | `2.5.5` | `3.0.1b1-conda` |
|---|---|---|
| OrthoFinder | 2.5.5 (stable, 2023-05) | 3.0.1b1 (**beta**, 2024-10-07) |
| Base image | `python:3.10-slim-bullseye` | `debian:trixie-slim` |
| Install method | source tarball, Debian `apt` packages, plus pre-compiled helper binaries downloaded during the build | one bioconda package; every dependency resolved by conda |
| Sequence search | BLAST+ (Debian `ncbi-blast+`) | DIAMOND and MMseqs2 (BLAST+ also available) |
| MSA / tree programs | MAFFT, FastTree, FastME | MAFFT, FastTree, FastME, IQ-TREE, RAxML, RAxML-NG, Muscle |
| ASTRAL-Pro3 (`--assign`) | not available | installed (conda package `aster`) |
| Default tree inference | DendroBLAST | MSA-based (MAFFT + FastTree) |
| Architectures | `linux/amd64` only — the FastTree/FastME helper binaries are x86_64 | `linux/amd64`, `linux/arm64` |
| Runs as | `root` | `dnalinux` (unprivileged) |
| `CMD` | none set, so the base image's Python REPL starts | `/bin/bash` |

Which one to use:

- **Use `3.0.1b1-conda`** for new work, and on ARM machines. It is the only one of the two that works on `linux/arm64`, it ships the faster search programs (DIAMOND/MMseqs2 instead of BLAST+), and it is the only one with the 3.x workflow.
- **Use `2.5.5`** if a pipeline or paper pins the 2.x behaviour. Note that 3.0.1b1 is a *beta* of the 3.x series, so results and options are subject to change — reproduce published 2.5.5 analyses with the 2.5.5 image.

What is new in 3.0.1b1 compared with 2.5.5 (from the upstream release notes):

- **`--core` / `--assign` workflow**: new species can be assigned to orthogroups previously inferred for a smaller core set of species, removing the need for a costly all-vs-all search. A core run is done first, then `orthofinder --core RESULTS_CORE --assign NEW_SPECIES`.
- **ASTRAL-Pro3** is used for species tree inference when `--assign` is used.
- **MSA-based gene tree inference is now the default** (it scales better); DendroBLAST inference can be selected with `-M dendroblast`.
- **Large reductions in RAM usage**, and multi-threading instead of multiprocessing when calling external programs.
- New gene-similarity score for sparse hit sets (`--scores-v2`), and `--c-homologs` to run the phylogenetic analysis on complete gene families.

## Building the image

```bash
cd 3.0.1b1-conda
docker build -t dnalinux/orthofinder:3.0.1b1-conda .
```

To build and push both architectures at once with Buildx:

```bash
cd 3.0.1b1-conda
docker buildx build --platform linux/amd64,linux/arm64 \
    -t dnalinux/orthofinder:3.0.1b1-conda --push .
```

The OrthoFinder version is passed to the conda solver through the `software_version` build argument, which defaults to `3.0.1b1`. A later 3.x release can be installed with `--build-arg software_version=3.1.5`, but the `LABEL` strings in the Dockerfile are literal and have to be updated by hand as well.

## Smoke test

`orthofinder -h` prints the version banner and the help text:

```bash
docker run -it --rm dnalinux/orthofinder:3.0.1b1-conda orthofinder -h
```

Check that the dependencies are on `PATH`:

```bash
docker run -it --rm dnalinux/orthofinder:3.0.1b1-conda bash -c \
  'for t in diamond mmseqs mcl fastme mafft FastTree iqtree astral-pro; do printf "%-12s %s\n" $t $(command -v $t); done'
```

A real, small analysis can be run on the `ExampleData` (four *Mycoplasma* proteomes) shipped inside the image. Keep the results out of the conda environment, which is not writable — either copy the data or pass `-o`:

```bash
docker run -it --rm dnalinux/orthofinder:3.0.1b1-conda bash -c \
  'orthofinder -f /opt/miniconda3/envs/orthofinder/share/orthofinder/ExampleData \
      -o /home/dnalinux/example_out -og -t 4'
```

`-og` stops the run after orthogroup inference, which is enough to exercise the search program, MCL and the results writer.

## Running OrthoFinder on your own data

Put one protein FASTA per species in a directory (`.fa`, `.faa`, `.fasta`, `.fas` and `.pep` extensions are recognised) and mount it:

```bash
docker run -it --rm --ulimit nofile=1000000:1000000 \
    -v $(pwd)/fastas:/home/dnalinux/fastas \
    -v $(pwd)/results:/home/dnalinux/results \
    dnalinux/orthofinder:3.0.1b1-conda \
    orthofinder -f /home/dnalinux/fastas -o /home/dnalinux/results -t 8
```

Notes:

- By default OrthoFinder writes its `OrthoFinder/Results_<date>` directory *next to the input FASTA directory*. Pass `-o` to write elsewhere, which is what the mounted `results` directory above is for.
- Use `--ulimit nofile=1000000:1000000`; OrthoFinder opens many files at once and the default limit on some systems is too low.
- OrthoFinder uses one sequence per gene per species as input and expects the proteins to be the primary transcripts (use `primary_transcript.py` from the OrthoFinder scripts for GFF/GTF-derived proteomes).
- Memory is the practical limit: a few dozen proteomes run on a laptop, hundreds of proteomes want a server. Set `-t` to the number of cores actually available to the container.

### Adding species to a previous analysis (3.x only)

```bash
# 1. infer orthogroups for a core set of species
docker run -it --rm -v $(pwd)/data:/home/dnalinux/data \
    dnalinux/orthofinder:3.0.1b1-conda \
    orthofinder -f /home/dnalinux/data/core_fastas -o /home/dnalinux/data -n Core

# 2. assign the remaining species to those orthogroups
docker run -it --rm -v $(pwd)/data:/home/dnalinux/data \
    dnalinux/orthofinder:3.0.1b1-conda \
    orthofinder --core /home/dnalinux/data/Results_Core --assign /home/dnalinux/data/additional_fastas
```

## Note on the 3.0.1b1 version

The `3.0.1b1` release is a **beta** of the 3.x series. Upstream dropped the pre-packaged executable in this release and recommends installing from conda, which is what this Dockerfile does — the bioconda package also pulls in the architecture-specific helper binaries (DIAMOND, MMseqs2, MCL, FastME, MAFFT, FastTree, IQ-TREE, RAxML, ASTRAL-Pro3), which is what makes the image work on both x86_64 and ARM64.

## License

OrthoFinder is released under the GNU General Public License version 3 (GPLv3). See `License.md` in the upstream source distribution. Files in this repository are Apache 2.0 unless noted otherwise.
