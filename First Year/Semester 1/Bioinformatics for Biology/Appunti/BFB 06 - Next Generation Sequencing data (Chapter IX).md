---
course: "[[Bioinformatics for Biology]]"
module: "[[Bioinformatics for Biology]]"
source: "MCB/BFB/Bioinformatics_for_Biology.docx"
order: 6
tags: [note, bfb]
---

> [[BFB 05 - Basic Local Alignment Search Tool – BLAST (Chapter IV)|← Basic Local Alignment Search Tool – BLAST (Chapter IV)]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]]

# Next Generation Sequencing data (Chapter IX)

## 6.1 From cells to reads

The logic of an NGS experiment, taking a differential expression design as the example: biological samples (e.g. 3 wild-type replicates vs 3 mutant/KO samples) → extraction of **all mRNAs**, either with poly-T capturing anchors or by ribosomal depletion (e.g. RiboZero) → reverse transcription into cDNA → fragmentation → sequencing of the fragments.

The quantitative principle of the whole technique: **the number of fragments is proportional to gene expression**. The sequencer (e.g. an Illumina NextSeq 500) returns a set of short sequences — the **reads** — whose abundance is correlated with the number of fragments and therefore with transcript expression.

What to do with those sequences: align them onto a reference genome. The result holds two pieces of information — the **read sequences**, and **where each one aligns on the genome** — and is stored in a **BAM** file, accompanied by a **BAI** index file that speeds up access to it.

<figure>
![[BFB-image7.png|556]]
<figcaption aria-hidden="true"><p>Aligning reads on the reference genome: short reads from the sequencer are placed at the genomic positions they match.</p></figcaption>
</figure>

## 6.2 Visualizing a BAM: IGV

Tools for visualizing BAM files: `samtools tview` (command line, fast, weak), Tablet (the first good GUI), SeqMonk (for ChIP-Seq), and the **Integrative Genomics Viewer (IGV)**, which is what everybody uses.

Two versions: the online one at `https://igv.org/app/`, used in the lab, and the local one at `https://software.broadinstitute.org/software/igv/download`, which is more powerful (it can show more reads at once) and is the one to use outside the lab.

The lab dataset: RNA-Seq of mouse cells, mutant (MUT1) vs wild type (WT1), restricted to chromosome 19 to keep files small, downloadable from `https://github.com/federicogiorgi/lessons/releases/tag/ngs_mouse`.

Procedure and pitfalls:

- **Set the correct genome first.** The dataset is aligned on mouse **mm10**, which is the same thing as **GRCm38** (mm10 is the UCSC nomenclature, GRCm38 the NCBI one). For human the current equivalents are **hg38** = **GRCh38**.
- Load the BAM *and* its BAI from Tracks. The BAM is sorted by coordinate for faster access.
- Zoom in: the chromosome is too long to show features. Drag a rectangle on the coordinate bar, click `+`, search a gene (e.g. `Ccs`), or type a coordinate (e.g. `chr19:25,421,476-25,427,225`).

<figure>
![[BFB-image8.png|559]]
<figcaption aria-hidden="true"><p>An RNA-Seq BAM loaded in IGV: genomic coordinates on top, the coverage and read tracks in the middle, gene tracks at the bottom. Rectangles are alignments, lines are alignment skips (e.g. over introns).</p></figcaption>
</figure>

What an RNA-Seq alignment shows in IGV — “all genomics in a nutshell”:

- Gene expression levels, and differential expression between samples.
- Variants from the reference genome (single nucleotides or short indels). Distinguishing them: isolated “mutations” are sequencing **errors**, whereas real mutations are frequent and recurrent across reads — remembering that there are two alleles per gene, so a heterozygous variant shows in roughly half the reads.
- Splicing and alternative splicing.
- Transcript orientation, by coloring reads by “read strand”.

Lab exercises: find genes with novel alternative splicing (e.g. an exon skip) supported by at least one read (suggestion: `Kank1`); load MUT1 beside WT1 and look for differentially expressed genes (`Slc1a1`, `Slc25a45`, `Cyp2c55`, `Pnlip` — the coverage range must be scaled to compare them); find two genes with inverted orientation that may share the same promoter (e.g. `Rnls`).

## 6.3 Sequencing technologies

<figure>
![[BFB-image9.png|559]]
<figcaption aria-hidden="true"><p>The technology landscape: read length on the x axis, quality on the y axis, throughput growing to the right. Illumina (HiSeq, NextSeq, MiSeq) gives short, high-quality reads; Sanger gives long, very accurate reads at low throughput; Oxford Nanopore and SMRT PacBio give very long reads at lower per-base quality. They all produce the same file formats.</p></figcaption>
</figure>

