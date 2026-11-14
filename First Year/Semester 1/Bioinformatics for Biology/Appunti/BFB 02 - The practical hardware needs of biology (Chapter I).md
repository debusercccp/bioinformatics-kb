---
course: "[[Bioinformatics for Biology]]"
module: "[[Bioinformatics for Biology]]"
source: "MCB/BFB/Bioinformatics_For_Biology.docx"
order: 2
tags: [note, bfb]
---

> [[BFB 01 - Introduction to bioinformatics|← Introduction to bioinformatics]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]] · [[BFB 03 - Access to sequence data and related information (Chapter II)|Access to sequence data and related information (Chapter II) →]]

# The practical hardware needs of biology (Chapter I)

## 2.1 From the first genome to petabyte databases

The first fully sequenced genome was *Saccharomyces cerevisiae* (1996), 13 Mbp ≈ 13 MB. For comparison, in *Homo sapiens* an average chromosome is ~150 MB and the whole genome ~3 GB. Both still fit on a USB stick.

A modern consortium dataset does not. The Cancer Genome Atlas (TCGA) holds ~20,000 patients with DNA (3 GB each), RNA (10 GB each), methylome (10 GB each), proteomics and more, for a total of ~2.5 petabytes (2,500,000 GB).

| Size      | Abbreviation | \# bytes | Example                              |
|:----------|:-------------|:---------|:-------------------------------------|
| Bytes     | —            | 1        | A single text character (A, C, G, T) |
| Kilobytes | 1 KB         | 10³      | Text file                            |
| Megabytes | 1 MB         | 10⁶      | Word document                        |
| Gigabytes | 1 GB         | 10⁹      | One zipped RNA-Seq sample: 10 GB     |
| Terabytes | 1 TB         | 10¹²     | 1000 Genomes Project: 500 TB         |
| Petabytes | 1 PB         | 10¹⁵     | NGS data (SRA) at NCBI: 60 PB        |
| Exabytes  | 1 EB         | 10¹⁸     | Annual worldwide output: \> 2 EB     |

The Sequence Read Archive (SRA) at NCBI is the database for next generation sequencing data, and its growth is measured in petabytes — equivalently petabases. The inflection point is 2008, when NGS caused the boom in biological data production, coupled with the collapse of the cost of sequencing.

## 2.2 Three hardware aspects

Any analysis is constrained by three distinct resources, and it is important not to confuse them:

- **Disk space**: where raw and processed data are stored.
- **RAM**: active memory, where data are kept while being processed.
- **Processor (CPU)**: the better it is, the faster the data are analysed. Measured in FLOPs (FLoating point Operations Per Second), usually GFLOPs.

Typical requirements for one human RNA + DNA sample via NGS: 10 GB of disk space for raw data, 32 GB of RAM as the minimum for processing and high-level analysis, ~1 hour of processing at 1,000 GFLOPs. Time to integrate with other data: it depends.

Dataset sizes scale badly: a small lab works with ~12 samples, a large consortium (e.g. TCGA) with ~20,000. Worldwide production is estimated at ~200,000 samples per year, which means ~2 PB of disk space, many terabytes of RAM for parallel processing, and ~200,000,000 GFLOPs (200 PFLOPs) of compute. A single laptop (~100 GFLOPs) fully dedicated to this would need 20 million hours, i.e. 2,283 years — and then there is the problem of where to store the results.

## 2.3 Scaling up the hardware

| Class | Order of compute | Typical configuration | What it is good for |
|:---|:---|:---|:---|
| Laptop | ~100 GFLOPs | 16 GB RAM, 512 GB SSD, Intel i7 | Writing papers, analysing preprocessed data, accessing bigger machines |
| Workstation | ~1,000 GFLOPs | 64 GB RAM, 2 + 2 TB NVMe + 8 TB HDD, AMD Ryzen 9 (12 c / 24 t), RTX 3070 Ti | One common large-scale NGS dataset (e.g. 100 human RNA-Seq samples) |
| Lab server | ~40,000 GFLOPs | 512 GB RAM, AMD Epyc 24-core, 4× RTX A5000, NAS with ~100 TB | Heavy lifting (thousands of samples), plus a second server for web serving |
| Supercomputer | ~11,150,000 GFLOPs | MareNostrum4: Linux, 11.15 PFLOPs, 384.75 TB RAM, 3,456 servers | National/European-scale computation |

The structural problem of the field: data grow ~17% per year and compute ~28% per year, but the number of bioinformaticians grows ~1.4% per year. Vacancies are consistently open (over a thousand in the USA, a few dozen in Germany, a handful in Italy).

## 2.4 Two worlds: web-based vs command-line bioinformatics

**Web-based bioinformatics.** Tools, data and resources available on the internet, including the major genome browsers and portals (NCBI, Ensembl, UCSC). Philosophy: accessible (no programming skills needed at the entry point), easy to browse, popular (many users → more funding → better websites), cross-browser.

**Command-line bioinformatics.** CLI = Command-Line Interface; the best operating system for it is Linux. It is required because high-throughput technologies generate tens of gigabytes per experiment, and tools such as Excel are simply not powerful enough to manipulate that.

Should you learn to program? Yes, if you want to do non-mainstream analyses (e.g. process a transcriptomics experiment to remove particular RNA-edited nucleotides, then query an online database for matches). The course covers a bit of Linux (scripting rather than programming proper) and a bit of R; the popular languages in the field are Python and R.

---
> [[BFB 01 - Introduction to bioinformatics|← Introduction to bioinformatics]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]] · [[BFB 03 - Access to sequence data and related information (Chapter II)|Access to sequence data and related information (Chapter II) →]]
