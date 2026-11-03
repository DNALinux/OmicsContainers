# pyBigWig

This directory contains Dockerfiles for **pyBigWig**, a Python library for reading and writing bigWig files.

## What is pyBigWig?

**pyBigWig** (https://github.com/deeptools/pyBigWig) is a Python extension for quick access to bigBed and bigWig files, built on top of the UCSC `libBigWig` C library. It lets you create, query and modify bigWig coverage tracks (and bigBed feature files) from Python, for example to build custom tracks or aggregate signal over intervals.

## Available images

The images are already published to Docker Hub, so in most cases you can simply pull the one you need:

```bash
docker pull dnalinux/pybigwig:0.3.29-pip
```

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/pybigwig/general

- **`dnalinux/pybigwig:0.3.29-pip`** — pyBigWig 0.3.29 installed with `pip` into a virtual environment at `/pyBigWig` on `debian:trixie-slim`.

## Building the image

If you prefer to build the image yourself instead of pulling it, give it a local tag of your choosing. The `dnalinux/` prefix identifies the images published by the DNALinux project and is not needed for a local build:

```bash
cd 0.3.29-pip
docker build -t pybigwig:0.3.29-pip .
```

## Smoke test

pyBigWig is a library rather than a command, and it is installed in a virtual environment, so call that environment's interpreter. Use the image name you have locally, either the pulled `dnalinux/pybigwig:0.3.29-pip` or your own `pybigwig:0.3.29-pip`:

```bash
docker run -it --rm pybigwig:0.3.29-pip /pyBigWig/bin/python -c 'import pyBigWig; print(pyBigWig.__version__)'
```

## License

pyBigWig is distributed under the MIT license (https://github.com/deeptools/pyBigWig/blob/master/LICENSE). The Dockerfile records `about.license="MIT"`.
