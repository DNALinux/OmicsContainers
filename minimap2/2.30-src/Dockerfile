# Stage 1: Build environment
FROM debian:trixie-slim AS builder

# Automatically populated by buildx
ARG TARGETPLATFORM

RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

# Download version 2.30
RUN wget https://github.com/lh3/minimap2/archive/refs/tags/v2.30.tar.gz \
    && tar -xzf v2.30.tar.gz

WORKDIR /tmp/minimap2-2.30

# Conditional compilation based on the target platform
RUN if [ "$TARGETPLATFORM" = "linux/amd64" ]; then \
        echo "Building for x86_64..." && \
        make; \
    elif [ "$TARGETPLATFORM" = "linux/arm64" ]; then \
        echo "Building for ARMv8 (64-bit)..." && \
        make arm_neon=1 aarch64=1; \
    elif [ "$TARGETPLATFORM" = "linux/arm/v7" ]; then \
        echo "Building for ARMv7 (32-bit)..." && \
        make arm_neon=1; \
    else \
        echo "Platform $TARGETPLATFORM not explicitly handled, attempting default make..." && \
        make; \
    fi

# Stage 2: Final runtime image
FROM debian:trixie-slim

LABEL software="minimap2" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      base_image="debian:trixie-slim" \
      container="minimap2" \
      about.summary="Versatile pairwise aligner for genomic and spliced nucleotide sequences" \
      about.home="https://github.com/lh3/minimap2" \
      software.version="2.30-src" \
      upstream.version="2.30" \
      version="1" \
      extra.identifiers.biotools="minimap2" \
      about.license="MIT" \
      extra.binaries="/usr/local/bin/minimap2"

# Install runtime dependency
RUN apt-get update && apt-get install -y \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

# Copy binary from builder
COPY --from=builder /tmp/minimap2-2.30/minimap2 /usr/local/bin/minimap2

WORKDIR /data

ENTRYPOINT ["minimap2"]
CMD ["--help"]
