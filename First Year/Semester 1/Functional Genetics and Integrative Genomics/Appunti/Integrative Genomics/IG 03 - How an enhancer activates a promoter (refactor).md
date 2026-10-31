---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 3
tags: [note, ig]
---

> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]

# How an enhancer activates a promoter

The **promoter** positions the initiation machinery and fixes the **direction and accurate initiation** of transcription. The **enhancer** increases the **rate of firing** of its target genes, and can sit hundreds of kb away and skip nearer genes. Chromatin folding brings the two together, so **enhancer targeting depends on both regulatory activity and 3D genome organization**.

## The model, step by step

Integrated model from the lecture and **[SF19]** (“selecting – facilitating – specifying”).

![[IG-image10.png|231]]

1. **Selecting.** Pioneer TFs bind compacted chromatin, chromatin remodelers (SWI/SNF) open it, histone methyltransferases deposit H3K4me1, and p300/CBP add H3K27ac. A cell-type-specific subset of enhancers becomes accessible and “active”.
2. **Recruitment.** Cell-type TFs bind the open enhancer and recruit coactivators (Mediator, p300/CBP, BRD4 which reads H3K27ac) and **RNA Pol II**.
3. **Facilitating.** 3D genome structure reduces the search space: compartments (A/B), TADs and CTCF–cohesin loops, relocation to transcription factories/phase-separated condensates (BRD4 and MED1 form condensates at super-enhancers).
4. **Loop formation.** Cohesin is loaded by NIPBL and extrudes a loop until it meets CTCF sites in convergent orientation; WAPL unloads it.
5. **Specifying.** Proteins bound at enhancer and promoter (Mediator, YY1 homodimers, LDB1) stabilize the chance encounter into a preferential contact. No “postcode” is predicted.
6. **Output.** Contact brings enhancer-bound factors to the promoter: assembly of the transcription machinery (initiation), higher burst frequency, and **release of paused Pol II** (P-TEFb phosphorylates DSIF and NELF, NELF dissociates, Pol II enters elongation).

## Step 1 in detail: enhancer states

| State | Marks |
|:---|:---|
| Neutral/intermediate | H3K4me1 |
| Poised | H3K4me1 + H3K27me3 |
| Active | H3K4me1 + H3K27ac |

Active enhancers have a high **H3K4me1:H3K4me3 ratio**, since H3K4me3 is typical of promoters. Poised enhancers let embryonic cells move quickly to an active or silenced state, with no slow chromatin remodelling from scratch.

Marks overestimate real enhancers: only ~12% of H3K27ac peaks work in an MPRA in hESCs, and 41–48% of candidate enhancers fail in VISTA in vivo assays [SF19].

## Steps 3–4 in detail: TADs and loop extrusion

### Loop extrusion

- NIPBL–MAU2 loads **cohesin** (SMC1, SMC3, RAD21 ring) on DNA.
- Cohesin extrudes DNA through its ring, making a growing loop.
- Extrusion stops at two **convergent CTCF** sites (forward and reverse oriented).
- WAPL removes cohesin; residence time controls loop size.

**Evidence:** cohesin depletion weakens loops/TADs and *strengthens* compartments; WAPL loss → larger loops; NIPBL loss → smaller loops; inverting CTCF sites disrupts loops.

**Limit:** the model is not proven to be what directs E–P contacts. Only a minority of CTCF sites coincide with active genes/enhancers, and the Sox2 enhancer loop persists after CTCF site deletion.

### What TADs do

**TADs** (topologically associating domains) are **submegabase domains** with preferential contacts inside themselves. Their **spatial insulation** facilitates enhancer–promoter contacts inside a domain and limits aberrant gene activation between adjacent TADs.

The insulation is **preferential, not absolute**, and cannot be the only mechanism of specificity. TADs raise the probability that an enhancer meets the promoters of the same domain and lower it for promoters in the next domain. This helps explain why the **enhancer–gene assignment must be made from 3D contact maps**, not from the linear distance.

### The chain of evidence

