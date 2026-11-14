---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 11
tags: [note, ig]
---

> [[IG 10 - ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing)|← ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing)]] · [[Integrative Genomics|↑ Integrative Genomics]]

# Next-generation sequencing (NGS): the read-out of every -seq method

Hi-C, ChIP-seq, ATAC-seq, bisulfite sequencing and RNA-seq all end with **massively parallel sequencing of short fragments**, mostly on Illumina (sequencing by synthesis).

### Step by step: Illumina sequencing

- **1. Library preparation:** fragment (sonication, enzymes or Tn5; 0.1–1 µg DNA), end repair, A-tailing, ligate adaptors carrying flow-cell binding sites, primer sites and an index (barcode) for multiplexing.
- **2. Size selection and PCR:** ~300 bp fragments, a few PCR cycles.
- **3. Cluster generation:** molecules bind flow-cell oligos (8 lanes); bridge (or exclusion) amplification makes ~1,000 copies each, a clonal cluster bright enough to detect.
- **4. Sequencing by synthesis:** each cycle adds one fluorescent reversible-terminator nucleotide; the camera reads each cluster, then dye and terminator are removed. Read length = number of cycles (50–150 bp).
- **5. Paired-end reading:** both ends of each fragment are read at a known distance → better mapping in repeats, fragment length, structural rearrangements (e.g. inversion breakpoints in NA18507).
- **6. Analysis:** demultiplex by index, align, remove PCR duplicates, count signal.

### Why ~300 bp fragments if 16 bp are enough?

- **The 16 bp calculation:** 4¹⁶ ≈ 4.3 × 10⁹ \> haploid human genome (~3.1 × 10⁹ bp), so a 16-mer is in theory **unique** in a random genome (~17 bp counting both strands: 4¹⁷ ≈ 1.7 × 10¹⁰).
- **Why it fails in practice:** ~half the genome is repeats (Alu, LINEs, satellites, duplications), plus sequencing errors and SNPs. Unique mapping needs ≥ 36–50 bp, ideally 2 × 100–150 bp paired-end.
- **Read length vs fragment length:** ~300 bp is the fragment (insert + adaptors); only 50–150 bases are read from each end.
- **Why the fragment must be that long:** (i) adaptors add ~120 bp; (ii) bridge amplification works best at ~200–600 bp (short fragments and adaptor dimers waste reads, long ones give weak clusters); (iii) paired reads must not overlap or run into the adaptor; (iv) known insert size helps place reads in repeats.
- **Biological link:** ~150 bp = one nucleosome (MNase-seq, ATAC-seq ladder, section 18); 200–500 bp sets ChIP-seq resolution (section 17).

### Key terms

- **Depth (coverage):** ~20–40 M reads for TF ChIP-seq, ~30× for WGBS, billions of read pairs for high-resolution Hi-C.
- **Multiplexing:** indexes let many samples share one run.
- **Duplicates:** PCR copies of the same molecule; removed so they do not inflate the signal.
- **Long-read sequencing:** PacBio and Oxford Nanopore read 10–100+ kb single molecules without amplification; they resolve repeats and detect 5mC directly.

## 20. Cautions and corrections to keep in mind

