---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 13
tags: [note, sataumv]
---

> [[SATAUMV 12 - Summary statistics and genetic distances|← Summary statistics and genetic distances]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 14 - Clustering and inference of admixture|Clustering and inference of admixture →]]

# Population structure analyses: principal component analysis (PCA)

## 13.1 Population structure analyses

**Population structure analyses** describe how genetic variation is organized among individuals and populations. The main approaches, often used together on the same genome-wide dataset, are:

- **ADMIXTURE** (model-based clustering): estimates for each individual the **membership coefficients (Q)** to K ancestral components, shown as a bar plot in which each vertical bar is one individual (section 14.5);
- **PCA**: summarizes genotype variation into a few principal components and plots the individuals in a low-dimensional space;
- **Fine-scale clustering**: groups individuals according to their genetic similarity (shared haplotypes), producing trees of genetically homogeneous clusters;
- **LD decay**: describes how r² between pairs of markers decreases with physical distance (kb) in each population (section 5.6), reflecting its demographic history.

With genome-wide data, as the **number of loci rises** the variation we can observe among individuals (e.g. the combinations of possible genotypes) **increases**, particularly if the loci are independent (no LD). With enough loci each **individual can be identified as genetically unique**, so we can compare **each individual against every other individual** for all SNPs and measure the **degree of similarity** between two individuals as summarized by all SNPs: the analysis moves **from populations to individual-based comparisons**.

The other side of the coin is that, as the number of variables increases, so does the **complexity** of the statistical approaches required to analyze the data, as well as the **difficulty of summarizing, describing and interpreting** such large quantities of information in a clear and comprehensible way.

## 13.2 Multivariate methods: dimensionality reduction

To fully display the variability patterns among a set of elements described by **n variables**, **n − 1 dimensions** are required: with one variable the elements are points on a line, with two on a plane, with three in a cube, and so on. With hundreds of thousands of SNPs this is impossible to visualize.

![[SATAUMV-image59.jpg|520]]

**Dimensionality reduction** reduces multiple dimensions to 2–3 in order to summarize the observed variability **while minimizing the loss of information**, giving a more immediate and intuitive visualization of the data and an effective exploration of variability. Since data can be complex and highly dimensional, the goal is to find a **more compact representation** of the data, with fewer "variables" to consider. Dimensionality reduction helps to:

- visualize and discover the main patterns of variation;
- remove noise, outliers and biases;
- pre-process the data for later analyses.

## 13.3 Principal Component Analysis (PCA)

**Principal Component Analysis (PCA)** is a statistical method that uses an **orthogonal transformation** to convert a set of original (possibly correlated) variables into a set of new **linearly uncorrelated and independent variables**, called **principal components (PCs)**. It simplifies complexity by identifying a smaller number of variables that capture the main patterns of variation present in the dataset.

![[SATAUMV-image60.jpg|604]]

Geometrically, by a linear transformation of the original variables PCA identifies the line passing through the **centroid** of the data that best fits the observations. Two criteria define it, and they are equivalent:

- **Maximum variance**: the first component is the direction along which the projections of the data have the **largest variance**;
- **Minimum error**: the same direction **minimizes the sum of squared orthogonal distances** between the observations and the line.

The second component is the direction **orthogonal** to the first that captures the largest part of the remaining variance, and so on. In this way PCA **encapsulates as much variability as possible** while **minimizing the loss of information**.

Note — how PCA is applied to genotype data: genotypes are arranged in a matrix of individuals × SNPs, coded as 0, 1 or 2 copies of an allele (as in section 11.7); each SNP is centered on its mean (and usually normalized). The **eigenvectors** of the covariance matrix between individuals give the coordinates of each individual on the PCs, and the corresponding **eigenvalues** give the variance explained by each PC. Because PCA assumes that the variables are independent, it is usually run on an LD-pruned set of SNPs (section 11.5).

## 13.4 Properties of the principal components, input and output files

The new components capture and organize the variance with two main advantages:

- **Variance-based ordering**: PCs are **ranked according to the variance** they explain, so subsequent components account for progressively smaller proportions of the total variance;
- **Orthogonality and reduced redundancy**: PCs are mutually **orthogonal and uncorrelated**, so PCA reorganizes the information contained in the original, potentially correlated variables into a set of independent linear combinations that maximize the variance.

