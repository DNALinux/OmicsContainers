# JBrowse 2

This directory contains Dockerfiles for the **JBrowse 2** command-line tool.

## What is JBrowse 2?

**JBrowse 2** (https://jbrowse.org/jb2/) is a genome browser for visualising and sharing genomic data. These images install only the command-line interface, the `jbrowse` command from the `@jbrowse/cli` npm package, described upstream as "a command line tool for working with JBrowse 2". The JBrowse web server and browser are not included — the Dockerfiles' own `about.summary` says "CLI for jbrowse2 (CLI only, not the web server)".

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/jbrowse2/general

- **`dnalinux/jbrowse2:cli-3.6.5`** — the JBrowse CLI 3.6.5, installed globally with `npm install -g @jbrowse/cli@3.6.5` on `node:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).
- **`dnalinux/jbrowse2:cli-3.6.4`** — the JBrowse CLI 3.6.4, installed globally with `npm install -g @jbrowse/cli@3.6.4` on `node:trixie-slim`. Multi-arch (`linux/amd64`, `linux/arm64`).

There is no `latest` tag.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd cli/3.6.5
docker build -t jbrowse2:cli-3.6.5 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/jbrowse2:cli-3.6.5 jbrowse --version
```

## Note

`dnalinux/jbrowse` is a separate Docker Hub repository publishing the same CLI at version 3.6.4.

## License

The JBrowse CLI is licensed under the Apache License 2.0 (`about.license` label of the Dockerfiles; the `@jbrowse/cli` package is likewise Apache-2.0).
