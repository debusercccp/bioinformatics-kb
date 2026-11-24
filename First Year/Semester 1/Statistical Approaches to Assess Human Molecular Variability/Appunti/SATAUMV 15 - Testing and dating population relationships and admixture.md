---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 15
tags: [note, sataumv]
---

> [[SATAUMV 14 - Clustering and inference of admixture|← Clustering and inference of admixture]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 16 - Haplotype-based analyses|Haplotype-based analyses →]]

# Testing and dating population relationships and admixture

## 15.1 Formal tests of population relatedness and admixture: F-statistics

The **F-statistics** are a family of **allele-sharing statistics**:

- mathematical tools used in population genomics to **test hypotheses about population relationships**: test population splits, detect **admixture** and infer relationships involving multiple populations;
- they can compare **individual genomes** allele by allele, or **groups of genomes** (i.e. populations) by allele frequency, for a set of SNVs;
- they are **computationally simple** and **statistically robust**.

They compare the **observed** allele sharing with what is **expected** **if the populations are related by a simple tree** (three populations for the f3-statistics, four for the f4-statistics). The one used to test for admixture is the **admixture f3-statistic**.

## 15.2 Admixture f3-statistics: the 3-population test

The **f3-statistic**, also known as the **3-population test**, is a **formal test of admixture**. It can provide clear evidence of admixture even if the gene-flow events occurred **hundreds of generations ago**. It compares three populations and tests their relationship in terms of **treeness**.

**Question:** given three populations A, B and C, is their relationship compatible with a simple tree? In other words, do the observed frequencies of genetic markers agree with a tree-like structure or not?

- **Null hypothesis (H0)**: the relationship reflects a **tree-like structure** (good “treeness”);
- **Alternative hypothesis (H1)**: the relationship between the three populations is best described by an **admixture event**, where C is the result of the admixture between A and B.

![[SATAUMV-image80.png|176]]In the trees on the slide: under **H0**, B and C are sister populations and A is the outgroup, so C descends from a single branch of the tree; under **H1**, C receives ancestry from **two branches**, one related to B and one related to A, so C is a **mixture** of the two lineages and cannot be placed on a single branch.

The test is commonly used in the form **f3(C; A, B)**, where **C** is the putative **admixed/hybrid population** and **A** and **B** are the putative **source populations**. Mathematically, f3 is the **product of the differences in allele frequency between population C and A and between C and B**, averaged over all genotyped sites:

***f3(C; A, B) = (1/J) · Σ<sub>j=1…J</sub> (c<sub>j</sub> − a<sub>j</sub>) · (c<sub>j</sub> − b<sub>j</sub>)***

where a<sub>j</sub>, b<sub>j</sub> and c<sub>j</sub> are the **allele frequencies of marker *j*** in populations A, B and C, **and J is the number of markers**. Intuitively, if the allele frequency of the target population C is **on average intermediate** between those of A and B, the two differences have opposite signs and **f3 becomes negative**. Extreme example: at a site where a = 0, b = 1 and c = 0.5, (c − a)(c − b) = 0.5 × (−0.5) = −0.25.

Interpretation:

- for a simple **tree-like relationship (H0)**, f3(C; A, B) is expected to be **positive**;
- if f3(C; A, B) has a **negative** mean, C is **admixed** from populations close to A and B (**H1**).

The test also computes a **Z-score**, the number of standard deviations by which the estimated statistic differs from 0; in **ADMIXTOOLS** the Z-score acts as a **statistical significance test**. If **f3 is negative and Z \< −3**, there is a strong departure from the null hypothesis (zero), and we can say that there is a **statistically significant signal for C resulting from the mixture of populations A and B**.

Note — the sources A and B do not need to be the true ancestral populations, only populations related to them (“populations close to A and B”). A positive f3 does not exclude admixture: strong genetic drift in C after the admixture event (e.g. a bottleneck) can mask the negative signal. In practice the test is run with qp3Pop (ADMIXTOOLS) or the R package admixtools.

