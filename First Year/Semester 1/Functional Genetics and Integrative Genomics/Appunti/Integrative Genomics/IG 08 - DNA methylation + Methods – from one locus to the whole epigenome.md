---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/Functional_Genetics/IntegrativeGen_RS.docx"
order: 8
tags: [note, ig]
---

> [[IG 07 - Histone variants, the histone code and epigenetic memory|← Histone variants, the histone code and epigenetic memory]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 09 - ChIP-seq (chromatin immunoprecipitation followed by sequencing) … Next-generation sequencing (NGS) – the read-out of every -seq method|ChIP-seq (chromatin immunoprecipitation followed by sequencing) … Next-generation sequencing (NGS) – the read-out of every -seq method →]]

# DNA methylation

### The modified bases

- **5-methylcytosine (5mC)** is made by DNA methyltransferases (**DNMTs**) with SAM as methyl donor, at carbon 5 of cytosine, mostly at **CpG** (C 5′ of G).
- **TET dioxygenases** oxidise 5mC → **5hmC** → **5fC** → **5caC**; 5fC/5caC are removed by TDG and base excision repair = **active demethylation**. Passive demethylation = no maintenance during replication.
- **Deamination:** C → U (recognised as foreign and repaired), but **5mC → T**, which gives a T:G mismatch that is often not repaired. This is why CpG is depleted in the genome and methylated CpGs are mutation hotspots.
- In embryonic cells, cytosine methylation also occurs at **CpNpG** and other non-CpG contexts (CA, CT). Symmetric sites (CG/GC, CNG/GNC) can be copied after replication; asymmetric ones (CA, CT, CC) cannot.

### DNMTs: maintenance vs de novo

- **Maintenance (DNMT1):** after replication CpGs are **hemimethylated**; DNMT1 (with UHRF1) copies the pattern onto the new strand. Domains: DMAP1-binding, PCNA-binding (works at the fork), NLS, RFTS, CXXC (binds unmethylated CpG), BAH1/BAH2, catalytic motifs I–X.
- **De novo (DNMT3A, DNMT3B):** PWWP (reads H3K36me) + ADD (binds unmethylated H3K4) + catalytic domain; establish patterns in the germline and early embryo.
- **DNMT3L:** has ADD and an incomplete catalytic domain, so it is **catalytically inactive**; it is an accessory protein that stimulates DNMT3A/3B in the germline.
- **Link to \[VB25\]:** DNMT3B may have an essential non-catalytic, accessory role like DNMT3L (section 16).

### Methylation and gene silencing

- Methylated CpGs in a promoter block the binding of TFs that need an unmethylated site (TF cannot bind → target gene silenced) and recruit methyl-CpG-binding proteins with HDACs.
- **CpG island (CGI):** a region of **0.2 to 1–2 kb** where CpG frequency is higher than in the rest of the genome; usually **unmethylated**; found at ~60% of gene promoters.
- **Bioinformatic definition** (Gardiner-Garden & Frommer): length ≥ 200 bp, GC content \> 50%, and **observed/expected CpG \> 0.6**, where Obs/Exp = N(CpG) × L / (N(C) × N(G)). A sliding window computes both curves along the sequence; windows that pass the thresholds are called putative islands.
- **Cancer:** in normal cells the CGI of a tumour suppressor is unmethylated with H3K4me3 nucleosomes (gene ON); in cancer the CGI is hypermethylated with H3K9me nucleosomes (gene OFF). Example: **MLH1** (mismatch repair).

### Methylation dynamics in the early mouse embryo \[S12\]

- Reduced-representation bisulfite sequencing from gametes to post-implantation embryos: **sperm** is highly methylated, the **oocyte** intermediate.
- After fertilisation, methylation drops genome-wide to a **minimum in the ICM/blastocyst**, then rises again at implantation (E6.5–E7.5) to the high somatic level (brain, heart, liver).
- High-CpG-density regions (CGIs) stay unmethylated at all stages; the changes involve mostly low-CpG-density regions.

