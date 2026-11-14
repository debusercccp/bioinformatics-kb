---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 1
tags: [note, ig]
---

> [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family →]]

# Lecture notes – key facts

**Integrative Genomics** = How does the genome shape the phenotype?

- The first eukaryotic RNA Pol II structure was solved from *S. cerevisiae* (Kornberg, Nobel 2006); today bacterial and human RNA pol structures are also available
- Humans have ≈ 20,000 genes and 10<sup>14</sup> cells
- *C. elegans* has ≈ 20,000 protein-coding genes and 959 somatic cells (adult hermaphrodite; invariant cell lineage)
- **Surfomics** = all the proteins on the plasma membrane
- The majority of genes in *C. elegans* go through **trans-splicing**
- Every time there's a level of complexity, there's also a level of control
- **Nonsense-mediated decay** = control pathway that finds and destroys mRNAs with premature stop codons
- ~170 known types of RNA modifications (epitranscriptome)
- IG combines bioinformatics with genomics

Paper tags such as \[SF19\], \[W26\] or \[R00\] are expanded in **Papers of the course**, at the end of these notes.

## 1. The big question

- Integrative genomics combines genomics, transcriptomics, proteomics, metabolomics, epigenetics, physiology, ecology across scales (molecule → cell → organism → ecosystem).
- Core question: **how does the genome shape the phenotype?** The link between GENOME and PHENOTYPE is the **regulation of genome expression**.
- Coding sequence is \<2% of the mammalian genome; the rest is full of *cis*-regulatory elements (promoters, enhancers, silencers, insulators) that act with *trans*-acting factors to decide when and where genes are expressed \[SF19\].

![[IG-image1.png|512]]

**Take-home:** a phenotype can be altered at any of these levels, so integrative genomics layers one assay type per level to follow GENOME → PHENOTYPE.

## 2. Enhancer–promoter crosstalk

### Two major questions

- How do enhancers find their target genes in nuclear space?
- How are enhancers prevented from aberrantly activating non-target genes?

Technologies that made progress possible: (a) genome-wide mapping of E–P contacts, (b) unbiased screening of regulatory elements in native context by genome/epigenome editing, (c) engineering of E–P contacts.

### What the crosstalk is

One chapter of the paper \[SF19\] asks what the crosstalk between E and P is: the promoter can instruct the **direction** and the accurate **initiation** of the transcription, but it is not sufficient to control the rate of transcription — we need **other elements** that are involved in stimulating or repressing the polymerase (promoter vs enhancer in detail below).

### The pre-initiation complex (PIC)

Early in vitro experiments in the 1980s defined the stepwise assembly of the Pre-Initiation Complex (PIC).

- The process begins with TFIID (whose major subunit, the TATA-Binding Protein or TBP, binds the TATA box) and TFIIB.
- Additional basal transcription factors join to fully assemble the PIC, providing the scaffold onto which RNAPII associates.
- Finally, TFIIH phosphorylates the C-Terminal Domain (CTD) of RNAPII’s major subunit. The specific pattern of this phosphorylation triggers the transition from transcriptional initiation to elongation, and eventually termination.

![[IG-image2.png|483]]States to know: **closed PIC**, **open PIC** (promoter DNA, TFIIA/B/D/E/F/H, Pol II), **initially transcribing complex** (transcription bubble, nascent RNA, NTPs, ATP) and **elongation complex** (elongation factors, 5′ cap). Use it to place what enhancers act on: PIC assembly, escape and the move into elongation.

**Paper — Tupler, Perini & Green, 2001** (Nature 409:832–833): the survey of the human genome behind this part. Transcription of protein-coding genes by RNA Pol II needs the general (basic) transcription factors — TFIID, TFIIA, TFIIB, TFIIE, TFIIF and TFIIH — which assemble on the promoter into the PIC, with TFIID (TBP plus the TAFs) as the primary sequence-specific DNA-binding component that starts the assembly on the TATA box; searching the genome for new factors of transcription, pre-mRNA splicing and 3′-end formation revealed a substantial but selective increase in complexity compared with Drosophila and C. elegans.

### The “sufficiency” paradox

In the 1990s, in vitro experiments showed that a synthetic naked DNA template, RNA Polymerase II and all the general transcription factors (GTFs) are sufficient to assemble the pre-initiation complex, and that adding nucleotides (NTPs) gives a basal level of transcription. This is **not true in vivo**: inside the cell DNA is wrapped in repressive **chromatin**, so a stable and efficient transcript requires **specific combinations of activating TFs and coactivators**, which stabilize RNAPII, stimulate its firing rate and recruit chromatin remodelers.

### “Sometimes being weak means being strong”

In eukaryotes, maximizing gene activity requires the coordination of multiple TFs (humans have roughly 1,600 specific TFs).

Yeast only needs one factor to activate about 15% of its genes ⇒ an ON/OFF switch mechanism, because the maximum activity is already reached with one TF bound;

in multicellular organisms the maximum is reached with 6–10 TFs bound ⇒ many “weak” TFs instead of a few strong ones.

This “weakness is a strength” paradigm allows high variability and precise fine-tuning: combining multiple weak, tissue-specific TFs with cofactors (e.g. p300, Mediator, BRG1) generates highly specific, combinatorial transcriptional responses. Apes together, strong lol.

**Paper — Lambert et al., 2018** (Cell 172:650–665): the catalog behind the number of human TFs — over 1,600 likely TFs, with binding motifs known for about two thirds of them. The major classes differ markedly in evolutionary trajectory and expression pattern, and the review stresses that it remains hard to say from the motif alone where a TF binds in the genome and how that binding relates to the regulation of transcription.

### Key facts: promoter vs enhancer

- **Promoter**: sits just upstream of the TSS; recruits TFs and RNA Pol II, fixes **direction and accurate initiation** of transcription.
- **Enhancer**: activates or **increases the rate of firing** of target genes; can sit upstream, downstream, in introns, even of unrelated genes; position/orientation independent. Hundreds of kb away in some cases and can skip nearer genes, so “nearest gene” assignment is often wrong.
- Bound by tissue-specific TFs and cofactors (p300, Mediator, BRG1).
- **Enhancer states** (histone marks):
  - **neutral/intermediate**: H3K4me1
  - **poised**: H3K4me1 + H3K27me3 (Like a runner on his way to sprint when he hears the gunshot lol: the histone mark H3K4me1 prepares it, but the repressive methylation H3K27me3 keeps it in the starting blocks.)
  - **active**: H3K4me1 + H3K27ac
- Number of enhancers: ~1,000,000 putative enhancers (this is the **\[SF19\]** estimate; **\[W26\]** quotes \>400,000 from ENCODE, of which only ~40,000–65,000 are actively transcribed). Different counting methods, so quote the source. Mark-based enhancer calls overestimate the real ones: only ~12% of H3K27ac peaks work in an MPRA in hESCs, and 41–48% of candidate enhancers fail in VISTA in vivo assays \[SF19\].

### The poised state in development

This poised state is crucial during embryonic development. Embryonic stem cells (e.g., within a mouse blastocyst containing 40–50 undifferentiated cells) possess many poised enhancers. Upon implantation into the uterus, signaling cascades instruct lineage commitment. Because these enhancers are already “poised,” the cell does **not need to remodel chromatin from scratch**; genes can **rapidly transition to an active or silenced state** to drive tissue differentiation.

---
> [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family →]]
