# Stage 1: Build
FROM debian:trixie-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    zlib1g-dev \
    wget \
    ca-certificates \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

# Download and extract bwa-mem2 v2.3
RUN wget https://github.com/bwa-mem2/bwa-mem2/releases/download/v2.3/Source_code_including_submodules.zip \
    && unzip Source_code_including_submodules.zip \
    && rm Source_code_including_submodules.zip

WORKDIR /tmp/bwa-mem2-2.3

# PATCH: Fix implicit declarations across the entire safestringlib submodule
# This adds <stdlib.h> for abort() and <ctype.h> for toupper() to all relevant C files
RUN find ext/safestringlib/safeclib/ -name "*.c" -exec sed -i '1i #include <stdlib.h>\n#include <ctype.h>' {} +

# Build for x86_64 (amd64)
RUN make

# Stage 2: Final Image
FROM debian:trixie-slim

LABEL software="bwa-mem2" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      base_image="debian:trixie-slim" \
      container="bwa-mem2" \
      about.summary="Next generation of the BWA-MEM algorithm" \
      about.home="https://github.com/bwa-mem2/bwa-mem2" \
      software.version="2.3-src" \
      upstream.version="2.3" \
      version="1" \
      extra.identifiers.biotools="bwa-mem2" \
      about.license="MIT" \
      extra.binaries="/usr/local/bin/bwa-mem2"

RUN apt-get update && apt-get install -y --no-install-recommends \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

# Copy the compiled binaries
COPY --from=builder /tmp/bwa-mem2-2.3/bwa-mem2* /usr/local/bin/

WORKDIR /data

ENTRYPOINT ["bwa-mem2"]
