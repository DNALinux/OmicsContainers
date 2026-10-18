# KofamScan

This directory contains Dockerfiles for **KofamScan**, a gene function annotation tool based on KEGG Orthology and profile hidden Markov models.

## What is KofamScan?

**KofamScan** annotates protein sequences with KEGG Orthology (KO) identifiers. It searches a query FASTA of amino-acid sequences with unique sequence names against the KOfam profile HMM database using HMMER, and reports KO assignments. The entry point is the `exec_annotation` script.

- Project page: https://www.genome.jp/tools/kofamkoala/

KofamScan requires the **KOfam database**, which is not included in the image.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/kofamscan/general

- **`dnalinux/kofamscan:latest`** — currently points to `1.3.0`
- **`dnalinux/kofamscan:1.3.0`** — KofamScan 1.3.0 built from the `takaram/kofam_scan` v1.3.0 source release on `debian:trixie-slim`, with `ruby`, `hmmer` and `parallel` from Debian. Multi-arch (`linux/amd64`, `linux/arm64`).

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 1.3.0
docker build -t kofamscan:1.3.0 .
```

## Smoke test

KofamScan needs the KOfam database to annotate anything, but the entry point can be checked on its own:

```bash
docker run -it --rm dnalinux/kofamscan:1.3.0 /kofam_scan-1.3.0/exec_annotation -h
```

## Reference data

The KOfam database (the profile HMMs and the `ko_list` file) is not part of the image. Upstream instructs downloading and decompressing it from `ftp://ftp.genome.jp/pub/db/kofam/`, then pointing KofamScan at it with `-p/--profile` and `-k/--ko-list` (or a `config.yml` next to `exec_annotation`).

## License

KofamScan is released under the MIT license (per the image `LABEL` metadata). The KOfam database and the KEGG Orthology definitions it contains are provided by KEGG and are copyrighted by Kanehisa Laboratories; they are not covered by the MIT license (per the upstream project).
