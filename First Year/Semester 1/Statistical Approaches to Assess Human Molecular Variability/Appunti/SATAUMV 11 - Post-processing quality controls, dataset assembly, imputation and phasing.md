---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 11
tags: [note, sataumv]
---

> [[SATAUMV 10 - Reference sequences and population genomic databases|← Reference sequences and population genomic databases]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 12 - Summary statistics and genetic distances|Summary statistics and genetic distances →]]

# Post-processing quality controls, dataset assembly, imputation and phasing

## 11.1 Overview: from raw genotypes to analysis-ready data

Genome-wide data are never used "as is": both **biological artefacts** (contamination, relatedness, population structure) and **technical artefacts** (missing data, batch effects, strand or build inconsistencies) must be detected and removed or corrected first.

All the QC procedures described here are implemented in **PLINK**, a free, open-source genomic analysis toolset designed to perform a large range of analyses in a computationally efficient manner. PLINK reads genotype data in its own format.

## 11.2 Per-individual (per-sample) QC

Per-individual QC consists of at least four steps:

- identification of individuals with a **high missingness genotype rate**;
- identification of samples with **outlying heterozygosity rate**;
- identification of **duplicated or related individuals**;
- identification of **sex mismatches** (comparison of reported sex with genetically determined sex from X-chromosome homozygosity).

**Sample missingness rate.** The missingness rate of an individual is the **number of missing genotypes divided by the total number of genotyped markers**. PLINK calculates missingness with the **--missing** command and produces two files: **.imiss** (per individual) and **.lmiss** (per locus). Samples with high missingness rates (e.g. **\> 1% or \> 5%**) are often removed with the **--mind** PLINK function.

![[SATAUMV-image36.png|283]]**Heterozygosity rate.** For a given individual the heterozygosity rate is computed as (N.NM − O.HOM) / N.NM, where N.NM is the total number of **non-missing genotypes** and O.HOM is the **observed number of homozygous genotypes**. The PLINK **--het** function produces a file with individual heterozygosity information used to calculate this rate.

Heterozygosity and missingness are best examined **jointly** (heterozygosity on the y-axis, SNP missingness on the x-axis): samples with **high heterozygosity** are suggestive of **contamination** (DNA from more than one individual), whereas samples with **low heterozygosity** suggest **inbreeding**. Samples with high missingness are simply **poor quality**. Thresholds are usually set at ±3 standard deviations from the mean heterozygosity, and failing samples are removed.

**Relatedness.** In PLINK the **--genome** function estimates identity-by-descent (IBD) sharing between all pairs of individuals. The key statistic is **PI_HAT (π̂)**, the proportion of the genome that is IBD, calculated as **Z2 + 0.5 × Z1**, where Z0, Z1 and Z2 are the probabilities that two individuals share zero, one or two alleles IBD at a given locus. Expected values for the main relationship classes:

![[SATAUMV-image37.png|432]]

![[SATAUMV-image38.png|354]]

| **Relationship** | **PI_HAT (approx.)** | **Z0 (approx.)** | **Z1 (approx.)** | **Z2 (approx.)** |
|:---|:---|:---|:---|:---|
| Duplicate / monozygotic twins (MZ) | 1 | 0 | 0 | 1 |
| Full siblings (FS) | 0.5 | 0.25 | 0.5 | 0.25 |
| Parent-offspring (PO) | 0.5 | 0 | 1 | 0 |
| Half-siblings (HS) | 0.25 | 0.5 | 0.5 | 0 |
| Unrelated (U) | 0 | 1 | 0 | 0 |

A histogram of π̂ across all pairs shows clear modes: unrelated pairs cluster near 0, third-degree relatives near ~0.125–0.25, second-degree near ~0.25, first-degree near 0.5 and duplicates near 1. In population-genetic analyses unrelated individuals are usually kept (one of each duplicate pair is removed); in association studies one member of each related pair is typically removed, or relatedness is modelled explicitly.

**Assigned-sex check.** The homozygosity score on chromosome X is compared with the reported sex: males (XY) are expected to be homozygous at nearly all X-chromosome markers, whereas females (XX) show heterozygosity. Discordant samples are flagged and usually removed (they may indicate sample swaps or contamination).

