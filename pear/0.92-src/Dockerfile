#FROM debian:bookworm-slim
FROM ubuntu:16.04

LABEL    software="PEAR" \ 
    base_image="debian:bookworm-slim" \ 
    about.summary="PEAR is an ultrafast, memory-efficient and highly accurate pair-end read merger. It is fully parallelized and can run with as low as just a few kilobytes of memory." \ 
    about.home="http://biopython.org" \ 
    software.version="0.9.2" \ 
    upstream.version="0.9.2" \ 
    version="1" \ 
    about.copyright=" " \ 
    about.license="other" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""


ENV PEAR_VERSION="0.9.2"

RUN apt-get update -y \
    && apt-get install -y wget build-essential unzip



RUN wget https://github.com/hisplan/docker-PEAR/raw/refs/heads/master/PEAR-master.zip

#COPY PEAR-master.zip /tmp



# install PEAR
RUN unzip PEAR-master.zip \
    && cd PEAR-master \
    && ./configure \
    && make \
    && make install

# clean up
RUN rm -rf PEAR-master.zip PEAR-master/
