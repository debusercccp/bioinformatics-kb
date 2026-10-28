---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 12
tags: [note, sataumv]
---

> [[SATAUMV 11 - Post-processing quality controls, dataset assembly, imputation and phasing|← Post-processing quality controls, dataset assembly, imputation and phasing]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 13 - Summary of the main points|Summary of the main points →]]

# Summary statistics and genetic distances

## 12.1 Describing and making inferences from patterns of genetic variation

Methods for studying human population genomic variation rely on **genome-wide data**: WGS, SNP arrays or other high-throughput technologies are used to assess variation across the entire genome. These methods address several related questions:

- **Measures of genetic diversity**: how much variation exists within and between populations, and how it is distributed;
- **Patterns of genetic variation**: evolutionary forces (genetic drift, gene flow, natural selection) leave different signals on the patterns of genetic variation;
- **Methods for inferring demographic history**: reconstruct past population sizes, bottlenecks, expansions, migrations and admixtures;
- **Methods for testing natural selection**: find genes and pathways involved in adaptation to environments;
- **Health relevance**: investigate variants influencing traits, including those potentially linked to disease susceptibility, in different populations.

There are two main goals: the **description of the distribution of present diversity** and **inferences about how diversity evolved**. Moving from single locus-based analyses to the exploration of genome-scale data gives a more exhaustive picture of the actual amount of variation.

These two goals correspond to two complementary families of methods, descriptive and inferential, which differ in what they aim to achieve and in how they treat the data:

- **Descriptive methods summarize** the genetic variation observed in the sample without assuming an explicit model of how it was generated. They answer the question "what does the variation look like?" and include **summary statistics** of intra-population diversity (e.g. heterozygosity, nucleotide diversity, haplotype diversity), measures of inter-population differentiation such as **FST** and **genetic distance matrices**, and exploratory representations such as **trees** (UPGMA, NJ) and **MDS** plots. Their results are direct and largely model-free, but they do not by themselves explain the causes of the observed patterns;
- **Inferential methods** use the observed data to draw conclusions about unobserved processes and parameters, such as past population sizes, divergence times, migration rates, admixture events or the action of natural selection. They rely on an **explicit population-genetic model** (e.g. Wright-Fisher, coalescent), estimate its parameters and test hypotheses by **comparing the observed data with the expectations under the model**, usually with a measure of uncertainty (confidence intervals, p-values, likelihoods). They answer the question "how and why did the variation arise?".

In practice, the two approaches are used in sequence: descriptive analyses **reveal patterns** and **generate hypotheses**, which inferential methods then formally **test** against models of demographic and selective history.

## 12.2 Summary statistics of intra-population variability

**Summary statistics** describe the amount of variability observed within a given sample. They are useful to intuitively compare populations or loci (for example, boxplots of nucleotide diversity, average number of nucleotide differences and haplotype diversity across five populations), but with two caveats:

- they **summarize** the amount of variation, so part of the information contained in the data is **lost**;
- **different processes may lead to comparable values** (for example, both a bottleneck and a selective sweep reduce diversity), so the same value can have different explanations.

![[SATAUMV-image46.png|548]]

The two simplest statistics are:

- **Number of segregating sites (S)**: the number of polymorphic (variable) nucleotide sites present in a population sample;
- **Number of haplotypes (k)**: the number of unique allelic combinations observed at a genomic region in a population. It does not necessarily correspond to the number of individuals, since multiple individuals may share the same haplotype.

![[SATAUMV-image47.png|415]]

In the example, six sequences of 16 nucleotides differ at three positions (4, 12 and 15), so **S = 3**. The alleles at these sites form three distinct combinations — AGT (2 sequences), GTA (3 sequences) and AGA (1 sequence) — so **k = 3**. Both S and k are **highly dependent on sample and sequence size**: the more (and the longer) the sequences analysed, the more segregating sites and haplotypes are found, so they cannot be compared directly between samples of different size.

## 12.3 Nucleotide diversity and gene (haplotype) diversity

