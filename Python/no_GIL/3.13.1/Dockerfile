FROM debian:bookworm-slim

LABEL base_image="debian:bookworm-slim" \
      software="Python" \
      software.version="3.13.1" \
      about.summary="Python with no GIL" \
      about.home="https://github.com/astral-sh/python-build-standalone" \
      upstream.version="3.13.1" \
      about.copyright="MIT" \
      about.license="PSL" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>"

USER root

ENV python_version=3.13.1
ENV python_build_date=20250115

RUN apt update && apt install -y wget tar zstd libgomp1

WORKDIR /opt/

RUN arch=$(uname -m) && \
    if [ "$arch" = "x86_64" ]; then \
        python_asset=cpython-${python_version}+${python_build_date}-x86_64-unknown-linux-gnu-freethreaded+pgo+lto-full.tar.zst; \
        python_url=https://github.com/astral-sh/python-build-standalone/releases/download/${python_build_date}/${python_asset}; \
    elif [ "$arch" = "aarch64" ]; then \
        python_asset=cpython-${python_version}+${python_build_date}-aarch64-unknown-linux-gnu-freethreaded+lto-full.tar.zst; \
        python_url=https://github.com/astral-sh/python-build-standalone/releases/download/${python_build_date}/$python_asset; \
    else \
        echo "Architecture $arch is not supported" >&2; \
        exit 1; \
    fi && \
    wget $python_url -O $python_asset \
    && tar --use-compress-program=unzstd -xf $python_asset \
    && rm $python_asset \
    && apt purge -y wget zstd \
    && apt autoremove -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/*

ENV PATH="/opt/python/install/bin:$PATH"

WORKDIR /scripts

COPY . .
