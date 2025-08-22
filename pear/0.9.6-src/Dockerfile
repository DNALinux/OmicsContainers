#FROM debian:bookworm-slim
FROM ubuntu:16.04

LABEL    software="PEAR" \ 
    base_image="debian:bookworm-slim" \ 
    about.summary="PEAR is an ultrafast, memory-efficient and highly accurate pair-end read merger. It is fully parallelized and can run with as low as just a few kilobytes of memory." \ 
    about.home="http://biopython.org" \ 
    software.version="0.9.6" \ 
    upstream.version="0.9.6" \ 
    version="1" \ 
    about.copyright=" " \ 
    about.license="other" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""


ENV PEAR_VERSION="0.9.6"

RUN apt-get update -y \
    && apt-get install -y wget build-essential



RUN wget https://depot.galaxyproject.org/software/pear/pear_0.9.6_src_all.tar.gz

#COPY PEAR-master.zip /tmp



# install PEAR
RUN tar -xvzf pear_0.9.6_src_all.tar.gz

COPY reader.c pear-0.9.6-src/src/

RUN cd pear-0.9.6-src \
    && ./configure \
    && make \
    && make install

# clean up
RUN rm -rf pear_0.9.6_src_all.tar.gz pear-0.9.6-src/
