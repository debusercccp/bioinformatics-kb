---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 3
tags: [note, ig]
---

> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]

*Approfondimento: [[IGx 01 - Selecting, Facilitating, Specifying|Selecting, Facilitating, Specifying]]*

# TADs as facilitators of enhancer–promoter communication

TADs (topologically associating domains), i.e. submegabase domains with **preferential contacts inside themselves** (how they appear and how they are called on a Hi-C map: section 5, steps 4–5), impose a **spatial insulation**, so they mediate or facilitate enhancer–promoter contacts inside the domains and prevent aberrant gene activation between adjacent TADs.

### The chain of evidence

- **Reporter integrations.** Random integrations of a **single-copy reporter** in the genome (hundreds of “regulatory sensors”, Symmons et al.): reporters integrated inside the same TAD display the **same tissue-specific expression**, while **reporters in neighbouring TADs behave differently**. Interpretation: an enhancer can reach everything inside its TAD, and **TADs may favour enhancer–promoter contacts** that otherwise could occur **too infrequently**. Caveat: the same result could also reflect a **permissive chromatin environment** shared by the whole domain.
- **Rearranging the *Shh* TAD.** Mouse lines carrying inversions, deletions and duplications of the locus: **changing the distances inside the TAD has little effect on Shh**, while **inversions that break the TAD prevent the ZRS from reaching Shh**, which gives **loss of Shh and monodactyly**; so the **boundaries**, not the distance, matter.
- **Human disease.** Structural variants that remove a boundary at the WNT6–IHH–EPHA4–PAX3 locus let *Ihh*, *Wnt6* and *Pax3* contact the **EPHA4 enhancers**, causing **limb malformations**; a duplication exposes *Kcnj2* to the *Sox9* enhancers.
- **Cancer.** The deletion or the methylation of CTCF sites at the boundaries of insulated neighbourhoods activates nearby **proto-oncogenes** through new enhancer contacts (e.g. PDGFRA in IDH-mutant gliomas).
- **Removing the architects.** The insulation is **not absolute**: about **one third** of the contacts between promoters and distal elements **cross the TAD boundaries**, and after an **acute degradation of CTCF or cohesin** (auxin-inducible degron) loops and TADs disappear within hours (while compartments remain, or even get stronger), but **only a few genes change their expression**.
- **Single cells.** **Single-cell (super-resolution) chromatin tracing** shows TAD-like domains in single cells even without cohesin, so TADs are not just an averaging artefact of Hi-C.

### Putting it together

TADs impose a **preferential, not absolute, insulation** and cannot be the only mechanism of specificity: they raise the probability that an enhancer meets the promoters of the same domain and lower it for promoters in the next domain, which helps explain why the **enhancer–gene assignment must be made from 3D contact maps**, not from the linear distance.

## 7. Loop extrusion in detail

- NIPBL–MAU2 loads **cohesin** (SMC1, SMC3, RAD21 ring) on DNA.
- Cohesin extrudes DNA through its ring, making a growing loop.
- Extrusion stops at two **convergent CTCF** sites (forward and reverse oriented).
- WAPL removes cohesin; residence time controls loop size.
- Evidence: cohesin depletion weakens loops/TADs and *strengthens* compartments; WAPL loss → larger loops; NIPBL loss → smaller loops; inverting CTCF sites disrupts loops.
- The model is not proven to be what directs E–P contacts: only a minority of CTCF sites coincide with active genes/enhancers, and the Sox2 enhancer loop persists after CTCF site deletion.

## 8. Step by step: how an enhancer activates a promoter

Integrated model from the lecture and **\[SF19\]** (“selecting – facilitating – specifying”).

### 1. Selecting (Phase 1): Which enhancers switch on

Pioneer TFs **bind compacted chromatin**, **chromatin remodelers (SWI/SNF) open it**, histone methyltransferases deposit H3K4me1 (intermediate state), and **p300/CBP add H3K27ac** (H3K4me1 + H3K27ac = active). A cell-type-specific subset of enhancers becomes accessible and “active”.

