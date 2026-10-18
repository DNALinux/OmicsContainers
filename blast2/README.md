# BLAST2

This directory contains Dockerfiles for **NCBI BLAST+**, a widely used suite of command-line tools for comparing nucleotide or protein sequences against biological sequence databases.

## What is BLAST?

**BLAST** (Basic Local Alignment Search Tool) finds regions of similarity between biological sequences. It is used to infer functional and evolutionary relationships between sequences and to identify members of gene families. BLAST+ is the modern C++ implementation from NCBI and includes tools such as `blastn`, `blastp`, `blastx`, `tblastn`, `tblastx`, and `makeblastdb`.

## Available images

Pre-built images are published to Docker Hub:

- **`dnalinux/blast2:latest`** — recommended; currently points to `2.17.0-bin`
- **`dnalinux/blast2:2.17.0-bin`** — most recent BLAST+ 2.17.0 release, multi-arch (`linux/amd64`, `linux/arm64`)
- **`dnalinux/blast2:2.16.0-bin`** — BLAST+ 2.16.0 binaries, multi-arch
- **`dnalinux/blast2:2.15.0-bin`** — BLAST+ 2.15.0 binaries, multi-arch

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/blast2/general

## Note on older `-mix` directories

The directories `2.15.0-mix` and `2.16.0-mix` were early experiments that tried to mix pre-compiled binaries on x86_64 with source builds on aarch64. They are **not supported** and are kept here only for historical reasons. Please use the corresponding `-bin` images instead.

## How to use

Pull the latest image from Docker Hub:

```bash
docker pull dnalinux/blast2:latest
```

Run BLAST+ interactively:

```bash
docker run -it dnalinux/blast2:latest
```

Run a specific BLAST command, mounting a local directory with your data:

```bash
docker run -v $(pwd):/data dnalinux/blast2:latest \
    blastn -query /data/query.fasta -db /data/db -out /data/results.txt
```

Create a local BLAST database:

```bash
docker run -v $(pwd):/data dnalinux/blast2:latest \
    makeblastdb -in /data/reference.fasta -dbtype nucl -out /data/db/reference
```

The image sets `BLASTDB=/blast/blastdb:/blast/blastdb_custom` and adds `/blast/bin` to `PATH`.

## Building from source

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

To build a specific version locally:

```bash
cd 2.17.0-bin
docker build -t blast2:2.17.0-bin .
```

## License

NCBI BLAST+ is in the public domain. See the NCBI website for details.
