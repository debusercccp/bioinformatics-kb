---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 20
tags: [note, mbd]
---

> [[MBD 19 - Module 7 – Correlation and Regression|← Module 7 – Correlation and Regression]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 21 - Appendix A · A.1 Module 1|Appendix A · A.1 Module 1 →]]

# Module 8 — Principal Component Analysis

## 8.1 Formulation and algorithm

**The problem.** Many descriptors can characterise a set of objects: for proteins, residue composition (20 values), dipeptide composition (400), length, average hydrophobicity; for individuals, dimensions, weight, metabolite concentrations. How can a minimal set of descriptors be extracted *without losing information on the variability of the set*?

**Data reduction.** Summarise the $p$-dimensional description of $n$ objects by a smaller set of $k$ derived (synthetic, composite) variables. Whatever is not retained is “residual” variation. A good reduction balances clarity of representation against oversimplification.

**The key idea.** *Directions with the largest variance best describe the dataset.* A direction along which all points have the same value carries no information about differences between them. But when variables are **correlated**, the variance of each individual variable is not enough to identify the important directions — the informative direction can be a diagonal combination of the originals. PCA finds those directions.

### 8.1.1 The algorithm, step by step

**1. Centre the data.** Compute the mean $M_{j}$ of each variable and subtract it from every measurement, so each variable has zero mean.

> Centring is not cosmetic. Without it the first “principal component” would point at the centroid of the cloud — it would capture the mean, not the variation — and the Gram matrix of §1.3.7 would not be the covariance matrix.

**2. Compute the covariance (or correlation) matrix.**

$$
{COV}_{jk} = cov\left( x_{j},x_{k} \right) \in \mathbb{R}^{p \times p}
$$

with the variances $\sigma_{j}^{2}$ on the diagonal.

> **Covariance vs correlation PCA — the choice that changes the answer.** Covariance PCA is sensitive to measurement units and is **dominated by high-variance variables**: measure one variable in grams instead of kilograms and it swamps the first component. Standardising each variable to zero mean and unit variance replaces COV with the **correlation matrix**, putting every variable on an equal footing. Use covariance PCA only when all variables share the same units and their relative variances are meaningful; otherwise use correlation PCA. The 1000 Genomes analysis below uses correlation PCA because allele frequencies differ across SNPs.

**3. Eigen-decomposition (diagonalisation).** COV is real and symmetric, so by the spectral theorem (§3.4.3) solve

$$
COV \cdot u_{i} = \lambda_{i}u_{i},\quad\quad\det(COV - \lambda I) = 0
$$

This yields $p$ **real** eigenvalues and $p$ **orthonormal** eigenvectors. The eigenvectors form the columns of the orthogonal rotation matrix $U$ ($U^{T}U = I$, $U^{- 1} = U^{T}$), so that

$$
U^{T}\, COV\, U = \Lambda = diag\left( \lambda_{1},\ldots,\lambda_{p} \right)
$$

In the rotated coordinate system the new variables have **zero covariance** — they are uncorrelated — and their variances **are** the eigenvalues $\lambda_{i}$.

> **Correction.** Both the slide and the earlier draft write this as $U^{T}\, COV\, U = COV = diag\left( \lambda_{1},\ldots \right)$. The middle term must be $\Lambda$, a *different* matrix from COV; writing COV on both sides says the covariance matrix is already diagonal, which is the conclusion, not the hypothesis.
>
> **Why the eigenvalues are guaranteed real and non-negative.** COV is symmetric (so real eigenvalues, §3.4.3) **and** positive semi-definite, being a Gram matrix of centred data (§1.3.7). Positive semi-definiteness is what guarantees $\lambda_{i} \geq 0$ — and since $\lambda_{i}$ *is* the variance along PC$_{i}$, a negative eigenvalue would be a negative variance. PCA is well-posed exactly because of this.
>
> Note also that $U$ is **orthogonal**, so the transformation preserves norms and angles (§2.1): ${\widetilde{x}}^{T}\widetilde{x} = x^{T}UU^{T}x = x^{T}x$. PCA **rotates** the cloud of points, it does not deform it. No distance between samples is changed by the full rotation — only by the subsequent truncation to $k$ components.

**4. Sort the eigenvalues**, $\lambda_{1} \geq \lambda_{2} \geq \ldots \geq \lambda_{p}$. The fraction of total variance explained by PC$_{j}$ is

$$
\frac{\lambda_{j}}{\sum_{i = 1}^{p}\lambda_{i}}
$$

The denominator $\sum_{i}^{}\lambda_{i} = Tr(COV)$ is the total variance — invariant under rotation (§3.2.3). PCA redistributes a fixed amount of variance; it does not create or destroy any.

**5. Project the data.**

- **Loadings:** the components $U_{ij}$ of the eigenvectors — the old coordinates of the new axes. They quantify how much original variable $i$ contributes to PC$_{j}$.
- **PC scores:** for each item $x$, the coordinate along the $i$-th principal component is the scalar product