### 6.3.1 Illumina sample preparation

1.  **Purify mRNA** — starting from 0.1–4 µg of total RNA, polyadenylated RNA is captured with poly-T oligo-attached magnetic beads (for Affymetrix microarrays, 2–3 µg are needed instead).
2.  **Fragment mRNA** — 94 °C for 3–8 minutes; this step also primes the fragments for cDNA synthesis.
3.  **First strand cDNA synthesis** — reverse transcriptase plus random hexamer primers converts the cleaved mRNA into single-stranded cDNA.
4.  **Second strand cDNA synthesis** — the RNA template is removed (e.g. RNase H) and a second cDNA strand is polymerized, using RNA fragments as primers. The resulting ds-cDNA is very stable at 4 °C.
5.  **End repair** — overhangs are turned into blunt ends: a 3’→5’ exonuclease removes 3’ overhangs and a standard DNA polymerase fills in the 5’ overhangs.
6.  **Ligate adapters** — each library receives specific nucleotide sequences used as **indexes** when the sequencing lane is multiplexed.
7.  **Selective enrichment** — only fragments carrying indexes on both sides are amplified by PCR.
8.  **Select fragment size** — fragment size is standardized on an agarose gel.

### 6.3.2 Sequencing by synthesis

Fragments bind randomly to the inside surface of a **flow cell**; solid-phase amplification with unlabeled nucleotides and enzyme generates several million dense clusters of double-stranded DNA per channel. Sequencing then adds nucleotides carrying (1) fluorophores and (2) **reversible terminators**, one base at a time: the succession of colors in each spot gives the sequence.

<figure>
![[BFB-image10.png|559]]
<figcaption aria-hidden="true"><p>Sequencing by synthesis: each cycle adds one fluorescently labeled, reversibly terminated nucleotide, and the color read out at each spot builds the sequence base by base.</p></figcaption>
</figure>

<figure>
![[BFB-image11.png|474]]
<figcaption aria-hidden="true"><p>Paired-end sequencing: the same fragment is sequenced from the other side too, with a second primer and after the first reaction, so that two reads (30–350 nt each) cover the two borders of a fragment of ≥ 150 nt. The two sequences are called a pair.</p></figcaption>
</figure>

The cycles are repeated to read the whole fragment. **Multiplexing deconvolution**: based on the index, the reads of a multiplexed lane are assigned to their sample of origin and written to their own FASTQ file.

## 6.4 The four main NGS experiment types

They are recognized in IGV by the shape of the coverage profile, which is the practical point of the whole section.

| Code | Experiment | Starting material | Typical IGV profile |
|:---|:---|:---|:---|
| **WGS** | Whole Genome Sequencing | DNA, fragmented and sequenced — the easiest | Uniform coverage, no splicing |
| **WXS** | Whole eXome Sequencing | DNA enriched for exons (PCR amplification of all exons, or probe-specific capture, array-based or in-solution) | Non-uniform coverage, no splicing, reads mostly on exons, **gentle** decline at intron/exon junctions |
| **RNA-Seq** | RNA Sequencing | RNA (mRNA in 99.9% of cases), converted to cDNA, fragmented, sequenced | Non-uniform coverage, **presence of splicing**, **sharp** drop of coverage at exon/intron junctions |
| **ChIP-Seq** | Chromatin ImmunoPrecipitation Sequencing | DNA bound to a specific protein | Non-uniform coverage, no splicing, reads piled on some promoter regions; peak width indicates how wide the protein–DNA binding region is |

<figure>
![[BFB-image12.png|537]]
<figcaption aria-hidden="true"><p>WGS: uniform coverage along the genome, no splicing.</p></figcaption>
</figure>

<figure>
![[BFB-image13.png|537]]
<figcaption aria-hidden="true"><p>WXS: coverage concentrated on exons with a gentle decline at the junctions, because the enrichment is imperfect.</p></figcaption>
</figure>

<figure>
![[BFB-image14.png|537]]
<figcaption aria-hidden="true"><p>RNA-Seq: coverage follows the exons with sharp junction drops, and reads skip across introns — the signature of splicing.</p></figcaption>
</figure>

<figure>
![[BFB-image15.png|537]]
<figcaption aria-hidden="true"><p>ChIP-Seq: coverage forms peaks at the regions bound by the immunoprecipitated protein, typically promoters for a transcription factor.</p></figcaption>
</figure>

**Uses of WXS**: detecting mutations in the coding sequence (single nucleotides, short indels), sometimes restricted to the exons of specific genes (e.g. cancer genes).

