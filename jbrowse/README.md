# JBrowse

This directory contains a Dockerfile for the **JBrowse** command-line tool.

## What is JBrowse?

**JBrowse 2** (https://jbrowse.org/jb2/) is a genome browser for visualising and sharing genomic data. This image installs only the command-line interface, the `jbrowse` command from the `@jbrowse/cli` npm package, described upstream as "a command line tool for working with JBrowse 2". The JBrowse web server and browser are not included — the Dockerfile's own `about.summary` says "CLI for jbrowse (CLI only, not the web server)".

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/jbrowse/general

- **`dnalinux/jbrowse:cli-3.6.4`** — the JBrowse CLI 3.6.4, installed globally with `npm install -g @jbrowse/cli@3.6.4` on `node:trixie-slim`. `linux/amd64` only. This is the only tag in the repository, and there is no `latest`.

## Building the image

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. To build it yourself instead, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing.

```bash
cd cli/3.6.4
docker build -t jbrowse:cli-3.6.4 .
```

## Smoke test

```bash
docker run -it --rm dnalinux/jbrowse:cli-3.6.4 jbrowse --version
```

## Note

`dnalinux/jbrowse2` is a separate Docker Hub repository publishing the same CLI at versions 3.6.4 and 3.6.5.

## License

The JBrowse CLI is licensed under the Apache License 2.0 (`about.license` label of the Dockerfile; the `@jbrowse/cli` package is likewise Apache-2.0).
