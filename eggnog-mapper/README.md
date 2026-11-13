# eggNOG-mapper

This directory contains a Dockerfile for **eggNOG-mapper**, a tool for fast functional annotation of novel sequences using eggNOG orthology assignments.

## What is eggNOG-mapper?

**eggNOG-mapper** annotates protein sequences, coding sequences, genomes and metagenomes by transferring functional information from the precomputed orthologous groups and phylogenies of the eggNOG database. Instead of a plain BLAST search, it uses the orthology assignments in eggNOG so that annotations are transferred from fine-grained orthologues rather than from close paralogues. Searches are run with DIAMOND (default), MMseqs2 or HMMER, and genomes or contigs can be gene-predicted with Prodigal in the same run.

- Source code and releases: https://github.com/eggnogdb/eggnog-mapper
- Documentation: https://github.com/eggnogdb/eggnog-mapper/wiki
- Online service: http://eggnog-mapper.embl.de
- Citation: Cantalapiedra CP, Hernández-Plaza A, Letunic I, Bork P, Huerta-Cepas J. *eggNOG-mapper v2: functional annotation, orthology assignments, and domain prediction at the metagenomic scale.* Molecular Biology and Evolution, 2021. https://doi.org/10.1093/molbev/msab293

This image provides the stable 2.1.x line. The upstream `v3.0.0-beta6` release targets the eggNOG 7 database and is not compatible with eggNOG 5 data; it is not packaged here.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/eggnog-mapper/general

- **`dnalinux/eggnog-mapper:latest`** — currently points to `2.1.15-src`
- **`dnalinux/eggnog-mapper:2.1.15-src`** — eggNOG-mapper **2.1.15** installed from the upstream v2.1.15 source tarball on `debian:trixie-slim`, with DIAMOND, HMMER, MMseqs2, Prodigal and the Python dependencies from Debian. `esl-reformat` is built from the HMMER 3.4 Easel sources, which Debian does not package. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`.

Upstream publishes 2.1.15 as an annotated git tag (`v2.1.15`, tagged 2026-05-22 with the message "eggNOG-mapper v2.1.15 — final v2 release") but did not create a GitHub Release for it, so it does not appear on the project's Releases page. It is the final v2 release: compared with the `v2.1.14` tag, only the version string and the database download URL in `download_eggnog_data.py` change (the URL fix announced with 2.1.14). Bioconda also packages 2.1.15 from this tag.

The upstream tarball bundles pre-compiled x86-64 copies of DIAMOND, MMseqs2, Prodigal and HMMER. They are deleted during the build so that the architecture-neutral Debian packages are always used.

The image sets `CMD ["emapper.py", "--help"]`, so running it without arguments prints the help text. All scripts from the release are on `PATH`: `emapper.py`, `download_eggnog_data.py`, `create_dbs.py`, `hmm_mapper.py`, `hmm_server.py` and `hmm_worker.py`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 2.1.15-src
docker build -t eggnog-mapper:2.1.15-src .
```

For a multi-arch build use buildx with `--platform` and `--push`:

```bash
cd 2.1.15-src
docker buildx build --platform linux/amd64,linux/arm64 \
    -t dnalinux/eggnog-mapper:2.1.15-src --push .
```

## Smoke test

`emapper.py --version` prints the eggNOG-mapper version together with the detected DIAMOND and MMseqs2 versions:

```bash
docker run --rm dnalinux/eggnog-mapper:2.1.15-src emapper.py --version
```

Check that the external tools and the Easel helper resolve from `PATH`:

```bash
docker run --rm dnalinux/eggnog-mapper:2.1.15-src bash -c \
  'for t in diamond hmmsearch hmmpress mmseqs prodigal esl-reformat; do printf "%-14s %s\n" $t $(command -v $t); done'
```

## Reference data

The eggNOG database is **not** included in the image. Download it once into a directory on the host so it survives the container. The default download (annotation database, taxonomy database and DIAMOND database) is several GB; the DIAMOND database alone is about 4 GB after decompression.

```bash
mkdir -p "$PWD/emapperdb"
docker run --rm -v "$PWD/emapperdb:/db" dnalinux/eggnog-mapper:2.1.15-src \
    download_eggnog_data.py --data_dir /db -y
```

Options for the other search modes: `-M` downloads the MMseqs2 database, `-P` the Pfam database and `-H -d TAXID` an eggNOG HMM database. Run `download_eggnog_data.py --help` for the full list.

The downloader writes to `/opt/eggnog-mapper/data` unless `--data_dir` or the `EGGNOG_DATA_DIR` environment variable is set, so pass `--data_dir` (or set `EGGNOG_DATA_DIR`) when running `emapper.py` as well. The directory must already exist.

## Usage

Annotate a protein FASTA file with DIAMOND:

```bash
docker run --rm -v "$PWD:/data" -v "$PWD/emapperdb:/db" \
    dnalinux/eggnog-mapper:2.1.15-src \
    emapper.py -i /data/proteins.fa --data_dir /db -o /data/annotation --cpu 8
```

Annotate a genome: add `--itype genome` (gene prediction is inferred from the DIAMOND/MMseqs2 hits by default, or run with Prodigal by adding `--genepred prodigal`). Use `--itype CDS` for coding sequences and `--itype metagenome` for metagenomic contigs.

Select the search engine with `-m diamond` (default), `-m mmseqs` or `-m hmmer`. To produce the Excel summary, add `--excel`. Pfam domain realignment (`--pfam_realign`) additionally needs the Pfam database (`download_eggnog_data.py -P`) and the `esl-reformat` binary included in this image.

Results are written next to `-o` as `.emapper.annotations`, `.emapper.hits`, `.emapper.seed_orthologs` and, when requesting them, the `.genepred.gff`/`.decorated.gff` and `.xlsx` files.

## License

eggNOG-mapper is distributed under the GNU Affero General Public License, version 3 (the upstream `LICENSE.txt`; the Python source headers mention GPL v2 and `setup.cfg` says "GPLv3"). The Dockerfile records `about.license="AGPL-3.0-only"`, matching the bioconda package metadata. The eggNOG database is provided by the eggNOG/EMBL team under its own terms.
