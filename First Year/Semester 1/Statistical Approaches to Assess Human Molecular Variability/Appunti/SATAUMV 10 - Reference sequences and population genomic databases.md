---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 10
tags: [note, sataumv]
---

> [[SATAUMV 09 - Technologies for genomic data generation and data formats|← Technologies for genomic data generation and data formats]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 11 - Post-processing quality controls, dataset assembly, imputation and phasing|Post-processing quality controls, dataset assembly, imputation and phasing →]]

# Reference sequences and population genomic databases

## 10.1 Two fundamental steps beyond technology

In addition to the technological advances described in the previous chapter, **two other fundamental steps** signaled massive advances in the study of human genomic variation: the public availability of the **human reference sequence** and the creation of **large-scale population genomic databases**.

- **Human reference sequence:** the coordinate system that serves as the fundamental standard for identifying differences and describing genetic variation.
- **Population genomic databases:** collections of genomes that capture diversity across different human populations and give a picture of the distribution of genetic variation.

If the reference genome provides the **"map"**, population genomic databases reveal the **"variation" across the map**.

- Although human genomes are **99.9%** similar, they still contain **millions of genetic variants** (e.g. SNPs) between individuals and populations.
- Exploring human genetic diversity is of undeniable importance and is the basic foundation of **human population genetic studies**.
- Knowledge of the **genetic structure and variability** within and among populations is also a framework for **other applications**: controlling biases and avoiding spurious signals due to **population stratification in GWAS**, calculating **polygenic risk scores (PRS)** for complex traits and diseases, and building **reference panels for imputation and phasing**.

## 10.2 The Human Genome Project and the first reference sequence

The human reference genome provides the **coordinate system** and the **fundamental standard** for all genomic analyses: every variant is described as a difference with respect to it. However, the original reference sequence announced in **2001** (the Human Genome Project, HGP, whose results appeared on the covers of *Nature* and *Science*) is a **haploid mosaic assembly**. It was built from the DNA of **over 20 volunteers**, with a **single individual contributing about 70%** of the sequence; the remaining stretches come from other donors of African, American, East Asian, European and South Asian ancestry, with European ancestry the most represented.

## 10.3 Evolution of the reference assembly

The reference is periodically updated by the **Genome Reference Consortium (GRC)**. Recent assemblies and their UCSC equivalents are:

| **Release name** | **Date of release**    | **Equivalent UCSC version** |
|:-----------------|:-----------------------|:----------------------------|
| NCBI Build 34    | Jul 2003               | hg16                        |
| NCBI Build 35    | May 2004               | hg17                        |
| NCBI Build 36.1  | Mar 2006               | hg18                        |
| GRCh37           | Feb 2009               | hg19                        |
| GRCh38           | Dec 2013               | hg38                        |
| GRCh39           | Indefinitely postponed | –                           |
| T2T-CHM13        | January 2022           | hs1                         |

The **first version** of the reference genome (hg4) had about **150,000 unresolved gaps**; the number of bases grows with each release as gaps are filled. The current GRCh38 build has only about **350 gaps** across the entire assembly.

**The Telomere-to-Telomere (T2T) Consortium.** Using **third-generation long-read sequencing** technologies, the T2T Consortium presented a complete sequence of **3.055 billion base pairs** (T2T-CHM13). It includes **gapless assemblies for all chromosomes (except the Y chromosome)** and covers the more **structurally complex regions** (centromeres, satellite arrays, segmental duplications) that were previously missing. The sequence derives from the **CHM13 cell line**, so it is a haploid genome without a Y chromosome.

## 10.4 The Human Pangenome Project

A single linear reference, even if complete, cannot represent global variation, and sequences that differ from it are harder to align (**reference bias**). The **Human Pangenome Project** aims at building a **human pangenome reference** that better represents **global genomic variation**, by providing a collection of accurate **telomere-to-telomere assembled genomes**, annotations and alignments from multiple individuals.