**Nucleotide diversity (π)** is the probability that two copies of the same nucleotide, chosen at random from a set of sequences, are **different**. Equivalently, it is the **average number of nucleotide differences per site** between two randomly chosen sequences (the proportion of nucleotide sites where they differ). It is **normalized** with respect to **the number of individuals**:

*π = n/(n − 1) × Σᵢⱼ xᵢ xⱼ dᵢⱼ*

where the sum runs over all pairs of sequences i, j (from 1 to q, the number of sequences), **xᵢ** and **xⱼ** are the **frequencies of sequences** i and j, and **dᵢⱼ** is the number of **nucleotide differences** per site between sequences i and j. The factor **n/(n − 1)** corrects for sample size (n).

**Gene (Nei) diversity** is the probability that two **alleles** (or haplotypes) chosen at random from the population are **different**, i.e. the expected heterozygosity. When it is computed on haplotypes it is called **haplotype diversity**:

*h = n/(n − 1) × (1 − Σᵢ pᵢ²)*

where **k** is the total number of alleles/haplotypes (the sum runs from i = 1 to k) and **pᵢ** is the frequency of the i-th allele/haplotype in the sample; again, n/(n − 1) corrects for sample size.

Worked example with the six sequences of section 12.2 (n = 6, L = 16 sites; haplotype frequencies AGT = 1/3, GTA = 1/2, AGA = 1/6):

| **Statistic** | **Calculation** | **Result** |
|----|----|----|
| Pairwise differences | AGT vs. GTA = 3; AGT vs. AGA = 1; GTA vs. AGA = 2 | — |
| Mean number of differences | n/(n − 1) × Σ xᵢxⱼdᵢⱼ = 6/5 × 2 × (1/3·1/2·3 + 1/3·1/6·1 + 1/2·1/6·2) = 6/5 × 1.444 | 1.733 |
| Nucleotide diversity π (per site) | 1.733 / 16 | ≈ 0.108 |
| Haplotype diversity h | 6/5 × (1 − (1/9 + 1/4 + 1/36)) = 6/5 × 0.611 | ≈ 0.733 |

![[SATAUMV-image48.png|245]]The same value (1.733) is obtained by averaging the differences over all 15 pairs of sequences: (6 × 3 + 2 × 1 + 3 × 2) / 15 = 26/15.

In real data, nucleotide diversity is highest in African samples (YRI, LWK: about 0.0009), lower in Europeans (CEU, TSI: about 0.0007) and lowest in East Asians (CHB, CHD, JPT: about 0.00065). Likewise, genome-wide haplotype heterozygosity **declines with distance from East Africa** (Addis Ababa), from about 0.8 in Africa to below 0.5–0.6 in the Americas: this is the signature of the **serial founder effects** of the Out-of-Africa expansion (chapter 1).

## 12.4 Genome-wide estimation: sliding windows

Summary statistics can be estimated at the **genomic level** using a **sliding windows approach**: the statistic is computed within a window of fixed size (e.g. **window size 100 kbp**), then the window is shifted along the genome by a fixed **step size** (e.g. **10 kbp**), so that consecutive windows overlap, and the calculation is repeated until the whole genome is covered.

![[SATAUMV-image49.png|604]]

In the example, a genome-wide scan of nucleotide diversity (windows of 100 kbp, step of 10 kbp) is shown for **two sub-populations** (red and green); horizontal dashed lines are the **mean** pairwise nucleotide diversity of each sub-population, and vertical dashed lines are chromosome **boundaries**.

The **genome-wide distributions** of these statistics serve as an **empirical baseline** against which to evaluate regions with **reduced or higher levels of diversity**: for example, windows with unusually low diversity may point to a selective sweep, and windows with unusually high diversity to balancing selection (chapter 8).

## 12.5 Measures of inter-population differences: distance matrices

A **distance matrix** is a summary table that shows the **pairwise differences between a set of N points, objects or elements**. Starting from a data frame A (n objects described by p variables, with values aᵢₖ), a distance dᵢⱼ is computed for each pair of objects i and j, producing the distance matrix D. It has three properties:

- **Square N × N**: for N elements the matrix has N × N cells, with the same number of rows and columns;
- **Zero diagonal**: every entry on the main diagonal is 0, because the distance of an item from itself is zero;
- **Symmetry**: the distance from A to B equals the distance from B to A (dᵢⱼ = dⱼᵢ).

For these reasons, a distance matrix is frequently represented in **triangular form** (only the lower or the upper half, without the diagonal), since the other half carries no additional information.

![[SATAUMV-image50.png|415]]

## 12.6 Genetic distances: FST

**Genetic distances** are statistics that allow comparing the **relatedness of populations (or molecules)**. The most used one is **FST** (chapter 6):

*FST = (HT − HS) / HT*

where **HT** is the expected heterozygosity of the entire (meta)population and **HS** is the mean expected heterozygosity across sub-populations. FST is often used as a measure of **genetic distance**, because it is the **proportion of genetic variation that is due to allele frequency differences between populations**. An equivalent formulation is:

*FST = Var(p) / \[p̄(1 − p̄)\]*

where **p̄** and **Var(p)** are the **mean** and the **variance** of the allele frequency across populations. **FST = 0** implies that two or more populations have identical allele frequencies; **FST = 1** implies that they are fixed for different alleles.

Example: two populations of equal size with allele frequencies p₁ = 0.2 and p₂ = 0.8. Then p̄ = 0.5 and Var(p) = 0.09, so FST = 0.09 / (0.5 × 0.5) = **0.36**. With the heterozygosities: HT = 2 × 0.5 × 0.5 = 0.5, HS = 2 × 0.2 × 0.8 = 0.32 in both populations, so FST = (0.5 − 0.32)/0.5 = **0.36** — the two formulas agree.

Wright's guidelines for interpreting FST:

| **FST values** | **Level of genetic differentiation** |
|----------------|--------------------------------------|
| \< 0.05        | Little                               |
| 0.05–0.15      | Moderate                             |
| 0.15–0.25      | Great                                |
| \> 0.25        | Very great                           |

The **pairwise FST distance matrix** of genome-wide average FST values among human populations (shown as a triangular heatmap) has very low values within continental groups (e.g. \< 0.01 among East Asian populations), values around 0.1 between Europe and East Asia, and the highest values (about 0.15–0.19) between African and non-African populations: on Wright's scale, differentiation among human populations is mostly little to moderate.

![[SATAUMV-image51.png|403]]

## 12.7 Tree reconstruction

A **tree** is a branching diagram showing the **relationships between different entities** (populations, sequences, species). Many different methods exist for constructing trees, not all of them suitable for all the types of data available, and no single method predominates. They are classified according to two criteria:

- **Type of data**: **distance-based methods** are based on measures of genetic distance among pairs of entities; **character-based methods** use discrete units, e.g. single-base changes in a nucleotide sequence;
- **Construction method**: **clustering methods** use an iterative algorithm to combine taxa in a hierarchical fashion (one by one); **searching methods** generate a large number of hypothetical trees and choose the best fit according to an optimality criterion.

| **Method**              | **Type of data** | **Construction method** |
|-------------------------|------------------|-------------------------|
| Neighbor-Joining (NJ)   | Distance-based   | Clustering              |
| UPGMA                   | Distance-based   | Clustering              |
| Maximum Parsimony (MP)  | Character-based  | Searching               |
| Maximum Likelihood (ML) | Character-based  | Searching               |
| Bayesian                | Character-based  | Searching               |

## 12.8 Unweighted Pair-Group Method with Arithmetic mean (UPGMA)

In **UPGMA** an initial **distance matrix** is constructed between the sequences (or populations). An **iterative clustering** process then combines the **two taxa with the smallest genetic distance**, forming a new (composite) taxon. The genetic distances between this composite taxon and the other taxa are calculated as the **average of the distances** from the single original taxa. The procedure is repeated until all the entities are grouped into a single phylogeny.

Worked example with six taxa (A–F):

