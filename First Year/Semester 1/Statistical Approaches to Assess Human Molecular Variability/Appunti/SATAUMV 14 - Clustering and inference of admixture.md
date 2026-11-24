---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 14
tags: [note, sataumv]
---

> [[SATAUMV 13 - Population structure analyses – principal component analysis (PCA)|← Population structure analyses – principal component analysis (PCA)]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 15 - Testing and dating population relationships and admixture|Testing and dating population relationships and admixture →]]

# Clustering and inference of admixture

## 14.1 Discriminant Analysis of Principal Components (DAPC)

**Discriminant Analysis of Principal Components (DAPC)** is a multivariate method designed to **identify and describe clusters of genetically related individuals**. It is a **two-step process**:

- **Principal Component Analysis (PCA)**: the original high-dimensional data are transformed into a smaller set of uncorrelated variables, the principal components, which capture the variation, reduce noise and remove redundancy (section 13.3);
- **Linear Discriminant Analysis (LDA)**: the retained PCs are then subjected to a **discriminant analysis**. Unlike PCA, which summarizes the overall variance of the dataset, LDA **maximizes the separation between pre-defined or inferred groups while minimizing the variation within those groups**.

The **linear discriminants** therefore describe the **largest between-group variance and the smallest within-group variance**, not the entire variance as in PCA. In the figure, individuals (dots) are positioned on a plane using the values of two variables: PCA searches for the direction showing the largest total variance (dotted arrow), whereas DA (plain arrow) maximizes the separation between the clusters (colored groups) while minimizing the variation within each group.

![[SATAUMV-image71.jpg|393]]

DAPC can be used in two ways:

- **when group priors are lacking**, it infers the clusters with **sequential K-means and model selection**: the find.clusters function (adegenet package, R) runs the K-means clustering method sequentially, testing an increasing number of clusters (K). The different clustering solutions are compared with a summary statistic of goodness of fit (by default the **BIC**, Bayesian Information Criterion), and the optimal number of clusters is usually the K that **minimizes the BIC**;
- **to test the robustness of pre-defined groups** (e.g. groups suggested by PCA): the R function dapc(x, grp, ...) computes the discriminant functions and **assigns individuals to clusters**.

> ![[SATAUMV-image72.png|325]]![[SATAUMV-image73.png|332]]

DAPC provides two main outputs:

- a **scatterplot of the discriminant functions**, a visual tool to investigate how distinct the different groups or populations are from one another;
- **membership probabilities** (or assignment probabilities), i.e. the probability for each individual to belong to a specific cluster or population. They can be used to assess **assignment uncertainty** and the **robustness of the groupings**, as indicators of how clear-cut the clusters are.

**Example — Italy** (Sazzini et al. 2016, Sci Rep; section 13.5): DAPC was used to **test the pre-defined groups pointed out by the previous PCA** (Sardinia, northern, central and southern Italy). The membership probabilities to these clusters, calculated via DAPC and averaged per sampling location, are shown as pie charts on the map of Italy.

## 14.2 Admixture and gene flow

When populations meet, two different processes can take place:

- **Gene flow**: ongoing, **bidirectional** exchange of individuals between neighboring populations (chapter 7);
- **Admixture**: **formation of a hybrid population from the mixing of ancestral populations that previously had been relatively isolated from one another** (section 13.6).

> ![[SATAUMV-image74.png|256]]![[SATAUMV-image75.png|279]]

Admixture can be detected, and ancestry profiles inferred, with several approaches. In a **PCA** the admixed population lies between the parental clusters (section 13.6), while **model-based methods** such as **STRUCTURE** and **ADMIXTURE** estimate for each individual the proportion of ancestry derived from each parental population.

## 14.3 Methods based on allele frequency

Consider a **hybrid population (H)** that results from the admixture of **two parental populations (A and B)**. If we know the frequency of a given allele in the ancestral populations (p<sub>A</sub> and p<sub>B</sub>) and in the hybrid population (p<sub>H</sub>), we can estimate the **proportion (M) that ancestral population A contributed to the admixed population**. We assume that the allele frequency in H equals the frequency in A multiplied by the contribution of A (M), plus the frequency in B multiplied by the contribution of B (1 − M):