$$
y_{i} = x^{T}u_{i} = u_{i}^{T}x,\quad\quad\text{or in matrix form}\quad y = U^{T}x
$$

and conversely $x = \sum_{i = 1}^{p}y_{i}u_{i}$.

> **Scores vs loadings — the distinction that causes most PCA confusion.**

|  | **Scores** $y_{i}$ | **Loadings** $U_{ij}$ |
|----|----|----|
| One per | **item** (sample, cell, individual) | **variable** (gene, SNP) |
| Answer to | where does this sample sit on PC1? | which genes define PC1? |
| Plotted in | the PCA scatter plot | the loadings plot / biplot arrows |
| Computed as | projection of the sample onto the eigenvector | the eigenvector components themselves |

> A score is a projection in the sense of §1.2.5 — and because $\parallel u_{i} \parallel = 1$, there is no denominator in the formula.

**Why “principal”?** Given an $n$-dimensional representation of $m$ samples, to represent them in $p < n$ dimensions using only linear transformations, the best possible choice — the one retaining maximum variance, equivalently minimising the squared reconstruction error — is the first $p$ principal components.

### 8.1.2 How many PCs to retain?

| Criterion | Rule | Caveat |
|----|----|----|
| **Kaiser** | retain PCs with $\lambda > 1$ (correlation PCA) | intuition: a useful PC should explain more than a single standardised variable. Tends to **over-retain** when $p$ is large |
| **Scree plot (elbow)** | plot eigenvalues in decreasing order, cut at the elbow | subjective, but easy to visualise and widely used |
| **Permutation / Tracy–Widom** | compare each eigenvalue to its null distribution from shuffled data | more principled; standard in genomics (`smartpca`, `FLASHPCA`) |

There is no single correct answer — the choice depends on the downstream task. This is the §7.2.2 trade-off once more: too few components lose signal, too many fit noise.

### 8.1.3 What the slides omit: PCA in practice is SVD

No software diagonalises the covariance matrix. Every implementation (`prcomp`, `scikit-learn`, `irlba`) takes the **singular value decomposition** of the centred data matrix $X = U\Sigma V^{T}$ (§3.5). The right singular vectors $V$ are the loadings, $U\Sigma$ gives the scores, and $\lambda_{i} = \sigma_{i}^{2}/(n - 1)$.

Two reasons this matters: with $p \approx 10^{6}$ SNPs the $p \times p$ covariance matrix would occupy terabytes and is never formed; and SVD is numerically far more stable, since forming $X^{T}X$ squares the condition number and destroys precision in the small eigenvalues — exactly the ones that decide where the elbow falls.

> **PCA is not clustering.** PCA is **unsupervised** and knows nothing about groups; it maximises variance, full stop. If samples separate by condition on a PCA plot, that is a *result*, not something PCA was asked to do — and as §8.2 shows, they may equally well separate by batch. Clustering ($k$-means, Leiden) assigns labels; PCA only provides coordinates, often as the input to a clustering step.

## 8.2 Biological case studies and pitfalls

### 8.2.1 Human population genetics (1000 Genomes Project)

**Dataset.** The 2015 release characterised ~84 million SNPs in $n = 2,504$ individuals from 26 populations across Africa, Europe, East Asia, South Asia and the Americas. Variables: allele dosage at each SNP, coded 0, 1, 2 (homozygous reference, heterozygous, homozygous alternate). Working matrix: $n = 2,504$ individuals (rows = items), $p \approx 1,000,000$ SNPs (columns = variables) — the typical $p \gg n$ high-dimensional setting. **Correlation PCA**, because allele frequencies vary across SNPs.

**Geographic mirroring.**

| Component | Variance explained       | Separates                        |
|-----------|--------------------------|----------------------------------|
| PC1       | $\approx 0.30\%$       | African vs non-African           |
| PC2       | $\approx 0.15\%$       | European vs East Asian           |
| PC3       | $\approx 0.08\%$       | South Asian                      |
| PC4–PC10  | $0.03$–$0.05\%$ each | finer within-continent structure |

PC1–PC2 reproduce the world’s geographic map from DNA alone.

> **Each component explains well under 1% of the variance** — and the result is still robust. This is not a contradiction: almost all genetic variation is *within* populations rather than between them, so population structure is a small but highly consistent signal spread over millions of SNPs. “Low variance explained” and “not meaningful” are different statements, and in $p \gg n$ settings they routinely come apart.

**Interpreting the loadings.** Large positive loadings on PC1 are SNPs frequent in Africa; large negative ones arose after the Out-of-Africa migration; the PC1 score approximates African ancestry proportion. Top-loading SNPs cluster in genes under strong selective sweeps — *SLC24A5* (skin pigmentation), *LCT* (lactase persistence), *EDAR* (hair texture). Natural selection is visible in a PCA plot.

