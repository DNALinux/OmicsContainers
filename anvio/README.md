# anvi'o

This directory contains Dockerfiles for **anvi'o**, an analysis and visualization platform for 'omics data.

## What is anvi'o?

**anvi'o** (https://github.com/merenlab/anvio) is an analysis and visualization platform for 'omics data. It provides a large family of `anvi-*` programs covering metagenomics, pangenomics, phylogenomics and related workflows, plus an interactive interface for exploring the results.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/anvio/general

- **`dnalinux/anvio:7.1`** — anvi'o 7.1 installed with `pip` into a Miniconda environment (`anvio-71py37`, Python 3.7) on `debian:bookworm-slim`. `linux/amd64` only. There is no `latest` tag.

## Building the image

```bash
cd 7.1
docker build -t dnalinux/anvio:7.1 .
```

## Smoke test

The image sets `ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "anvio-71py37"]`, so commands run inside the anvi'o conda environment:

```bash
docker run -it --rm dnalinux/anvio:7.1 anvi-interactive --version
```

## Notes

- The conda environment is defined by `anvio71.yaml`; `requirements.txt` lists the Python packages installed into it. The build also installs `dendropy==5.0.1`.
- The build downloads the SqueezeMeta v1.6.3 source tree into the image.
- The published image is large (about 3.4 GB compressed) because it bundles the full anvi'o conda environment.

## License

anvi'o is released under the GNU General Public License version 3 (GPL-3.0), per the upstream repository.
