---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_common.docx"
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

> **Focus — ERT2-Gal4. Tamoxifen-inducible GAL4: the promoter gives the where, the drug the when.**

### The reporter

- **Strictly quantitative** reporters (e.g. **luciferase**).

- **“Morphological” and quantitative fluorescent** reporters (e.g. **GFP, RFP, Kaede** and others).

- **Combined-domain quantitative fluorescent** reporters, with **subcellular resolution** (nuclear, mitochondrial, membrane…) or reporting a **specific intracellular signal** (Ca²⁺, ROS, pH, oxygen…). Example: ***elavl3:H2B-GCaMP6s***, a calcium sensor fused to histone H2B, i.e. targeted to the nuclei of all neurons.

> **Focus — Kaede. Photoconvertible green → red, used for lineage tracing.**

### ![[FG-image57.png|326]]Cell-physiology reporters

- **FRET-based** (Förster/fluorescence resonance energy transfer) reporters: energy passes from a **donor** to an **acceptor** fluorophore only when they are very **close** (a few nm), so the ratio of the two emissions reports a molecular change.

- **Tension reporter** (Lagendijk et al., 2017): **tension pulls the two components apart** → **FRET goes down**.

- **H₂O₂ reporter** (Panieri et al., 2017), targeted to the cytoplasm, mitochondria or nucleus.

- **GCaMP**: **ligand-mediated structural changes correlate with intensity** — Ca²⁺ binding increases fluorescence (Fosque et al., 2015).

> **Focus — How GCaMP works. A Ca²⁺-sensitive GFP whose brightness reports neuronal activity.**

### Anatomy and signaling-pathway reporters

- ![[FG-image58.png|192]]**Major anatomical systems are conserved** with humans (insulin-producing cells, heart and blood cells…), with some exceptions (e.g. **lungs**).

- **Signaling pathway reporter lines**: multimerized binding sites for the transcription factor at the end of a pathway, a minimal promoter and a fluorescent protein. For Wnt the sites are those of **Pan** (*D. melanogaster*) / **Lef1** (all vertebrates) (Moro et al., 2013).

- The binding sites used are responsive elements conserved across species, so the line reports where a pathway is active rather than where a tissue-specific promoter fires, and the intensity of the fluorescence gives a quantitative read-out of pathway activity.

- **Signaling map** at 3 dpf: red, **Wnt**; green, **Notch**; cyan, **Shh**; magenta, **BMP** reporter.

- **Brain signaling atlas** (ViBEZ), 3 dpf: Tgf-β, BMP, Stat3, FGF, Shh, glucocorticoid, Notch, Wnt, hypoxia, Yap/Taz, CREB.

*Signaling map at 3 dpf: Wnt (red), Notch (green), Shh (cyan), BMP (magenta) reporter lines.*

---
> [[FG 17 - Danio rerio · Transgenesis and gene targeting|← Danio rerio · Transgenesis and gene targeting]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 19 - Danio rerio · CRISPRCas9 – from gene to disease model|Danio rerio · CRISPRCas9 – from gene to disease model →]]