In PLINK the sex check is run with **--check-sex**: F \> 0.8 = male, F \< 0.2 = female. Individuals whose sex inferred from the homozygosity of the X chromosome doesn't match the reported sex are removed, because the mismatch suggests a sample mix-up.

## 11.3 Per-marker QC

Per-marker QC consists of at least three steps:

- identification of SNPs with an **excessive missing rate**, because they might not have been genotyped properly;
- identification of SNPs demonstrating a **very strong deviation from Hardy-Weinberg equilibrium (HWE)**;
- identification of markers with a **very low minor allele frequency**.

![[SATAUMV-image39.png|353]]

**Marker missingness rate.** The missingness rate of a SNP is the proportion of individuals for whom that variant was not successfully genotyped; it is used to filter out low-quality markers. PLINK again uses **--missing** (output .lmiss), and markers are removed with the **--geno** option followed by a threshold for the lower limit of the call rate. For example, **--geno 0.02** removes all SNPs with more than 2% missing data, i.e. it keeps only SNPs with at least 98% successful call rate. A plot of the proportion of markers remaining as a function of the call-rate threshold typically shows an "elbow": removing variants with more than 1% missing leaves almost all variants (≥ 99% call rate), whereas pushing the threshold towards 100% discards an increasingly large fraction of the data.

The proportion of SNPs remaining decreases as the call rate threshold increases: with a threshold of 0.99, all the variants with more than 1% missing genotypes are removed and only the variants with at least 99% call rate remain (about 94% of the SNPs), while with stricter thresholds the proportion drops rapidly, down to about 40% with a threshold close to 1.

**Hardy-Weinberg equilibrium test.** The **--hardy** option in PLINK writes a list of genotype counts and HWE exact test statistics to a **.hwe** file.

The **--hwe** option filters out all variants whose HWE exact-test p-value is below the provided threshold. A very stringent (low) threshold is recommended, because the goal is to detect **serious genotyping or calling errors**, which often yield extreme p-values, rather than genuine biological departures from HWE (e.g. caused by selection, drift or inbreeding — see chapter 3). A typical genome-wide threshold is a chi-square test p-value of 10⁻⁶ to 10⁻⁴; markers are usually filtered on the control/unrelated subset to avoid removing true associations in case-control data. Interpretation of the p-value: **p \> 0.05** means no significant deviation from HWE; **p \< 0.05** means significant deviation.

(A typical genome-wide threshold is p \< 10⁻⁶, e.g. --hwe 1e-6, much lower than 0.05, because with hundreds of thousands of SNPs many of them would be below 0.05 just by chance. Also, PLINK uses an exact test, not a chi-square test.)

Example of the calculation of the HWE exact test statistics using PLINK: GENO reports the counts of the three genotypes (A1A1/A1A2/A2A2), O(HET) and E(HET) the observed and expected heterozygosity and P the p-value of the exact test. For example, at position 1:14930:A:G, out of 502 samples there are 407 heterozygous genotypes (written 0\|1 or 1\|0), 4 homozygous genotypes AA (0\|0) and 91 homozygous genotypes GG (1\|1), so the observed heterozygosity (0.81) is much higher than expected (0.485) and the p-value (4.864 × 10⁻⁶¹) indicates a strong deviation from HWE. The same happens at 1:104186:T:C (observed heterozygosity 0.70 vs 0.5 expected, p = 6.418 × 10⁻²⁰), while the other SNPs have high p-values (no deviation).

![[SATAUMV-image40.png|563]]

**Minor allele frequency (MAF).** It is the frequency at which the *second most common* allele occurs in each population. Some analyses require the removal of markers with very low MAF because they may lead to low detection power or spurious signals. The minor allele frequency of each SNP is reported with the **--freq** option, and SNPs are removed with the **--maf** function followed by a lower-limit threshold. Generally a threshold **below 1%** is recommended to filter SNPs with too-low frequency and any extremely rare SNPs, including monomorphic SNPs. The MAF histogram is strongly skewed: the vast majority of SNPs are very rare (MAF \< 0.01), and the threshold is placed at the point where the curve flattens.