**LD-pruning and GWAS control.** Long-range linkage disequilibrium means neighbouring SNPs are highly correlated; an LD block of a thousand correlated SNPs acts like one variable repeated a thousand times and artificially inflates the loadings of that region. Standard practice is **LD-pruning** (remove one SNP of each pair with $r^{2} > 0.2$) before PCA. Individual PC scores are then included as covariates in mixed-model GWAS (BOLT-LMM, SAIGE), so that associations driven by population stratification rather than biology do not appear as false positives. Without this correction, stratification inflates false positives by orders of magnitude.

*Varimax rotation* can rotate the PCs toward a simpler structure, making loadings easier to interpret biologically — at the cost of losing orthogonality.

### 8.2.2 Prokaryotic thermostability

116 fully sequenced prokaryotic genomes: 16 thermophilic (11 archaea, 5 bacteria) with optimal growth temperature OGT $> 60^{\circ}$C, 100 mesophilic (95 bacteria, 5 archaea) with OGT $< 45^{\circ}$C, and 7 quasi-mesophilic bacteria with OGT between 45 and 60 °C. PCA was run on residue composition, codon usage and codon composition.

**Result.** The **second** component of codon and residue composition correlates with OGT and separates thermophiles from mesophiles along the temperature gradient. (Montanucci, Martelli, Fariselli, Casadio, *J Proteome Res*, 2007.)

> **Note that it is PC2, not PC1.** The dominant source of variation in genome composition is GC content, which is unrelated to growth temperature. The biologically interesting signal is the *second* direction. A standard mistake is to look only at PC1 and conclude there is no signal; always inspect several components against the covariates of interest.

### 8.2.3 Single-cell RNA sequencing

**Dataset.** $n \approx 10,000$ cells $\times$ $p \approx 20,000$ genes — extremely high-dimensional and sparse.

**Standard pipeline (Seurat / Scanpy).**

1.  Select the top 2,000–5,000 highly variable genes (HVG filter).
2.  Log-normalise, $\log\left( \text{count} + 1 \right)$, to stabilise variance.
3.  Run PCA, retain the top ~50 PCs.
4.  Build a $k$-nearest-neighbour graph in PC space, cluster with Leiden or Louvain.
5.  Project to 2D with UMAP or t-SNE *using the PCs as input*.

**What PCA captures.** PC1 often reflects cell-cycle phase (S vs G2/M vs G1); PC2–PC5 separate major cell types (T cells, B cells, monocytes); doublets and low-quality cells scatter as outliers.

> **Why the pipeline reduces to 50 PCs before clustering, rather than clustering the genes directly.** The curse of dimensionality (§1.3.6): in 20,000 dimensions Euclidean distances concentrate and nearest neighbours become meaningless, so the $k$-NN graph would be noise. Projecting to 50 dimensions restores meaningful distances and, incidentally, denoises — the discarded components are mostly technical noise.
>
> Note also that UMAP and t-SNE are **non-linear** and are used for *visualisation only*. Distances and cluster sizes on a UMAP plot are not quantitatively interpretable, and the clustering is done on the PCs, not on the UMAP coordinates.

### 8.2.4 Pitfalls

**Linearity assumption.** PCA rests on the Pearson covariance or correlation matrix and so captures only **linear** relationships among variables. Where the relationship is non-linear, Pearson’s coefficient underestimates its strength, and PCA underestimates the structure of a curved manifold. Remedies: kernel PCA, diffusion maps, UMAP, autoencoders.

**Batch effects.** Systematic technical variation — day of experiment, sequencing run, operator, reagent lot — is unrelated to biology but can dominate the total variance. Since PCA is unsupervised and simply maximises variance, **PC1 may separate batches rather than conditions**. If cancer samples were sequenced in run 1 and controls in run 2, batch and biology are perfectly confounded and no analysis can separate them afterwards.

- *Detection:* colour the PCA biplot by technical covariates (lab, date, instrument); test the correlation of PC scores with them, flagging $R^{2} > 0.1$.
- *Correction:* **ComBat** (empirical Bayes), **RUVSeq** (housekeeping genes or spike-ins), **PEER/SVA** (surrogate variables from residuals), or simply include batch as a covariate in the linear model rather than modifying the expression matrix.
- *Rule of thumb:* always run PCA before and after batch correction and compare the biplots.

> **The design lesson behind the statistics.** Batch correction can only ever be partial; the real fix is **randomising samples across batches at the design stage**, so that batch and condition are not confounded in the first place. No amount of ComBat recovers information that the experimental design destroyed.

## Collegamenti
- [[AML 43 - Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA]] — PCA nel corso di ML
- [[AML 45 - Autoencoders]] — autoencoder come PCA non lineare

---
> [[MBD 19 - Module 7 – Correlation and Regression|← Module 7 – Correlation and Regression]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 21 - Appendix A · A.1 Module 1|Appendix A · A.1 Module 1 →]]
