# syntax=docker/dockerfile:1

# PaperJev v1.0 is distributed as a source archive, not as a pip package.
FROM debian:trixie-slim AS source

ARG paperjev_version=1.0
ARG paperjev_sha256=8fb9b6884ecbfe324d824c6062eee005f9d8a1c73c95916248f473d7479ad519

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    mkdir -p /src && \
    curl -fsSL "https://github.com/ToyokoLabs/PaperJev/archive/refs/tags/v${paperjev_version}.tar.gz" -o /tmp/paperjev.tar.gz && \
    echo "${paperjev_sha256}  /tmp/paperjev.tar.gz" | sha256sum -c - && \
    tar xzf /tmp/paperjev.tar.gz -C /src --strip-components=1 && \
    rm /tmp/paperjev.tar.gz

# ---- Stage 1: frontend build ----
FROM node:22-alpine AS frontend

WORKDIR /build
COPY --from=source /src/frontend/package.json /src/frontend/package-lock.json ./
RUN npm ci
COPY --from=source /src/frontend/ ./
RUN npm run build

# ---- Stage 2: backend + static frontend ----
FROM python:3.10-slim-bookworm

LABEL software="paperjev" \
    base_image="python:3.10-slim-bookworm" \
    container="paperjev" \
    about.summary="Biology paper toolset: PubMed retrieval, PDF theme summarization and relevance filtering" \
    about.home="https://github.com/ToyokoLabs/PaperJev" \
    software.version="1.0-src" \
    upstream.version="1.0" \
    version="1" \
    about.copyright="Toyoko Labs" \
    about.license="GPL-3.0" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="literature,text-mining,pubmed,llm"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:${PATH}" \
    OLLAMA_URL="http://host.docker.internal:11434"

COPY --from=ghcr.io/astral-sh/uv:0.13.1 /uv /uvx /usr/local/bin/

WORKDIR /app

COPY --from=source /src/pyproject.toml /src/uv.lock /src/README.md ./
RUN uv sync --frozen --no-dev

COPY --from=source /src/app ./app/
COPY --from=source /src/pubmed_client.py /src/models.py ./
COPY --from=source /src/pubmed_downloader.py /src/pdf_summarizer.py \
    /src/relevance_filter.py /src/relevance_filter_LLM.py /src/relevance_filter_nimble.py ./
COPY --from=source /src/config.json.sample /src/ollama_config.json.sample ./
COPY --from=frontend /build/dist ./frontend/dist

RUN useradd --create-home --shell /bin/bash dnalinux && \
    chown -R dnalinux:dnalinux /app

USER dnalinux

EXPOSE 8000

CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Usage example:
# docker run -d --name paperjev -p 8000:8000 \
#     -v $(pwd)/config.json:/app/config.json:ro \
#     -v $(pwd)/ollama_config.json:/app/ollama_config.json:ro \
#     -v paperjev_sessions:/tmp/bio_papers_sessions \
#     --add-host=host.docker.internal:host-gateway \
#     dnalinux/paperjev:1.0-src
# Then open http://localhost:8000