***p<sub>H</sub> = M·p<sub>A</sub> + (1 − M)·p<sub>B</sub>** → **M = (p<sub>H</sub> − p<sub>B</sub>) / (p<sub>A</sub> − p<sub>B</sub>)***

The figure shows two examples, both giving M = 0.4 (40% contribution from A and 60% from B):

- **population-specific alleles** (p<sub>A</sub> = 0, p<sub>B</sub> = 1.0, p<sub>H</sub> = 0.6): M = (0.6 − 1.0)/(0 − 1.0) = −0.4/−1.0 = 0.4;
- **population-differentiated alleles** (p<sub>A</sub> = 0.2, p<sub>B</sub> = 0.7, p<sub>H</sub> = 0.5): M = (0.5 − 0.7)/(0.2 − 0.7) = −0.2/−0.5 = 0.4.

![[SATAUMV-image76.jpg|506]]

**Assumptions and limitations.** The approach has several complications:

- what if we **do not know** or **misidentify** the possible ancestral populations?
- what happens in case of **complex admixture scenarios** (e.g. more than two ancestral groups)?
- what if an allele in the admixed population is **not found** in either ancestral population, or is present at **similar frequencies** in both (with p<sub>A</sub> ≈ p<sub>B</sub> the denominator of M is close to zero)?
- what are the effects of **other processes** (e.g. **genetic drift** and **selection**) on the allele frequencies of the populations?

The figure illustrates **locus ancestry** in an individual with West African and European ancestry: along the chromosome each segment derives from one of the two parental populations, and at each AIM the observed number of West African alleles (0, 1 or 2) reflects the ancestry of the two chromosome copies at that locus.

Note — AIMs (ancestry-informative markers) are markers with large allele-frequency differences between the parental populations, so that the allele observed at the locus is informative about the population it comes from.

## 14.4 Clustering methods using genome-wide data

**Cluster analyses** group individuals into **K different clusters based on genetic similarity**, i.e. individuals within a cluster are more similar to each other than to individuals in other clusters (section 13.8). There is **no a priori hypothesis**: the algorithm is run several times with different K, and each run gives a **fit of the clusters to the data**.

Each individual is given a **membership coefficient** (probability) for every cluster; the coefficients can also be interpreted as the **fractions of the genome** having membership in those clusters. In the example (populations from Pakistan: Balochi, Brahui, Makrani, Sindhi, Pathan, Burusho, Hazara, Uygur and Kalash) each individual is a vertical bar divided into K = 5 colored segments; the zoom on the Uygur sample (10 individuals) shows how the bar of each individual is split among the five clusters in proportion to its membership coefficients.

![[SATAUMV-image77.png|624]]

## 14.5 ADMIXTURE: model-based estimation of ancestry

**ADMIXTURE** does not simply assign everyone to one population: it estimates the **proportion of ancestry** that can be attributed to each of **K inferred ancestral populations**. Given the genotypes of hundreds or thousands of individuals, the model simultaneously estimates **two sets of parameters**:

- **Q matrix (ancestry fractions)**: the **proportion of ancestry** that each individual *i* **derives from population *k***;
- **F matrix (allele frequencies)**: the **frequency** of a particular allele *j* **within the ancestral population *k***.

The two matrices are linked by the expected allele frequency of each individual:

***p<sub>ij</sub> = Σ<sub>k=1…K</sub> q<sub>ik</sub> · f<sub>kj</sub>***

where p<sub>ij</sub> is the expected frequency of the allele in individual *i* at SNP *j*, q<sub>ik</sub> is the ancestry proportion of individual *i* from population *k*, and f<sub>kj</sub> is the allele frequency at SNP *j* in population *k*. Both the allele frequencies and the ancestry proportions are estimated **directly from the observed genotype data**, answering the question: **which combination of ancestral populations and allele frequencies provides the best statistical explanation of the observed genetic data?**