**Uses of RNA-Seq**: measuring gene expression and differential expression; detecting mutations in expressed sequences; identifying new isoforms. Compared with WXS/WGS it additionally reveals **RNA editing** (mutations generated post-transcription) and **allele-specific expression** (whether one allele is more expressed than the other).

**How ChIP-Seq works**, step by step: genomic DNA in living cells is complexed with proteins (chromatin) — some structural and bound everywhere (histones), some functional and bound at specific locations (transcription factors). (1) DNA is crosslinked to its proteins with covalent bonds, e.g. by formaldehyde. (2) Naked DNA, not bound to proteins, is degraded. (3) A specific antibody pulls down one protein only. (4) All proteins are degraded, leaving the DNA. (5) The remaining DNA — the DNA bound by the chosen protein — is sequenced. This is how the target genes of a transcription factor, its **regulon**, are identified.

Other applications listed: qualitative RNA-Seq (catalog of transcripts, alternative splicing), reverse engineering of gene networks, metagenomics and metatranscriptomics.

**Exercise — three mystery datasets** (`stark`, `lannister`, `baratheon`, from `https://github.com/federicogiorgi/lessons/releases/`): load each BAM in IGV and decide which class of experiment it came from, coloring reads by “read strand”. Stark: leukemia cells, human hg19, chromosome 22 only, from ArrayExpress E-MTAB-4313. Lannister: human hg38, chromosome 22, from GEO GSE-12782 (hint: genes `C1QTNF6`, `APOL6`, `PLA2G3`, and the situation at `chr22:36,065,000`). Baratheon: neuroblastoma, human hg38, reads around gene `E2F3` on chr6.

## 6.5 File formats

| Format | Content |
|:---|:---|
| **FASTA** | Entire genome (or protein/transcript) sequence |
| **FASTQ** | Many sequenced reads, each nucleotide with a quality score |
| **SAM / BAM** | Reads aligned on a genome — SAM is the text version, BAM the compressed binary one |
| **BED** | Genomic regions |
| **GFF3 / GTF** | Hierarchical gene structure |
| **WIG / BIGWIG** | Coverage, i.e. a score along the genome |

SAM, BAM, BED, GFF3, GTF, WIG and BIGWIG are all **tab-separated**. Practical tip: open large text files with an editor that can handle them — Notepad++ or Sublime Text on Windows, Sublime Text on macOS — because they open larger files than Notepad/TextEdit, show line numbers, toggle word wrapping and highlight file types automatically.

### 6.5.1 FASTA and FASTQ

**FASTA** can be a huge file (a human genome ≈ 3 GB) and is usually compressed (`.gz`, `.zip`). It can contain multiple headers, each starting with `>`. It holds **less** information than FASTQ — no per-nucleotide quality — so it is used for sequences that are trusted fully: validated genomes, proteins, transcripts. IGV takes FASTA as a reference genome, and both the local and web versions come with preloaded genomes in FASTA.

**FASTQ** cannot be loaded in IGV at all, because it lacks the information on where the reads align.

<figure>
![[BFB-image16.png|446]]
<figcaption aria-hidden="true"><p>The FASTQ format: four lines per read — identifier, sequence, separator, and the per-nucleotide quality string.</p></figcaption>
</figure>

<figure>
![[BFB-image17.png|559]]
<figcaption aria-hidden="true"><p>Phred+33 quality encoding: the ASCII characters <code>!</code> through <code>J</code> encode quality scores 0 to 41. The score converts to an error probability through Q = −10 log₁₀(P), i.e. P = 10^(−Q/10).</p></figcaption>
</figure>

### 6.5.2 Alignment: from FASTQ to SAM/BAM

Input FASTQ, output SAM. Aligners: **BWA**, **Bowtie**, **Bowtie2** for DNA; **Tophat**, **STAR** for RNA; **Hisat2** for both.

SAM and BAM hold the same data in two formats — text and large vs binary and smaller. A SAM/BAM can contain only the aligned reads (making it smaller than the FASTQ) or all the reads, in which case the original FASTQ files can be deleted. Specification: `https://samtools.github.io/hts-specs/SAMv1.pdf`.

**The FLAG column.** The number is a univocal sum of individual flags, in powers of 2:

| Decimal | Description                                                   |
|:--------|:--------------------------------------------------------------|
| 1       | Template having multiple segments in sequencing (read paired) |
| 2       | Each segment properly aligned according to the aligner        |
| 4       | Segment unmapped                                              |
| 8       | Next segment in the template unmapped                         |
| 16      | SEQ being reverse complemented (read in reverse strand)       |
| 32      | SEQ of the next segment being reversed                        |
| 64      | The first segment in the template                             |
| 128     | The last segment in the template (second in pair)             |
| 256     | Secondary alignment                                           |
| 512     | Not passing quality controls                                  |
| 1024    | PCR or optical duplicate                                      |
| 2048    | Supplementary alignment                                       |

Worked example: read paired (1) + both reads aligned (2) + reverse strand (16) + second in pair (128) = **147**. Useful trick: **if the FLAG is an odd number, the dataset has paired reads**, because only flag 1 is odd. Decomposition helper: `https://broadinstitute.github.io/picard/explain-flags.html`. On Linux, `samtools` extracts the reads matching a flag or combination of flags.

<figure>
![[BFB-image18.png|559]]
<figcaption aria-hidden="true"><p>The SAM FLAG column and the full table of flag values.</p></figcaption>
</figure>

**The CIGAR column** is a string describing how the read aligns with the reference. It consists of one or more components, each an operator plus the number of bases it applies to.

| Operator | Meaning |
|:---|:---|
| `M` | Match — either an alignment match or a mismatch; the nucleotide is present in the reference |
| `I` | Insertion — the nucleotide is present in the read but not in the reference |
| `D` | Deletion — the nucleotide is present in the reference but not in the read |
| `N` | Skipped region — a region of nucleotides is not present in the read (splicing) |
| `S` | Soft clipping — the clipped nucleotides are present in the read |
| `H` | Hard clipping — the clipped nucleotides were removed from the SAM/BAM file (used to save bytes, now factually deprecated) |
| `P` | Padding — fixes coordinates when multiple reads with different insertion lengths overlap (very rare) |

<figure>
![[BFB-image19.png|559]]
<figcaption aria-hidden="true"><p>The CIGAR column in a SAM file and the meaning of its operators.</p></figcaption>
</figure>

**Read length from the CIGAR string.** The rule to memorize: **M, I, S and H count towards read length; D, N and P do not.**

<figure>
![[BFB-image20.png|537]]
<figcaption aria-hidden="true"><p>Inferring read length from the CIGAR string: only the operators describing bases present in the read are summed.</p></figcaption>
</figure>

| CIGAR                   | Read length | Splicing? |
|:------------------------|:------------|:----------|
| `8M1000N3M`             | 11          | **Yes**   |
| `3S10M1D13M2S`          | 28          | No        |
| `3H15M3I3M1H`           | 25          | No        |
| `100M3D10M3I100M`       | 213         | No        |
| `50M3P10M5S`            | 65          | No        |
| `3S10M2500N10M1D10M10S` | 43          | **Yes**   |

Splicing is signalled by `N`, the skipped region: a long `N` stretch means the read crosses an intron.

### 6.5.3 BED, WIG/BIGWIG, GFF3/GTF

**BED** stores genomic regions. The first three fields are required — `chrom` (chromosome or scaffold name), `chromStart`, `chromEnd` — followed by 9 optional fields, among them `name` (the label displayed to the left of the line in IGV) and `score` (0–1000, determining the level of grey used to display the feature). BED is used for gene locations, transcription factor binding sites, promoters, enhancers, and regions of open/closed chromatin.

<figure>
![[BFB-image21.png|559]]
<figcaption aria-hidden="true"><p>The BED format and its fields.</p></figcaption>
</figure>

**WIG** files give a score at a given genomic location; **BIGWIG** is the compressed version, exactly as BAM is to SAM. Writing with a `span` compresses runs of identical values:

    WIG without span:              WIG with span (same information):
    variableStep chrom=chr19       variableStep chrom=chr19 span=5
    300701  12.5                   300701  12.5
    300702  12.5                   300706  15
    300703  12.5
    300704  12.5
    300705  12.5
    300706  15

WIG is used to visualize quantities across the genome: gene expression (RNA-Seq), TF binding strength (ChIP-Seq), evolutionary conservation, GC content, mutational distribution (TCGA publishes many such files for cancer samples).

|                                        |
|:--------------------------------------:|
| The WIG format, with and without span. |

The WIG format, with and without span.

**GFF3 and GTF** are the main choice for gene annotation: like BED they give locations, but they also encode **hierarchy** (gene → transcript → exons). Fields: `seqid` (chromosome/scaffold/reference name), `source` (who annotated the feature), `type` (gene, transcript, exon…), `start`, `end`, `score` (a float, e.g. peak intensity for ChIP-Seq), `strand` (`+` forward, `−` reverse), `phase` (0, 1 or 2 for coding sequences: 0 means in frame, 1 and 2 that the codon is shifted by 1 or 2 bases), and `attributes` (e.g. `gene_type`, `gene_name`).

