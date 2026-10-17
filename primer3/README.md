# Primer3

This directory contains a Dockerfile for **Primer3**, the standard tool for designing PCR primers and other oligonucleotides.

## What is Primer3?

**Primer3** is a widely used program for designing PCR primers (PCR = "Polymerase Chain Reaction"), and it can also design hybridization probes and sequencing primers. It has many input parameters that tell it exactly what characteristics make good primers for a given goal. The command-line program is `primer3_core`; the Debian package also provides `oligotm`, `ntthal` and `ntdpal`.

- Home page: http://primer3.sourceforge.net

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/primer3/general

- **`dnalinux/primer3:latest`** — recommended; currently points to `2.6.1`
- **`dnalinux/primer3:2.6.1`** — Primer3 2.6.1, installed from the Debian packages `primer3` and `primer3-examples` on `debian:bookworm`. Multi-arch (`linux/amd64`, `linux/arm64`).

The repository holds a single Primer3 version directory, `2.6.1-4-deb`, which builds both tags. The image sets `WORKDIR /data/`.

## Building the image

```bash
cd 2.6.1-4-deb
docker build -t dnalinux/primer3:2.6.1 .
```

## Smoke test

`primer3_core --about` prints one line with the Primer3 release number and exits:

```bash
docker run -it --rm dnalinux/primer3:2.6.1 primer3_core --about
```

## License

GPL-2+. The Dockerfile `LABEL` records `about.license="GPL-2+"` and points at `/usr/share/doc/primer3/copyright`.
