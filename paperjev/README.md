# PaperJev

This directory contains a Dockerfile for **PaperJev**, a biology paper toolset for retrieving, summarizing and filtering scientific literature.

## What is PaperJev?

**PaperJev** (https://github.com/ToyokoLabs/PaperJev) retrieves recent biology papers from NCBI PubMed, summarizes the common themes of a set of PDF papers with a local Ollama instance, and filters the retrieved papers by relevance. Each step can be run from the command line, or all of them together through the bundled web app.

The image is the web app: a FastAPI backend serving the built React frontend on port `8000`. It also contains the command-line modules (`pubmed_downloader.py`, `pdf_summarizer.py`, `relevance_filter.py`, `relevance_filter_LLM.py` and `relevance_filter_nimble.py`).

## Available images

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/paperjev/general

- **`dnalinux/paperjev:1.0-src`** — PaperJev **1.0** built from the `v1.0` source archive (SHA-256 pinned in the Dockerfile). The frontend is built with Node 22 and the backend runs on `python:3.10-slim-bookworm` with its dependencies installed from `uv.lock`. Multi-arch (`linux/amd64`, `linux/arm64`), runs as the unprivileged user `dnalinux`, exposes port `8000`.

## Configuration

PaperJev reads two files from its working directory, `/app`:

- `config.json` — NCBI e-mail/API key and, optionally, the TypeSafe API key.
- `ollama_config.json` — Ollama URL, model name and generation parameters.

Sample files are included in the image as `/app/config.json.sample` and `/app/ollama_config.json.sample`. Do not put credentials in the image; mount the real files at run time. You can extract the samples from a pulled image:

```bash
docker run --rm --entrypoint cat dnalinux/paperjev:1.0-src /app/config.json.sample > config.json
docker run --rm --entrypoint cat dnalinux/paperjev:1.0-src /app/ollama_config.json.sample > ollama_config.json
```

The web app creates the TypeSafe client when it starts, so the container exits if no API key is available. Provide it in `config.json` or with `-e TYPESAFE_API_KEY=...`.

Ollama runs outside the container. `OLLAMA_URL` defaults to `http://host.docker.internal:11434`; on Linux add `--add-host=host.docker.internal:host-gateway` so that name resolves.

## Running the web app

The image is already published on Docker Hub; pull the tag you need from the repository listed under **Available images**. If you prefer to build it yourself, see below.

```bash
docker run -d --name paperjev -p 8000:8000 \
    -v $(pwd)/config.json:/app/config.json:ro \
    -v $(pwd)/ollama_config.json:/app/ollama_config.json:ro \
    -v paperjev_sessions:/tmp/bio_papers_sessions \
    --add-host=host.docker.internal:host-gateway \
    dnalinux/paperjev:1.0-src
```

Then open http://localhost:8000. Session artifacts are kept in the `paperjev_sessions` volume; in-flight sessions live in memory and are lost when the container restarts.

## Running the command-line modules

Run the container with a working directory mounted for inputs and outputs, and with the configuration files available there:

```bash
docker run --rm -it \
    -v $(pwd)/work:/work \
    -v $(pwd)/work/config.json:/work/config.json:ro \
    -v $(pwd)/work/ollama_config.json:/work/ollama_config.json:ro \
    --add-host=host.docker.internal:host-gateway \
    dnalinux/paperjev:1.0-src \
    bash -c 'cd /work && python /app/pubmed_downloader.py --count 200'
```

Use the same pattern for `pdf_summarizer.py --dir /work/pdfs` and `relevance_filter.py`.

## Building the image

If you prefer to build the image yourself instead of pulling it, use any local tag you like — the `dnalinux/` prefix is only used by the project maintainers when publishing:

```bash
cd 1.0-src
docker build -t paperjev:1.0-src .
```

## Smoke test

```bash
docker run -it --rm -e TYPESAFE_API_KEY=dummy paperjev:1.0-src \
    python -c 'import app.main; print("PaperJev app import OK")'
```

## License

PaperJev is released under the GNU General Public License v3 (GPL-3.0). See `LICENSE` in the upstream repository.