## 15.3 Formal tests for dating admixture: admixture-induced LD

![[SATAUMV-image81.png|255]]When two ancestral populations, A and B, contribute to a new admixed population H, **admixture generates LD between loci with different allele frequencies in the parental populations**, even for loci that are distant or unlinked (i.e. that segregate independently or reside on different chromosomes) in the original populations:

- **immediately after admixture**, alleles inherited from population A tend to occur together on ancestry segments originating from A (**linked by ancestry**), and the same applies to alleles originating from B. This creates **admixture-induced LD**;
- over subsequent generations, **recombination** progressively breaks down these associations, so the signal **decays over generations** (section 5.6).

**LD decay** can therefore be used as a proxy to estimate the **time since the admixture event**: the older the admixture, the more time recombination has had to break the linkage.

The diagram follows the chromosomes through time:

- **ancestral populations A and B**: each carries its own set of variants, both linked (on the same chromosome) and unlinked;
- **first-generation hybrids**: each chromosome comes entirely from A or entirely from B, so all the alleles of A are **linked by ancestry**, even those that are unlinked in the parental populations;
- **after few generations**: recombination produces chromosomes made of a few long segments of A and B ancestry;
- **after many generations**: more recombination produces many short segments, and the admixture-induced LD between distant loci is lost.

## 15.4 Estimating the date of admixture: ALDER

The **ALDER** software (Loh et al. 2013) is based on the computation of **weighted linkage disequilibrium (LD) curves**, which can be used to infer admixture parameters including the **dates of admixture**. The method works in four steps:

- **calculate weighted LD**: LD scores are computed between pairs of SNPs (*i* and *j*) in the target admixed population, weighting each value by the allele-frequency differences between the reference populations: **D<sub>ij</sub> × (p<sub>A,i</sub> − p<sub>B,i</sub>) × (p<sub>A,j</sub> − p<sub>B,j</sub>)**;
- **group pairs of SNPs by genetic distance**: the weighted LD values are summarized across bins of genetic distance (cM), giving a curve of weighted LD against distance;
- **fit an exponential decay curve** to the observed weighted LD decay: **y = a · e^(−b·x)**, where y is the weighted LD signal, a the initial magnitude of the admixture-related LD signal, e the exponential function (Euler’s number), b the decay rate (related to the time since admixture) and x the genetic distance between SNPs in cM;
- **estimate the admixture time**: the decay rate (b, written β on the slide) of admixture LD as a function of genetic distance is **converted into the number of generations since admixture**.

In the example on the slide, the weighted LD curve of an admixed population, using Mbuti and San–Yoruba as reference populations, decays with genetic distance (0–50 cM), and the exponential fit gives **30 ± 3 generations** since admixture.

Note — LD between two sites at distance d (in Morgans) decays by a factor (1 − d) per generation, i.e. about e^(−t·d) after t generations. So, with x in Morgans, the fitted decay rate is directly the number of generations t; with x in cM, t = 100 × b. Multiplying by a generation time (often 25–30 years) gives the date in years.

Caveat on dating: **if admixture is continuous or occurred multiple times**, the LD-based methods date **only the most recent event**.

## 15.6 Admixture in genomics

The study of admixture is used to:

- **reconstruct the demographic history** of populations, e.g. infer and date past processes of migration and admixture;
- **identify specific chromosomal segments** (local ancestry) that may be useful in studying **natural selection** or in pinpointing population variants, including those influencing **traits and disease susceptibility**.

The admixture-induced LD (D<sub>t</sub>) decays with the generations since admixture, faster for higher recombination fractions r (from r = 0, no decay, to r = 0.5, unlinked loci); and in an admixed population formed from two ancestral populations after n generations, we can estimate both the **global ancestry** (the proportion of each ancestry in an individual’s genome) and the **local ancestry** (the ancestry of each chromosomal segment).

---
> [[SATAUMV 14 - Clustering and inference of admixture|← Clustering and inference of admixture]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 16 - Haplotype-based analyses|Haplotype-based analyses →]]