![[SATAUMV-image41.png|426]]

In the MAF distribution of the SNPs (from 0 to 0.5), the first bin (MAF ≤ 0.005) contains about 19,000 SNPs, many more than the other bins (about 2,500–7,000 each). Zooming in on the MAF from 0 to 0.05, most of them are very rare SNPs with MAF ≤ 0.001 (about 11,000), followed by rare SNPs, which decrease quickly in number; with the 0.01 (1%) threshold, all the SNPs on the left of 0.01 are removed.

Summary of the QC steps and the corresponding PLINK options:

| **QC step**                    | **Option(s) in PLINK** |
|:-------------------------------|:-----------------------|
| Sample missing rate            | --missing, --mind      |
| Individual heterozygosity rate | --het                  |
| Sample relatedness             | --genome               |
| SNP/marker missing rate        | --missing, --geno      |
| Hardy-Weinberg equilibrium     | --hardy, --hwe         |
| Minor allele frequency         | --freq, --maf          |

After QC, the dataset is assembled in the three steps below, and the critical one is data integration, in which a dataset is integrated and compared with other comparison datasets, merging the variants from the different datasets.

## 11.4 Dataset assembly: merging datasets

Dataset assembly proceeds in three steps:

- **Step 1 — Prepare data:** prepare variant data from multiple sources (datasets 1…n), each QCed as above.
- **Step 2 — Data integration:** merge variants from the different datasets into a single file; it must consider the batch effect.
- **Step 3 — Data analysis:** perform population structure and other analyses on the merged dataset.

**Key issues in merging different population-genomics datasets:**

- **Computational challenges:** merging large-scale datasets requires huge storage space and processing power.
- **Differences in technologies/platforms and batch effects:** technical, non-biological differences between groups of samples/datasets/experiments that may confound the data and cause systematic errors in analysis, leading to false discoveries, reduced reproducibility and invalid results. Batch effects are identified with **Principal Component Analysis (PCA)** or **hierarchical clustering**: samples group by chip type, platform, dataset or experiment rather than by biological variability.
- **Different variant sets and missing data:** not all datasets overlap completely — a Venn diagram of three datasets shows private and shared variant sets, so the merged dataset is **limited to a set of common and uniformly coded variants**.
- **Reference genome inconsistencies:** datasets may be mapped to different versions of the reference genome (e.g. hg19 vs. hg38); variants must then be **lifted over** (genomic coordinates converted between builds, e.g. with the UCSC LiftOver tool). It is essential that both datasets are codified on the same genome build and that SNP rsIDs, chromosome coding and positions are harmonized.

Merging datasets in PLINK uses the **--merge** or **--bmerge** command to combine PED/MAP or binary BED/BIM/FAM files. By default PLINK performs a **union merge** (keeping all variants, with missing genotypes where a dataset lacks a marker). For an **intersection** of SNPs, first identify the common SNPs and then filter both datasets with the **--extract** option before merging. Strand flips (A/T vs. T/A, C/G vs. G/C ambiguous SNPs) must also be resolved, e.g. with **--flip**, to avoid creating false heterozygotes.

*Note:* another typical issue is the strand: the same SNP can be coded on opposite strands in two datasets (e.g. A/G in one and T/C in the other), which PLINK reports as variants with 3+ alleles; they are fixed with --flip, while the ambiguous A/T and C/G SNPs are often removed.

## 11.5 Linkage disequilibrium and LD pruning

![[SATAUMV-image42.png|270]]**Linkage disequilibrium (LD)** is the non-random association of alleles at different loci: specific combinations of alleles (haplotypes) occur more or less frequently than expected by chance. The **closer the markers**, the **stronger the LD**, because recombination occurs at a lower rate between them. LD is created by mutation, drift, inbreeding, admixture, population structure and selection, and decays over generations as *D<sub>t</sub> = (1 − r)<sup>t</sup> × D₀*. The overall LD pattern carries important signals for population-genetic inferences (demographic history, selection events) and is useful in GWAS to detect causal variants; however, some analyses require **site independence** (markers in approximate linkage equilibrium).