Each PC (eigenvector) is independent and encapsulates as much of the remaining variation as possible, and we can compute the **proportion of the total variance** summarized within the reduced dimensions. In the example, the top five PCs explain 38.3%, 24.2%, 15.6%, 9.9% and 7.0% of the variance (95% in total), and a plot of PC1 vs. PC2 represents 38.3 + 24.2 = 62.5% of the variance.

![[SATAUMV-image61.png|402]]**Pros**: reduces the dimensionality of complex multivariate datasets; captures the main patterns of variation.

**Cons**: may lose specific details (the variance not captured by the plotted PCs); interpretation issues (PCs are mathematical axes, not necessarily distinct biological processes).

**Input files.** PCA is a **multivariate data analysis technique** that allows the **reduction of dimensionality**: it uses fewer variables while preserving much of the information in the original data. New variables, the principal components, are constructed as **linear combinations of the original variables**, capturing as much variability as possible while minimizing the loss of information; this allows a quick visualization of the main patterns of genetic variation in a lower-dimensional plot (usually 2D or 3D). The SNP input file has one row per sample, with its population label and its genotypes at markers M1…Mn (samples S1…Sn from populations P1…Pn):

| **Sample** | **Population** | **M1** | **M2** | **…** | **Mn** |
|------------|----------------|--------|--------|-------|--------|
| S1         | P1             | AG     | CT     | …     | AA     |
| S2         | P1             | GG     | CC     | …     | CG     |
| ⋮          | ⋮              | ⋮      | ⋮      |       | ⋮      |
| S11        | P2             | AG     | CT     | …     | GG     |
| S12        | P2             | GG     | CC     | …     | AC     |
| ⋮          | ⋮              | ⋮      | ⋮      |       | ⋮      |
| Sn         | Pn             | AA     | TT     | …     | GG     |

In practice the genotypes come from the formats seen in section 9.4 (PLINK PED/MAP or BED/BIM/FAM, or the EIGENSOFT formats) and are recoded as allele counts (0, 1, 2) before computing the PCs.

**Output files.** The output of a PCA on genotype data (e.g. with EIGENSOFT smartpca; PLINK --pca writes the equivalent .eigenvec and .eigenval files) consists of two files:

- **Eigenvectors file** (.evec or .pca.evec): the **projection** of each individual onto the PCs, one row per sample with its ID, its coordinates on PC1, PC2, …, PCn and its population label. These are the values plotted to show population structure;
- **Eigenvalues file** (.eval or .pca.eval): the **ordered eigenvalues** (one per line) corresponding to the eigenvectors; each eigenvalue represents the amount of genetic variance explained by that PC.

The percentage of variance explained by a specific PC is its eigenvalue divided by the sum of all eigenvalues:

***Variance explained (PCₖ)*** *= λₖ / Σ λ*

where λₖ is the eigenvalue of the k-th PC and the sum runs over all eigenvalues. For example, with (hypothetical) eigenvalues 4.0, 2.5, 1.5, 1.0 and 1.0 (sum = 10), PC1 explains 4.0/10 = 40% and PC2 2.5/10 = 25% of the variance. In the plot of the example, eigenvector 1 explains 4.63% and eigenvector 2 4.54% of the observed genetic variation.

![[SATAUMV-image62.jpg|604]]

## 13.5 Examples of PCA

PCA summarizes the overall patterns of genomic variability in a flat low-dimensional plot.

![[SATAUMV-image63.jpeg|345]]**Worldwide variation: the Simons Genome Diversity Project** (Mallick et al. 2016, Nature; section 10.8): high-coverage whole-genome sequencing data of 300 individuals from 142 diverse populations, 1,152,838 SNPs. PC1 (7.8% of the variance) separates African samples from all the others, while PC2 (4.0%) stretches the non-African samples from West Eurasia through South Asia to East Asia and America, with Oceania apart.

