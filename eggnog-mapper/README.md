# eggNOG-mapper

This directory contains Dockerfiles for **eggNOG-mapper**, a tool for fast functional annotation of novel sequences using eggNOG orthology assignments.

## What is eggNOG-mapper?

**eggNOG-mapper** annotates protein sequences, coding sequences, genomes and metagenomes by transferring functional information from the precomputed orthologous groups and phylogenies of the eggNOG database. Instead of a plain BLAST search, it uses the orthology assignments in eggNOG so that annotations are transferred from fine-grained orthologues rather than from close paralogues. Searches are run with DIAMOND (default), MMseqs2 or HMMER (v2 only), and genomes or contigs can be gene-predicted with Prodigal in the same run.

- Source code and releases: https://github.com/eggnogdb/eggnog-mapper
- Documentation: https://github.com/eggnogdb/eggnog-mapper/wiki (v2) and https://github.com/eggnogdb/eggnog-mapper/blob/master/USAGE.md (v3)
- Citation (v2): Cantalapiedra CP, Hernández-Plaza A, Letunic I, Bork P, Huerta-Cepas J. *eggNOG-mapper v2: functional annotation, orthology assignments, and domain prediction at the metagenomic scale.* Molecular Biology and Evolution, 2021. https://doi.org/10.1093/molbev/msab293
- Citation (v3/eggNOG 7): Hernández-Plaza A, Deng Z, Robledo-Yagüe F, Szklarczyk D, von Mering C, Bork P, Huerta-Cepas J. *eggNOG v7: phylogeny-based orthology predictions and functional annotations.* Nucleic Acids Research 54(D1):D402–D408, 2026. https://doi.org/10.1093/nar/gkaf1249

The two versions use **incompatible databases**: v3 requires eggNOG 7 data, v2 requires eggNOG 5 data. They can be installed side by side by mounting different database directories.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/eggnog-mapper/general

- **`dnalinux/eggnog-mapper:latest`** — currently points to `3.0.0-beta6-src`
- **`dnalinux/eggnog-mapper:3.0.0-beta6-src`** — eggNOG-mapper **3.0.0-beta6** (eggNOG 7, beta) installed from the upstream v3.0.0-beta6 source tarball into a Python 3.12 virtual environment on `python:3.12-slim-trixie`, with the Cython extensions compiled. DIAMOND, HMMER, MMseqs2, Prodigal and the Easel `esl-reformat` helper are available on `PATH`; the first four come from Debian (DIAMOND 2.1.11, HMMER 3.4, MMseqs2 15, Prodigal 2.6.3), `esl-reformat` is built from the HMMER 3.4 Easel sources. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`.
- **`dnalinux/eggnog-mapper:2.1.15-src`** — eggNOG-mapper **2.1.15** (eggNOG 5, final v2 release) installed from the upstream v2.1.15 source tarball on `debian:trixie-slim`, with DIAMOND, HMMER, MMseqs2, Prodigal and the Python dependencies from Debian. `esl-reformat` is built from the HMMER 3.4 Easel sources. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`.

| | `2.1.15-src` | `3.0.0-beta6-src` |
|---|---|---|
| Status | final stable v2 release | beta of v3 |
| Database | eggNOG 5 (`5.0.2`) | eggNOG 7 (`7.0.0`) |
| Core database size | several GB (DIAMOND DB ~4 GB) | ~45 GB |
| Search backends | DIAMOND, MMseqs2, HMMER | DIAMOND, MMseqs2 (HMMER only for `--pfam_realign`) |
| Python | Debian Python 3.13 | Python 3.12 (venv, Cython extensions) |
| Output columns | 25 | 22 |

Use `3.0.0-beta6-src` for eggNOG 7 data and new work; keep `2.1.15-src` for reproducibility with eggNOG 5 / v2 results.

Upstream publishes 2.1.15 as an annotated git tag (`v2.1.15`, tagged 2026-05-22 with the message "eggNOG-mapper v2.1.15 — final v2 release") but did not create a GitHub Release for it, so it does not appear on the project's Releases page. It is the final v2 release: compared with the `v2.1.14` tag, only the version string and the database download URL in `download_eggnog_data.py` change (the URL fix announced with 2.1.14). Bioconda also packages 2.1.15 from this tag.

The v2 tarball bundles pre-compiled x86-64 copies of DIAMOND, MMseqs2, Prodigal and HMMER. They are deleted during the build so that the architecture-neutral Debian packages are always used. v3 no longer bundles them and resolves every tool from `PATH`.

Both images set `CMD ["emapper.py", "--help"]`, so running them without arguments prints the help text. The v2 image exposes `emapper.py`, `download_eggnog_data.py`, `create_dbs.py`, `hmm_mapper.py`, `hmm_server.py` and `hmm_worker.py`; v3 exposes the same scripts except `hmm_mapper.py`, which was removed together with the HMMER search mode.

## Building the images

The images are already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build one yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd 3.0.0-beta6-src
docker build -t eggnog-mapper:3.0.0-beta6-src .