**Key points**: the enhancer marks (H3K4me1 ± H3K27ac, poised = H3K4me1 + H3K27me3), the high H3K4me1:H3K4me3 ratio and the fact that mark-based calls overestimate real enhancers are in section 2 (Key facts: promoter vs enhancer).

### 2. Recruitment (linking step): The open enhancer recruits factors

Cell-type-specific TFs bind the accessible DNA and **recruit coactivators** (Mediator, p300/CBP, BRD4 which reads H3K27ac) and **RNA Pol II**, which **transcribes the enhancer**, often bidirectionally (eRNAs).

**Key points**: what eRNAs do, and why the correlation between eRNA and mRNA does not prove causality, are in section 10.

### 3. Facilitating (Phase 2): The search space shrinks

3D genome structure **shrinks the search space** from the whole nucleus: compartment A (active) **segregates** from B, sub-megabase TADs **favour internal contacts**, CTCF–cohesin loops form, and genes relocate to transcription factories/condensates (BRD4 and MED1 at super-enhancers).

**Key points**: TAD insulation is **preferential** and not absolute, the enhancer–gene assignment needs 3D contact maps rather than the linear distance, and at the Shh locus the boundaries matter while the internal distance matters little (section 6).

### 4. Loop formation (linking step): Cohesin extrudes the loop

![[IG-image9.png|231]]NIPBL–MAU2 loads cohesin (SMC1–SMC3–RAD21 ring), which extrudes DNA **until it reaches two convergent CTCF sites**, bringing enhancer and promoter together; WAPL unloads it, so loops are dynamic.

**Key points**: what happens when CTCF or cohesin is degraded, and why it is not proven that extrusion is what directs E–P contacts, is in sections 6 and 7.

### 5. Specifying (Phase 3): A random encounter becomes stable

Proteins bound at both elements turn brief chance encounters into **preferential contacts**: Mediator bridges them, YY1 dimerises, LDB1 stabilises. No “postcode” is needed: specificity = encounter probability + stabilisation.

**Key points**: the promoter in the neighbouring TAD is reached rarely, not never, and removing a boundary reassigns enhancers to the wrong genes (section 6).

### 6. Output (result): Contact switches on transcription

Contact brings enhancer-bound factors to the promoter: the machinery assembles (initiation); P-TEFb phosphorylates DSIF and NELF, NELF leaves and paused Pol II enters elongation; burst frequency rises.

**Key points**: proximity can be causal (forced looping at the Hbb locus, section 3), but it is permissive and not sufficient (ZRS and Shh, section 4), it is not universal (Shh in the developing brain and EDN1, section 3), and an eRNA can act as a NELF decoy (section 10).

**Points to remember:** contact frequency alone does not prove regulation; contacts may “prime” genes and a second trigger (e.g. p53 binding, eRNA production, stalled Pol II release) can be required.

### Enhancer–promoter communication

Chromatin folding brings distant regulatory elements together:

- **Complementary roles**: the **promoter** positions the **initiation machinery**, while **enhancers increase** the **transcription** of target genes;
- **Physical communication**: **DNA looping** brings enhancer-bound factors close to the promoter and its transcription machinery;
- **Target specificity**: **TADs** favour **contacts** within a **domain** (preferential, not absolute), and their boundaries help limit the activation of genes in neighbouring domains;
- **Experimental evidence**: **3C** and **Hi-C map contacts**, and forced looping at the **Hbb locus** supports a **functional role for proximity**.

Mediator and **cohesin** can support **regulatory contacts**. So, **enhancer targeting** depends on both **regulatory activity** and **3D genome organization**.

### Transcriptional activation and eRNAs

Active enhancers are accessible with H3K4me1 + H3K27ac; Pol II transcribes enhancers (often bidirectional eRNAs); enhancer communication can raise initiation and promote pause release; some eRNAs support looping or cofactor retention and keep a transcription-permissive state. Mechanisms vary by locus, stable direct contact and functional eRNAs are not universal requirements, and eRNA–mRNA correlation does not prove causality.

---
> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]