**Genes mirror geography within Europe** (Novembre et al. 2008, Nature): 3,192 European individuals genotyped for 500,568 SNPs. After rotating the PC axes, the PC1–PC2 plot closely resembles the map of Europe: genetic variability within Europe shows **northwest-to-southeast** patterns of variation and strongly reflects geography, following the **isolation-by-distance** model. A large number of samples and markers is required to reveal such **fine-scale population structure**.

**Italy** (Sazzini et al. 2016, Sci Rep): 780 Italian samples, about 550,000 SNPs. In the PC1–PC2 scatterplot, northern (N_ITA), central (C_ITA) and southern (S_ITA) Italians lie along a cline between continental European (C_EUR, E_EUR) and Mediterranean/Middle Eastern (CYP, M_EAST) samples, while Sardinians (SARD) form a distinct cluster. A **Procrustes analysis**, which rotates and scales the PC coordinates to best match the geographic coordinates of the sampled provinces, shows that **detailed sampling** is required to reveal **micro-geographical clines** of diversity.

## 13.6 Challenges of PCA

**Scale and dataset composition.** PCA results are always **relative to the dataset being analyzed** and should not be interpreted in absolute terms: the **composition** of the dataset and the **geographical** **scale** determine the **patterns of variation observed** and the **percentage of variance captured**. In a worldwide PCA (A), the first dimension explains 7.1% of the variance and separates Africans (AFR) from the other groups; in a PCA restricted to European populations (B), the first dimension explains only 0.5%, and differences invisible at the worldwide scale (e.g. Finns, FIN, and Russians, RUS, vs. the other Europeans) become the main axis of variation.

![[SATAUMV-image64.jpg|604]]

**Number of samples and markers.** A large number of samples and markers is required to reveal fine-scale population structure, and the observed patterns reflect only a fraction of the total genetic variability. In a PCA of the same European individuals with 100, 1,000, 10,000 and 100,000 loci, the samples form a single undifferentiated cloud with 100 or 1,000 loci, while the geographic structure (e.g. Iberian, Italian and northern European samples) emerges only with 10,000–100,000 loci (Novembre & Peter 2016). The variance explained by PC1 decreases (1.63%, 0.42%, 0.31%, 0.29%): the higher values with few loci do not mean more structure, because with few loci the top PCs mostly capture random noise.

![[SATAUMV-image65.jpg|604]]

**Sample sizes, clines and sampling.** With individuals from K spatially structured and differentiated populations, visual inspection will show **K distinct clusters** of samples, stratified across **K − 1 PCs**. The positions of the groups and their relative differentiation, however, depend on the **sample sizes**: if these are highly variable, the spacing will produce a **distorted view** of the true differentiation.

The alternative to discrete population structure is the case where individuals are distributed across a **spatial continuum**. If sampling is uniform, PCA will show no clusters but **sinusoidal functions over geographical clines** (Novembre & Stephens 2008, Nat Genet): PC1 typically shows a gradient along the main geographic axis and PC2 a perpendicular gradient. The figure compares the theoretical PC maps expected when genetic similarity decays with geographic distance, the PC maps of simulated data (stepping-stone model) and the PC maps of real data for Africa. Such gradients arise from continuous isolation by distance and should not be over-interpreted as distinct migration events.

![[SATAUMV-image66.jpeg|287]]

**Admixture.** Using PCA, individuals admixed from two ancestral populations **lie on a cline between the parental clusters**, with their exact position determined by the ancestral contributions of the parental populations. In the worldwide PCA (about 200,000 SNPs genotyped in about 4,000 individuals), admixed individuals fall between the American, European and African clusters, and North African, Middle Eastern and Central Asian samples lie between the main continental clusters.

**Admixture**: Formation of a hybrid population from the mixing of two (or more) different ancestral groups.

*\[Not in the updated slides, deck 11 TOT\]* However, **alternative demographic models can produce similar PCA patterns**: population C lies between A and B, with individuals carrying more ancestry from A or from B, as expected from admixture; but **substructure and a higher Ne of C** could have generated the same pattern **even if A never existed**. Moreover, when data from only one population are available, admixture is detectable only if individuals **differ in their admixture proportions**: **ancient admixture**, after which all individuals carry the same proportions, is not detectable.

![[SATAUMV-image67.jpg|491]]

