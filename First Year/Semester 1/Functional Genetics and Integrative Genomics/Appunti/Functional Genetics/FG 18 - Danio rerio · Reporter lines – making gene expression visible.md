---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 18
tags: [note, fg]
---

> [[FG 17 - Danio rerio · Transgenesis and gene targeting|← Danio rerio · Transgenesis and gene targeting]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 19 - Danio rerio · CRISPRCas9 – from gene to disease model|Danio rerio · CRISPRCas9 – from gene to disease model →]]

# Reporter lines: making gene expression visible

The two **main factors** in any experiment with fluorescent reporters are **(1) the promoter/enhancer region** and **(2) the expressed gene (the reporter)**; together they determine **the outcome (the signal)**.

### The promoter/enhancer

- **Tissue-specific**: e.g. **insulin** promoter (β-cells), **cmlc2** promoter (cardiomyocytes), **crystallin** promoter (lens). Examples: *ins:DsRed*, *fli1a:EGFP* (endothelium), *cmlc2:eGFP*, *crybb:CFP*.

- **Time-specific**: e.g. **HSP70** (heat-shock) promoter.

- **Ubiquitous**: ubiquitin, α-actin.

- **Combinatorial**: **simple** — in **space** (*ins:Gal4* × *UAS:GFP*) or in **time** (*HSP70:Gal4* × *UAS:GFP*); **conditional, in space and time** (*HuC:ERT2-Gal4* × *UAS:GFP*).

**Focus — ERT2-Gal4.** The GAL4/UAS system is imported directly from the fly (see *Drosophila*). In ERT2-Gal4, GAL4 is fused to a mutated ligand-binding domain of the oestrogen receptor that responds to **4-hydroxytamoxifen** but not to endogenous oestrogen: without the drug the fusion is held in the cytoplasm, adding the drug sends it to the nucleus. The *HuC* (*elavl3*) promoter gives the space (neurons), tamoxifen the time — the same principle as GeneSwitch in *Drosophila*.

### The reporter

- **Strictly quantitative** reporters (e.g. **luciferase**).

- **“Morphological” and quantitative fluorescent** reporters (e.g. **GFP, RFP, Kaede** and others).

- **Combined-domain quantitative fluorescent** reporters, with **subcellular resolution** (nuclear, mitochondrial, membrane…) or reporting a **specific intracellular signal** (Ca²⁺, ROS, pH, oxygen…). Example: ***elavl3:H2B-GCaMP6s***, a calcium sensor fused to histone H2B, i.e. targeted to the nuclei of all neurons.

**Focus — Kaede.** Kaede is a **photoconvertible** protein: green, it turns irreversibly **red** after UV/violet light. Converting a single cell or region and following the red signal over time is a direct way to trace cell fate and movement in the living embryo.

### GFP and its variants

**2008 Nobel Prize in Chemistry**: **Osamu Shimomura** first isolated GFP from the jellyfish ***Aequorea victoria*** and found that it glowed bright green under UV light; **Martin Chalfie** demonstrated its value as a **luminous genetic tag**; **Roger Tsien** explained how GFP fluoresces and made **variants with different colours**.

- **238 aa**, natural green fluorescence.

- Used as a **transcriptional and translational reporter** (bacteria, yeast, *Drosophila*, *C. elegans*, mammals).

- **Detectable in living cells**: monitoring **dynamic patterns of gene expression**, and the **subcellular localisation** of N- or C-terminally tagged proteins.

- **Enhanced GFP (eGFP)**: a mutant GFP (F64L) with **higher-intensity emission** than wild type.

- **Spectral variants** allow simultaneous labelling and tracing of **multiple genes in the same cell or organism**.

| **Colour** | **Variant** | **Source** | **Property** |
|----|----|----|----|
| Green | wtGFP / eGFP | Aequorea victoria | Original GFP / increased thermostability and fluorescence |
| Blue (cyan) | ECFP | Aequorea (GFP variant) | Blue-shifted GFP variant |
| Yellow | EYFP / Venus / Citrine | Aequorea (GFP variants) | Red-shifted; Venus matures faster and is brighter; Citrine more photostable and less pH-sensitive |
| Red | DsRed1, DsRed2, DsRed-T1/Express, mRFP1 | Discosoma sp. | DsRed1: obligate tetramer, slow maturation; later variants faster; mRFP1 monomeric and fast |
| Far red | HcRed | Heteractis crispa | Far-red fluorescent protein |

![[FG-image57.png|271]]Each protein has **distinct excitation and emission spectra** (from blue to far red: ECFP \< EGFP \< EYFP \< DsRed2 \< HcRed1). For multicolour experiments choose proteins whose spectra overlap as little as possible. The search for new, spectrally distinct fluorescent proteins continues. GFP emission has been observed during development and in adult mice in muscle, pancreas, kidney, heart and other organs.

**Focus — eGFP mutations.** The standard eGFP carries **F64L plus S65T**: S65T shifts the excitation peak to 488 nm (the argon laser line) and F64L improves folding at 37 °C; codon optimisation for mammals then increases expression.

### ![[FG-image58.png|326]]Cell-physiology reporters

- **FRET-based** (Förster/fluorescence resonance energy transfer) reporters: energy passes from a donor to an acceptor fluorophore only when they are very close (a few nm), so the ratio of the two emissions reports a molecular change.

- **Tension reporter** (Lagendijk et al., 2017): **tension pulls the two components apart** → **FRET goes down**.

- **H₂O₂ reporter** (Panieri et al., 2017), targeted to the cytoplasm, mitochondria or nucleus.

- **GCaMP**: **ligand-mediated structural changes correlate with intensity** — Ca²⁺ binding increases fluorescence (Fosque et al., 2015).

**Focus — How GCaMP works.** GCaMP is a **circularly permuted GFP** fused to **calmodulin** and the calmodulin-binding **M13** peptide. When Ca²⁺ rises, calmodulin binds M13, the chromophore environment changes and the protein becomes brighter. Since neuronal firing causes Ca²⁺ influx, GCaMP is used as a proxy for activity — the READ tool of the optogenetics section below.

### Anatomy and signalling-pathway reporters

- **Major anatomical systems are conserved** with humans (insulin-producing cells, heart and blood cells…), with some exceptions (e.g. **lungs**).

- **Signalling pathway reporter lines**: multimerised binding sites for the transcription factor at the end of a pathway, a minimal promoter and a fluorescent protein. For Wnt the sites are those of **Pan** (*D. melanogaster*) / **Lef1** (all vertebrates) (Moro et al., 2013).

- **Signalling map** at 3 dpf: red, **Wnt**; green, **Notch**; cyan, **Shh**; magenta, **BMP** reporter.

- **Brain signalling atlas** (ViBEZ), 3 dpf: Tgf-β, BMP, Stat3, FGF, Shh, glucocorticoid, Notch, Wnt, hypoxia, Yap/Taz, CREB.

![[FG-image59.png|454]]

*Signalling map at 3 dpf: Wnt (red), Notch (green), Shh (cyan), BMP (magenta) reporter lines.*

---
> [[FG 17 - Danio rerio · Transgenesis and gene targeting|← Danio rerio · Transgenesis and gene targeting]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 19 - Danio rerio · CRISPRCas9 – from gene to disease model|Danio rerio · CRISPRCas9 – from gene to disease model →]]