- **eRNA “necessary”:** in the literature the necessity differs by locus; correlation of eRNA with mRNA is not causal.
- **Size of 2D-eRNAs:** \<150 nt in \[W26\], not \<500.
- **Histone mark ratio:** high H3K4me1/H3K4me3, not high H3K4me3.
- **Number of enhancers:** ~1,000,000 candidates (\[SF19\]) vs \>400,000 (ENCODE, \[W26\]).
- **“Contacts in all TADs”:** TAD boundaries are leaky; CTCF/cohesin removal changes few genes.
- **Marks do not identify enhancers by themselves**: mark-based calls overestimate the real ones (section 2).
- **HO**: the slides call it a “recombinase”/transposase; it is an endonuclease (section 11).
- **Product of the methyltransferase assay:** SAM gives its methyl group and becomes **S-adenosyl-L-homocysteine (SAH)**, not S-adenosyl-L-methionine as written on the slide.
- **Spelling:** the syndrome is **Rubinstein**–Taybi (not “Rubistein”).
- **KO ≠ loss of activity:** for many writers/erasers (HDAC3, DNMT3B, KAT2A, TET1) the null phenotype is much more severe than the catalytic-dead one; a KO phenotype cannot be attributed to the enzymatic activity without a catalytic mutant \[VB25\].
- **MS-PCR on the slides = methylation-sensitive restriction + PCR.** Do not confuse it with MSP (methylation-specific PCR, primers designed on bisulfite-converted DNA).
- **Bisulfite does not distinguish 5mC from 5hmC:** both remain C (oxidative bisulfite or TAB-seq are needed to separate them).
- **CpG island size:** 0.2 to 1–2 kb (the slide has a typo, “0,2 t 1-2 kb”).
- **EZH2 is inactive alone:** in \[R00\] the isolated EZH2 SET fragment does not methylate H3; EZH2 works only inside PRC2 (with EED, SUZ12).

## Papers of the course

The papers in the course folder (**paper/integrative**), in alphabetical order, with the section of these notes where each one is discussed. In the text, the papers that are not the subject of a section of their own are summarised in one or two sentences in a paragraph starting with **Paper —**.

- Côté J, Quinn J, Workman JL, Peterson CL (1994). *Stimulation of GAL4 derivative binding to nucleosomal DNA by the yeast SWI/SNF complex.* Science 265:53–60. → **11. Chromatin and remodelling** (How it was shown biochemically) \[**C94**\]
- Lambert SA, Jolma A, Campitelli LF, Das PK, Yin Y, Albu M, Chen X, Taipale J, Hughes TR, Weirauch MT (2018). *The human transcription factors.* Cell 172:650–665. → **2. Enhancer–promoter crosstalk** (“Sometimes being weak means being strong”) \[**L18**\]
- Schoenfelder S, Fraser P (2019). *Long-range enhancer–promoter contacts in gene expression control.* Nat Rev Genet 20:437–455. → **sections 2–8** (the backbone of the whole first part) \[**SF19**\]
- Tupler R, Perini G, Green MR (2001). *Expressing the human genome.* Nature 409:832–833. → **2. Enhancer–promoter crosstalk** (the pre-initiation complex) \[**T01**\]
- Vanyai HK, Blewitt ME (2025). *Catalytic-independent roles of chromatin modifiers in mammalian development and the implications for treating human disease.* Biochem Soc Trans 53:1507–1516, doi:10.1042/BST20253098. → **16. Catalytic-independent roles of chromatin modifiers** \[**VB25**\]
- Wang Q, ten Dijke P, Fan C (2026). *Deciphering the regulatory landscape of enhancer RNAs in health and disease.* Signal Transduct Target Ther 11:29. → **10. Enhancer RNAs (eRNAs)** \[**W26**\]

Cited in these notes but not in the folder: \[**B93**\] Braunstein, Rose, Holmes, Allis & Broach, *Transcriptional silencing in yeast is associated with reduced nucleosome acetylation*, Genes Dev 7:592–604 (1993) → **11–12**; \[**R00**\] Rea, Eisenhaber, O’Carroll, Strahl, Sun, Schmid, Opravil, Mechtler, Ponting, Allis & Jenuwein, *Regulation of chromatin structure by site-specific histone H3 methyltransferases*, Nature 406:593–599 (2000) → **12** (Experiment \[R00\]); \[**S12**\] Smith et al., *A unique regulatory phase of DNA methylation in the early mammalian embryo*, Nature 484:339–344 (2012) → **14** (Methylation dynamics in the early mouse embryo).

---
> [[IG 10 - ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing)|← ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing)]] · [[Integrative Genomics|↑ Integrative Genomics]]