Under linkage equilibrium the frequency of each haplotype is the product of the frequencies of its alleles, while under LD some haplotypes, such as Ab and aB, are more frequent and others, such as AB and ab, less frequent. The measures of LD (D, D′ and r²) are the same seen in chapter 5. In LD plots, each diamond represents the LD between two SNVs (low, moderate or high LD), and in real data the plot shows blocks of high LD.

**LD pruning** removes markers in **high LD to ensure that the remaining sites are independent**. PLINK implements this with the **--indep-pairwise** option, which performs LD thinning based on pairwise r² so that all SNP pairs within a certain distance have LD below a specified threshold. All pairs of markers within a moving window are compared, and if any pair exceeds the threshold one marker of the pair is removed. The command takes three parameters:

- **window size** (number of SNPs in the window, e.g. 50);
- **step size** (how far the window shifts forward each time, e.g. 5 SNPs);
- **r² threshold** (e.g. 0.5).

For example, **--indep-pairwise 50 5 0.5** considers a window of 50 SNPs, calculates LD between each pair of SNPs in the window, removes one SNP of any pair whose r² is greater than 0.5, then shifts the window 5 SNPs forward and repeats the procedure. The output consists of two SNP lists: **plink.prune.in** (SNPs kept) and **plink.prune.out** (SNPs removed). The LD-heatmap comparison on the slide shows the dramatic effect: before pruning, large red (high-LD) blocks are visible; after default pruning the map is almost entirely blue (low LD).

| **Command** | **Comment** |
|:---|:---|
| `plink --file ``data_in`` --``indep``-pairwise 50 5 0.5 --out ``data_out` | Window size 50 SNPs, step size 5 SNPs, r² threshold 0.5 |

## 11.6 From genotypes to haplotypes: phasing

**Genotype:** the set of alleles present at each locus, without knowing which alleles are physically linked together on the same chromosome.

**Haplotype:** a group of alleles at multiple loci that have been inherited together on the same chromosome. **Phasing** is the process of determining **which alleles at different variant sites are located on the same chromosome copy** (the gametic phase), i.e. of reconstructing the two haplotypes of a diploid individual from unphased genotypes. In VCF terms: unphased genotypes are written with "/" (alleles unordered, e.g. 0/1), phased genotypes with "\|" (alleles assigned to specific haplotypes, e.g. 0\|1).

While it is "easy" to determine which alleles are present at each locus, it is not the same to reconstruct the gametic phase, i.e. how they are physically associated together on a chromosome, forming a haplotype.

After mapping and variant calling of the WGS reads, we get pairs of unordered alleles at each position, written in the unphased VCF with "/"; after haplotype phasing, the alleles are assigned to specific haplotypes, written in the phased VCF with "\|":

|                  | **Position 1** | **Position 2** | **Position 3** | **Position 4** |
|:-----------------|:---------------|:---------------|:---------------|:---------------|
| Reference genome | G              | C              | T              | A              |
| Genotype         | A/A            | C/A            | C/T            | A/A            |
| Unphased VCF     | 1/1            | 0/1            | 1/0            | 0/0            |
| Haplotype 1      | A              | C              | T              | A              |
| Haplotype 2      | A              | A              | C              | A              |
| Phased VCF       | 1\|1           | 0\|1           | 0\|1           | 0\|0           |

Only the heterozygous sites (C/A and C/T) are phase-informative sites, because at homozygous sites both haplotypes carry the same allele.

**Phasing from pedigrees or trios (father-mother-child).** Haplotypes can be deduced from the parental genotypes: where the child is heterozygous and both parents are homozygous for different alleles, the phase is fully resolved; where the child is heterozygous and one parent is also heterozygous at both sites, the phase may remain ambiguous.

For example, for an autosomal locus containing two SNVs (G/A and T/C) and a child with genotype GA,TC:

