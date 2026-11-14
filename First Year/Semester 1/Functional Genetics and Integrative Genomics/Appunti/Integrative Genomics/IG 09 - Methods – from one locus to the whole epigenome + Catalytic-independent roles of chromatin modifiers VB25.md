---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 9
tags: [note, ig]
---

> [[IG 08 - DNA methylation|← DNA methylation]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 10 - ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing)|ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing) →]]

# Methods: from one locus to the whole epigenome

### Bisulfite sequencing

- **Steps:** **denaturation** at 95 °C (bisulfite acts only on single strands) → **conversion** with sodium bisulfite, 65 °C, pH 5–6 (C → uracil-sulfonate) → **desulfonation** at high pH, room temperature, 15 min → uracil.
- ![[IG-image27.png|350]]**5mC and 5hmC are not converted**; after PCR U → T. Unmethylated C → read as T; methylated C → stays C. Bisulfite cannot tell 5mC from 5hmC (oxidative bisulfite or TAB-seq needed).
- **UNG and bisulfite:** after conversion the template is full of U, so the PCR needs a polymerase that reads U as A (standard Taq; many proofreading enzymes stall on uracil), and the common anti-contamination trick (dUTP + UNG treatment before PCR) cannot be used, because UNG would destroy the converted template itself.
- Chromatogram: non-CpG Cs all become T (complete conversion); a surviving C at a CpG = methylated.
- Output: the clones are drawn as lollipops, one row per clone, filled = methylated CpG.
- Sequencing: Sanger with radioactive lanes (A, C, G, T) or four fluorescent dideoxy terminators in one capillary (96 capillaries in parallel, laser detection → chromatogram).

> **MLH1:** Bisulfite sequencing of the MLH1 promoter CGI (each row = one clone, filled circle = methylated CpG): in normal lymphocytes (A) the CpGs are unmethylated, while in leukemia/lymphoma cell lines (B) Kg1a is almost fully and Raji partly methylated (HL60 stays unmethylated); this hypermethylation silences the MMR gene MLH1, an epigenetic way for tumors to lose a tumor suppressor.
>
> ![[IG-image28.jpeg|361]]![[IG-image29.png|279]]

### Genome-wide methods

- **MeDIP** (methylated DNA immunoprecipitation): sonicate DNA, IP with **anti-5mC**, compare IP vs input on a two-color microarray or by sequencing (MeDIP-seq). PCR check: unmethylated region only in input, methylated in both. Resolution set by fragment size and probe spacing (promoter vs tiling arrays at 205 or 100 bp).
- **Whole-genome bisulfite sequencing** = bisulfite + NGS; base resolution (\[S12\] used reduced representation).
- **Chromatin-state tracks** (C. elegans chr IV): **Pol** II, **H3K4me3** (promoters), **H3K27ac** (active promoters/enhancers) and **H3K36me3** (transcribed gene bodies) mark active regions; **H3K27me3** and **H3K9me3** form broad domains over silent regions, anti-correlated with active marks.

## 16. Catalytic-independent roles of chromatin modifiers \[VB25\]

Main message: the KO phenotype of a writer or eraser is **not** automatically the loss of its enzymatic activity. Comparing **null** alleles (no protein) with **catalytic-dead** alleles (protein present, no activity) in mice shows that many of these proteins are essential for development as **scaffolds/recruiters**; catalytic-dead mice usually survive longer than nulls.

### Examples by class

- **HDAC3 (deacetylase):** activated by the DAD of NCOR/SMRT. *Hdac3*⁻/⁻ → death before E9.5. **NS-DADm** mice (DAD mutated in both NCOR and SMRT → HDAC3 present but inactive) survive to adulthood with normal viability; adults only have mild hepatic steatosis and age-related muscle defects, so enzymatic activity matters later in life. In the heart, wild-type or catalytic-dead HDAC3 both recruit **PRC2** to the *Tgf-β* locus and restore H3K27me3 (100% vs 50%) and silencing.
- **DNMT3B (DNA methyltransferase):** *Dnmt3b*⁻/⁻ die at E11.5–15.5; catalytic-dead *Dnmt3b*<sup>P656V;C657D</sup> homozygotes survive. Only ~5% of DMRs vs null. Proposed accessory role (like DNMT3L) supporting DNMT3A; it is not yet clear if DNMT3A is up-regulated to compensate.
- **KAT2A/GCN5 (acetyltransferase):** null → death ~E9.5 (mesoderm apoptosis, neural tube and yolk-sac vascular defects); catalytic-dead *Kat2a*<sup>E568A;D609A</sup> → most pass mid-gestation but die E12.5–E16.5. In neural crest (Wnt1-Cre), no protein → severe nasal clefting and loss of craniofacial skeleton; catalytic-dead protein → no clefting, jaws form. Both catalytic and non-catalytic roles are needed.
- **TET1 (demethylase):** different *Tet1* KO lines give discordant phenotypes (fully viable to 100% lethal), possibly because some 3′ deletions still produce an N-terminal fragment that binds chromatin (unintended catalytic mutants) and because of genetic background. Catalytic mutants (H1620Y;D1622A, or the 'stalled' T1610V) are milder. Non-catalytic TET1 still protects sperm DNA from hypermethylation at ~75% of the DMRs of the KO (occupancy blocks DNMT3), and represses genes by recruiting **JMJD8**, **SIN3A** or **HDAC1**.

### Lineage and life stage matter

- Catalytic-dead **TET2** causes myeloid disease but protects from the lymphoid disease of the full KO. Catalytic-dead **DNMT3A** suppresses *Dnmt3b* in T-cell lymphoma, but cannot rescue the differentiation of *Dnmt3a*-KO neural stem cells. So the requirement is cell-type specific: one cell line (often mESCs) is not enough.
- Development seems more tolerant to loss of catalytic activity than to loss of the protein; the authors suggest catalytic activities may provide finer regulation for exposures later in life.

### Implications for therapy

- If disease is driven by a non-catalytic function, an enzymatic inhibitor will fail, but removing the whole protein can work: **PROTAC** degraders of **SMARCA2/4**, **EZH2** and **p300/CBP** are more effective than inhibitors of the enzymatic domain or the bromodomain (the bromodomain ligand alone does not stop proliferation; used as a PROTAC handle it does).
- Conversely, when the enzymatic activity is the driver (e.g. some pediatric cancers), an inhibitor may be better, with fewer effects because the rest of the protein is kept.
- Whether a **mark** is causal can now be tested by tethering an enzyme, or its catalytic-dead mutant, with **dCas9** (same logic as the dCas9 looping experiments in section 3).

### How the paper connects to the lectures

- Lecture 4 presents writers and erasers through their **activity** (HAT, HDAC, HMTase assays); \[VB25\] adds that the **same proteins** also act as platforms that recruit other complexes (HDAC3 → PRC2; TET1 → JMJD8/SIN3A/HDAC1).
- Lecture 5 presents DNMT3L as an inactive accessory; \[VB25\] proposes that DNMT3B has an essential accessory function of the same kind.
- Section 12 explains HDAC inhibitors in cancer; \[VB25\] warns that an inhibitor only removes the catalytic part, which may not be the disease driver.

---
> [[IG 08 - DNA methylation|← DNA methylation]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 10 - ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing)|ChIP-seq (chromatin immunoprecipitation followed by sequencing) + ATAC-seq (assay for transposase-accessible chromatin with sequencing) →]]
