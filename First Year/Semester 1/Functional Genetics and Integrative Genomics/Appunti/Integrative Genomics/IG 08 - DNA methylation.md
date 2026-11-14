---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 8
tags: [note, ig]
---

> [[IG 07 - Histone variants, the histone code and epigenetic memory|← Histone variants, the histone code and epigenetic memory]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 09 - Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25|Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25 →]]

# DNA methylation

### The modified bases

- 5-methylcytosine (5mC) is made by DNA methyltransferases (DNMTs) with SAM as methyl donor, at carbon 5 of cytosine, mostly at CpG (C 5′ of G): in ~99% of cases a methylated C is followed by a G. CpG islands at **active promoters** are instead **normally unmethylated** (below).
- **TET dioxygenases** oxidize 5mC → **5hmC** → **5fC** → **5caC**; 5fC/5caC are removed by TDG and base excision repair = **active demethylation**. Passive demethylation = no maintenance during replication.
- **DNMT inhibitors**: 5-azaC (azacitidine) and 5-aza-dC (decitabine) are cytidine analogs with N at position 5. 5-aza-dC goes only into DNA; 5-azaC mostly into RNA.
- Mechanism: the DNMT binds C6 covalently but cannot methylate N5 or detach → enzyme trapped and degraded → DNMT1 depleted → passive demethylation at each replication (dividing cells only).
- Effects: low dose = hypomethylation and re-expression of silenced genes (e.g. p16, inactive X); high dose = cytotoxic. Used for MDS and AML.
- Use: re-expression after treatment means silencing was methylation-dependent (e.g. 5-azaC turned 10T1/2 fibroblasts into muscle, Taylor & Jones 1979 → MyoD).
- Deamination: C → U (recognized as foreign and repaired), but 5mC → T, which gives a T:G mismatch that is often not repaired (the repair logic is in the next point).
- **Uracil DNA glycosylase (UNG/UDG):** base excision repair (BER) enzyme that removes uracil from DNA, whether it comes from cytosine deamination (U:G mismatch) or from dUTP misincorporated during replication (U:A). It slides along the DNA, **flips the uracil out** of the double helix into its active-site pocket and cleaves the **N-glycosidic bond** between the base and the deoxyribose → **abasic (AP) site**. Then APE1 cuts the backbone at the AP site, DNA Pol β inserts the correct C opposite G, and DNA ligase III/XRCC1 seals the nick → the original C:G is restored without errors.
- **Why UNG ignores thymine:** the pocket is **shaped for uracil**; the 5-methyl group of T clashes sterically with it (a tyrosine side chain blocks it), so T is never removed. This is the reason DNA uses T instead of U: any U in DNA can only come from **damage**, so it is recognized as foreign. The flip side: 5mC deaminates to **T**, a normal base that UNG does not touch. The T:G mismatch is left to the much less efficient **TDG** and **MBD4** (thymine DNA glycosylases; MBD4 binds methyl-CpG); if replication comes first, the T is copied → permanent C:G → T:A transition. This is the molecular reason why **methylated CpGs are mutation hotspots** and why CpG has been lost from the genome over evolution (see CpG islands below). TDG is also the eraser step of active demethylation (removes 5fC/5caC, above).
- In embryonic cells, cytosine methylation also occurs at **CpNpG** and other non-CpG contexts (CA, CT). **Symmetric sites** (CG/GC, CNG/GNC) can be **copied** after replication; asymmetric ones (CA, CT, CC) cannot.

### DNMTs: maintenance vs de novo

