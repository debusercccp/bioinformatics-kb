---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 9
tags: [note, sataumv]
---

> [[SATAUMV 08 - Shaping diversity – natural selection|← Shaping diversity – natural selection]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 10 - Reference sequences and population genomic databases|Reference sequences and population genomic databases →]]

# Technologies for genomic data generation and data formats

## 9.1 Variant classes and typing methods

The classes of variation described in Section 1.2 cannot all be typed with the same technology: the method depends on the size of the genomic segment involved. **SNPs**, the focus of this chapter, can be typed with three main technologies: **Sanger sequencing**, **SNP chips** (and other typing methods) and **next-generation sequencing (NGS)**.

![[SATAUMV-image21.png|413]]

**Five technological advances** revolutionized the study of human molecular variability:

- Invention of the **polymerase chain reaction (PCR)**.
- Development of **capillary sequencing** of DNA and **Sanger sequencing** technology.
- Determination of the **human genome reference sequence**.
- Cheap and accurate methods for **high-throughput genome-wide typing** (SNP chips).
- Development of **next-generation whole genome sequencing** methods.

## 9.2 Sanger sequencing: first generation

**Chain-termination sequencing:** fluorescently labelled **dideoxynucleotides (ddNTPs)** are incorporated into the growing DNA strand and act as chain terminators. A ddNTP lacks the oxygen (OH group) on the 3′ carbon, so no further nucleotide can be attached and synthesis terminates right after its incorporation. The method has five steps:

- **Primer annealing and chain extension:** a primer anneals to the template and the polymerase extends the new strand.
- **ddNTP binding and chain termination:** whenever a ddNTP is incorporated instead of a normal dNTP, extension stops.
- **Fluorescently labelled DNA sample:** the result is a set of fragments of every length, each ending with a labelled ddNTP (one colour per base: G, A, T, C).
- **Capillary electrophoresis and fluorescence detection:** fragments are separated by size, a laser excites the label and a detector reads the colour.
- **Sequencing analysis and reconstruction:** the sequence of colours (chromatogram peaks, e.g. G A C T A G) is read as the base sequence.

Typical performance: **96- or 384-well plates**, reads of **up to 1 kb** of DNA, **accuracy greater than 99%**.

| **Pros** | **Cons** |
|:---|:---|
| **Accuracy**; short turnaround time | **Cost** for large-scale, genome-wide studies; limited **capacity** and **throughput** |

## 9.3 SNP chips: microarray-based technologies

![[SATAUMV-image22.png|179]]

A **SNP-chip microarray** uses DNA probes fixed on a solid matrix to genotype millions of SNPs/SNVs across the genome simultaneously.

- The array contains **beads** on which **allele-specific oligonucleotide probes** are immobilized (50-nt SNV-specific primers; 3 µm beads sit in wells of a silicon wafer, built by photolithography: photoresist, plasma etching, cleaning).
- **Fragmented DNA** (whole-genome amplified) binds by complementarity to the probes; a **single-base extension reaction** then incorporates **fluorescent-labelled ddNTPs**.
- A **detection system** records the **hybridization signals**; the intensity of the signal conveys the genotype at each analysed locus. In the slide figure, one dominant colour indicates a homozygote for that allele and both colours indicate a heterozygote.

![[SATAUMV-image23.png|624]]

**Genome-wide association studies (GWAS)** use these high-throughput genotyping technologies to examine hundreds of thousands of common SNPs and compare their variants in large numbers of affected cases with those in unaffected controls, to determine which SNPs are associated with disease.

| **Pros** | **Cons** |
|:---|:---|
| **High-throughput, cost-effective:** hundreds of thousands to millions of markers across the genome | **Only known SNVs:** not all variability is captured and no new variants can be discovered |
| **Large-scale population studies:** large numbers of samples can be analysed | **Ascertainment bias** (non-random choice of SNPs): SNPs detected mainly in some populations; SNPs at moderate to high frequencies; tag SNPs with reduced LD |
| **Versatile:** flexibility with custom content | **Only common variants:** rare variants are not detected |

## 9.4 PLINK data format

SNP-chip genotypes are usually stored in **PLINK** format, which exists in a **human-readable (text)** version and in a **binary** version.

![[SATAUMV-image24.png|470]]