- **First cycle**: the smallest distance is d(A,B) = 2, so A and B are joined (each branch has length 2/2 = 1). New distances: d(AB,C) = (4 + 4)/2 = 4, d(AB,D) = (6 + 6)/2 = 6, d(AB,E) = 6, d(AB,F) = 8;
- **Second cycle**: D and E (distance 4) are joined, each branch of length 2;
- **Third cycle**: AB is joined with C (distance 4);
- **Fourth cycle**: ABC is joined with DE (distance 6);
- **Fifth cycle**: F is finally joined to ABCDE (distance 8).

![[SATAUMV-image52.png|453]]

UPGMA produces a tree in which the **distance between each taxon and the root is the same**, i.e. all the terminal nodes are aligned (an ultrametric tree). This implicitly assumes a constant rate of change along all branches (a molecular clock).

Example: dendrogram based on pairwise FST genetic distances among Euro-Mediterranean populations (1,571 individuals from about 70 populations genotyped for a common set of about 350k SNPs); populations cluster largely according to geography.

![[SATAUMV-image53.png|604]]

## 12.9 Neighbor-Joining (NJ) method

**Neighbor-joining (NJ)** is a clustering method that, based on the distance matrix, attempts to find the tree with the **shortest sum of branch lengths (S)**, following the principle of **minimum evolution**:

- a distance matrix is constructed between the sequences and an initial **unrooted star-like tree** is created from it;
- the two nodes whose merging makes the overall length of the tree branches (S) as small as possible are joined, and a **new node** connecting these two clusters is created (the distance matrix is updated);
- the new node is connected to the central node, updating the tree topology; the step is repeated until all entities are connected into a single tree.

![[SATAUMV-image54.png|453]]

Unlike UPGMA, NJ **does not assume that all terminal nodes are equidistant** from the root, so branches can have different lengths and the resulting tree is unrooted.

Example: NJ trees based on the **inter-population FST matrix** calculated from allele frequencies in the 51 populations of the **Human Genome Diversity Panel** (938 unrelated individuals, 650,000 common SNPs). Populations group into continental clusters (Africa, Middle East, Europe, Central and South Asia, East Asia, Oceania, America), with African populations being the most differentiated.

![[SATAUMV-image55.png|566]]

## 12.10 Multidimensional scaling (MDS)

**Multidimensional scaling (MDS)** is a set of statistical techniques that visualizes the **similarity or dissimilarity among a set of objects** by translating complex data into a **lower-dimensional representation**, easier to visualize and interpret. Its primary goal is to create a spatial representation that maintains the inherent relationships within the original data: the distances between each pair of n objects are translated into a configuration of n points in a 2D/3D Cartesian space, in such a way that the positions of the points reflect their relationships in terms of genetic distances.

MDS uses optimization algorithms to minimize the discrepancy between the distances in the low-dimensional representation and the actual distances in the original high-dimensional space. This discrepancy is measured by the **stress statistic**:

*Stress = S = Σ (Dᵢⱼ − dᵢⱼ)²*

where dᵢⱼ are the distances in the original matrix and Dᵢⱼ the distances on the 2D plane. The **lower the stress**, the better the MDS fit to the data and the **less information is lost**.

![[SATAUMV-image56.png|484]]

Example: MDS based on pairwise FST among 52 human populations of the HGDP. The first dimension separates African populations (on one side) from the Americas (on the other), while the second separates Oceania and East Asia from the Americas, Europe and the Middle East; the plot closely recalls the geographic distribution of the populations.

![[SATAUMV-image57.png|604]]

## 12.11 Genome-wide FST distribution

The **genome-wide distribution of FST** (calculated SNP by SNP) shows how genetic variation and population differentiation are distributed across all chromosomes. **Most genomic sites show very low FST**, because of shared ancestry or gene flow, so the global distribution is concentrated on low values. On top of it, some **genomic regions contain extreme outlier FST values** (e.g. the top 1% of the distribution), forming clustered peaks in specific chromosomal regions: these highly differentiated regions are candidates for local adaptation (positive selection, chapter 8).

![[SATAUMV-image58.png|491]]

---
> [[SATAUMV 11 - Post-processing quality controls, dataset assembly, imputation and phasing|← Post-processing quality controls, dataset assembly, imputation and phasing]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 13 - Summary of the main points|Summary of the main points →]]
