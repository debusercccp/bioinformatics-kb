---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 10
tags: [note, ig]
---

> [[IG 09 - Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25|← Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 11 - Next-generation sequencing (NGS) – the read-out of every -seq method … Papers of the course|Next-generation sequencing (NGS) – the read-out of every -seq method … Papers of the course →]]

# ChIP-seq (chromatin immunoprecipitation followed by sequencing)

ChIP-seq maps genome-wide **where a protein binds DNA or a histone mark sits**: DNA pulled down by an antibody is sequenced (section 19), reads are mapped, and read pile-ups (peaks) are the binding sites.

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
- Methylation: the central CpG of CACGTG can be methylated, which blocks MYC/MAX (section 14).
- **Accessibility:** motifs in nucleosomes or heterochromatin are usually unbound (except pioneer factors); ATAC-seq or DNase-seq shows open motifs.
- **Direct proof:** ChIP-seq (or CUT&RUN) shows actual binding; de novo motif analysis of peak centers finds the motif. Most reliable: motif + unmethylated CpG + open chromatin + ChIP peak.

---
> [[IG 09 - Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25|← Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 11 - Next-generation sequencing (NGS) – the read-out of every -seq method … Papers of the course|Next-generation sequencing (NGS) – the read-out of every -seq method … Papers of the course →]]