- **Goal:** at least **350 high-quality human diploid genomes** from different ethnic and biogeographical ancestry groups.
- **First draft (May 2023):** **47 phased human diploid genomes** from individuals of different ancestral backgrounds.
- **Phased diploid assemblies:** each individual contributes both haplotypes, so the pairs of underlying chromosome sequences are resolved.
- **Not a single consensus sequence but a genome graph model:** the sequences of all individuals are aligned into a graph in which shared segments are common nodes and alternative paths represent variants. The slide shows examples of a **CNV**, an **SNV** and an **inversion**.

![[SATAUMV-image36.png|598]]

## 10.5 Human Genome Diversity Project (HGDP)

- **Purpose:** describing **global human genetic variation**: DNA from worldwide populations, storing renewable biological materials, with data publicly available.
- **Panel:** **1,064 individuals** from **52 representative worldwide populations**, including indigenous populations and groups relevant from an anthropological, cultural, linguistic and historical point of view. The populations are grouped in seven regions: Africans, Europeans, Western Asians, Central and Southern Asians, Eastern Asians, Oceanians and Native Americans.
- **Collection:** reusable **lymphoblastoid cell lines (LCL)** stored at the Center for the Study of Human Polymorphism (CEPH), together with sex, population and geographic origin (**no phenotypic information**).
- **Data:** initial **microarray genotyping** data (SNPs, indels, microsatellites) first published in **2002**; later **whole-genome sequencing** data for **929 samples** of the original HGDP-CEPH collection, at an average coverage of **35X** (Bergström et al. 2020).

## 10.6 HapMap Project

- **Purpose:** develop a **haplotype map** of the human genome to define patterns of common genetic variation and of **linkage structure** (see the notes on LD); guide **genome-wide association studies**; public release of all data (genotypes, arrays).
- **First two stages:** DNA from **270 individuals** from **four large-scale populations** of African, Asian and European ancestry (YRI, CEU, CHB, JPT). **Phase I (2005):** 1.3 million SNPs. **Phase II (2007):** 3.2 million SNPs.
- **HapMap 3 (2010):** follow-up effort with data on about **1,300 samples from 11 populations**, with approximately **1.6 million common SNPs and copy number variants (CNVs)**. The new populations were ASW, CHD, GIH, MXL, LWK, MKK and TSI.

The heat maps on the slide show the LD pattern for YRI, CEU and CHB+JPT: the red triangles mark blocks of strongly correlated SNPs. The block structure differs among populations, in line with their demographic history (see the notes on LD decay).

*Note on the slide:* the HapMap sample size is reported with different values in the slides: 270 individuals (phases I and II), about 1,300 samples (HapMap 3), 708–1,600 in the summary table and 692 people in the *Nature* milestone figure. The differences come from counting different subsets (phases, related individuals and trios). The summary table also lists the technology as "sequencing", but HapMap data are **genotypes obtained with arrays**, as stated in the HapMap slide.

![[SATAUMV-image37.png|610]]

## 10.7 1000 Genomes Project (1KGP)

- **Purpose:** research effort launched in **2008** to provide a large-scale catalog of human genetic variation (at least **one thousand genomes**) based on **whole-genome sequencing**.
- **Final phase 3 release:** data from **2,504 healthy unrelated individuals** from **26 populations** (including those from the HapMap collection) with ancestry in **five continental regions** (Africa, Americas, East Asia, Europe, South Asia). Published as "A global reference for human genetic variation" (*Nature* 526, 68–74, 2015).
- **Variants:** **84.7 million SNVs**, **3.6 million indels** and about **60,000 SVs**.
- **Follow-up high-coverage data (30X)** for **3,202 samples**, including the 2,504 1KGP samples and **602 additional complete trios** (Byrska-Bishop et al. 2022).

*Note on the slide:* the label "variants with frequency ≥ 1%" placed next to the counts should be read with care. The totals of 84.7 million SNVs, 3.6 million indels and about 60,000 SVs, as far as I know, are all the variants discovered in the phase 3 samples, and most of them are rare; only a minority reach a frequency of 1% or more. Admixed populations of African ancestry sampled in the Americas (ASW, ACB) are grouped in the Americas.

## 10.8 Simons Genome Diversity Project (SGDP)

