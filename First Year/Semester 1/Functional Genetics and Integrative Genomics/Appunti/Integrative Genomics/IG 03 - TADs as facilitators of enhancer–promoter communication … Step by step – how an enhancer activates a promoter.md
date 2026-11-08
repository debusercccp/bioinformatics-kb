---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/Functional_Genetics/IntegrativeGen_RS.docx"
order: 3
tags: [note, ig]
---

> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]

# TADs as facilitators of enhancer–promoter communication

**TADs** (topologically associating domains), i.e. **submegabase domains** with preferential contacts inside themselves, impose a **spatial insulation**, so they **mediate** or **facilitate enhancer–promoter contacts** inside the domains and **prevent aberrant gene activation between adjacent TADs.**

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

Pioneer TFs **bind compacted chromatin**, **chromatin remodelers (SWI/SNF) open it**, histone methyltransferases deposit H3K4me1 (intermediate state), and p300/CBP add H3K27ac (H3K4me1 + H3K27ac = active). A cell-type-specific subset of enhancers becomes accessible and “active”.

**Key points**

- Poised = H3K4me1 + H3K27me3: embryonic cells switch quickly to either active or silenced.
- The H3K4me1:H3K4me3 ratio is high at active enhancers; H3K4me3 is typical of promoters.
- Marks overestimate: only ~12% of H3K27ac peaks are functional in MPRA (hESC), and 41–48% of candidates fail in VISTA in vivo assays.

### 2. Recruitment (linking step): The open enhancer recruits factors

Cell-type-specific TFs bind the accessible DNA and **recruit coactivators** (Mediator, p300/CBP, BRD4 which reads H3K27ac) and **RNA Pol II**, which **transcribes the enhancer**, often bidirectionally (eRNAs).

**Key points**

- Some eRNAs support looping or retain cofactors.
- eRNA–mRNA correlation does not prove causality, and functional eRNAs are not a universal requirement.

### 3. Facilitating (Phase 2): The search space shrinks

3D genome structure **shrinks the search space** from the whole nucleus: compartment A (active) **segregates** from B, sub-megabase TADs **favour internal contacts**, CTCF–cohesin loops form, and genes relocate to transcription factories/condensates (BRD4 and MED1 at super-enhancers).

**Key points**

- TAD insulation is preferential, not absolute: about one third of promoter–distal element contacts cross boundaries.
- Assigning an enhancer to a gene requires 3D contact maps: linear distance is not enough.
- At the Shh locus, boundaries matter and internal distance matters little: disrupting the TAD causes loss of Shh and monodactyly.

### 4. Loop formation (linking step): Cohesin extrudes the loop

![[IG-image10.png|231]]NIPBL–MAU2 loads cohesin (SMC1–SMC3–RAD21 ring), which extrudes DNA **until it reaches two convergent CTCF sites**, bringing enhancer and promoter together; WAPL unloads it, so loops are dynamic.

**Key points**

- When CTCF or cohesin is degraded, loops and TADs disappear within a few hours, compartments persist or strengthen, and only a few genes change expression.
- It is not proven that this mechanism directs E–P contacts: few CTCF sites coincide with active genes or enhancers, and the Sox2 enhancer loop persists after deletion of the CTCF site.

### 5. Specifying (Phase 3): A random encounter becomes stable

Proteins bound at both elements turn brief chance encounters into **preferential contacts**: Mediator bridges them, YY1 dimerises, LDB1 stabilises. No “postcode” is needed: specificity = encounter probability + stabilisation.

**Key points**

- The promoter in the neighbouring TAD is reached rarely, not never: insulation is not absolute.
- Removing a boundary reassigns enhancers to the wrong genes: EPHA4 onto Ihh, Wnt6, Pax3 (limb malformations); PDGFRA in IDH-mutant gliomas.

### 6. Output (result): Contact switches on transcription

Contact brings enhancer-bound factors to the promoter: the machinery assembles (initiation); P-TEFb phosphorylates DSIF and NELF, NELF leaves and paused Pol II enters elongation; burst frequency rises.

**Key points**

- Proximity can be causal: forced looping at the Hbb locus activates transcription and increases burst fraction, not burst size.
- It is permissive, not sufficient: ZRS and Shh are close even where Shh is off; the distance is smallest (\< 200 nm) in the ZPA.
- It is not universal: Shh in the developing brain and EDN1 are expressed with no detectable contact.
- An eRNA can bind NELF as a decoy: probably a contributing factor, not the sole determinant.

**Points to remember:** contact frequency alone does not prove regulation; contacts may “prime” genes and a second trigger (e.g. p53 binding, eRNA production, stalled Pol II release) can be required.

### 

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