<figure>
![[BFB-image22.png|559]]
<figcaption aria-hidden="true"><p>The GFF3/GTF format and its nine fields.</p></figcaption>
</figure>

### 6.5.4 Annotation repositories and loading a GTF in IGV

**ENSEMBL** (`http://www.ensembl.org/info/data/ftp/index.html`) is the repository for genomes and standard gene annotations. **GENCODE** (`https://www.gencodegenes.org/`) provides a highly curated annotation, including non-coding genes and rare isoforms, and therefore shows many more tracks than the default IGV/RefSeq annotation. Note the two independent version numbers: for mouse, `M33` is the *annotation* version while `mm39`/`GRCm39` is the *sequence* version.

Exercise: download `Mus_musculus.GRCm39.gtf.gz`, count the lines, then count the gene entries. The trick for counting genes is to count the lines whose `type` field is exactly `gene`, searching for `\tgene\t` — in Notepad++ with “extended” search mode and the Count button, in Sublime Text with regular expressions and Find All.

A GTF cannot be loaded into IGV as it is downloaded. It must be (1) **sorted** and (2) **indexed**, both done from the local IGV under Tools → Run igvtools (command `sort`, then accept the indexing prompt); the web version is not powerful enough for this.

## 6.6 How the BAM files were generated

The whole upstream pipeline runs on Linux, on a high-performance machine (64 GB of RAM):

1.  Start from the **FASTQ** produced by the sequencer.
2.  **Filtering** (removing low-quality reads) and **trimming** (removing low-quality portions of reads) — the program `fastp` does both.
3.  Prepare the genome by building an alignable form of the FASTA with `hisat2-build`.
4.  Align the cleaned FASTQ on the built genome with `hisat2` → SAM/BAM.
5.  `samtools sort` → sorted BAM; `samtools index` → BAI; `samtools view` to keep only the chr19 alignments, so the file stays downloadable.
6.  Optionally, quantify gene expression with `featureCounts` using a GTF/GFF3 annotation.

<figure>
![[BFB-image23.png|559]]
<figcaption aria-hidden="true"><p>The full pipeline from experiment to sorted BAM, with the program used at each step.</p></figcaption>
</figure>

## 6.7 From BAM to gene expression

The predominant reads in an RNA-Seq BAM derive from messenger RNAs. Their peculiarities: they are short (36–250 bases), have high error rates (~1%), come in hundreds of millions, and many span exon–exon junctions. Consequently the alignment is **not uniform** — the number of reads is proportional to transcript expression — and it is not uniform *within* a transcript either, because exonucleases cut from the 5’ and 3’ ends. Alternative isoforms and RNA editing add further variability.

Counting is done by `htseq-count` (or the more recent `featureCounts`), which takes the BAM alignment plus a GFF3/GTF annotation and returns counts — per gene, per exon, per transcript, or per any feature defined in the annotation.

<figure>
![[BFB-image24.png|559]]
<figcaption aria-hidden="true"><p>A count matrix: rows are genes, columns are samples, and each cell is the number of reads for that gene in that sample (example from the GTEx blood samples).</p></figcaption>
</figure>

## 6.8 Public repositories of NGS data

| Repository | Who | Notes |
|:---|:---|:---|
| **GEO** (Gene Expression Omnibus), `https://www.ncbi.nlm.nih.gov/geo/` | NCBI, Bethesda, USA | Largest repository of high-throughput data in the world; both NGS and microarrays |
| **ArrayExpress / ENA / BioStudies** | EBI, Hinxton, UK | More recent than GEO, with better search tools; partially redundant with GEO |
| **SRA** (Sequence Read Archive) | NCBI | Subset of GEO specifically for NGS (no microarrays); holds the raw data, essentially FASTQ files compressed and optionally encrypted in the SRA format |

Common pipeline when starting from a public dataset: find a suitable dataset (ArrayExpress or GEO) → find the link to the sample IDs (SRA or FASTQ) → download the SRA or FASTQ files → (optionally) convert SRA to FASTQ → quality control of the FASTQ → optional trimming/adapter removal → alignment on the reference genome (BAM) → visualization → downstream analysis. The first four steps are what NCBI’s **SRA Toolkit** is for.

---
> [[BFB 05 - Basic Local Alignment Search Tool – BLAST (Chapter IV)|← Basic Local Alignment Search Tool – BLAST (Chapter IV)]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]]
