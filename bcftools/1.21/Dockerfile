FROM debian:bookworm-slim

MAINTAINER Sebastian Bassi <sebastian@toyoko.io>
LABEL software="bcftools" \ 
    base_image="debian:bookworm-slim" \ 
    container="bcftools" \ 
    about.summary="Variant callilng and file manipulation" \ 
    about.home="https://samtools.github.io/bcftools/howtos/index.html" \ 
    software.version="1.21-deb" \ 
    upstream.version="1.21" \ 
    version="1" \ 
    about.copyright="Genome Research Ltd" \ 
    about.license="other" \ 
    about.license_file="/usr/share/doc/bcftools/copyright" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags="field::biology:bioinformatics"

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y bcftools=1.21-deb && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*