- **Maintenance (DNMT1):** after replication CpGs are **hemimethylated**; DNMT1 (with UHRF1) copies the pattern onto the new strand. Domains: DMAP1-binding, PCNA-binding (works at the fork), NLS, RFTS, CXXC (binds unmethylated CpG), BAH1/BAH2, catalytic motifs I–X.
- **De novo (DNMT3A, DNMT3B):** PWWP (reads H3K36me) + ADD (binds unmethylated H3K4) + catalytic domain; establish patterns in the germline and early embryo.
- **DNMT3L:** has ADD and an incomplete catalytic domain, so it is **catalytically inactive**; it is an accessory protein that stimulates DNMT3A/3B in the germline.
- **Link to \[VB25\]:** DNMT3B may have an essential non-catalytic, accessory role like DNMT3L (section 16).
- **Catalytic mechanism:** the DNMT flips the target cytosine out of the helix into its active site; a conserved cysteine (PC motif IV) attacks C6, which activates C5 to take the methyl from SAM (→ SAH); β-elimination then releases the enzyme. This is the step blocked by 5-aza drugs.
- **UHRF1:** its SRA domain recognizes hemimethylated CpG and flips out the 5mC; it ubiquitinates H3 (K18/K23), which recruits DNMT1 through the RFTS domain and releases its autoinhibition.
- **DNMT2 (TRDMT1):** despite the name, it methylates tRNA (C38 of tRNA-Asp), not DNA.
- **Knockouts and disease:** in mouse, Dnmt1−/− and Dnmt3b−/− are embryonic lethal, Dnmt3a−/− die about 4 weeks after birth, Dnmt3l−/− males are sterile. In humans, DNMT3B mutations cause ICF syndrome and DNMT3A is often mutated in AML.

### Methylation and gene silencing

- Methylated CpGs in a promoter block the binding of TFs that need an unmethylated site (TF cannot bind → target gene silenced) and recruit methyl-CpG-binding proteins with HDACs.
- **CpG island (CGI):** a region of **0.2 to 1–2 kb** where CpG frequency is higher than in the rest of the genome; usually **unmethylated**; found at ~60% of gene promoters.
- **Bioinformatic definition** (Gardiner-Garden & Frommer): length ≥ 200 bp, GC content \> 50%, and **observed/expected CpG \> 0.6**, where Obs/Exp = N(CpG) × L / (N(C) × N(G)). A sliding window computes both curves along the sequence; windows that pass the thresholds are called putative islands.
- **Probability of finding a CpG (the “expected” value):** if the four bases were equally frequent and independent, the chance that a given position starts a CpG is P(C) × P(G) = 1/4 × 1/4 = **1/16 ≈ 6%**, i.e. one CpG every ~16 bp. The human genome is only ~40% GC (P(C) = P(G) ≈ 0.2), so the expected frequency is ≈ 0.2 × 0.2 = **0.04 → one CpG every ~25 bp**. The observed frequency is ~1%, about **one CpG every ~100 bp**, so in bulk DNA Obs/Exp ≈ 0.2–0.25 (**CpG depletion / CpG suppression**). The missing CpGs were lost by deamination of 5mC → T (UNG cannot repair it, above): CpG became TpG (and CpA on the other strand), which are correspondingly over-represented.
- **Why islands exist:** CGIs are the regions that kept Obs/Exp close to 1 because they stay **unmethylated in the germline**: no 5mC → no deamination → the CpGs are not lost. An island is therefore the evolutionary footprint of a region that is never methylated, not a random cluster. Worked example: in a 200 bp window with 50% GC (N(C) = N(G) = 50) the expected number of CpGs is N(C) × N(G) / L = 50 × 50 / 200 = **12.5**; bulk-genome DNA (Obs/Exp ≈ 0.25) would contain only ~3, while an island needs at least 0.6 × 12.5 ≈ **8 CpGs**. The human genome has roughly **28,000–30,000 CGIs**, covering only ~1% of the sequence.
- **How to find them, step by step (slide 25 = output of a cpgplot-type program):** (1) take the sequence (e.g. the promoter region from a genome browser), with repeats masked; (2) slide a window (100–200 bp, moving 1 bp at a time) and compute for each window the **GC%** and the **CpG Obs/Exp**; (3) mark the windows that pass **both** thresholds (GC \> 50%, Obs/Exp \> 0.6); (4) merge consecutive passing windows and keep the regions **≥ 200 bp** → putative islands.
- **Reading slide 25:** a ~6 kb sequence. Top panel = Obs/Exp along the sequence; middle = GC%; bottom = putative islands. Obs/Exp exceeds 0.6 in several places (peaks of ~1.4 at ~2,150 and ~5,400), but only the region at ~2,000–2,350 also has a GC content well above 50% (up to ~75%) for a long enough stretch → **one island (~350 bp)**. At ~5,400 Obs/Exp is high but GC% drops (down to ~25%) → not called. Both criteria must be met at the same time. **Slide 24** shows the same idea by eye: CpGs highlighted in pink are sparse in the flanking sequence and become dense from ~12,600 (asterisks) to ~13,500 = the island.
- **Cancer:** in normal cells the CGI of a tumor suppressor is unmethylated with H3K4me3 nucleosomes (gene ON); in cancer the CGI is hypermethylated with H3K9me nucleosomes (gene OFF). Example: **MLH1** (mismatch repair).

