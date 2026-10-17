# HMMER

This directory contains a Dockerfile for **HMMER**, a suite of programs for biological sequence analysis based on profile hidden Markov models.

## What is HMMER?

**HMMER** (http://hmmer.org/) is a suite of programs for profile hidden Markov model analysis of protein and DNA sequences: searching sequence databases for homologous sequences, building profile HMMs and multiple alignments, and related tasks. The Debian package installed in this image puts the HMMER programs in `/usr/bin`, including `hmmsearch`, `hmmscan`, `hmmbuild`, `hmmalign`, `hmmpress`, `hmmstat`, `nhmmer`, `phmmer` and `jackhmmer`.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/hmmer/general

- **`dnalinux/hmmer:latest`** — recommended; currently points to `3.4dfsg-2-deb`
- **`dnalinux/hmmer:3.4dfsg-2-deb`** — HMMER 3.4, installed from the Debian package `hmmer=3.4+dfsg-2` on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

```bash
cd 3.4dfsg-2-deb
docker build -t dnalinux/hmmer:3.4dfsg-2-deb .
```

## Smoke test

`hmmsearch -h` prints the HMMER version banner and the option list:

```bash
docker run -it --rm dnalinux/hmmer:3.4dfsg-2-deb hmmsearch -h
```

The image contains only the Debian `hmmer` package: no profile HMM database (Pfam or similar) is bundled, so one has to be provided to run a search.

## License

HMMER is distributed under the GNU General Public License, version 3 (`about.license` label; the Debian copyright file is `/usr/share/doc/hmmer/copyright`).
