---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 4
tags: [note, sataumv]
---

> [[SATAUMV 03 - Hardy-Weinberg equilibrium (HWE)|← Hardy-Weinberg equilibrium (HWE)]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 05 - Generating diversity – recombination|Generating diversity – recombination →]]

# Generating diversity: mutation

## 4.1 General features

- Mutation is the **sole process that generates new alleles**, providing the raw material on which the other evolutionary forces act.
- A mutation is any change in the DNA of a single cell, but **evolutionary consequences arise only from changes in the germ line**. Somatic mutations affect only the individual.
- Sources of mutation: **endogenous** (replication errors, metabolic free radicals) and **exogenous** (low-energy ionizing radiation such as an alpha-emitter, high-energy ionizing radiation such as gamma rays, chemical mutagens, low-energy radiation such as UV, which mainly causes somatic mutations).
- Thanks to the accuracy of **DNA polymerases** and **DNA repair**, germ-line mutations occur at **very low rates**. However, given the huge size of the human genome, they are **inevitable in every replication cycle**.

## 4.2 Mutation rate by class of variant

The mutation rate **μ** differs enormously among variant classes (ordered here from fastest to slowest, with the approximate order of magnitude shown on the slide scale):

| **Variant class** | **Approximate rate (per locus per generation)** |
|:---|:---|
| Some expanded pathogenic microsatellites | Close to 10⁰ to 10⁻¹ |
| Minisatellites | About 10⁻¹ to 10⁻² |
| Microsatellites | About 10⁻³ |
| Structural variants including copy-number variants | About 10⁻⁴ to 10⁻⁶ |
| Base substitutions (SNPs) | About 10⁻⁸ to 10⁻⁹ |
| Retroelement insertions | About 10⁻¹⁰ to 10⁻¹¹ |

## 4.3 Properties of SNPs for evolutionary studies

- The mutation rate of base substitutions is low (10⁻⁸–10⁻⁹ per locus per generation), so **recurrent and back mutations are unlikely**. Independent occurrences are not usually found at appreciable frequencies.
- Hence SNPs generally show **identity-by-descent**: the same base at a SNP in two independent genomes usually implies **inheritance from a common ancestor**. This is different from **identity-by-state**, where two independent mutations produce the same base (shown on the slide as two separate T→C events).
- The **direction of evolutionary change** can generally be established, i.e. the **ancestral** and **derived** state can be identified. Example from the slides: orangutan, gorilla and chimpanzee all carry T (ancestral state, coded 0), while the human lineage carries C (derived state, coded 1).
- Base substitutions are also known as **binary / biallelic polymorphisms** or **unique event polymorphisms (UEPs)**.

## 4.4 Mutational models

**Infinite-allele model** (Crow and Kimura, 1970): each mutation creates a new allele. The frequency of the original allele after *t* generations is:

*P<sub>t</sub> = P<sub>0</sub> · e<sup>−μt</sup>*

At low mutation rates, **mutation pressure** (the change in allele frequencies caused by the occurrence of mutations over generations) is a **slow force** that has an appreciable impact only over long time scales. The slide gives the example of a fixed nucleotide (P₀ = 1) with a rate of 2 × 10⁻⁹ per generation whose frequency drops from 1.0 to 0.998 after 1000 generations.

*Note on the slide example:* inserting those numbers in the formula gives e<sup>−2×10⁻⁹×1000</sup> ≈ 0.999998, not 0.998. A value of 0.998 would correspond to μ = 2 × 10⁻⁶ (mutation pressure is still very slow).

**Infinite-site model:** each mutation occurs at a different site, so a nucleotide cannot be hit by more than one mutation. It discounts the possibility of **back mutations** and **recurrent mutations**.

**Finite-site model:** real DNA sequences have a **finite length** and show **mutational hot-spots**, so mutations can occur several times at the same site. More complex models are needed because several changes may have occurred in the same position. Ignoring this leads to **underestimating** the real number of mutations. The simplest estimate, the p-distance, is:

*p-distance = number of substitutions / number of sites*

The slide table compares observed with actual substitutions (sequence 1 versus sequence 2):

| **Type of substitution** | **Sequence 1** | **Sequence 2** | **Observed** | **Actual** |
|:---|:---|:---|:---|:---|
| Unique | C | C → A | 1 | 1 |
| Multiple | A | A → C → T | 1 | 2 |
| Coincidental at the same site | C → A | C → G | 1 | 2 |
| Parallel | T → A | T → A | 0 | 2 |
| Convergent | C → T → A | C → A | 0 | 3 |
| Reverse | C → T → C | C | 0 | 2 |

**Nucleotide substitution models**, from simplest to most general:

- **Jukes-Cantor (1969):** all substitutions occur at the same rate.
- **Kimura 2-parameter (1980):** distinguishes transitions from transversions.
- **Felsenstein (1981):** allows unequal base frequencies.
- **Hasegawa, Kishino and Yano, HKY (1985):** combines unequal base frequencies with different transition and transversion rates.
- **General time-reversible model (GTR):** the most general; separate rate parameters for each pair of nucleotides, plus the frequency π of each nucleotide in the sequence.

---
> [[SATAUMV 03 - Hardy-Weinberg equilibrium (HWE)|← Hardy-Weinberg equilibrium (HWE)]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 05 - Generating diversity – recombination|Generating diversity – recombination →]]
