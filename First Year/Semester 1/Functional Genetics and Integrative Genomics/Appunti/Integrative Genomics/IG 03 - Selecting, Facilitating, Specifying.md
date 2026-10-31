---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "Schoenfelder & Fraser 2019"
order: 3
tags: [note, ig, enhancer, 3D-genome]
---

> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]

# Selecting, Facilitating, Specifying

*IG 03 · integrated model, lecture + Schoenfelder & Fraser 2019 · schematic, not to scale*

Interactive 3D model: [Selecting, Facilitating, Specifying](https://claude.ai/code/artifact/1aab35c0-275b-4492-b5f2-373f6b8d9ce0)

## 1. Selecting (Phase 1): Which enhancers switch on

A cell-type-specific subset of enhancers becomes accessible and active.

- **Compact chromatin**: The enhancer is wrapped around nucleosomes. Next to it is another enhancer that will stay closed in this cell.
- **The pioneer TF arrives**: Pioneer TFs bind DNA even in compact chromatin.
- **SWI/SNF opens**: The remodeler shifts the nucleosomes and leaves a stretch of accessible DNA.
- **H3K4me1**: Histone methyltransferases deposit H3K4me1 on nearby nucleosomes. Neutral/intermediate state.
- **H3K27ac**: p300/CBP adds H3K27ac. With H3K4me1 + H3K27ac the enhancer is active.

**Key points**

- Poised = H3K4me1 + H3K27me3: embryonic cells switch quickly to either active or silenced.
- The H3K4me1:H3K4me3 ratio is high at active enhancers; H3K4me3 is typical of promoters.
- Marks overestimate: only ~12% of H3K27ac peaks are functional in MPRA (hESC), and 41–48% of candidates fail in VISTA in vivo assays.

## 2. Recruitment (linking step): The open enhancer recruits factors

Cell-type-specific TFs bind the accessible DNA and bring in coactivators and RNA Pol II.

- **Open, marked enhancer**: We start where step 1 ended: accessible DNA, with neighbouring nucleosomes carrying H3K4me1 + H3K27ac.
- **Cell-type-specific TFs**: They bind their sequences in the open stretch.
- **Mediator and p300/CBP**: The TFs recruit the coactivators.
- **BRD4 reads H3K27ac**: BRD4 docks onto the acetylated nucleosomes.
- **RNA Pol II**: The polymerase is also recruited to the enhancer.
- **eRNA**: Pol II transcribes the enhancer, often in both directions.

**Key points**

- Some eRNAs support looping or retain cofactors.
- eRNA–mRNA correlation does not prove causality, and functional eRNAs are not a universal requirement.

## 3. Facilitating (Phase 2): The search space shrinks

The orange dots are the places the enhancer can explore. 3D genome structure narrows them down at each level.

- **The whole nucleus**: Without organisation, the enhancer would have to search for its promoter across the entire nuclear volume.
- **Compartment A**: Active chromatin segregates from inactive chromatin (compartment B).
- **TAD**: A sub-megabase domain with preferential contacts inside it. It insulates enhancer and promoter from other domains.
- **Condensate**: Relocation into transcription factories or phase-separated condensates. BRD4 and MED1 form condensates at super-enhancers.

**Key points**

- TAD insulation is preferential, not absolute: about one third of promoter–distal element contacts cross boundaries.
- Assigning an enhancer to a gene requires 3D contact maps: linear distance is not enough.
- At the Shh locus, boundaries matter and internal distance matters little: disrupting the TAD causes loss of Shh and monodactyly.

## 4. Loop formation (linking step): Cohesin extrudes the loop

Cohesin reels DNA through its ring until it reaches two convergent CTCF sites.

- **Linear DNA**: Enhancer and promoter are far apart along the fibre.
- **NIPBL loads cohesin**: NIPBL–MAU2 loads the SMC1, SMC3, RAD21 ring.
- **Extrusion**: DNA slides through the ring and the loop grows. The dashed line is the 3D distance between enhancer and promoter.
- **Stop at convergent CTCF**: Extrusion halts at two sites in convergent orientation.
- **WAPL unloads**: WAPL removes cohesin, so the loop is dynamic.

**What happens if…**

- **Normal**: Cohesin stops at two convergent CTCF sites. Enhancer and promoter end up close together in the loop, then WAPL unloads cohesin.
- **Inverted CTCF**: With the right-hand site inverted, cohesin doesn't stop there and continues to the next convergent site. The original loop is lost.
- **WAPL lost**: Without WAPL, cohesin stays on DNA longer and loops get bigger: residence time controls loop size.
- **NIPBL lost**: With less cohesin loading, loops stay smaller; here extrusion doesn't reach the enhancer and promoter.

**Key points**

- When CTCF or cohesin is degraded, loops and TADs disappear within a few hours, compartments persist or strengthen, and only a few genes change expression.
- It is not proven that this mechanism directs E–P contacts: few CTCF sites coincide with active genes or enhancers, and the Sox2 enhancer loop persists after deletion of the CTCF site.

## 5. Specifying (Phase 3): A random encounter becomes stable

Proteins bound to the enhancer and promoter turn a random contact into a preferential one.

- **Brief encounters**: Within the domain, enhancer and promoter touch by chance and drift apart again.
- **Mediator acts as a bridge**: Mediator binds factors on both enhancer and promoter, and the contact lasts longer.
- **YY1 homodimers**: YY1 bound to both elements dimerises.
- **LDB1**: LDB1 also stabilises the contact.
- **No "postcode"**: The model does not require a dedicated code for each pair. Specificity arises from encounter probability plus stabilisation.

**Key points**

- The promoter in the neighbouring TAD is reached rarely, not never: insulation is not absolute.
- Removing a boundary reassigns enhancers to the wrong genes: EPHA4 onto Ihh, Wnt6, Pax3 (limb malformations); PDGFRA in IDH-mutant gliomas.

## 6. Output (result): Contact switches on transcription

The contact brings enhancer-bound factors to the promoter.

- **Assembly at the promoter**: The transcription machinery assembles. This is the initiation step.
- **Paused Pol II**: DSIF and NELF hold Pol II near the promoter.
- **P-TEFb phosphorylates**: P-TEFb phosphorylates DSIF and NELF.
- **NELF leaves**: Pol II enters elongation.
- **More bursts**: New polymerases fire from the same promoter, so burst frequency increases.

**Key points**

- Proximity can be causal: forced looping at the Hbb locus activates transcription and increases burst fraction, not burst size.
- It is permissive, not sufficient: ZRS and Shh are close even where Shh is off; the distance is smallest (< 200 nm) in the ZPA.
- It is not universal: Shh in the developing brain and EDN1 are expressed with no detectable contact.
- An eRNA can bind NELF as a decoy: probably a contributing factor, not the sole determinant.

## Sources

- **[SF19]** Schoenfelder & Fraser, *Long-range enhancer–promoter contacts in gene expression control*, Nat Rev Genet 20:437–455 (2019)
- **[W26]** Wang, ten Dijke & Fan, *Deciphering the regulatory landscape of enhancer RNAs in health and disease*, Signal Transduct Target Ther 11:29 (2026)

---
> [[IG 02 - Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family|← Evidence that physical contact matters … Measuring contacts – 3C, Hi-C and the whole family]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|Genomic imprinting + Enhancer RNAs (eRNAs) →]]
