![An old rock in the desert](/imgs/omics.png) 

# Omics Containers

This is a curated collection of containers for bioinformatics, developed as part of the [DNALinux](https://dnalinux.com/) project. It is based on the [BioContainers project](https://github.com/BioContainers/containers). All containers are hosted at [Docker Hub](https://hub.docker.com/repositories/dnalinux).

## Available containers

Containers are grouped by category. Each name links to its directory, which contains the Dockerfile(s), available tags and usage notes.

### Data access and databases

- [NCBI Datasets](NCBI-Datasets/) — download genome sequences, annotations and metadata from NCBI databases.
- [SRA Toolkit](sra-toolkit/) — download and convert sequencing data from the NCBI Sequence Read Archive.
- [NCBI tools (legacy)](ncbi-tools-bin/) — legacy NCBI text-based utilities and libraries.

### Read processing and quality control

- [FastQC](fastqc/) — quality control for high-throughput sequencing data.
- [fastp](fastp/) — ultra-fast all-in-one FASTQ preprocessor: QC, filtering and adapter trimming.
- [Trimmomatic](trimmomatic/) — flexible read trimming for Illumina NGS data.
- [PEAR](pear/) — ultrafast, memory-efficient paired-end read merger.

### Genome assembly and scaffolding

- [SPAdes](spades/) — genome assembler for isolate and single-cell datasets.
- [Hifiasm](hifiasm/) — haplotype-resolved de novo assembler for PacBio HiFi reads.
- [3D-DNA](3d-dna/) — Hi-C-based scaffolding and chromosome-length assembly.
- [AllHiC](allhic/) — Hi-C scaffolding of contigs.
- [Redundans](redundans/) — scaffolding and reduction of heterozygous genome assemblies.
- [SSPACE-LongRead](sspace-longread/) — long-read scaffolder for pre-assembled contigs.
- [LR_Gapcloser](lr_gapcloser/) — close gaps in scaffold assemblies using error-corrected long reads.
- [MitoHiFi](mitohifi/) — assemble mitochondrial genomes from PacBio HiFi reads.
- [gfatools](gfatools/) — manipulate GFA and rGFA assembly and pangenome graphs.

### Assembly quality and polishing

- [QUAST](quast/) — evaluate genome assemblies by computing quality metrics.
- [Pilon](pilon/) — automated genome assembly improvement and variant detection.

### Read mapping and alignment

- [BWA](bwa/) — Burrows-Wheeler Aligner for short reads.
- [BWA-MEM2](bwa-mem2/) — next-generation, faster BWA-MEM.
- [Bowtie 2](bowtie2/) — ultrafast and memory-efficient read aligner.
- [Minimap2](minimap2/) — versatile aligner for genomic and spliced nucleotide sequences.

### Sequence search and protein analysis

- [BLAST+](blast2/) — NCBI BLAST+ for searching nucleotide and protein databases.
- [DIAMOND](diamond-aligner/) — accelerated BLAST-compatible local sequence aligner.
- [HMMER](hmmer/) — profile hidden Markov models for protein sequence analysis.
- [InterProScan](interpro/) — scan proteins against InterPro member databases for domains and function.

### Genome annotation

- [Bakta](bakta/) — rapid, standardized annotation of bacterial genomes, MAGs and plasmids.
- [Prokka](prokka/) — rapid prokaryotic genome annotation.
- [funannotate](funannotate/) — eukaryotic genome prediction, annotation and comparison pipeline.
- [antiSMASH](antismash/) — detection and analysis of secondary metabolite biosynthetic gene clusters.
- [KofamScan](kofamscan/) — KEGG Orthology-based gene function annotation using HMM profiles.
- [EvidentialGene](evidential-gene/) — evidence-directed gene construction for eukaryotic genomes.
- [RepeatMasker](repeatmasker/) — screen DNA sequences for interspersed repeats and low-complexity DNA.

### Variant calling and analysis

- [GATK](gatk/) — variant discovery and genotyping in high-throughput sequencing data.
- [bcftools](bcftools/) — variant calling and VCF/BCF file manipulation.
- [NanoCaller](nanocaller/) — call SNPs and indels from long-read sequencing data.
- [CADD](cadd-scripts-with-envs/) — score the deleteriousness of human SNVs and indels.
- [METAL](metal/) — meta-analysis of large-scale genome-wide association studies.

### Comparative genomics and phylogenetics

- [OrthoFinder](orthofinder/) — infer orthogroups, orthologues, gene trees and rooted species trees.
- [Clustal Omega](clustalo/) — accurate multiple sequence alignment of protein sequences.
- [MUSCLE](muscle/) — multiple alignment of protein sequences.
- [PHYLIP](phylip/) — package of programs for inferring phylogenies.
- [CVTree](cvtree/) — build phylogenetic trees from genome or protein composition vectors.
- [RSAT](rsat/) — analyse cis-elements: motif discovery, transcription factor binding and regulatory variation.

### Metagenomics and microbial genomics

- [anvi'o](anvio/) — analysis and visualization platform for metagenomics, pangenomics and phylogenomics.
- [CheckM2](checkm2/) — rapid assessment of genome bin quality using machine learning.

### Transcriptomics and single-cell

- [scRNA-seq R workflow](scrnaseq_r_workflow/) — R environment for single-cell RNA-seq QC, integration, clustering and differential expression.
- [BLAZE](blaze/) — barcode identification from long reads for single-cell gene expression analysis.

### Proteomics and mass spectrometry

- [OpenMS](openms/) — C++ libraries and tools for MS/MS data analysis.
- [DIA-NN](diann/) — data-independent acquisition (DIA) proteomics data processing.

### Imaging and microscopy

- [Cellpose](cellpose/) — generalist algorithm for cell and nucleus segmentation.
- [DIPY](dipy/) — analysis of diffusion MRI data.

### Literature and text mining

- [PaperJev](paperjev/) — retrieve PubMed papers, summarize PDF themes with a local LLM and filter by relevance.

### Genome browsers and visualization

- [JBrowse](jbrowse/) — JBrowse 2 command-line interface for setting up genome browsers.
- [JBrowse 2](jbrowse2/) — JBrowse 2 command-line interface, current release.

### Genomic utilities

- [samtools](samtools/) — process SAM, BAM and CRAM alignment files.
- [bedtools](bedtools/) — suite of utilities for comparing and manipulating genomic features.
- [bedGraphToBigWig](bedGraphToBigWig/) — convert bedGraph tracks to bigWig files.
- [tabix](tabix/) — generic indexer for TAB-delimited genome position files.
- [Jellyfish](jellyfish/) — fast, memory-efficient k-mer counting in DNA.
- [Primer3](primer3/) — design flanking oligonucleotides for DNA amplification.

### Base images, libraries and runtimes

- [biocontainers](biocontainers/) — base image for BioDocker/BioContainers-derived images.
- [Python](Python/) — free-threaded Python builds without the GIL.
- [Biopython](biopython/) — Python library for bioinformatics.
- [Dask](dask/) — flexible library for parallel computing in Python.

### Other

- [takollama](takollama/) — Python AI application, packaged with `uv`.

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
