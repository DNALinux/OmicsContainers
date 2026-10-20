# Bakta

This directory contains Dockerfiles for **Bakta**, a tool for the rapid and standardized annotation of bacterial genomes, MAGs and plasmids.

## What is Bakta?

**Bakta** annotates bacterial genomes and metagenome-assembled genomes (MAGs) rapidly and in a taxonomy-independent way, using alignment-free sequence identification. It produces dbxref-rich output — including small ORFs — in machine-readable JSON plus the usual bioinformatics formats. Installing the bioconda package brings in the programs Bakta drives:

- **Pyrodigal** — gene prediction
- **tRNAscan-SE** and **Aragorn** — tRNA and tmRNA detection
- **Infernal** — ncRNA detection
- **DIAMOND** and **BLAST+** — sequence search against the Bakta database
- **pyhmmer** (HMMER) — profile search
- **NCBI AMRFinderPlus** — antimicrobial resistance and virulence factor screening

Citation: Schwengers O., Jelonek L., Dieckmann M. A., Beyvers S., Blom J., Goesmann A. (2021). *Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification*. Microbial Genomics, 7(11). https://doi.org/10.1099/mgen.0.000685

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bakta/general

- **`dnalinux/bakta:1.12.2-conda`** — Bakta **1.12.2** installed from bioconda into its own mamba environment on `debian:trixie-slim`. Multi-arch: `linux/amd64` and `linux/arm64`.

The environment resolves to Bakta 1.12.2 with DIAMOND 2.2.8, BLAST+ 2.17.0, pyhmmer 0.12.3 (HMMER), Pyrodigal 3.7.1, tRNAscan-SE 2.0.13, Aragorn 1.2.41, Infernal 1.1.5, Piler-CR 1.06 and NCBI AMRFinderPlus 4.2.7, on Python 3.13.16. Exact dependency versions follow whatever the bioconda solver picks at build time.

## Note on architectures

The image is built for `linux/amd64` and `linux/arm64`. On `amd64` the whole environment, BLAST+ included, is resolved and installed by conda.

Bakta 1.12.x requires **BLAST+ >= 2.17.0**, but bioconda publishes no `linux-aarch64` build of BLAST+ newer than 2.16.0. On `arm64` the Dockerfile therefore downloads NCBI's prebuilt `ncbi-blast-2.17.0+-aarch64-linux.tar.gz` (verified against the MD5 published next to it) and wraps its binaries in a small local conda package named `blast`. That package is passed to the same solver together with `bakta`, so the rest of the environment still comes from bioconda/conda-forge and every dependency is resolved normally. `conda list` reports `blast 2.17.0 ncbi_0`, the binaries live in the environment's `bin/`, and `blastn -version` reports `2.17.0+`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 1.12.2-conda
docker build -t bakta:1.12.2-conda .
```

To build and publish both architectures in one step:

```bash
docker buildx build --platform linux/amd64,linux/arm64 \
    -t dnalinux/bakta:1.12.2-conda --push .
```

Building `linux/amd64` on an ARM host works through emulation but is slow: the conda solve and the Bakta environment creation run under QEMU.

## Smoke test (no database needed)

The database is only needed for real annotation runs, so the image can be verified without it:

```bash
docker run -it --rm dnalinux/bakta:1.12.2-conda bakta --version
docker run -it --rm dnalinux/bakta:1.12.2-conda bakta --help
docker run -it --rm dnalinux/bakta:1.12.2-conda bakta_db --help
```

The bundled helper programs can be checked the same way:

```bash
docker run -it --rm dnalinux/bakta:1.12.2-conda bash -c \
  'diamond --version && blastp -version && tRNAscan-SE -h | head -2 && aragorn -h | head -3 && cmsearch -h | head -1 && amrfinder --version'
```

## Downloading the Bakta database

The database is **not** included in the image. Bakta 1.12 uses database version 6.0: the **light** build is ~1.3 GB compressed (~3.9 GB unpacked) and the **full** build ~30 GB (~84 GB unpacked). Download it once onto the host, mounting the output directory so it persists:

```bash
mkdir -p bakta_db
docker run -it --rm -v $(pwd)/bakta_db:/home/dnalinux/db \
    dnalinux/bakta:1.12.2-conda \
    bakta_db download --output /home/dnalinux/db --type light
```

`bakta_db download` queries the upstream version list and fetches the database version compatible with the installed Bakta, so there is no version to track by hand. The light build is unpacked into `bakta_db/db-light`; the full build (`--type full`) into `bakta_db/db`. An existing database can be brought up to date in place:

```bash
docker run -it --rm -v $(pwd)/bakta_db:/home/dnalinux/db \
    dnalinux/bakta:1.12.2-conda \
    bakta_db update --db /home/dnalinux/db/db-light
```

Do not reuse an older database with this image: `bakta_db` aborts if the database's major version does not match the one the installed Bakta requires.

## Running annotations

Mount the database, your input and an output directory, and point Bakta at the database with `--db` (or the `BAKTA_DB` environment variable):

```bash
docker run -it --rm \
    -v $(pwd)/bakta_db:/home/dnalinux/db \
    -v $(pwd)/data:/home/dnalinux/data \
    dnalinux/bakta:1.12.2-conda \
    bakta --db /home/dnalinux/db/db-light \
        --output /home/dnalinux/data/results \
        --prefix mygenome \
        --threads 8 /home/dnalinux/data/genome.fasta
```

Notes:

- Instead of `--db`, set `BAKTA_DB=/home/dnalinux/db/db-light` when starting the container.
- Use the **full** database for the best feature coverage; the light database is for cases where download size, disk space or runtime are constrained.
- `--threads` should match the cores available to the container; Bakta is mostly single-genome work, so memory is rarely the limit — disk is (each run writes several output files).
- The output directory must be writable and is created if missing.

## Reference

Schwengers O., Jelonek L., Dieckmann M. A., Beyvers S., Blom J., Goesmann A. (2021). Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification. Microbial Genomics, 7(11). https://doi.org/10.1099/mgen.0.000685) 

## License

Bakta is released under the GPL-3.0 license. See `LICENSE` in the upstream repository.
