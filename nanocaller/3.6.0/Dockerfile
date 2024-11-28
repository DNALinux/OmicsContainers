
FROM continuumio/miniconda3
USER root

LABEL    software="nanocaller" \ 
    maintainer="Sebastian Bassi <sebastian@toyoko.io>" 

WORKDIR /app

SHELL [ "/bin/bash", "--login", "-c" ]

RUN wget https://github.com/WGLab/NanoCaller/archive/refs/tags/v3.6.0.tar.gz ;\
    tar xvfz v3.6.0.tar.gz

RUN conda env create -f /app/NanoCaller-3.6.0/environment.yml && conda clean --yes --all

RUN conda init bash

RUN echo "conda activate nanocaller_env" > ~/.bashrc

ENV PATH=/opt/conda/envs/nanocaller_env/bin:$PATH

RUN cp -r /app/NanoCaller-3.6.0/nanocaller_src /opt/conda/envs/nanocaller_env/bin/nanocaller_src
RUN cp /app/NanoCaller-3.6.0/NanoCaller /opt/conda/envs/nanocaller_env/bin/

RUN chmod +x /opt/conda/envs/nanocaller_env/bin/NanoCaller