## 15. Methods: from one locus to the whole epigenome

### Southern blot with methylation-sensitive isoschizomers

- **HpaII** and **MspI** both cut CCGG; HpaII is blocked by CmCGG, MspI is not. Cut with EcoRI + HpaII (H) or EcoRI + MspI (M) and probe with a CGI fragment.
- **MLH1:** **11,671 bp** EcoRI fragment with **15 HpaII sites** in the CGI; **608 bp** CGI probe.
- **Result:** tumours without MSI (1254, 1256): H = M (0.5 kb band) → unmethylated. Tumours **with MSI** (1170, 1141, 1164, 1173): H keeps large bands (11.7, 1.6 kb) → CGI methylated → MLH1 silenced → MMR deficiency → MSI.

### Methylation-sensitive restriction + PCR (MS-PCR)

- Digest with a methylation-sensitive enzyme, then **PCR** across the site. **Unmethylated:** cut → **no PCR** product. **Methylated:** protected → PCR product. Not to be confused with MSP (methylation-specific PCR on bisulfite-converted DNA).
- Controls: EcoRI alone (always a product); EcoRI + **MspI** (never a product); EcoRI + **HpaII** or **PmlI** (CACGTG = E-box) → product only if methylated.
- **Application (CASP8 in neuroblastoma, Diolaiti et al., unpublished):** CASP8, a MYC target, is often silenced by promoter hypermethylation. MS-PCR (PmlI) gives the methylation of each E-box; ChIP measures **N-MYC/MAX binding**. In LAN-1 (CASP8 off), **5-aza-2′-deoxycytidine** (AZA, DNMT inhibitor) ± TSA (HDAC inhibitor) restores expression and N-MYC/MAX binding → E-box CpG methylation blocks MYC/MAX.

### Bisulfite sequencing

- **Steps:** **denaturation** at 95 °C (bisulfite acts only on single strands) → **conversion** with sodium bisulfite, 65 °C, pH 5–6 (C → uracil-sulfonate) → **desulfonation** at high pH, room temperature, 15 min → uracil.
- **5mC and 5hmC are not converted**; after PCR U → T. Unmethylated C → read as T; methylated C → stays C. Bisulfite cannot tell 5mC from 5hmC (oxidative bisulfite or TAB-seq needed).
- Chromatogram: non-CpG Cs all become T (complete conversion); a surviving C at a CpG = methylated.
- **Output:** clones drawn as lollipops (filled = methylated CpG). MLH1: normal lymphocytes (NL-1, NL-2, NL-6) and HL-60 unmethylated; Kg1a and Raji heavily methylated.
- Sequencing: Sanger with radioactive lanes (A, C, G, T) or four fluorescent dideoxy terminators in one capillary (96 capillaries in parallel, laser detection → chromatogram).

### Genome-wide methods

- **MeDIP** (methylated DNA immunoprecipitation): sonicate DNA, IP with **anti-5mC**, compare IP vs input on a two-colour microarray or by sequencing (MeDIP-seq). PCR check: unmethylated region only in input, methylated in both. Resolution set by fragment size and probe spacing (promoter vs tiling arrays at 205 or 100 bp).
- **Whole-genome bisulfite sequencing** = bisulfite + NGS; base resolution (\[S12\] used reduced representation).
- **Chromatin-state tracks** (C. elegans chr IV): **Pol** II, **H3K4me3** (promoters), **H3K27ac** (active promoters/enhancers) and **H3K36me3** (transcribed gene bodies) mark active regions; **H3K27me3** and **H3K9me3** form broad domains over silent regions, anti-correlated with active marks.

---
> [[IG 07 - Histone variants, the histone code and epigenetic memory|← Histone variants, the histone code and epigenetic memory]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 09 - ChIP-seq (chromatin immunoprecipitation followed by sequencing) … Next-generation sequencing (NGS) – the read-out of every -seq method|ChIP-seq (chromatin immunoprecipitation followed by sequencing) … Next-generation sequencing (NGS) – the read-out of every -seq method →]]
