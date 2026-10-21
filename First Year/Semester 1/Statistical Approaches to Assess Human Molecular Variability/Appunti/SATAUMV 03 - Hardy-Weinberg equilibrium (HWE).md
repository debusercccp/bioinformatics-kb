---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 3
tags: [note, sataumv]
---

> [[SATAUMV 02 - Key concepts in population genetics|← Key concepts in population genetics]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 04 - Generating diversity – mutation|Generating diversity – mutation →]]

# Hardy-Weinberg equilibrium (HWE)

## 3.1 The principle

One of the first major applications of population genetics was to explain how allele frequencies in one generation can be used to **predict genotype proportions in the next one**. In a diploid species with two alleles **A** and **a** at the same locus, with frequencies **p** and **q** in the population, gametes combine at random into three genotypes.

|                   | **Female gamete A (p)** | **Female gamete a (q)** |
|:------------------|:------------------------|:------------------------|
| Male gamete A (p) | AA (p²)                 | Aa (pq)                 |
| Male gamete a (q) | Aa (pq)                 | aa (q²)                 |

**AA = p², Aa = 2pq, aa = q²**

*(and p + q = 1, so p² + 2pq + q² = 1)*

The two heterozygote combinations (Aa and aA) are indistinguishable, hence the factor 2 in 2pq. The theorem is credited to Wilhelm Weinberg (1862–1937) and Godfrey Harold Hardy (1877–1947).

## 3.2 Equilibrium over generations

If the genotype proportions in the offspring generation (F1) are the same as in the parental generation (F0), observed frequencies equal expected frequencies (p₀², 2p₀q₀, q₀² in F0 and p₁², 2p₁q₁, q₁² in F1). This implies:

**p₀ = p₁ and q₀ = q₁**

The population is in **Hardy-Weinberg equilibrium**: there are **no changes in allele frequencies**, i.e. **no evolution**.

**Check with the slide data.** With p = 0.6 and q = 0.4: p² = 0.36, 2pq = 2 × 0.6 × 0.4 = 0.48, q² = 0.16. These match exactly the observed genotype frequencies (0.36, 0.48, 0.16), so the 150-individual population is in HWE.

## 3.3 Assumptions and factors that violate HWE

By comparing the genetic composition of a **real population** with HWE expectations we can identify **deviations**, which point to the **evolutionary forces** and biological processes acting on genetic variation. (The statistical test for such a comparison, usually a chi-square test of observed against expected genotype counts, is not on the slides; for the example above the chi-square would be 0 because observed and expected counts coincide.)

![[SATAUMV-image3.jpg|559]]

## Collegamenti
- [[MBD 15 - Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem]] — richiami di probabilità

---
> [[SATAUMV 02 - Key concepts in population genetics|← Key concepts in population genetics]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 04 - Generating diversity – mutation|Generating diversity – mutation →]]