![[IG-image25.png|368]]

FAS receptor and FAS ligand: FASL binding to the FAS death receptor triggers apoptosis. In cancer cells the FAS promoter is often hypermethylated, so FAS is silenced and the cell escapes apoptosis.

Example: oncogenic (mutated) RAS triggers de novo methylation of the FAS promoter by DNMT3A/3B, which switches FAS off.

**Methylome=** the **genome-wide map of DNA methylation** (mostly 5mC at CpG) in one cell type at one moment. The genome is the same in every cell; the methylome, like the transcriptome, is **cell-type specific** and changes in development, aging and disease.

- **Cancer methylome:** global hypomethylation (repeats, genomic instability) together with focal hypermethylation of tumor-suppressor CGIs (e.g. MLH1, above). The "epigenetic clock" (Horvath) estimates age from the methylation of a few hundred CpGs.
- How it is measured (section 15): WGBS = whole-genome bisulfite sequencing, single-base and all CpGs (gold standard); RRBS = only the CpG-rich fraction (cheaper); arrays (Illumina EPIC, ~850,000 CpGs); MeDIP / MBD-seq = enrichment, lower resolution; long-read sequencing (nanopore, PacBio) reads 5mC directly.

### Methylation dynamics in the early mouse embryo \[S12\]

- ![[IG-image26.png|291]]Three levels of DNA methylation: high, intermediate and low (the anti-5mC enrichment used here, MeDIP, is in section 15).
- Reduced-representation bisulfite sequencing from gametes to post-implantation embryos: **sperm** is highly methylated, the **oocyte** intermediate. (both haploids)
- After fertilization, methylation drops genome-wide to a **minimum in the ICM/blastocyst**, then rises again at implantation (E6.5–E7.5) to the high somatic level (brain, heart, liver).
- High-CpG-density regions (CGIs) stay unmethylated at all stages; the changes involve mostly low-CpG-density regions.
- **Zygote:** TET3 actively demethylates the paternal (sperm) genome, oxidizing 5mC → 5hmC in the male pronucleus; the maternal genome loses methylation more slowly and passively, through DNA replication.

### Methylation at a glance: writer, reader, eraser

**One word, three meanings.** The methyl group (from SAM) is always the same, but its effect depends on the molecule, the residue and above all on who reads it. **Writer** = deposits the mark; **reader** = binds it and recruits activators or repressors (it decides the output); **eraser** = removes it, so the mark is reversible. Methylation can occur on three molecules:

- **DNA (5mC at CpG):** usually OFF (see above).
- **Histones (lysines of H3):** ON or OFF depending on the residue, e.g. H3K4me3 active vs H3K27me3/H3K9me3 silencing (section 12).
- **eRNA (m6A):** mostly ON; added to the eRNA after the enhancer is transcribed (section 10).

---
> [[IG 07 - Histone variants, the histone code and epigenetic memory|← Histone variants, the histone code and epigenetic memory]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 09 - Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25|Methods – from one locus to the whole epigenome + Catalytic-independent roles of chromatin modifiers VB25 →]]
