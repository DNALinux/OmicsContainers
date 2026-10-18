# CVTree

This directory contains a Dockerfile for **CVTree**, a set of programs that build phylogenetic trees from genome or protein sequence data using composition vectors.

## What is CVTree?

**CVTree** implements the Composition Vector (CV) method: it turns FASTA files (`.faa`, `.ffn` or `.fna`) into composition vectors for a set of *k* values, derives distance matrices from them, and infers trees. The sources are vendored in this directory (`cvtree/`, `kit/` and `CMakeLists.txt`) and were written by Dr. Guanghong Zuo (T-Life Research Center, Fudan University; the file headers also carry a Wenzhou Institute, Chinese Academy of Sciences copyright). The Dockerfile records no upstream URL.

The build produces ten programs, all copied into `/usr/local/bin`: `cvtree`, `g2cv`, `cvdump`, `cv2dm`, `getdist`, `mconv`, `diffmtx`, `dm2tree`, `treedist` and `treeboot`.

Two of them are documented by their own usage text:

- `cvtree` — the main program. It reads a list of genomes (default `list`), computes the CVs for the `-k` values (default `5 6 7`), and writes distance matrices and Newick trees under a `cvtree/` subdirectory of the working directory. `-b` adds bootstrapping and `-h` prints the usage message.
- `g2cv` — computes the CVs only, either for a list of genomes or for a single FASTA file given with `-f`. It takes the same `-k`, `-g` and `-h` options.

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/cvtree/general

- **`dnalinux/cvtree:latest`** — currently points to `3.0.0`
- **`dnalinux/cvtree:3.0.0`** — two-stage `alpine` build from the sources in this directory. The build stage adds `g++`, `make`, `cmake`, `zlib-dev` and `boost-dev`, plus `hdf5-dev` and `nlohmann-json` from the Alpine edge community repository, and runs `cmake`/`make`; the runtime stage copies the binaries to `/usr/local/bin` and adds `libgomp`, `libstdc++`, `hdf5`, `hdf5-dev` and `nlohmann-json`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as `root`, working directory `/root/data`.

The Dockerfile's `LABEL` records only a Dockerfile `Version=0.2` and a description, with no `software.version`, so the `3.0.0` of the directory and tag name is not repeated anywhere in the image metadata.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

The build context must be the `3.0.0` directory, since the Dockerfile copies `./cvtree`, `./kit` and `./CMakeLists.txt` from it:

```bash
cd 3.0.0
docker build -t cvtree:3.0.0 .
```

## Smoke test

`-h` prints the usage message:

```bash
docker run -it --rm dnalinux/cvtree:3.0.0 cvtree -h
```

## License

The Dockerfile records no license field, and the vendored sources carry no project-wide license statement. The only license text present is the CC BY 3.0 notice in `kit/memory.h` for a third-party memory-usage snippet.
