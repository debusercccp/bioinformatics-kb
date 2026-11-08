---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/Functional_Genetics/IntegrativeGen_RS.docx"
order: 9
tags: [note, ig]
---

> [[IG 08 - DNA methylation + Methods – from one locus to the whole epigenome|← DNA methylation + Methods – from one locus to the whole epigenome]] · [[Integrative Genomics|↑ Integrative Genomics]]

# ChIP-seq (chromatin immunoprecipitation followed by sequencing)

ChIP-seq maps **genome-wide where a protein binds DNA or a histone mark sits**: DNA pulled down by an antibody is sequenced (section 19), reads are mapped, and read pile-ups (peaks) are the binding sites.

### Step by step

- **1. Crosslinking:** ~1% formaldehyde, ~10 min, quenched with glycine. Histone marks can use native ChIP (no crosslink, MNase digestion).
- **2. Fragmentation:** sonication (or MNase) to ~200–500 bp; fragment size sets the resolution.
- **3. Immunoprecipitation:** antibody against a TF (CTCF, MYC), Pol II or a mark (H3K27ac, H3K27me3), pulled down on protein A/G beads. An aliquot kept before the IP = input.
- **4. Washes, elution and reverse crosslinking:** heat, RNase + proteinase K, DNA purification.
- **5. Library and sequencing:** end repair, A-tailing, adaptors, a few PCR cycles; ~20–40 M reads for a TF, more for broad marks.
- **6. Mapping and peak calling:** align, remove duplicates, call peaks vs input (MACS2, or PICS, e.g. NRSF). For a TF, + strand reads pile up on one side and − strand reads on the other; the site lies between.

### Controls and quality

- **Input:** corrects for easier shearing of open chromatin, copy number and mapping bias.
- **IgG or knockout/knockdown:** shows background and tests antibody specificity.
- **Validation:** ChIP-qPCR at positive and negative loci; replicates must agree (IDR); FRiP measures enrichment.

### What the peaks look like

- **Sharp peaks:** TFs, CTCF, H3K4me3 (promoters), H3K27ac (active promoters and enhancers).
- **Broad domains:** H3K36me3 (gene bodies), H3K27me3 and H3K9me3 (silent regions; section 15).
- **Combining tracks:** H3K4me1 + H3K27ac + p300 = active enhancers (section 2); H3K4me3 + H3K27me3 = bivalent promoters (section 13); CTCF + cohesin = loop anchors and TAD boundaries (sections 6–7).

### Limits and newer variants

- **Limits:** only as good as the antibody; ~10⁶–10⁷ cells; resolution ~100–300 bp; population average; binding ≠ function (section 2).
- **ChIP-exo:** exonuclease trims DNA up to the crosslinked protein → near base-pair resolution.
- **CUT&RUN and CUT&Tag:** no crosslinking or sonication; the antibody guides MNase or Tn5 to cut or tag DNA next to the target in situ → far fewer cells, lower background.
- **Related methods:** ChIA-PET and HiChIP add an IP to 3C-type methods (section 5); MeDIP uses an anti-5mC IP (section 15).

## 18. ATAC-seq (assay for transposase-accessible chromatin with sequencing)

ATAC-seq maps **open, nucleosome-free chromatin** (active promoters, enhancers, insulators) **genome-wide**. Instead of an antibody (ChIP-seq) or a nuclease (DNase-seq, MNase-seq), it uses a **transposase** that only inserts into DNA not wrapped around nucleosomes.

### Transposase and mobile elements

- **Transposons:** DNA (class II) transposons move by cut-and-paste via their transposase; retrotransposons (class I: LINEs, SINEs such as Alu, LTR elements) by copy-and-paste via RNA.
- **Tn5:** hyperactive bacterial transposase loaded with sequencing adaptors; in one step it cuts DNA and adds adaptors (tagmentation).
- **Why it reads accessibility:** nucleosomes and bound proteins block Tn5, so insertions mark open chromatin; read count = accessibility.

### Step by step

- **1. Nuclei:** ~50,000 cells (or single cells, scATAC-seq), gentle lysis, no crosslinking.
- **2. Tagmentation:** Tn5, ~30 min at 37 °C.
- **3. Purification and PCR** with indexed primers.
- **4. Sequencing and analysis:** paired-end reads mapped, mitochondrial reads removed, peaks called (MACS2).

### What ATAC-seq shows