*\[Not in the updated slides, deck 11 TOT\]* **Linkage disequilibrium.** PCA is also sensitive to **factors independent of population history**. If variants are in **LD**, some PCs can describe **LD blocks** rather than ancestry: in the example, individuals split into three parallel stripes, a pattern that can be produced by a genomic region with strong long-range LD (for instance a large inversion), where the three groups correspond to the three genotypes at that region. This is why PCA is run on LD-pruned SNPs (section 11.5), often also excluding known long-range LD regions.

![[SATAUMV-image68.jpg|453]]

**Batch effects and outliers.** The presence of single **divergent individuals or populations** can affect the analysis, because PCA is **sensitive to extreme values**: in the example, an extreme point (A) stretches the first component, while a point far from the main axis (B) appears as an outlier on PC2. At the same time, PCA can be used to **identify outliers** in the data and to help determine whether they represent true biological variation, data errors or artefacts.

![[SATAUMV-image69.jpeg|383]]**Batch effects** (section 11.4) are all the **technical variation** introduced during data generation, e.g. differences in genotyping platforms, laboratories or processing pipelines, and can create **artificial structure** in the data. PCA may capture batch effects as major components (**samples cluster by experiment**, as experiments A and B in the example), thus allowing such artefacts to be assessed and removed, so that they do not influence subsequent analyses: after batch-effect removal the two experiments overlap.

## 13.7 Applications of PCA

In genomics PCA is used to:

- **explore the main patterns of genetic variation** (population structure, clines of genetic variation, admixture, etc.): for example, admixed Latin American populations (MEX, COL, HON, CUB, DOM, PUR, HAI) are spread between the Native American, European and African reference clusters according to their ancestry proportions;
- **identify outliers, potential biases or artefacts** in the data, such as batch effects, that may influence downstream analyses;
- *\[Not in the updated slides, deck 11 TOT\]* **account for underlying patterns of variation in genome-wide association studies (GWAS)**.

*\[Not in the updated slides, deck 11 TOT\]* ![[SATAUMV-image70.jpeg|316]]In the presence of population structure, genetic variants that are more common in particular subpopulations may appear **spuriously associated** with a phenotype/trait, even in the absence of a causal relationship (population stratification): for example, if cases are over-represented in one subpopulation, every variant more frequent in that subpopulation will look associated with the disease. Incorporating the **PCs as covariates** in the association tests allows accounting for these underlying differences and thus reduces the risk of **confounding effects**: the PCs are calculated and the GWAS is run across the entire dataset including them (example with 56,146 cases and 602,280 controls). This correction was popularized by the EIGENSTRAT method (Price et al. 2006).

## 13.8 Multivariate analyses: dimensionality reduction and classification

**Multivariate analyses** are suitable for studies in which **many variables** (e.g. genetic markers) are collected **for each experimental unit** (e.g. individuals or populations). They allow each variable to be treated **at the same time** and **without assigning them different importance**. Two main families of methods can be distinguished:

- **Reduction of dataset dimensionality** → **explorative analyses**, e.g. MDS (section 12.10) and PCA (sections 13.3–13.7);
- **Classification** → **evaluation of data homogeneity**, e.g. DAPC and cluster analyses.

**Clustering methods** are a set of techniques to **identify and describe groups of observations** within a dataset: they **partition the units of data into different groups (clusters) based on similarity**, so that units in the same cluster are more similar to each other than to units in other clusters. In population genetics the units are usually individuals and similarity is measured on their genotypes (see also UPGMA and NJ, sections 12.8–12.9, and ADMIXTURE and fine-scale clustering, section 13.1).

**DAPC** (**Discriminant Analysis of Principal Components**; Jombart et al. 2010, BMC Genetics) combines the two families, running a discriminant analysis on the retained PCs: it is described in section 14.1.

## Collegamenti
- [[AML 43 - Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA]] — PCA nel corso di ML
- [[MBD 10 - Module 3 · Eigenvalues and eigenvectors]] — autovalori e autovettori

---
> [[SATAUMV 12 - Summary statistics and genetic distances|← Summary statistics and genetic distances]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 14 - Clustering and inference of admixture|Clustering and inference of admixture →]]
