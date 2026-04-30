FROM debian:trixie-slim AS builder

RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN wget https://github.com/lh3/bwa/archive/refs/tags/v0.7.19.tar.gz \
    && tar -xzf v0.7.19.tar.gz

WORKDIR /tmp/bwa-0.7.19
RUN make

FROM debian:trixie-slim

LABEL software="bwa" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
      base_image="debian:trixie-slim" \
      container="bwa" \
      about.summary="Burrows-Wheeler Aligner" \
      about.home="http://bio-bwa.sourceforge.net/" \
      software.version="0.7.19-src" \
      upstream.version="0.7.19" \
      version="1" \
      extra.identifiers.biotools="bwa" \
      about.copyright=" 2008 Genome Research Ltd (GRL)" \
      about.license="MIT" \
      about.license_file="/usr/share/doc/bwa/copyright" \
      extra.binaries="/usr/local/bin/bwa" \
      about.tags="biology::peptidic, field::biology, field::biology:bioinformatics,:c, interface::commandline, interface::text-mode,:program, use::analysing, use::comparing"

RUN apt-get update && apt-get install -y \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /tmp/bwa-0.7.19/bwa /usr/local/bin/bwa

WORKDIR /data

ENTRYPOINT ["bwa"]
CMD ["--help"]


# build:
# docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t dnalinux/bwa:latest --push .
