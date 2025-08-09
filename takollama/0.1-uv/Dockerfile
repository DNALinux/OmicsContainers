FROM debian:bookworm-slim

ARG FILE_URL="https://github.com/DNALinux/ai/releases/download/demo/takollama.tar.bz2"

RUN apt update && apt install -y --no-install-recommends \
    curl ca-certificates bzip2 python3 python3-venv python3-pip build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN curl -fsSL https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"

ADD "$FILE_URL" .

RUN tar -xjf takollama.tar.bz2 && rm takollama.tar.bz2

WORKDIR /app/ai
RUN uv sync --locked

