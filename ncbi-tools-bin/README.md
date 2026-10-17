# NCBI tools (ncbi-tools-bin)

This directory contains a Dockerfile for **ncbi-tools-bin**, Debian's package of NCBI's text-based bioinformatics utilities.

## What is ncbi-tools-bin?

`ncbi-tools-bin` is the Debian binary package that carries the command-line utilities of the NCBI Toolkit, described by the package as "NCBI libraries for biology applications (text-based utilities)". It is a collection of small programs rather than a single application — ASN.1 converters such as `asn2gb` and `gene2xml`, and sequence utilities such as `tbl2asn`, `vecscreen` and `spidey`. The Dockerfile does nothing but install the package from the Debian archive.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/ncbi-tools-bin/general

- **`dnalinux/ncbi-tools-bin:6.1.20170106`** — Debian package version `6.1.20170106+dfsg2-6` installed on `debian:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

The version directory is named `6.1.20170106+dfsg2-6.deb`, but the Docker Hub tag is `6.1.20170106`: `+` is not allowed in a Docker tag.

## Building the image

```bash
cd 6.1.20170106+dfsg2-6.deb
docker build -t dnalinux/ncbi-tools-bin:6.1.20170106 .
```

## Smoke test

The image installs a package of many programs and has no single main binary, so there is no version flag to invoke. Check the installed package instead:

```bash
docker run -it --rm dnalinux/ncbi-tools-bin:6.1.20170106 dpkg-query -W ncbi-tools-bin
docker run -it --rm dnalinux/ncbi-tools-bin:6.1.20170106 dpkg -L ncbi-tools-bin | grep /usr/bin/
```

## License

Public domain. The Dockerfile `LABEL` records `about.license="PD"`, copyright NCBI.
