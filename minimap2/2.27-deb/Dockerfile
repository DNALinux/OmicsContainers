FROM debian:trixie-slim

# Metadata Labels
LABEL software="minimap2" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      base_image="debian:trixie-slim" \
      container="minimap2" \
      about.summary="Versatile pairwise aligner for genomic and spliced nucleotide sequences" \
      about.home="https://github.com/lh3/minimap2" \
      software.version="2.27-deb" \
      upstream.version="2.27" \
      version="1" \
      extra.identifiers.biotools="minimap2" \
      about.license="MIT" \
      extra.binaries="/usr/bin/minimap2"

# Install minimap2 and verify the version matches 2.27
RUN apt-get update && apt-get install -y \
    minimap2 \
    && minimap2 --version | grep "2.27" \
    && rm -rf /var/lib/apt/lists/*

# Set working directory for genomic data
WORKDIR /data

# Default command
ENTRYPOINT ["minimap2"]
CMD ["--help"]