The software uses a **Maximum Likelihood Estimation (MLE)** approach: it combines the probabilities of all observed genotypes across all individuals and SNPs, and updates the values of Q and F to **increase the likelihood** until reaching **convergence**, i.e. it finds the configuration that makes the observed data the most likely outcome.

Note — in practice ADMIXTURE is run on a PLINK binary dataset (.bed/.bim/.fam, section 9.4), usually LD-pruned (section 11.5), once for each value of K (e.g. admixture --cv data.bed 3). For each K it writes a **.Q** file (the Q matrix) and a **.P** file (the F matrix); with --cv it also reports the cross-validation error used to choose K (section 14.7).

## 14.6 Individual-level resolution of analysis

With genome-wide data, ancestry is estimated **for each individual**.

**The .Q output file.** An ADMIXTURE **.Q file** is a space-delimited text matrix in which **each row corresponds to an individual** and **each column represents the ancestry fraction inherited from a theoretical ancestral population** (K columns). The values in each row **sum to exactly 1**. In the example (K = 3, 5 individuals) the first row, 0.9500 0.0400 0.0100, is drawn as a single bar divided into segments of 95%, 4% and 1%.

In this **structure-like clustering plot** individuals are shown as vertical bars colored in proportion to their estimated ancestry within each cluster.

![[SATAUMV-image78.jpg|566]]

![[SATAUMV-image79.jpeg|271]]

## 14.7 Choosing the number of ancestral populations (K)

A fundamental problem is **deciding the most likely number of clusters**. The K that gives the **best fit** to the data is the best estimate of the true number of clusters. With ADMIXTURE the fit is evaluated with the **cross-validation (CV) error**: the best K has the **lowest CV error** (K = 3 in the example). When several K give similar values, the **smallest value of K** can be assumed to be the best approximation of the true value.

## 14.8 Clustering: trees vs. DAPC vs. ADMIXTURE

The different clustering approaches can be compared on the same dataset. The combined plot of a **dendrogram** of genetic distances (sections 12.7–12.9), **ADMIXTURE** results at K = 2, 3 and 4, and **DAPC** clusters shows the **correspondence of the population structure** detected by the three methods.

## 14.9 Admixture proportions vary among individuals

An estimate of admixture proportions within a population **does not mean that all individuals have the same ancestry ratios**. For example, a population with **M = 0.2 (20%)** (M: average proportion of admixture contribution to a population) can result from five individuals with 20% each, or with 5%, 5%, 25%, 25% and 40%, or 30%, 30%, 40%, 0% and 0%, or 50%, 0%, 0%, 0% and 50%: the average is always 20%. Therefore **population admixture can be determined from individual admixture, but not vice versa**.

The spread of individual proportions may be informative about the time since admixture:

- **recent admixture** → individuals show the **full range of 0–100% of ancestry** (e.g. Mexican Americans, with African, European and Native American ancestry);
- **ancient admixture** → **narrow range of ancestry** among individuals (e.g. Micronesia and Polynesia, between Melanesia (Bougainville) and Taiwan/East Asia).

**Admixture dynamics.** Soon after a population arises from the admixture of previously isolated parental populations (PP1, PP2), the chromosomes of the **descendant admixed individuals** are entirely or almost entirely of a **single ancestry**. Over the generations these chromosomal segments of different ancestries are spliced into smaller pieces by the **recombination process**.

Genetic recombination **breaks ancestral genomes into blocks of different sizes**, so that the genomes of the descendants of an admixture event are composed of different combinations of these ancestral blocks. The **number and width of the admixture blocks** contain information about the **time since admixture**: more recombination events result in a greater number of blocks, which with time get **progressively narrower** and **more evenly distributed** along and among chromosomes (chapter 15).

Note — after admixture, recombination and mating within the admixed population redistribute the ancestral segments generation after generation, so individual proportions converge towards the population average: this is why ancient admixture leaves a narrow range of ancestry (see also section 13.6).

---
> [[SATAUMV 13 - Population structure analyses – principal component analysis (PCA)|← Population structure analyses – principal component analysis (PCA)]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 15 - Testing and dating population relationships and admixture|Testing and dating population relationships and admixture →]]