- In family (a), the father is GG,TT and the mother GA,CC, so the child received G and T from the father and A and C from the mother: the child's haplotypes are resolved by the parental genotypes (paternal G-T, maternal A-C);
- In family (b), the father is GG,TC and the mother AA,TC, so the child received G from the father and A from the mother, but both parents may have transmitted T or C: the child's haplotypes are not resolved by the parental genotypes (paternal G-T and maternal A-C, or paternal G-C and maternal A-T).

![[SATAUMV-image43.png|391]]

**Pros:** high accuracy; important for validation.

**Cons:** requires family data; sometimes can fail; limited applicability at massive, large-scale (unrelated) samples.

**Phasing in unrelated individuals — the main algorithmic approaches:**

**Clark's parsimony approach:** based on using unambiguous haplotypes (from individuals with at most one heterozygous marker) and parsimony, i.e. finding solutions that **minimize the number of unique haplotypes**. Ambiguous genotypes are resolved by assuming one of the possible haplotypes has been observed before, and deducing the other by subtraction.

**Pros:** performs well for very short segments and tightly linked variants, but loses accuracy for large datasets with a high number of SNPs.

**Cons:** requires homozygous or single-site heterozygous individuals to start; some haplotypes may remain unsolved; does not explicitly model the possibility of recombination.

The haplotypes are deduced step by step:

- Homozygous individual (ATGGTAC): the haplotypes are deduced automatically (ATGGTAC and ATGGTAC);
- Single-site heterozygous individual (GTGGT\[A/G\]C): the haplotypes are deduced automatically (GTGGTAC and GTGGTGC);
- Ambiguous individual (AT\[G/C\]G\[T/C\]AC), but one possible haplotype has been observed before: we assume it is ATGGTAC and deduce the other one by subtraction (ATCGCAC);
- Ambiguous individual (A\[T/A\]CG\[C/T\]AC), but one possible haplotype has been deduced before: we assume it is ATCGCAC and deduce the other one by subtraction (AACGTAC);
- And so on, using the haplotypes already found to resolve the other individuals.

![[SATAUMV-image44.png|345]]**Expectation-maximization (EM):** iteratively alternates an E-step, which computes **expected frequencies and assigns probabilities to all possible haplotype pairs that may explain the observed genotypes**, and an M-step, which updates the parameters to **maximize the likelihood of the observed genotypes**, until convergence.

**Pros:** effective for a small-to-moderate number of SNPs.

**Cons:** becomes computationally slow and loses accuracy for a large number of SNPs; assumes HWE; does not explicitly model recombination.

Further pro: EM also works with SNPs that are not tightly linked. Assuming HWE (random mating) is more a limitation than an advantage, because if the population deviates from HWE the estimates can be biased.

Worked example of one EM iteration (two SNPs, two individuals). Individual 1 (A/G, C/T) can be explained by the haplotype pairs AC+GT or AT+GC; individual 2 (A/A, C/T) by AC+AT or AT+AC. Starting from uniform haplotype frequencies (AC = AT = GC = GT = 0.25), the E-step gives each pair probability 0.5 within each individual; the M-step counts the expected haplotype occurrences (AC = 0.5×1 + 0.5×1 + 0.5×1 = 1.5, AT = 1.5, GC = 0.5, GT = 0.5) and converts them to frequencies by dividing by the total number of haplotypes (4), giving AC = 0.375, AT = 0.375, GC = 0.125, GT = 0.125. The procedure repeats until the frequencies stop changing: the EM algorithm pushes frequencies towards values that better explain the observed data.

Step by step, for example with two individuals genotyped at two SNPs.

**Step 0, observed genotypes:** list the possible haplotype pairs of each individual.

| **Individual** | **SNP1** | **SNP2** | **Possible haplotype pairs** |
|:---------------|:---------|:---------|:-----------------------------|
| 1              | A/G      | C/T      | AC + GT, AT + GC             |
| 2              | A/A      | C/T      | AC + AT, AT + AC             |

For individual 2, AC + AT and AT + AC are the same pair, because individual 2 is homozygous at SNP1 and has only one possible phase; counting it twice with probability 0.5 each gives the same result as counting it once with probability 1.

