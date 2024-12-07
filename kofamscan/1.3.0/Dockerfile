FROM debian:trixie-slim

LABEL    software="kofamscan" \
    base_image="debian:trixie-slim" \
    about.summary="KofamScan is a gene function annotation tool based on KEGG Orthology and hidden Markov model. You need KOfam database to use this tool" \
    about.home="https://www.genome.jp/tools/kofamkoala/" \
    software.version="1.3.0" \
    upstream.version="1.3.0" \
    version="1" \
    about.copyright="Aramaki T., Blanc-Mathieu R., Endo H., Ohkubo K., Kanehisa M., Goto S., Ogata H." \
    about.license="MIT" \
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" \
    about.tags=""

USER root
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y wget ruby hmmer=3.4+dfsg-2 parallel && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN git clone https://github.com/takaram/kofam_scan.git
RUN wget https://github.com/takaram/kofam_scan/archive/refs/tags/v1.3.0.tar.gz && tar xvfz v1.3.0.tar.gz && rm v1.3.0.tar.gz
