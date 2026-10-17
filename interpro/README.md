# InterProScan

This directory contains a Dockerfile for **InterProScan**, the protein sequence classification software from EMBL-EBI.

## What is InterProScan?

**InterProScan** (https://www.ebi.ac.uk/interpro/) scans protein sequences against the member databases of InterPro and reports the matching signatures, predicted domains and functional sites. Source code is at https://github.com/ebi-pf-team/interproscan and the documentation is at https://interproscan-docs.readthedocs.io/.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/interproscan/general

- **`dnalinux/interproscan:5.69-101.0`** — InterProScan 5.69-101.0, the "core" distribution downloaded from the EBI FTP at build time, on `ubuntu:20.04`. `linux/amd64` only. There is no `latest` tag.

Note that the directory is named `interpro` but the image is published to the `interproscan` repository.

## Reference data

InterProScan needs its `data/` directory to run an analysis, and the core distribution installed by this Dockerfile does not contain it. Upstream documents obtaining the matching data release from the EBI FTP (`ftp://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/`) and mounting it into the container at `/opt/interproscan/data`; see https://interproscan-docs.readthedocs.io/en/v5/HowToUseViaContainer.html.

## Building the image

```bash
cd 5.69-101.0
docker build -t dnalinux/interproscan:5.69-101.0 .
```

The build downloads `interproscan-core-5.69-101.0.tar.gz` from the EBI FTP, checks its published MD5, and unpacks it to `/opt/interproscan`.

## Smoke test

The image's entrypoint is `bash ./interproscan.sh` with `/opt/interproscan` as the working directory, so options are passed directly after the image name:

```bash
docker run --rm dnalinux/interproscan:5.69-101.0 --version
```

## License

InterProScan is licensed under the Apache License 2.0 (upstream repository `LICENSE`).
