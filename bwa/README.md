# BWA

This directory contains Dockerfiles for the **Burrows-Wheeler Aligner (BWA)**, a fast and widely used software package for mapping low-divergent sequences against a large reference genome.

## What is BWA?

**BWA** aligns short DNA sequences (reads) to a reference genome using the Burrows-Wheeler transform. It is one of the standard tools in genomics pipelines and supports both single-end and paired-end reads. BWA includes several algorithms:

- **`bwa aln`** — original algorithm for short reads up to ~100 bp
- **`bwa samse` / `bwa sampe`** — generate SAM output from `aln` alignments
- **`bwa bwasw`** — designed for long reads with high error rates
- **`bwa mem`** — recommended for reads from ~70 bp to a few megabases; widely used for Illumina and PacBio data

## Available images

Pre-built images are published to Docker Hub:

- **`dnalinux/bwa:0.7.19-src`** — BWA 0.7.19 built from source on Debian Trixie slim (multi-arch)
- **`dnalinux/bwa:0.7.18-1-deb`** — BWA 0.7.18 installed from Debian packages
- **`dnalinux/bwa:0.7.17-7-deb`** — BWA 0.7.17 installed from Debian packages

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/bwa/general

## How to use

Pull the image:

```bash
docker pull dnalinux/bwa:0.7.19-src
```

Run BWA with your data mounted into `/data`:

```bash
docker run -v $(pwd):/data dnalinux/bwa:0.7.19-src \
    mem /data/reference.fa /data/reads_1.fq /data/reads_2.fq > /data/aligned.sam
```

Index a reference genome:

```bash
docker run -v $(pwd):/data dnalinux/bwa:0.7.19-src \
    index /data/reference.fa
```

The `0.7.19-src` image uses `ENTRYPOINT ["bwa"]`, so the first argument after the image name is the BWA command.

## Building from source

To build the source-based image locally:

```bash
cd 0.7.19-src
docker build -t dnalinux/bwa:0.7.19-src .
```

## License

BWA is released under the MIT license. See the source repository for details.
