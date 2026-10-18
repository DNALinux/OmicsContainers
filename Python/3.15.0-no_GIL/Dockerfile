FROM debian:trixie-slim

LABEL base_image="debian:trixie-slim" \
      software="Python" \
      software.version="3.15.0" \
      about.summary="Python with no GIL by default" \
      about.home="https://github.com/astral-sh/python-build-standalone" \
      upstream.version="3.15.0" \
      about.license="PSL" \
      maintainer="Sebastian Bassi <sebastian@toyoko.io>"

USER root

ENV python_version=3.15.0
ENV python_build_date=20261013

# Use the free-threaded interpreter, and disable the GIL at startup for every
# process in the image (the regular CPython 3.15 build always has the GIL).
# A single process can still opt in with `python3 -X gil=1`.
ENV PYTHON_GIL=0

RUN apt update && apt install -y wget tar zstd libgomp1

WORKDIR /opt/

RUN arch=$(uname -m) && \
    if [ "$arch" = "x86_64" ]; then \
        python_asset=cpython-${python_version}+${python_build_date}-x86_64-unknown-linux-gnu-freethreaded+pgo+lto-full.tar.zst; \
    elif [ "$arch" = "aarch64" ]; then \
        python_asset=cpython-${python_version}+${python_build_date}-aarch64-unknown-linux-gnu-freethreaded+pgo+lto-full.tar.zst; \
    else \
        echo "Architecture $arch is not supported" >&2; \
        exit 1; \
    fi && \
    python_url=https://github.com/astral-sh/python-build-standalone/releases/download/${python_build_date}/${python_asset} && \
    wget "$python_url" -O "$python_asset" \
    && tar --use-compress-program=unzstd -xf "$python_asset" \
    && rm "$python_asset" \
    && apt purge -y wget zstd \
    && apt autoremove -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/*

ENV PATH="/opt/python/install/bin:$PATH"

WORKDIR /scripts

COPY . .