cd ../2.1.15-src
docker build -t eggnog-mapper:2.1.15-src .
```

For a multi-arch build use buildx with `--platform` and `--push`:

```bash
cd 3.0.0-beta6-src
docker buildx build --platform linux/amd64,linux/arm64 \
    -t dnalinux/eggnog-mapper:3.0.0-beta6-src --push .
```

## Smoke test

`emapper.py --version` prints the version and the detected DIAMOND version:

```bash
docker run --rm dnalinux/eggnog-mapper:3.0.0-beta6-src emapper.py --version
docker run --rm dnalinux/eggnog-mapper:2.1.15-src emapper.py --version
```

Check that the external tools and the Easel helper resolve from `PATH`:

```bash
docker run --rm dnalinux/eggnog-mapper:3.0.0-beta6-src bash -c \
  'for t in diamond hmmsearch hmmpress mmseqs prodigal esl-reformat; do printf "%-14s %s\n" $t $(command -v $t); done'
```

The v3 image also offers an end-to-end check that needs no full database: `emapper.py --selftest` downloads a ~15 MB reference bundle and runs all four input types (proteins, CDS, genome, metagenome).

```bash
docker run --rm dnalinux/eggnog-mapper:3.0.0-beta6-src emapper.py --selftest
```

At the time of writing the reference bundle published upstream still contains golden files in the pre-beta6 25-column layout, so beta6 reports `FAIL` for all four input types even though the annotations themselves match; the run still exercises the whole pipeline. Treat the self-test as an upstream-known issue until the bundle is refreshed.

To confirm the Cython extensions were compiled (instead of the pure-Python fallback):

```bash
docker run --rm dnalinux/eggnog-mapper:3.0.0-beta6-src python -c \
  'from eggnogmapper.annotator.codec import _BACKEND; print(_BACKEND)'
```

## Reference data

The eggNOG databases are **not** included in the images. Download the one matching the mapper version into a directory on the host so it survives the container. The directory must already exist.

**v3 / eggNOG 7** — core download (annotation DB, DIAMOND DB, taxonomy, GO OBO and prebuilt caches) is about 45 GB; add `-M` for the optional MMseqs2 database and `-P` for Pfam:

```bash
mkdir -p "$PWD/emapperdb-v7"
docker run --rm -v "$PWD/emapperdb-v7:/db" dnalinux/eggnog-mapper:3.0.0-beta6-src \
    download_eggnog_data.py --data_dir /db -y
```

**v2 / eggNOG 5** — the default download is several GB (the DIAMOND database alone is about 4 GB after decompression); `-M`, `-P` and `-H -d TAXID` add the optional MMseqs2, Pfam and HMM databases:

```bash
mkdir -p "$PWD/emapperdb-v5"
docker run --rm -v "$PWD/emapperdb-v5:/db" dnalinux/eggnog-mapper:2.1.15-src \
    download_eggnog_data.py --data_dir /db -y
```

Both downloaders write to a default location inside the image unless `--data_dir` or the `EGGNOG_DATA_DIR` environment variable is set, so pass `--data_dir` (or set `EGGNOG_DATA_DIR`) when running `emapper.py` as well.

## Usage

Annotate a protein FASTA file with DIAMOND (v3):

```bash
docker run --rm -v "$PWD:/data" -v "$PWD/emapperdb-v7:/db" \
    dnalinux/eggnog-mapper:3.0.0-beta6-src \
    emapper.py -i /data/proteins.fa --data_dir /db -o /data/annotation --cpu 8
```

The same command with the v2 image and the eggNOG 5 database directory:

```bash
docker run --rm -v "$PWD:/data" -v "$PWD/emapperdb-v5:/db" \
    dnalinux/eggnog-mapper:2.1.15-src \
    emapper.py -i /data/proteins.fa --data_dir /db -o /data/annotation --cpu 8
```

Annotate a genome: add `--itype genome` (gene prediction is inferred from the DIAMOND/MMseqs2 hits by default, or run with Prodigal by adding `--genepred prodigal`). Use `--itype CDS` for coding sequences and `--itype metagenome` for metagenomic contigs.

Select the search engine with `-m diamond` (default) or `-m mmseqs`. In v3 the HMMER search mode and `hmm_mapper.py` were removed; HMMER is still used internally for `--pfam_realign`, which additionally needs the Pfam database (`download_eggnog_data.py -P`) and the included `esl-reformat`. To produce the Excel summary, add `--excel`.

Results are written next to `-o` as `.emapper.annotations`, `.emapper.hits`, `.emapper.seed_orthologs` and, when requesting them, the `.genepred.gff`/`.decorated.gff` and `.xlsx` files. v3 writes 22 annotation columns; v2 writes 25.

## License

eggNOG-mapper is distributed under the GNU Affero General Public License, version 3 (the upstream `LICENSE.txt`; the v2 Python source headers mention GPL v2 and `setup.cfg` says "GPLv3"). Both Dockerfiles record `about.license="AGPL-3.0-only"`, matching the bioconda package metadata. The eggNOG database is provided by the eggNOG/EMBL team under its own terms.
