---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 6
tags: [note, sataumv]
---

> [[SATAUMV 05 - Generating diversity – recombination|← Generating diversity – recombination]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 07 - Shaping diversity – gene flow|Shaping diversity – gene flow →]]

# Eliminating diversity: genetic drift

No population is infinitely large as assumed under HWE: each generation is a *finite sample* drawn from the previous one. **Genetic drift** is the variation in allele frequencies over generations that occurs solely through **stochastic sampling**.

## 6.1 Overall effects of genetic drift

- The magnitude of genetic drift is related to **population size**: in small populations an allele is **rapidly fixed or lost**, while in large populations both alleles persist with more **subtle frequency variations**.
- The slide simulates two populations of **N = 20 and N = 1000** followed for 100 generations starting from an allele frequency of 0.5: the smaller the population size, the greater the drift.
- The overall effect of genetic drift on genetic variation is to progressively **reduce within-population variability** while **increasing differences among groups**.

![[SATAUMV-image10.png|528]]

## 6.2 Wright-Fisher model and effective population size

The **Wright-Fisher model** is the **theoretical framework** for understanding the dynamics of allele-frequency change under genetic drift and for quantifying its effects. It assumes:

- constant population size;
- random mating;
- non-overlapping generations.

The model contains many *unrealistic assumptions*, because these factors vary among populations. To compare the amount of drift experienced by different populations, Wright introduced the concept of **effective population size** (**N<sub>e</sub>**): the size of an idealized population that would experience the same amount of drift as the studied population.

N<sub>e</sub> is a basic parameter for many population-genetics models and is usually **smaller than** the absolute (census) population size N. Few populations are constant in size over many generations: the long-term N<sub>e</sub> equals the **harmonic mean** of population size over time (the reciprocal of the mean of the reciprocals), so N<sub>e</sub> stays close to the **smallest N**. For most of our past evolutionary history human populations had very small sizes, and *H. sapiens* expanded only recently; this is why N<sub>e</sub> is much smaller than N.

## 6.3 Bottleneck and founder effects

Present-day variation depends on **past small population sizes**. Two population processes shape genetic diversity by reducing the ancestral N<sub>e</sub> and causing a **loss of genetic diversity**:

- **Bottleneck effect:** more than 50% of a population is **killed or prevented from reproducing**, and the survivors carry only part of the original diversity.
- **Founder effect:** related to the process of **colonization**; a subset of individuals separates from the source population, carrying only a **subset of its diversity**.

![[SATAUMV-image11.png|535]]

## 6.4 Population subdivision

A **metapopulation** may not be randomly mating because it is made up of **partially isolated** populations (**demes**).

- Isolation leads to **genetic differentiation** of demes, because **drift acts independently** on each of them.
- Members of the **same deme** are more **closely related** than to members of different demes.
- Demes are not completely isolated: the **exchange of reproducing migrants** reduces differentiation.

## 6.5 Measures of population structure: F<sub>ST</sub>

F<sub>ST</sub> measures the **apportionment of variation between demes** by comparing the mean diversity of **demes** with the diversity of the **metapopulation**. It is the **proportion of genetic diversity** that is due to **allele frequency differences among subpopulations**:

*F<sub>ST</sub> = (H<sub>T</sub> − H<sub>S</sub>) / H<sub>T</sub>*

H<sub>T</sub> is the expected heterozygosity of the metapopulation and H<sub>S</sub> is the mean expected heterozygosity across demes. F<sub>ST</sub> lies between 0 and 1: F<sub>ST</sub> ≈ 0 means **little differentiation** (high gene flow), while F<sub>ST</sub> ≈ 1 means **high differentiation** (H<sub>T</sub> much larger than the diversity within demes).

Consider a locus with two alleles **A** and **a** with the following frequencies in three subpopulations:

| **Subpopulation** | **p** | **q** | **H = 2pq** |
|:------------------|:------|:------|:------------|
| S1                | 0.60  | 0.40  | 0.4800      |
| S2                | 0.52  | 0.48  | 0.4992      |
| S3                | 0.50  | 0.50  | 0.5000      |

The mean expected heterozygosity across demes is H<sub>S</sub> = (0.4800 + 0.4992 + 0.5000)/3 = **0.4931**. The mean allele frequencies p = (0.60 + 0.52 + 0.50)/3 = 0.54 and q = (0.40 + 0.48 + 0.50)/3 = 0.46 give H<sub>T</sub> = 2pq = 2 × 0.54 × 0.46 = **0.4968**, hence F<sub>ST</sub> = (0.4968 − 0.4931)/0.4968 = **0.0074**, i.e. very little differentiation among the three subpopulations.

## 6.6 Mating choice

**Non-random mating** mainly results from assortative mating and inbreeding:

- **Assortative mating:** choice of the partner on the basis of **shared phenotypic features**. Main effects: it generates at a locus a **lower heterozygote frequency** than expected under random mating, and it **augments genetic drift** by decreasing the effective population size.
- **Inbreeding:** **mating of relatives**. Main effects: it increases the frequency of **homozygous genotypes** with respect to random mating; unlike assortative/disassortative mating, which may affect only some genes, it **affects the whole genome**.

The **coefficient of consanguinity (F)** is the probability that two homologous alleles are **identical by descent** (IBD), i.e. inherited from a **common ancestor**, as opposed to **identity by state** (IBS), in which the alleles are the same due to **independent mutations**.

![[SATAUMV-image12.png|371]]

---
> [[SATAUMV 05 - Generating diversity – recombination|← Generating diversity – recombination]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 07 - Shaping diversity – gene flow|Shaping diversity – gene flow →]]
