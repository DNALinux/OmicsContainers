![An old rock in the desert](/imgs/omics.png) 

# Omics Containers

This is a curated collection of containers for bioinformatics, developed as part of the [DNALinux](https://dnalinux.com/) project. It is based on the [BioContainers project](https://github.com/BioContainers/containers). All containers are hosted at [Docker Hub](https://hub.docker.com/repositories/dnalinux).

## Available containers

Containers are grouped by category. Each name links to its directory, which contains the Dockerfile(s), available tags and usage notes.

---

### Index
1. [Data Access & Literature](#1-data-access--literature)
2. [Sequence Processing & Quality Control](#2-sequence-processing--quality-control)
3. [Assembly, Scaffolding & Quality](#3-assembly-scaffolding--quality)
4. [Alignment, Search & Variant Calling](#4-alignment-search--variant-calling)
5. [Annotation & Functional Genomics](#5-annotation--functional-genomics)
6. [Comparative Genomics & Phylogenetics](#6-comparative-genomics--phylogenetics)
7. [Specialized Omics & Imaging](#7-specialized-omics--imaging)
8. [Utilities, Runtimes & AI Tools](#8-utilities-runtimes--ai-tools)

---

### 1. Data Access & Literature
* [NCBI Datasets](/NCBI-Datasets) — Download genome sequences, annotations, and metadata from NCBI.
* [SRA Toolkit](/SRA-Toolkit) — Download and convert sequencing data from the NCBI Sequence Read Archive.
* [NCBI Tools (legacy)](/NCBI-Tools-legacy) — Legacy NCBI text-based utilities and libraries.
* [PaperJev](/PaperJev) — Retrieve PubMed papers, summarize PDF themes with local LLMs, and filter by relevance.

### 2. Sequence Processing & Quality Control
* [FastQC](/FastQC) — Quality control checks for high-throughput sequencing data.
* [fastp](/fastp) — Ultra-fast FASTQ preprocessor for QC, filtering, and adapter trimming.
* [Trimmomatic](/Trimmomatic) — Flexible read trimming for Illumina NGS data.
* [PEAR](/PEAR) — Memory-efficient paired-end read merger.

### 3. Assembly, Scaffolding & Quality
* **Assemblers:**
  * [SPAdes](/SPAdes) — Genome assembler for isolate and single-cell datasets.
  * [Hifiasm](/Hifiasm) — Haplotype-resolved *de novo* assembler for PacBio HiFi reads.
  * [MitoHiFi](/MitoHiFi) — Assemble mitochondrial genomes from PacBio HiFi reads.
* **Scaffolding & Finishing:**
  * [3D-DNA](/3D-DNA) — Hi-C-based scaffolding and chromosome-length assembly.
  * [AllHiC](/AllHiC) — Hi-C scaffolding of contigs.
  * [Redundans](/Redundans) — Scaffolding and reduction of heterozygous assemblies.
  * [SSPACE-LongRead](/SSPACE-LongRead) — Long-read scaffolder for pre-assembled contigs.
  * [LR_Gapcloser](/LR_Gapcloser) — Close gaps in assemblies using long reads.
  * [gfatools](/gfatools) — Manipulate GFA/rGFA assembly and pangenome graphs.
* **Evaluation & Polishing:**
  * [QUAST](/QUAST) — Evaluate genome assemblies by computing quality metrics.
  * [Pilon](/Pilon) — Automated assembly improvement and variant detection.

### 4. Alignment, Search & Variant Calling
* **Aligners:**
  * [BWA](/BWA) / [BWA-MEM2](/BWA-MEM2) — Burrows-Wheeler Aligner for short reads (standard & high-speed).
  * [Bowtie 2](/Bowtie-2) — Ultrafast read aligner for short reads.
  * [Minimap2](/Minimap2) — Versatile aligner for genomic and spliced nucleotide sequences.
* **Sequence Search:**
  * [BLAST+](/BLAST) — NCBI tool for searching nucleotide and protein databases.
  * [DIAMOND](/DIAMOND) — Accelerated BLAST-compatible sequence aligner.
  * [HMMER](/HMMER) — Profile hidden Markov models for protein analysis.
* **Variant Analysis:**
  * [GATK](/GATK) — Variant discovery and genotyping framework.
  * [bcftools](/bcftools) — Variant calling and VCF/BCF file manipulation.
  * [NanoCaller](/NanoCaller) — Call SNPs and indels from long-read data.
  * [CADD](/CADD) — Score deleteriousness of human SNVs and indels.
  * [METAL](/METAL) — Meta-analysis of large-scale GWAS studies.

### 5. Annotation & Functional Genomics
* **Prokaryotic & Eukaryotic Annotation:**
  * [Bakta](/Bakta) — Rapid, standardized annotation of bacterial genomes, MAGs, and plasmids.
  * [Prokka](/Prokka) — Rapid prokaryotic genome annotation.
  * [funannotate](/funannotate) — Eukaryotic genome prediction, annotation, and comparison pipeline.
  * [EvidentialGene](/EvidentialGene) — Evidence-directed gene construction pipeline.
* **Functional & Specialized Annotation:**
  * [antiSMASH](/antiSMASH) — Detection and analysis of secondary metabolite gene clusters.
  * [InterProScan](/InterProScan) — Scan protein sequences against InterPro databases.
  * [KofamScan](/KofamScan) — KEGG Orthology-based gene function annotation via HMMs.
  * [RepeatMasker](/RepeatMasker) — Screen DNA sequences for repeats and low-complexity regions.

### 6. Comparative Genomics & Phylogenetics
* [OrthoFinder](/orthofinder) — Infer orthogroups, gene trees, and rooted species trees.
* [Clustal Omega](/Clustal-Omega) — Accurate multiple sequence alignment of protein sequences.
* [MUSCLE](/MUSCLE) — High-throughput multiple sequence aligner.
* [PHYLIP](/PHYLIP) — Package of programs for inferring phylogenies.
* [CVTree](/CVTree) — Composition-vector-based phylogenetic tree construction.
* [RSAT](/RSAT) — Regulatory sequence analysis tools (motif discovery, TF binding).

### 7. Specialized Omics & Imaging
* **Metagenomics:**
  * [anvi'o](/anvio) — Analysis and visualization platform for metagenomics and pangenomics.
  * [CheckM2](/CheckM2) — Assessment of genome bin quality using machine learning.
* **Transcriptomics & Single-Cell:**
  * [scRNA-seq R workflow](/scrnaseq_r_workflow) — R environment for single-cell RNA-seq integration and clustering.
  * [BLAZE](/BLAZE) — Barcode identification from long reads for single-cell gene expression.
* **Proteomics & Mass Spectrometry:**
  * [OpenMS](/OpenMS) — Tools and C++ libraries for MS/MS data analysis.
  * [DIA-NN](/DIA-NN) — Processing data-independent acquisition (DIA) proteomics data.
* **Imaging & Browsers:**
  * [Cellpose](/Cellpose) — Generalist algorithm for cell and nucleus segmentation.
  * [DIPY](/DIPY) — Computational anatomy and diffusion MRI analysis.
  * [JBrowse 2](/JBrowse-2) — Next-generation genome browser CLI.

### 8. Utilities, Runtimes & AI Tools
* **Genomic Utilities:**
  * [samtools](/samtools) — Process SAM, BAM, and CRAM alignment files.
  * [bedtools](/bedtools) — Suite of utilities for feature manipulation and overlap analysis.
  * [bedGraphToBigWig](/bedGraphToBigWig) — Convert bedGraph tracks to bigWig format.
  * [tabix](/tabix) — Generic indexer for TAB-delimited genomic position files.
  * [Jellyfish](/Jellyfish) — Fast, memory-efficient k-mer counting.
  * [Primer3](/Primer3) — Design PCR primers and flanking oligonucleotides.
* **Base Images & Libraries:**
  * [biocontainers](/biocontainers) — Base image for BioDocker/BioContainers distributions.
  * [Python](/Python) — Free-threaded Python builds (GIL-disabled).
  * [Biopython](/Biopython) — Python library for computational biology.
  * [Dask](/Dask) — Library for parallel computing in Python.
* **AI Applications:**
  * [takollama](/takollama) — Local LLM integration and agentic AI application for biology (packaged with `uv`).
## FAQ

#### Why another biocontainer project?

The original BioContainers project contains many containers that are over five years old, with outdated bioinformatics software and based on older Linux versions. The goal of Omics Containers is to provide up-to-date software whenever possible, both at the operating system level and for bioinformatics tools. Additionally, it aims to make the containers compatible with multiple architectures when available.

#### How do I use a container? 

You can use it from source and build a docker image. If you don't want to build the image yourself, you can pull it from [Docker Hub](https://hub.docker.com/repositories/dnalinux).
Once you have the image, you can run it to instanciate a container.

#### How do I build a docker image?

Go to the directory where the Dockerfile is, and run:

```
docker build -t name .
```

#### How do I pull a docker image?

Search for the docker image you want in [Docker Hub](https://hub.docker.com/repositories/dnalinux), select the version and run:

```
docker pull dnalinux/bwa
```

#### How do I run a docker image?

Each docker image has its own way to run it, see the **overview** section in DockerHub or the Dockerfile.

#### How do I request a new container?

Open an issue in this repo telling which program you need.

#### Who is behind Omics Containers?

Omics Containers is supported by [DNALinux](https://dnalinux.com/), [Toyoko Bio](https://www.toyoko.io/), and a dedicated bioinformatics community.

#### Is it free?

Yes, every file in this repository is un the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) license, unless noted (some files comes with their own license). If you run these container in a cloud provider, they may charge you for the computer time needed to run the containers. 

## Related Resources

- **Tonina** — https://github.com/DNALinux/tonina
- **DNALinux Docker Hub** — https://hub.docker.com/u/dnalinux
- **DNALinux** — https://dnalinux.com/
- **Toyoko Bio** — https://toyoko.io/
- **BioContainers** — https://github.com/BioContainers/containers

## Authors

- [Sebastian Bassi](https://www.github.com/sbassi)
- [Virginia Gonazalez](https://www.github.com/virmax)
- [Gretta Yagudayev](https://www.github.com/gyagu98)
- Tristan Yang
- [Diya Sandeep Nair](https://github.com/diyanair30)
- [Facundo Mercado](https://www.github.com/Facundo1224)

## License

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)

## Feedback

If you have any feedback, please reach out to us at dnalinux@toyoko.io
