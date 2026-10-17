# SSPACE-LongRead

This directory contains Dockerfiles for **SSPACE-LongRead**, a scaffolder that uses long reads to extend pre-assembled contigs.

## What is SSPACE-LongRead?

**SSPACE-LongRead** is distributed as the Perl script `SSPACE-LongRead.pl`, version `1-1`. It takes a FASTA file of contig sequences and a file of PacBio long reads, aligns the reads to the contigs with BLASR, and uses the resulting links to order and orient the contigs into scaffolds.

The script is installed from the copy kept in this directory; it declares no separate upstream site or package.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/sspace_longread/general

- **`dnalinux/sspace_longread:latest`** — points to `1-1`
- **`dnalinux/sspace_longread:1-1`** — `debian:sid` with `libperl4-corelibs-perl` (needed by the script's `getopts.pl`) and `SSPACE-LongRead.pl` copied into the image. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

```bash
cd 1-1
docker build -t dnalinux/sspace_longread:1-1 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/sspace_longread:1-1 perl /SSPACE-LongRead.pl -h
```

## Note on the alignment step

The script calls `blasr` for its alignment step, but BLASR is not installed in this image, and neither are any PacBio reads. The alignment step therefore has to be provided for separately when the script is run.

## License

Neither the Dockerfile nor the bundled script declares a license.
