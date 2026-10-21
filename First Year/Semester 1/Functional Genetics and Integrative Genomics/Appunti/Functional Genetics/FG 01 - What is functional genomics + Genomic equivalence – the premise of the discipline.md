---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 1
tags: [note, fg]
---

> [[Functional Genetics|↑ Functional Genetics]] · [[FG 02 - Why function requires perturbation + Forward genetics|Why function requires perturbation + Forward genetics →]]

# What is functional genomics?

**Definition.** Functional genomics tries to understand the relationship between **genotype and phenotype on a global scale**, i.e. across the whole genome and not one gene at a time.

It looks at the processes that turn genomic information into biology: **transcription, translation, epigenetic regulation, protein–protein interaction**. The typical questions are:

- How does expression vary between **cell types** and between **states**?

- What do different genes **do**, and in which **processes** do they take part?

- How are genes **regulated**? Which promoters are active in a given cell?

- How do genes and their products **interact**?

- How does expression change in **disease** and after **treatment**?

**Functional genomics vs classical molecular biology.** Classical molecular biology concentrates on the *single gene*. Functional genomics integrates molecular biology with cell biology and studies the overall structure, function and regulation of a gene **and its relationships with all the other genes**. Its promise is to produce genomic and proteomic knowledge while accounting for the **dynamic** nature of these relationships, giving a more complete picture of how the genome specifies the function of each gene.

**Why it matters now.** With the completion of the **Human Genome Project** (2003; 20th anniversary in 2023) one of the main goals of biomedical research became to understand the function of *every* gene and its contribution to disease. That immediately raises the practical question: **which experimental models do we use?**

## Genomic equivalence: the premise of the discipline

**Principle.** Every somatic cell carries essentially the same genome, the one established in the fertilised egg. Therefore **cell types cannot differ in gene content, only in gene expression**.

- Well-known exception: **T and B cells**, whose antigen-receptor loci are rearranged during maturation.

- The problem this raises: *how can nuclear genes direct development if the genes are the same in every cell type?* The answer (formulated around 1960) is **differential gene expression**: animal development depends on the differential expression of a **constant genome** to produce diverse cell types during embryogenesis.

This was a **claim that had to be demonstrated**. It was demonstrated by **nuclear transfer** experiments, in a sequence of increasingly stringent tests.

### Spemann, 1938 – the "nuclear transfer theory" (newt)

- Spemann tied a fine ligature (a hair loop) around a newt zygote, so that the constriction plane coincided with the **first cleavage plane** (the grey crescent is cut in half).

- The nucleus divides on one side only. After a few cleavages (8→16 blastomeres) one nucleus can slip through the constriction into the previously nucleus-free half, which then develops into a complete embryo.

- ![[FG-image1.png|347]]**Conclusion:** the nuclei of the early cleavage stages are **equivalent** (each can support complete development).

**Type of intervention:** **mechanical micromanipulation of the embryo** (a ligature/constriction with a hair loop). Nothing is taken from another cell and **no genetic modification** is made: the nucleus simply reaches the other half late ("**delayed nucleation**"). It is a natural, intra-embryo version of nuclear transfer; Spemann proposed the real experiment but could not perform it.

### Briggs and King, 1952 (frog)

- The nucleus of an unfertilised egg is inactivated/removed.

- A nucleus from an **embryonic cell** is transplanted into this enucleated oocyte.

- The result is a normal tadpole and frog with all cell types, so the donor nucleus **retained all the original information**.

- Key idea: the egg cytoplasm contains factors that **reactivate genes silenced during differentiation** → **reprogramming**.

![[FG-image2.png|262]]**Type of intervention:** **nuclear transfer (cloning) by micromanipulation**. The recipient egg (*Rana pipiens*) is activated and **enucleated mechanically** (pricked with a glass needle, nucleus removed); a blastula cell is drawn into a micropipette, which breaks its membrane, and the nucleus is **injected** into the egg. **No genetic modification**: the genome is transferred whole and unchanged. This is **cloning, not transgenesis**.