**Step 1, initial guess** of the haplotype frequencies, which can be random or uniform: here f(AC) = f(AT) = f(GC) = f(GT) = 0.25.

**Step 2, E-step:** compute the probability of each pair as the product of the frequencies of its haplotypes:

*P(h₁ + h₂) = f(h₁) × f(h₂)*

For individual 1, P(AC + GT) = 0.25 × 0.25 = 0.0625 and P(AT + GC) = 0.25 × 0.25 = 0.0625, so after normalization each pair has probability 0.0625/(0.0625 + 0.0625) = 0.5; the same happens for the two pairs of individual 2.

**Step 3, M-step:** update the haplotype frequencies, by computing the expected count of each haplotype (the sum of the probabilities of the pairs that contain it) and converting it to a frequency:

*f(h) = expected count of h / total number of haplotypes*

| **Haplotype** | **Initial frequency** | **Expected count** | **Updated frequency** |
|:---|:---|:---|:---|
| AC | 0.25 | 0.5 (ind. 1) + 1 (ind. 2) = 1.5 | 1.5/4 = 0.375 |
| AT | 0.25 | 0.5 (ind. 1) + 1 (ind. 2) = 1.5 | 1.5/4 = 0.375 |
| GC | 0.25 | 0.5 (ind. 1) | 0.5/4 = 0.125 |
| GT | 0.25 | 0.5 (ind. 1) | 0.5/4 = 0.125 |

**Step 4, repeat** the E-step and the M-step until the frequencies stop changing and reach convergence.

**Hidden Markov Model (HMM):** models each individual's haplotypes as **mosaics** of haplotypes from a **reference** panel (or of other individuals in the cohort) and explicitly **accounts for recombination events** (and the possibility of mutation). The reference panel is a collection of previously phased haplotypes that act as **templates**, providing a set of genetic patterns the model can copy from.

**Pros:** efficient and scalable to large datasets; suited for high-density SNP data and genome-wide phasing; explicitly models recombination; captures local LD patterns.

**Cons:** less accurate for very rare variants; depends on the quality and representativeness of the reference panel; may perform poorly in highly admixed or underrepresented populations.

Hap 5 is a mosaic of two reference haplotypes, and the switch from Hap 1 to Hap 4 corresponds to a recombination event. The hidden states of the model are the reference haplotypes copied at each position, and the switches between them represent recombination; tools such as SHAPEIT, Eagle and Beagle are based on this model.

![[SATAUMV-image45.png|388]]

## 11.7 Genotype imputation

**Genotype imputation** is the process of **inferring unobserved or missing genetic variants** by leveraging phased haplotype data, exploiting the LD structure of the genome and the availability of a reference population. After phasing, each individual's haplotype is aligned to a reference panel of densely genotyped or sequenced haplotypes (e.g. the 1000 Genomes Project); by matching haplotypes between the two panels, the genotypes of unobserved or missing variants can be predicted based on shared haplotype segments. Reference haplotypes are used to impute alleles into samples to create imputed genotypes.

The process is:

- Start from genotype data with missing data at untyped SNVs (? = untyped SNVs; 0 = homozygous ancestral state, 1 = heterozygous, 2 = homozygous derived state);
- Phase each sample and model its haplotypes as a mosaic of the haplotypes of a reference panel (e.g. 1000 Genomes Project);
- Use reference haplotypes to impute the alleles into the samples, creating imputed genotypes at the untyped SNVs.

**Pros:** inference of variants not directly genotyped; increased marker density; improved power and resolution of some analyses.

**Cons:** less robust for rare variants; strongly depends on the representativeness of the reference panel; poorly matched panels or underrepresented populations may suffer from lower accuracy and bias; errors in phasing propagate into imputation results; computationally demanding for very large datasets.

## Collegamenti
- [[MBD 20 - Module 8 – Principal Component Analysis]] — PCA per la struttura di popolazione

---
> [[SATAUMV 10 - Reference sequences and population genomic databases|← Reference sequences and population genomic databases]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 12 - Summary statistics and genetic distances|Summary statistics and genetic distances →]]
