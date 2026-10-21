---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 3
tags: [note, fg]
---

> [[FG 02 - Why function requires perturbation + Forward genetics|← Why function requires perturbation + Forward genetics]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 04 - Effects of mutations on gene function – Müller's classification|Effects of mutations on gene function – Müller's classification →]]

# Reverse genetics

**Idea:** start from a **gene of interest** (directed, often disease-driven) and ask what happens when it is mutated.

**Workflow**

1.  **Select a gene** of interest.

2.  **Target it for mutation.** Experimental design choices: transient vs stable; knock-down / knock-in / specific mutations; **RNAi**; **CRISPR/Cas9**.

3.  **Analyse the mutant phenotype** and **infer the function** of the gene product.

4.  **Understanding of the biological process.**

**Tools of reverse genetics:** transgenesis by gene addition, single-gene knock-outs and knock-ins, conditional gene modifications, chromosomal rearrangements, genome editing.

**Pitfalls:** it will miss **redundant** or **conditionally required** genes (same limits as forward genetics).

### Forward vs reverse – summary

|  | Forward | Reverse |
|:---|:---|:---|
| Starting point | Phenotype / process | Gene |
| Direction | phenotype → gene | gene → phenotype |
| Nature | Non-directed, mutation-driven | Directed, often disease-driven |
| Strength | Unbiased discovery of new genes | Precise, hypothesis-driven |
| Weakness | Misses redundant/essential genes | Misses redundant/conditional genes |

**Today the forward/reverse categorization no longer strictly holds**: full genome sequences plus genome-manipulation approaches (e.g. CRISPR screens) blend the two into innovative genetic approaches. Both routes converge on the same goal: understanding the biological process.

## Gene mutation: molecular consequences ("what is the nature of the allele?")

### Types of DNA change

- **Base-pair substitutions**

  - **Transitions**: purine ↔ purine (A↔G) or pyrimidine ↔ pyrimidine (C↔T).

  - **Transversions**: purine ↔ pyrimidine (or vice versa).

- **Insertions**: addition of one or more base pairs.

- **Deletions**: removal of one or more base pairs.

- **Inversions**: a DNA segment is excised and re-inserted in the same place in reverse orientation.

- **Translocations**: a segment breaks off one chromosome and attaches to the same or another chromosome.

- **Duplications**: part of a chromosome present in two or more copies.

### Effect on the coding sequence

**Point mutations**

- **Silent**: the codon changes but the amino acid does not – no change in protein.

- **Nonsense**: a codon becomes a **STOP** (e.g. AAG → TAG), giving a truncated protein.

- **Missense**: one amino acid is replaced by another.

  - **Conservative**: similar amino acid with similar chemical properties (Arg → Lys, via AGA → AAA), mild effect.

  - **Non-conservative**: very different amino acid (Arg → Ile, via AGA → ATA), more likely to damage function.

**Frameshift** (insertion or deletion of a number of bases not divisible by 3 in a coding region): the reading frame shifts, so **every codon downstream changes** and a premature stop is usually met. Example from the slide: AAG AGA GGT (Lys Arg Gly) becomes Glu Glu Arg… after insertion of a G, or Arg Glu Val… after deletion of an A.

---
> [[FG 02 - Why function requires perturbation + Forward genetics|← Why function requires perturbation + Forward genetics]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 04 - Effects of mutations on gene function – Müller's classification|Effects of mutations on gene function – Müller's classification →]]
