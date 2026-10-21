---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 2
tags: [note, fg]
---

> [[FG 01 - What is functional genomics + Genomic equivalence – the premise of the discipline|← What is functional genomics + Genomic equivalence – the premise of the discipline]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 03 - Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele)|Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele) →]]

# Why function requires perturbation

- **Expression tells you where a gene is on. Only perturbation tells you what it does.**

- **Function = the set of phenotypes produced when gene activity is altered.**

Expression data (e.g. an in situ pattern) is correlative; to attribute a role we must change gene activity and observe the phenotype.

**Genetic control of development – the questions:** Which genes control development? Where and when are they active? How are they regulated? Through what mechanisms do they direct development? And, above all, **how can we find the genes that guide development?**

Two logics, running in opposite directions between phenotype and genotype:

- **Forward genetics: phenotype → genotype (gene)**

- **Reverse genetics: genotype (gene) → phenotype**

## Forward genetics

**Idea:** start from a **biological process** or phenotype of interest and find the gene(s) responsible. It is a **non-directed, mutation-driven** method. Because it screens phenotypes rather than being driven by a known disease mutation, it is very useful to find *new* genes and pathways (e.g. human diseases).

**Workflow**

1.  **Select a biological process.**

2.  **Mutagenesis screen** – a laboratory procedure used to obtain mutant organisms.

3.  **Isolation of mutants** defective in that process: define the assay, screen for the phenotype. Mutants can then be characterized by **allelic series, genetic mosaics, epistasis tests**.

4.  **Map and clone** the mutated gene → identify the gene, the **molecular lesion** and the **biochemical function**.

5.  **Understanding of the biological process.**

**What mutagenesis is.** Mutagenesis = exposing an organism to an agent (a **mutagen**) that raises the mutation rate far above the spontaneous one. Spontaneous mutations are too rare to find a mutant for a given process in reasonable time; with **EMS** in *C. elegans* you get roughly **one loss-of-function hit per gene every ~2,000 mutagenised genomes**, so screening a few thousand animals hits most genes at least once. Key rule: **the mutagen decides the type of lesion**, and therefore which kind of allele the screen can recover.

**Mutagens – the mutagen decides what the screen can recover**

| Type | Examples | What it produces |
|:---|:---|:---|
| Physical | X-rays | Large **deletions, translocations**, often affecting several genes at once |
| Chemical | EMS, ENU (N-ethyl-N-nitrosourea) | **Point mutations**; can give an **allelic series** (different alleles of the same gene with different strengths) |
| Insertional / biological | Transposons, viral vectors | Fewer events, but the insertion **tags** the gene, making it easy to clone |

**In practice.** **X-rays** → deletions and rearrangements, useful to make deficiencies and balancer-like chromosomes, poor for studying a single gene. **EMS/ENU** → point mutations, hence an **allelic series** (null, hypomorph, sometimes antimorph): what Müller's classification needs. **Insertions** → fewer events, but the gene is **tagged** by a known sequence, so cloning it is fast.

**Pitfalls**

- *You get what you are screening for*: the result depends on how good and specific the assay is.

- *You will miss redundant genes* (another gene compensates, so no phenotype) *and essential genes* (the mutant dies too early to be scored).

### Essential genes

Essential genes are required for sustaining life.

- In **single-celled organisms or single cells** derived from multicellular ones: genes needed for proliferation of individual cells (**cellular gene essentiality**).

- In **multicellular organisms**: genes needed for growth and development from a zygote to a fertile adult, or for reproduction (**organismal gene essentiality**).

- A core set of essential genes shows a **stringently lethal phenotype** upon loss (cell death).

**Conditionally essential genes =\>** Their necessity depends on a specific **environmental condition, developmental stage or tissue**. Mutants may show **no obvious phenotype under optimal laboratory conditions**. Examples: immune system genes (become essential on infection), stress responses, growth with limited nutrients. Many genes may be conditionally essential but the *condition* is simply unknown.

**Key concept:** gene essentiality is **not an absolute and static property** of a gene. It depends on the environment and on the genetic context, and on how function is measured. To test whether a gene is essential you need a **null** mutation.

---
> [[FG 01 - What is functional genomics + Genomic equivalence – the premise of the discipline|← What is functional genomics + Genomic equivalence – the premise of the discipline]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 03 - Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele)|Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele) →]]