- **Purpose:** provide the largest dataset of **diverse, high-quality** human genome sequences.
- **Different approach:** populations are sampled to represent as much **anthropological, linguistic and cultural diversity** as possible, including many divergent human populations that are **not well represented in other datasets** (compare the SGDP collection sites with the 1KGP sites on the map).
- **Data:** high-quality genomes (mean coverage **43X**) of **300 individuals from 142 diverse populations** (Mallick et al. 2016).

## 10.9 Comparison of the main projects

| **Project** | **Years** | **Samples** | **Technology** | **Individual data** |
|:---|:---|:---|:---|:---|
| HGDP | 1991–2002 | 1,064 | Microarray and sequencing | Public |
| HapMap | 2002–2007 | 708–1,600 | Genotyping arrays (the slide table says sequencing) | Public |
| 1KGP | 2008–2014 | 2,504 | Sequencing | Public |
| ExAC | 2015 | ~60,000 | Sequencing | Private |
| gnomAD | 2017–2021 | ~200,000 | Sequencing | Private |
| HRC | 2016 | ~65,000 | Sequencing | Private |
| Estonian Biobank | 2000–ongoing | ~200,000 | Microarray | Controlled access |
| UK Biobank | 2006–ongoing | ~500,000 | Microarray and sequencing | Controlled access |

Two biobanks are much richer in non-genetic information:

- **Estonian Biobank:** about 202,000 participants, biological samples, multi-omics data, lifestyle questionnaires.
- **UK Biobank:** about 500,000 participants, biological samples, whole-genome and exome data, lifestyle questionnaires, medical records, physical measures and phenotype data.

Despite their differences, **HapMap, HGDP, SGDP and 1KGP** had many similarities, which make them among the most important reference databases still used today:

- they collected individuals following **specific population criteria**;
- they used **immortalized cell lines** to guarantee the possibility of further analyses with newer technologies;
- they made **genetic data publicly available** to the scientific community.

*Note on the slide:* for HRC, "~65,000" most likely counts **haplotypes** (about 32,000 individuals, i.e. about 65,000 haplotypes), and ExAC consists of exome data. SNP chips are usually designed on variants discovered in panels like these, which is one origin of the **ascertainment bias** discussed in the comparison of SNP chips and NGS.

## 10.10 From one genome to a tapestry of ancestry

The *Nature* feature "From one human genome to a complex tapestry of ancestry" summarizes how, in the 20 years since the first drafts of the human genome were made public, the explosion in genome sequencing has revealed how our **evolutionary history and health** can be understood by analysing the diversity of our genomes.

- **Milestones:** HGP (1 reference genome); HapMap (692 people, 11 populations); 1000 Genomes (2,504 people, 26 populations).
- **Ongoing national and large-scale projects:** Estonian Genome Project, deCODE genetics (whole genomes), H3Africa, Genome Denmark, Genomics England, TOPMed, All of Us, Qatar Genome, Australian Genomics and Genome Asia.
- **Geographic coverage:** in the maps of HGDP, HapMap and 1KGP the circles (population samples) show how sampling moved from a few widely spread populations (HGDP) to a handful of large samples from Africa, Europe and East Asia (HapMap) and then to a wider set of populations on five continental regions (1KGP). Regions such as Oceania remain little sampled in these panels.

Key messages: the **reference genome** is the **map** and population databases describe the **variation** on it. The first reference was a **haploid mosaic** of a few donors, then improved by the GRC releases (**hg19**, **hg38**) and completed by **T2T-CHM13**, while the **Human Pangenome** replaces the single sequence with a **graph of many diploid genomes**. **HGDP**, **HapMap**, **1KGP** and **SGDP** are the public panels that describe worldwide variation, based on cell lines and open data, whereas **gnomAD**, **UK Biobank** and similar biobanks are much larger but have **restricted or controlled access**.

---
> [[SATAUMV 09 - Technologies for genomic data generation and data formats|← Technologies for genomic data generation and data formats]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 11 - Post-processing quality controls, dataset assembly, imputation and phasing|Post-processing quality controls, dataset assembly, imputation and phasing →]]
