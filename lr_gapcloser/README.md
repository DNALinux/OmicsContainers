# LR_Gapcloser

This directory contains a Dockerfile for **LR_Gapcloser**, a tool that closes gaps in genome assemblies using long reads.

## What is LR_Gapcloser?

**LR_Gapcloser** closes gaps in scaffold assemblies using error-corrected long reads. It fragments the long reads, aligns them to the scaffolds with BWA mem, finds bridging alignments across each gap and fills the gap with the original read sequence.

- Source code: https://github.com/CAFS-bioinformatics/LR_Gapcloser

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/lr_gapcloser/general

- **`dnalinux/lr_gapcloser:latest`** — currently points to `2018.9.4`
- **`dnalinux/lr_gapcloser:2018.9.4`** — LR_Gapcloser cloned from its GitHub repository at build time on `debian:sid`, with `bioperl` and `libperl4-corelibs-perl` from Debian. Multi-arch (`linux/amd64`, `linux/arm64`).

## Note on the base image

The base image is `debian:sid` (Debian unstable), which is a moving release rather than a fixed one. It has no `LABEL` metadata block.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 2018.9.4
docker build -t lr_gapcloser:2018.9.4 .
```

## Smoke test

LR_Gapcloser is a shell script driven by flags and provides no version or help flag. The script is installed at `/LR_Gapcloser/LR_Gapcloser.sh`; its required arguments are `-i` (scaffold FASTA) and `-l` (error-corrected long reads).

## License

LR_Gapcloser is released under the GPL-3.0 license, as stated in its upstream repository.