- **Fragment sizes:** \< 100 bp = nucleosome-free; ~200, ~400, ~600 bp = one, two, three nucleosomes, a ladder that maps nucleosome positions.
- **Peaks:** promoters (H3K4me3), active and poised enhancers (H3K4me1 ± H3K27ac, section 2), CTCF sites (section 6); comparing cell types shows lineage-specific enhancers.
- **TF footprints:** a bound site is protected from Tn5 → dip in cuts flanked by high cuts; with the motif, suggests which TF is bound.
- **Advantages and limits:** fast, few cells, no antibody; but does not identify the protein, and accessibility ≠ activity.

### How to find where a TF binds

- **Motif:** e.g. the E-box CACGTG for MYC/MAX; short motifs occur by chance millions of times, so most matches are unbound.
- **Methylation:** the central CpG of CACGTG can be methylated, which blocks MYC/MAX (CASP8, section 15).
- **Accessibility:** motifs in nucleosomes or heterochromatin are usually unbound (except pioneer factors); ATAC-seq or DNase-seq shows open motifs.
- **Direct proof:** ChIP-seq (or CUT&RUN) shows actual binding; de novo motif analysis of peak centres finds the motif. Most reliable: motif + unmethylated CpG + open chromatin + ChIP peak.

## 19. Next-generation sequencing (NGS): the read-out of every -seq method

Hi-C, ChIP-seq, ATAC-seq, bisulfite sequencing and RNA-seq all end with **massively parallel sequencing of short fragments**, mostly on Illumina (sequencing by synthesis).

### Step by step: Illumina sequencing

- **1. Library preparation:** fragment (sonication, enzymes or Tn5; 0.1–1 µg DNA), end repair, A-tailing, ligate adaptors carrying flow-cell binding sites, primer sites and an index (barcode) for multiplexing.
- **2. Size selection and PCR:** ~300 bp fragments, a few PCR cycles.
- **3. Cluster generation:** molecules bind flow-cell oligos (8 lanes); bridge (or exclusion) amplification makes ~1,000 copies each, a clonal cluster bright enough to detect.
- **4. Sequencing by synthesis:** each cycle adds one fluorescent reversible-terminator nucleotide; the camera reads each cluster, then dye and terminator are removed. Read length = number of cycles (50–150 bp).
- **5. Paired-end reading:** both ends of each fragment are read at a known distance → better mapping in repeats, fragment length, structural rearrangements (e.g. inversion breakpoints in NA18507).
- **6. Analysis:** demultiplex by index, align, remove PCR duplicates, count signal.

### Why ~300 bp fragments if 16 bp are enough?

- **The 16 bp calculation:** 4¹⁶ ≈ 4.3 × 10⁹ \> haploid human genome (~3.1 × 10⁹ bp), so a 16-mer is in theory unique in a random genome (~17 bp counting both strands: 4¹⁷ ≈ 1.7 × 10¹⁰).
- **Why it fails in practice:** ~half the genome is repeats (Alu, LINEs, satellites, duplications), plus sequencing errors and SNPs. Unique mapping needs ≥ 36–50 bp, ideally 2 × 100–150 bp paired-end.
- **Read length vs fragment length:** ~300 bp is the fragment (insert + adaptors); only 50–150 bases are read from each end.
- **Why the fragment must be that long:** (i) adaptors add ~120 bp; (ii) bridge amplification works best at ~200–600 bp (short fragments and adaptor dimers waste reads, long ones give weak clusters); (iii) paired reads must not overlap or run into the adaptor; (iv) known insert size helps place reads in repeats.
- **Biological link:** ~150 bp = one nucleosome (MNase-seq, ATAC-seq ladder, section 18); 200–500 bp sets ChIP-seq resolution (section 17).

### Key terms

- **Depth (coverage):** ~20–40 M reads for TF ChIP-seq, ~30× for WGBS, billions of read pairs for high-resolution Hi-C.
- **Multiplexing:** indexes let many samples share one run.
- **Duplicates:** PCR copies of the same molecule; removed so they do not inflate the signal.
- **Long-read sequencing:** PacBio and Oxford Nanopore read 10–100+ kb single molecules without amplification; they resolve repeats and detect 5mC directly.

---
> [[IG 08 - DNA methylation + Methods – from one locus to the whole epigenome|← DNA methylation + Methods – from one locus to the whole epigenome]] · [[Integrative Genomics|↑ Integrative Genomics]]