The **.ped** file has one row per sample and a variable number of columns. The first six describe the individual: **Family ID**, **Sample ID** (the individual's identifier within the family), **paternal ID** (father, 0 if unknown), **maternal ID** (mother, 0 if unknown), **sex** (1 = male, 2 = female, 0 = unknown) and **phenotype** (−9 = missing). From column 7 onwards, each SNP takes **two columns**, one for each allele of the genotype (e.g. G G, A G). A genome-wide chip therefore gives about 10² rows (one per sample) and 10⁵–10⁶ SNPs, so roughly twice that number of genotype columns.

The **.map** file describes the SNPs, with one row per SNP and exactly four columns: **chromosome**, **SNP ID** (e.g. rs4911642), **genetic map position in cM** and **physical position in bp**. The rows of the .map must be in the same order as the SNPs along the .ped, because the *n*-th SNP of the .ped is described by the *n*-th row of the .map. The two files are therefore complementary: the .ped holds *who* carries *which genotype*, and the .map tells *where* each SNP lies in the genome.

The **binary** format has three files: .bed (the genotypes, encoded in binary), .bim (the .map information plus two extra columns, **Allele 1 = A1 = minor allele** and **Allele 2 = A2 = major allele**) and .fam (the first six columns of the .ped).

Binary files are much more compact and faster to read; conversion in both directions is done with PLINK:

| **Conversion** | **Command** |
|:---|:---|
| Text → binary | `plink --file ``mytextfile`` --make-bed --out ``mybinaryfile` |
| Binary → text | `plink --``bfile`` ``mybinaryfile`` --recode --out ``mytextfile` |

## 9.5 Next-generation sequencing

**Second-generation** technologies introduced **massive parallel sequencing**, with a large increase in **throughput** and sequencing speed. All second-generation platforms share two key features: (1) the **fragmentation** of genomic DNA into relatively short fragments and (2) the **immobilization** of the fragments on a solid surface before PCR amplification and sequencing.

**Third-generation** technologies are based on **single-molecule sequencing** methods, which typically eliminate the need for DNA fragmentation and PCR amplification and provide **long-read sequencing**. With respect to short-read platforms, however, they generally have lower throughput and higher costs.

| **Platform** | **Features** | **Applications** |
|:---|:---|:---|
| **Illumina** (2nd gen.) | High accuracy with short reads; scalable for small and large projects; exceptional for SNP detection and transcriptome profiling | Whole-genome sequencing, RNA-Seq and transcriptomics, population genetics studies |
| Ion Torrent (2nd gen.) | Real-time, fast sequencing; cost-effective for targeted panels; small-scale, lab-friendly workflow | Clinical diagnostics, targeted gene panels, microbial identification |
| Oxford Nanopore (3rd gen.) | Ultra-portable, real-time sequencing; ultra-long reads (megabase level); works in field conditions with minimal setup | Pathogen tracking, environmental DNA analysis, portable sequencing in remote locations |
| PacBio (3rd gen.) | Long-read sequencing with high fidelity (HiFi); ideal for detecting structural variants; excellent for resolving repeat regions and epigenetics | *De novo* genome assembly, epigenomics, structural variant detection |

![[SATAUMV-image25.png|624]]

## 9.6 Illumina's short-read sequencing

- ![[SATAUMV-image26.png|251]]**DNA fragmentation and library preparation:** genomic DNA is fragmented into short pieces of specific size (150–200 bp); the ends are repaired, an A overhang is added and "forward" and "reverse read" **adapters** are ligated at both ends of each fragment. Adapters allow binding to the flow cell and provide the binding sites for the **primers** needed during amplification and sequencing.
- ![[SATAUMV-image27.png|254]]**Bridge amplification and cluster generation:** fragments attached to the flow-cell surface are amplified locally through **bridge amplification**, producing **clusters of identical DNA molecules** with hundreds of copies of each original fragment (about 1000 molecules per cluster, millions of clusters, each ≤ 1 µm). A sequencing primer is then annealed.
- ![[SATAUMV-image28.png|252]]**Sequencing:** in each cluster a DNA polymerase incorporates **fluorescently labelled terminating nucleotides** into the growing strand. The fluorescent signal is recorded by imaging the clusters and its colour identifies which base was added; the terminator is then removed (deblock) and the cycle repeats to extend the strand. The process continues for all the copies of each cluster, so **multiple sequencing reads** are obtained for each single DNA fragment.
- ![[SATAUMV-image29.png|247]]**Alignment and data analysis:** the sequencing reads are **mapped and aligned** to a **reference genome** and **variant calling** is then performed. The slide figure shows reads carrying a *known SNV* and an *unknown SNV* relative to the reference sequence.

The chemistry is therefore related to Sanger sequencing (labelled terminating nucleotides), but it is run in cycles and in millions of clusters in parallel on the same flow cell.

## 9.7 From reads to variants: the NGS workflow

![[SATAUMV-image30.png|126]] ![[SATAUMV-image31.png|473]]

| **Step** | **Output** |
|:---|:---|
| Sequencing: image analysis and base calling; base quality (Phred scores) | **FASTQ** file |
| Read mapping to the reference genome (or *de novo* assembly) | **SAM/BAM** file |
| Variant calling | **VCF** file |
| Quality filtering | Filtered variant set |

**Coverage (read depth)** is the mean number of times a nucleotide is covered by sequencing reads. It is expressed as "X": 30X means that each base is covered on average by 30 reads.

In the slide figure the reads aligned to the reference sequence show a **heterozygous SNV (C/G)**: some reads carry the reference allele (C, REF) and others the alternative allele (G, ALT). Variants supported by a single read at isolated positions are **likely sequencing errors**, and **regions of poor coverage** have too few reads to support a reliable call. Hence the need for sufficient coverage to separate true heterozygotes from errors.

## 9.8 FASTQ files

A FASTQ file contains **four lines per read**:

![[SATAUMV-image32.png|624]]

| **Line** | **Content** |
|:---|:---|
| 1\. Read identifier | Starts with '@' |
| 2\. Nucleotide sequence | The bases of the read (N = base that could not be called) |
| 3\. Separator line | Starts with '+' |
| 4\. Quality scores | One character for each nucleotide of line 2 |

## 9.9 Phred quality score

The **Phred score (Q)** is a metric for the quality of nucleotide identification: it represents the probability (P) of an **incorrect base call**.

*Q = −10 log₁₀ P* and *P = 10<sup>−Q/10</sup>*

| **Phred quality score** | **Probability of incorrect base call** | **Base call accuracy** |
|:---|:---|:---|
| 10 | 1 in 10 | 90% |
| 20 | 1 in 100 | 99% |
| 30 | 1 in 1,000 | 99.9% |
| 40 | 1 in 10,000 | 99.99% |
| 50 | 1 in 100,000 | 99.999% |

**Q30** (1 chance in 1,000 of an error, 99.9% accuracy) is generally considered a good quality threshold in NGS and is typically used in **quality filtering** to remove low-quality items.

**ASCII encoding.** Phred scores are stored in the **last line** of the FASTQ record as a string of **ASCII characters**: each character corresponds to the Phred score of the nucleotide at the same position of the sequence line. To obtain the character, add **33** or **64** to the Phred score (Phred+33 or Phred+64) and take the ASCII character with that code.

| **Phred score** | **Phred+33 (ASCII)** | **Character** | **Phred+64 (ASCII)** | **Character** |
|:---|:---|:---|:---|:---|
| 30 | 30 + 33 = 63 | ? | 30 + 64 = 94 | ^ |
| 40 | 40 + 33 = 73 | I | 40 + 64 = 104 | h |

| **Format** | **Offset** | **Raw reads typically** |
|:---|:---|:---|
| Sanger | Phred+33 | 0–40 |
| Illumina 1.3+ | Phred+64 | 0–40 |
| Illumina 1.5+ | Phred+64 | 3–40 (0 and 1 unused; 2 = Read Segment Quality Control Indicator) |
| Illumina 1.8+ | Phred+33 | 0–41 |

Note: the offset must be known to read a FASTQ correctly, because the same character means different scores in the two schemes (for instance 'I', ASCII 73, is Q40 with Phred+33 but only Q9 with Phred+64). Current Illumina data use Phred+33.

## 9.10 SAM/BAM files

![[SATAUMV-image33.png|624]]

After sequencing, the reads in the FASTQ file are aligned to a reference genome and the alignments are stored in **SAM** or **BAM** files.

- **SAM – sequence alignment map:** text-based, tab-delimited, human-readable file containing the alignment information.
- **BAM – binary alignment map:** compressed binary version of the SAM file, smaller and computationally more efficient, especially for large datasets; machine-readable, not human-readable.

**Header section.** It contains information about the format version, the reference sequence, the read groups and the alignment program. Each line starts with \*\*@\*\*.

| **Line** | **Tags** | **Meaning** |
|:---|:---|:---|
| **@HD** – header line | VN; SO | Format version; sorting order of alignments (e.g. coordinate) |
| **@SQ** – reference sequence dictionary | SN; LN; AS | Reference sequence name (e.g. chr1); length (e.g. 249250261); assembly (e.g. NCBI37) |
| **@RG** – read group | ID; PL | Group ID; sequencing platform (e.g. ILLUMINA). A read group is a set of reads that were all the product of a single sequencing run on one lane |
| **@PG** – program information | ID; PN; VN | Program ID; program name (e.g. bwa); program version |
| **@CO** – comments |  | Free one-line text comments |

**Alignment section.** It contains the actual alignment data, with each line representing a single read and **11 mandatory tab-delimited fields**:

| **Col** | **Field** | **Type** | **Brief description** |
|:---|:---|:---|:---|
| 1 | QNAME | String | Query template name (read name) |
| 2 | FLAG | Int | Bitwise flag |
| 3 | RNAME | String | Reference sequence name |
| 4 | POS | Int | 1-based leftmost mapping position |
| 5 | MAPQ | Int | Mapping quality |
| 6 | CIGAR | String | CIGAR string |
| 7 | RNEXT | String | Reference name of the mate/next read |
| 8 | PNEXT | Int | Position of the mate/next read |
| 9 | TLEN | Int | Observed template length (called ISIZE in older versions and in the slide example) |
| 10 | SEQ | String | Segment sequence |
| 11 | QUAL | String | ASCII of Phred-scaled base quality |

Thus a line carries the read name and position (fields 1, 4), the reference sequence name (3), the sequence string (10) and the base qualities taken from the FASTQ (11), plus additional information such as mapping quality (5) and CIGAR string (6).

**MAPQ (mapping quality)** is equal to −10 log₁₀ Pr{mapping position is wrong}, rounded to the nearest integer: it is a Phred score of the alignment, not of the base calls. A value of 255 indicates that the mapping quality is not available.

**CIGAR** (Compact Idiosyncratic Gapped Alignment Report) is a concise code that describes how a read aligns to the reference genome, as a series of numbers and letters giving the length and type of each stretch of alignment; it saves space while detailing insertions, deletions and matches (set to '\*' if unavailable).

| **Op** | **BAM** | **Description**                   |
|:-------|:--------|:----------------------------------|
| M      | 0       | Alignment match                   |
| I      | 1       | Insertion to the reference        |
| D      | 2       | Deletion from the reference       |
| N      | 3       | Skipped region from the reference |
| S      | 4       | Soft clipping                     |
| H      | 5       | Hard clipping                     |
| P      | 6       | Padding                           |

Worked example from the slide: `read1 99 ref 2 30 3M1D2M1I1M = 14 20 CATCTAG *`. The read aligns at POS = 2 with MAPQ = 30, and the CIGAR **3M1D2M1I1M** reads: 3 aligned bases, 1 base deleted from the reference (present in the reference, absent in the read), 2 aligned bases, 1 base inserted (present in the read, absent in the reference), 1 aligned base. Check: the operations M + I + S must add up to the read length, 3 + 2 + 1 + 1 = 7 = length of CATCTAG. The fields "= 14 20" give the mate information (same reference, mate position, template length).

Second example, from the alignment-section slide: FLAG = 113, POS = 497, MAPQ = 37, CIGAR = 37M. 37M means that all 37 bases of SEQ align to the reference (match or mismatch); MAPQ 37 is a probability of wrong placement of about 2 × 10⁻⁴. FLAG 113 = 1 + 16 + 32 + 64: the read is paired, it maps to the reverse strand, its mate maps to the reverse strand and it is the first read in the pair.

## 9.11 Variant calling and the VCF format

**Variant calling** identifies genetic variants, i.e. the differences in DNA sequence between the reference genome and the analysed samples, based on the aligned reads (SAM/BAM/CRAM files in; VCF, or its binary version BCF, out). For each identified polymorphism a **genotype** is assigned to each individual from the combination of reference and/or alternative alleles observed, according to ploidy (diploid, n = 2: Ref/Ref, Ref/Alt, Alt/Alt).

![[SATAUMV-image34.png|624]]

- **REF:** the nucleotide matches the reference sequence.
- **ALT:** the nucleotide does not match the reference.

Note: REF/ALT are defined only with respect to the reference genome and **do not necessarily correspond to ANC/DER**. The reference base can be the derived allele, and polarizing alleles into ancestral and derived requires additional information (see Section 4.3).

**VCF** (Variant Call Format) files are tab-delimited text files that store the **genotype and variant information for all the analysed samples**. They have two parts: a **header section** with the metadata and the **body**, with actual information on the detected variants.

- **Header:** lines starting with `##`. They include the mandatory format line (`##``fileformat=VCFv4.2`), the `##contig` lines (chromosomes and lengths) and the `##INFO` and `##FORMAT` lines, which describe (ID, Number, Type, Description) the annotations used in the body. The last header line starts with `#CHROM` and gives the names of the columns of the body.
- **Body:** one row per variant, with **9 mandatory columns** followed by one column per sample.

| **Column** | **Content** |
|:---|:---|
| \#CHROM, POS | Chromosome and position of the variant |
| ID | Variant identifier (e.g. rs184) |
| REF, ALT | Reference allele and alternative allele(s) (e.g. A and G; CG and C for a deletion) |
| QUAL | Phred-scaled quality of the variant call |
| FILTER | Result of the quality filters (e.g. PASS) |
| INFO | Site-level annotations, e.g. **AC** = allele count in genotypes for each ALT allele; **DP** = approximate read depth (some reads may have been filtered) |
| FORMAT | List of the fields found in the sample columns (e.g. GT:AD:DP:GQ) |
| Sample columns | One per sample (e.g. NA12878, NA12879), with the values in the order given by FORMAT |

![[SATAUMV-image35.png|624]]

Fields of the sample columns:

- **GT (genotype):** allele values separated by **/** (unphased genotype) or **\|** (phased genotype). Alleles are encoded as 0 for the REF allele, 1 for the first allele listed in ALT, 2 for the second, and so on.
- **DP (read depth):** read depth at this position for this sample.
- **AD (allelic depths):** number of reads supporting the REF and ALT alleles, in the order listed.
- **GQ (genotype quality):** conditional genotype quality, encoded as a Phred quality, −10 log₁₀ P(genotype call is wrong).

Worked examples from the slide, variant chr1:239339 (A → G, AC = 1, DP = 4), with FORMAT GT:AD:DP:GQ. **NA12878 = 0/1:9,6:15:99**: heterozygous A/G (A = REF = 0 in GT with 9 reads, G = ALT = 1 in GT with 6 reads), DP = 15 = 9 + 6, GQ = 99. **NA12879 = 0/0:15,0:15:33**: homozygous reference A/A, 15 reads supporting REF and none ALT, GQ = 33. AC = 1 is consistent with these genotypes: it counts the ALT alleles over all samples (one in NA12878, none in NA12879). At chr1:240898, AC = 3 corresponds to 1/1 (two ALT alleles) plus 0/1 (one).

Note on the slide: it states that a GQ of 99 means a 1 in 100,000 chance of error. By the formula, 1 in 100,000 corresponds to Q = 50, whereas GQ = 99 corresponds to an error probability of about 10<sup>−9.9</sup>. In practice GQ is capped at 99, so a value of 99 simply means maximum confidence.

**Size and orientation of the files.** A whole-genome VCF has ≈ 30 M rows (1 × variant) and 1–10³ columns (1 × sample). The orientation is the opposite of the PLINK .ped file (samples in rows, SNPs in columns) and closer to the .map/.bim (variants in rows).

## 9.12 SNP chips vs. NGS

| **Feature** | **SNP chips** | **NGS** |
|:---|:---|:---|
| Variants captured | Only known, mostly common SNVs; no discovery of new variants | All classes of variants (common, low-frequency, rare) with no pre-selection or prior knowledge: full site frequency spectrum and novel variants |
| Ascertainment bias | Present | Absent: variants are discovered directly from the sampled genomes, so it is equally informative for all human populations, which is particularly important for understudied populations |
| Marker density | Hundreds of thousands to millions of markers | Dense variant data: better LD resolution and haplotype-based analyses |
| Cost | \$ | \$\$\$ (still significantly higher than SNP chips) |
| Data and computation | Few MB | Many GB; high computational power needed |
| Inference in population genetics | Large-scale population studies, GWAS | Improved inference of demographic history and improved detection of natural selection events |

Key messages: **Sanger** sequencing is accurate but has low throughput; **SNP chips** are cheap and high-throughput but limited to **known, common SNPs** and affected by **ascertainment bias**; **NGS** gives an **unbiased and comprehensive** description of variation, at a higher cost and with much greater computational needs. NGS data flow from **FASTQ** (reads and Phred qualities) to **SAM/BAM** (alignments) to **VCF** (variants and genotypes), while SNP-chip data are stored in **PLINK** files.

## Collegamenti
- [[BFB 03 - Access to sequence data and related information (Chapter II)]] — banche dati e formati di sequenza
- [[BFB 04 - Pairwise sequence alignment (Chapter III)]] — allineamento di sequenze / read mapping

---
> [[SATAUMV 08 - Shaping diversity – natural selection|← Shaping diversity – natural selection]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 10 - Reference sequences and population genomic databases|Reference sequences and population genomic databases →]]
