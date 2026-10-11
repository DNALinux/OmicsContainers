# Samtools

This directory contains Dockerfiles for **Samtools**, a suite of programs for interacting with high-throughput sequencing data.

## What is Samtools?

**Samtools** provides utilities for reading, writing, and manipulating sequence alignment data in the SAM, BAM, and CRAM formats. It is a cornerstone of most genomics and bioinformatics pipelines. Common tasks include:

- Converting between SAM, BAM, and CRAM
- Sorting, indexing, and querying alignments
- Viewing specific regions of an alignment
- Computing alignment statistics
- Merging or splitting BAM files
- Generating pileups and variant information

Samtools is developed by the SAMtools/HTSlib team and is used together with tools such as `bcftools` and `htslib`.

## Available images

Pre-built images are published to Docker Hub:

- **`dnalinux/samtools:1.24-src`** — Samtools 1.24 built from source on Debian sid slim
- **`dnalinux/samtools:1.23-sc`** — Samtools 1.23 built from source on Debian sid slim
- **`dnalinux/samtools:1.22.1-1+b1-deb`** — Samtools 1.22.1 installed from Debian packages
- **`dnalinux/samtools:1.20-3-deb`** — Samtools 1.20 installed from Debian packages
- **`dnalinux/samtools:1.20`** — Samtools 1.20 installed via Miniconda/Bioconda

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/samtools/general

## How to use

Pull the latest source-built image:

```bash
docker pull dnalinux/samtools:1.24-src
```

The `1.24-src` image uses `ENTRYPOINT ["samtools"]`, so the first argument after the image name is the samtools command.

Convert SAM to sorted, indexed BAM:

```bash
docker run -v $(pwd):/data dnalinux/samtools:1.24-src \
    sort -o /data/aligned.bam /data/aligned.sam

docker run -v $(pwd):/data dnalinux/samtools:1.24-src \
    index /data/aligned.bam
```

View a specific region:

```bash
docker run -v $(pwd):/data dnalinux/samtools:1.24-src \
    view /data/aligned.bam chr1:1000000-2000000
```

Get basic statistics:

```bash
docker run -v $(pwd):/data dnalinux/samtools:1.24-src \
    flagstat /data/aligned.bam
```

For the Debian/Conda-based images, run interactively or pass the command directly:

```bash
docker run -v $(pwd):/data dnalinux/samtools:1.20-3-deb \
    samtools view -b /data/aligned.sam > /data/aligned.bam
```

## Building from source

To build the source-based image locally:

```bash
cd 1.24-src
docker build -t dnalinux/samtools:1.24-src .
```

## License

Samtools is released under the MIT/Expat license. See the project repository for details.
