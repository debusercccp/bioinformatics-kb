---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 3
tags: [note, ig]
---

> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]

# TADs as facilitators of enhancer–promoter communication

**TADs** (topologically associating domains), i.e. **submegabase domains** with preferential contacts inside themselves, impose a **spatial insulation**, so they **mediate** or **facilitate enhancer–promoter contacts** inside the domains and **prevent aberrant gene activation between adjacent TADs.**

### The chain of evidence

(The slide gives one experiment; the review gives the whole chain.)

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

- **Selecting.** Pioneer TFs bind compacted chromatin, chromatin remodelers (SWI/SNF) open it, histone methyltransferases deposit H3K4me1, and p300/CBP add H3K27ac. A cell-type-specific subset of enhancers becomes accessible and “active”.
- ![[IG-image9.png|231]]**Recruitment.** Cell-type TFs bind the open enhancer and recruit coactivators (Mediator, p300/CBP, BRD4 which reads H3K27ac) and **RNA Pol II**.
- **Facilitating.** 3D genome structure reduces the search space: compartments (A/B), TADs and CTCF–cohesin loops, relocation to transcription factories/phase-separated condensates (BRD4 and MED1 form condensates at super-enhancers).
- **Loop formation.** Cohesin is loaded by NIPBL and extrudes a loop until it meets CTCF sites in convergent orientation; WAPL unloads it.
- **Specifying.** Proteins bound at enhancer and promoter (Mediator, YY1 homodimers, LDB1) stabilise the chance encounter into a preferential contact. No “postcode” is predicted.
- **Output.** Contact brings enhancer-bound factors to the promoter: assembly of the transcription machinery (initiation), higher burst frequency, and **release of paused Pol II** (P-TEFb phosphorylates DSIF and NELF, NELF dissociates, Pol II enters elongation).

**Points to remember:** contact frequency alone does not prove regulation; contacts may “prime” genes and a second trigger (e.g. p53 binding, eRNA production, stalled Pol II release) can be required.

### Slide summary 1 — Enhancer–promoter communication

Chromatin folding brings distant regulatory elements together:

- **Complementary roles**: the **promoter** positions the **initiation machinery**, while **enhancers increase** the **transcription** of target genes;
- **Physical communication**: **DNA looping** brings enhancer-bound factors close to the promoter and its transcription machinery;
- **Target specificity**: **TADs** favour **contacts** within a **domain** (preferential, not absolute), and their boundaries help limit the activation of genes in neighbouring domains;
- **Experimental evidence**: **3C** and **Hi-C map contacts**, and forced looping at the **Hbb locus** supports a **functional role for proximity**.

Mediator and **cohesin** can support **regulatory contacts**. So, **enhancer targeting** depends on both **regulatory activity** and **3D genome organization**.

### Slide summary 2 — Transcriptional activation and eRNAs

Active enhancers are accessible with H3K4me1 + H3K27ac; Pol II transcribes enhancers (often bidirectional eRNAs); enhancer communication can raise initiation and promote pause release; some eRNAs support looping or cofactor retention and keep a transcription-permissive state. Mechanisms vary by locus, stable direct contact and functional eRNAs are not universal requirements, and eRNA–mRNA correlation does not prove causality.

---
> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]