| Approach | Result | Reading |
|:---|:---|:---|
| **Reporter integrations**: random single-copy reporters, hundreds of “regulatory sensors” (Symmons et al.) | Reporters in the same TAD show the **same tissue-specific expression**; reporters in neighbouring TADs behave differently | An enhancer can reach everything inside its TAD, and TADs may favour contacts that would otherwise be **too infrequent**. Caveat: this could also reflect a **permissive chromatin environment** shared by the domain |
| **Rearranging the *Shh* TAD**: mouse inversions, deletions, duplications | Changing distances inside the TAD has little effect on Shh; inversions that break the TAD stop the ZRS reaching Shh, giving **loss of Shh and monodactyly** | The **boundaries**, not the distance, matter |
| **Human disease**: structural variants | Removing a boundary at the WNT6–IHH–EPHA4–PAX3 locus lets *Ihh*, *Wnt6* and *Pax3* contact the **EPHA4 enhancers**, causing **limb malformations**; a duplication exposes *Kcnj2* to the *Sox9* enhancers | Losing a boundary rewires enhancers onto the wrong genes |
| **Cancer** | Deleting or methylating CTCF sites at the boundaries of insulated neighbourhoods activates nearby **proto-oncogenes** through new enhancer contacts (e.g. PDGFRA in IDH-mutant gliomas) | Same rewiring, in tumours |
| **Removing the architects**: acute CTCF or cohesin degradation (auxin-inducible degron) | Loops and TADs disappear within hours, while compartments remain or even get stronger, but **only a few genes change expression**. About **one third** of promoter–distal element contacts **cross TAD boundaries** | The insulation is **not absolute** |
| **Single cells**: single-cell (super-resolution) chromatin tracing | TAD-like domains appear in single cells even without cohesin | TADs are not just an averaging artefact of Hi-C |

## Step 6 in detail: does contact cause activation?

- **Proximity can be causal.** Forced looping at the **Hbb locus** is direct evidence that a contact can cause transcription, which correlation between contact and expression cannot show.
- **Proximity is permissive, not sufficient.** The ZRS and the Shh promoter are close in space also in cells that do not express Shh; proximity is highest (< 200 nm) in the ZPA, where Shh is on.
- **Contacts tune bursting.** Forced looping raised **burst fraction** (how many alleles transcribe), not burst size.
- **Contact frequency alone does not prove regulation.** Contacts may “prime” genes, and a second trigger (e.g. p53 binding, eRNA production, stalled Pol II release) can be required.
- **Contact is not universal.** *Shh* in the developing brain and the EDN1 locus show expression without detectable promoter contact. It may be too rare to detect, or eRNAs/other mechanisms may be involved.

## Where eRNAs fit

Active enhancers are accessible with H3K4me1 + H3K27ac, and Pol II transcribes them, often into bidirectional eRNAs. Enhancer communication can raise initiation and promote pause release, and some eRNAs support looping or cofactor retention and keep a transcription-permissive state.

In pause release, Pol II is held near the promoter by NELF/DSIF. A stimulus induces an eRNA that binds NELF as a **decoy**, so NELF dissociates and Pol II enters elongation. This is probably a **contributor rather than the only determinant**, since pause release is also needed to produce the eRNAs.

Mechanisms vary by locus: stable direct contact and functional eRNAs are not universal requirements, and eRNA–mRNA correlation does not prove causality. Details are in [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs)]].

## Recap from the slides

- **Complementary roles:** the promoter positions the initiation machinery; enhancers increase the transcription of target genes.
- **Physical communication:** DNA looping brings enhancer-bound factors close to the promoter and its transcription machinery.
- **Target specificity:** TADs favour contacts within a domain (preferential, not absolute), and their boundaries help limit the activation of genes in neighbouring domains.
- **Experimental evidence:** 3C and Hi-C map contacts, and forced looping at the Hbb locus supports a functional role for proximity.
- **Supporting factors:** Mediator and cohesin can support regulatory contacts.

## Sources

- **[SF19]** Schoenfelder & Fraser, *Long-range enhancer–promoter contacts in gene expression control*, Nat Rev Genet 20:437–455 (2019)
- **[W26]** Wang, ten Dijke & Fan, *Deciphering the regulatory landscape of enhancer RNAs in health and disease*, Signal Transduct Target Ther 11:29 (2026)

---
> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]