### Gurdon, 1962 (*Xenopus*)

- Same procedure, but the donor nuclei come from **fully differentiated cells** (intestinal epithelium, epidermis).

- Result: tadpoles and adult frogs that are **genetically identical clones**.

- **Conclusion:** even differentiated nuclei still contain the full genome; differentiation is **not** irreversible loss of genes. (Gurdon shared the 2012 Nobel Prize for this.)

**Type of intervention:** **nuclear transfer (cloning)**, as above, but the egg nucleus is **destroyed by UV irradiation** instead of being removed by hand, and the donor nuclei come from **differentiated tadpole intestinal cells**. The donor carried a natural **genetic marker** (the *1-nu* mutation: one nucleolus instead of two) to prove that the clones came from the transplanted nucleus and not from a surviving egg nucleus. Still **no genetic modification**: the marker is a natural mutation, not a transgene.

![[FG-image3.png|532]]

### Wilmut et al., 1997 – Dolly, the first cloned mammal

- **Somatic Cell Nuclear Transfer (SCNT)**: the nucleus of an oocyte is removed and replaced by the nucleus of a somatic cell (here a mammary gland cell of a Finn Dorset ewe); the oocyte donor and the surrogate mother were Scottish Blackface sheep.

- Donor cells were **synchronised** (serum starvation, arrested in **G1**), which makes the nucleus more compatible with the oocyte cytoplasm.

- The reconstructed egg is activated by **electrical pulses**, cultured to morula/blastocyst, then implanted in a surrogate mother → lamb **Dolly**.

- **Efficiency was tiny: about 1 success per 434 oocytes implanted.** Meaning: the genome is unaltered, but reprogramming is hard and inefficient.

**Type of intervention:** **somatic cell nuclear transfer (SCNT) = reproductive cloning**, combined with **cell culture** and **embryo transfer**. Steps: culture of adult mammary cells and **serum starvation** (quiescence); **enucleation** of a metaphase II oocyte; **electrofusion** of donor cell and enucleated oocyte; **electrical activation**; in vitro culture; transfer into a **surrogate mother**. **No genetic modification**: Dolly is a genetic copy of the donor, not a transgenic animal.

![[FG-image4.png|346]]

### Take-home on reprogramming

**The more differentiated the donor cell, the lower its ability to be reprogrammed** (graph of Gurdon & Melton 2008: success of nuclear transfer falls from ~30% with blastula/blastocyst donors to a few % with adult donors, in both *Xenopus* and mammals). So the genome is equivalent, but the *epigenetic state* progressively restricts what a nucleus can do.

**Cloning vs transgenesis.** All four experiments above move a **whole, unchanged genome** into a new cytoplasm (**cloning / nuclear transfer**): they test whether the genome is complete, they do not change it. **Transgenesis** instead **adds, removes or modifies specific DNA sequences** in the genome, including the germline, so the change is **inherited** (e.g. knock-out mice, P-element lines). Intermediate cases in these notes: **RNA/morpholino injection** = transient manipulation, nothing is integrated into the genome; **iPSC reprogramming with retroviruses** = genetic modification of cultured cells, but no transgenic animal.

### Differentiation = differential gene expression

Different differentiation pathways switch different genes on (or off) in different cells. Gene expression can be controlled at **several levels**:

1.  **Transcriptional control** (nucleus: DNA → pre-mRNA)

2.  **RNA processing control** (pre-mRNA → mature mRNA)

3.  **mRNA transport and localisation control** (nucleus → cytosol)

4.  **mRNA degradation control** (functional vs non-functional transcript)

5.  **Translational control**

6.  **Protein activity control** (active vs inactive protein)

---
> [[Functional Genetics|↑ Functional Genetics]] · [[FG 02 - Why function requires perturbation + Forward genetics|Why function requires perturbation + Forward genetics →]]
