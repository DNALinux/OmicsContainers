# scRNA-seq R Workflow

This directory contains the Docker image for an **R-based single-cell RNA-seq workflow** built around [Seurat](https://satijalab.org/seurat/) and focused on a radiation skin analysis: **Control vs Irradiated** scRNA-seq samples.

## What is this image?

The image provides a reproducible R environment for running a scRNA-seq analysis pipeline that goes from raw 10x count matrices to condition-specific downstream analyses. It was originally designed for a radiation-skin study comparing control and irradiated skin cells, but the core steps are reusable for any two-condition scRNA-seq experiment.

Core packages installed:

- **Seurat** — single-cell data analysis and integration
- **Matrix** — sparse-matrix handling for 10x data
- **igraph** — network construction and graph analysis
- **bnlearn** — Bayesian network learning

## Workflow overview

The workflow reproduces the analysis described in the project PDF specification:

1. **Load processed 10x data** — features, barcodes, and MTX matrices
2. **Create Seurat objects** — one per sample/condition
3. **Quality control** — mitochondrial percentage, feature counts
4. **Normalization** — `LogNormalize` with `scale.factor = 10,000`
5. **Variable feature selection** — VST method
6. **RPCA integration** — reciprocal PCA anchors across conditions
7. **Dimensionality reduction & clustering** — PCA, neighbors, t-SNE
8. **Cell-type annotation** — marker module scores
9. **Condition-specific differential expression** — e.g., Irradiated vs Control fibroblasts
10. **Co-expression & optional Bayesian network analysis** — NR4A1-centered exploration

## Available image

Pre-built image is published to Docker Hub:

- **`dnalinux/scrnaseq-r-workflow:1.0.0`**

Docker Hub repository: https://hub.docker.com/repository/docker/dnalinux/scrnaseq-r-workflow/general

## How to use

Pull the image:

```bash
docker pull dnalinux/scrnaseq-r-workflow:1.0.0
```

Run an interactive R session:

```bash
docker run -it -v $(pwd):/data dnalinux/scrnaseq-r-workflow:1.0.0
```

Run a script from your local directory:

```bash
docker run -v $(pwd):/data dnalinux/scrnaseq-r-workflow:1.0.0 \
    Rscript /data/my_workflow.R
```

The container sets `/data` as the working directory, so mounting your project folder there is the expected pattern.

## Example workflow snippet

A minimal template matching the project specification:

```r
library(Seurat)
library(Matrix)

# Load 10x data
mat_con <- Read10X("/data/control_counts/")
mat_ir  <- Read10X("/data/irradiated_counts/")

# Create Seurat objects
con <- CreateSeuratObject(mat_con, project="Control", min.cells=3, min.features=500)
ir  <- CreateSeuratObject(mat_ir,  project="Irradiated", min.cells=3, min.features=500)

# QC
con[["percent.mito"]] <- PercentageFeatureSet(con, pattern="^MT-")
ir[["percent.mito"]] <- PercentageFeatureSet(ir,  pattern="^MT-")
con <- subset(con, subset = nFeature_RNA > 500 & nFeature_RNA < 5000 & percent.mito < 10)
ir  <- subset(ir,  subset = nFeature_RNA > 500 & nFeature_RNA < 5000 & percent.mito < 10)

# Normalize and find variable features
con <- NormalizeData(con) %>% FindVariableFeatures(selection.method="vst", nfeatures=1100)
ir  <- NormalizeData(ir)  %>% FindVariableFeatures(selection.method="vst", nfeatures=1100)

# Integrate with RPCA
features <- SelectIntegrationFeatures(object.list=list(con, ir), nfeatures=2000)
con <- ScaleData(con, features=features) %>% RunPCA(features=features, npcs=50)
ir  <- ScaleData(ir,  features=features) %>% RunPCA(features=features, npcs=50)
anchors <- FindIntegrationAnchors(object.list=list(con, ir), anchor.features=features,
                                   reduction="rpca", dims=1:30, k.anchor=5)
integrated <- IntegrateData(anchorset=anchors, dims=1:30)

# Cluster and annotate
integrated <- ScaleData(integrated) %>% RunPCA(npcs=50) %>% FindNeighbors(dims=1:35)
integrated <- FindClusters(integrated, resolution=0.6) %>% RunTSNE(dims=1:35)
```

## Important notes

- The thresholds in the example (e.g., `nFeature_RNA` 500–5000, `percent.mito` < 10%) are **study-specific choices** from the radiation-skin workflow, not universal defaults.
- Integration with RPCA is an analytical choice, not a mandatory step. The workflow supports a no-integration path when the condition effect itself is the main interest.
- The NR4A1 co-expression and Bayesian-network branches are optional exploratory analyses tied to the original biological question.

## Building from source

To build the image locally:

```bash
cd 1.0.0
docker build -t dnalinux/scrnaseq-r-workflow:1.0.0 .
```

## License

Files in this repository are licensed under Apache 2.0 unless otherwise noted. The R packages bundled in the image carry their own licenses.
