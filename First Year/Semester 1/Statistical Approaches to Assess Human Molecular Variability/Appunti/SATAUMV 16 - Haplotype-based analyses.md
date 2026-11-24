---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 16
tags: [note, sataumv]
---

> [[SATAUMV 15 - Testing and dating population relationships and admixture|← Testing and dating population relationships and admixture]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 17 - Summary of the main points|Summary of the main points →]]

# Haplotype-based analyses

## 16.1 Haplotype-based methods

**Haplotype-based methods** are statistical and computational techniques that, rather than using information about the variants present at a set of genomic markers in terms of **allele-frequency differences**, analyze specific **combinations of allelic variants**, capturing **multi-locus patterns of haplotype sharing**.

They **require haplotype phasing** (section 11.6): from the genotype of one individual at loci 1–7 (AA CG AG CC GG CT AA) we must reconstruct its two haplotypes (A-G-A-C-G-C-A and A-C-G-C-G-T-A). The **accuracy** of these methods therefore depends critically on the **type of data** and on the **quality of the haplotype phasing** process.

Exploiting **phased haplotype data**, they reveal patterns due **not only to allele-frequency differences** but also to **multilocus haplotype sharing**, and so they can detect **more subtle population structure and genetic relationships**. They provide **higher statistical power** for:

- detecting **finer population structure** and genetic relationships;
- inferring **demographic processes**;
- detecting **natural selection** signals;
- investigating variants possibly related to **traits and diseases**.

## 16.2 ChromoPainter: chromosome painting

**ChromoPainter** incorporates haplotype information through **chromosome painting**: a computational method that **“paints” the DNA of an individual as a mosaic of DNA segments (haplotypes)** inherited from or shared with other individuals in the dataset.

The genome of a set of **target individuals (recipients)** is compared with the genomes of a set of other individuals (**donors**), and each recipient’s genome is **colored according to the donor population that carries the most similar haplotypes**. The result is a **painted profile** for each recipient: along each chromosome, every segment has the color of the donor group it was copied from.

![[SATAUMV-image82.png|624]]

By determining the **patterns of haplotype sharing**, chromosome painting can be used to:

- **reconstruct population structure**: identify fine-scale genetic groups or subgroups of individuals based on shared patterns;
- **trace ancestry**: determine which particular regions of an individual’s genome likely originated from a particular donor population;
- **analyze admixture**: detect and date past human migrations and admixture events, even in complex scenarios.

Note — ChromoPainter is based on the Li & Stephens (2003) haplotype copying model: a hidden Markov model in which each recipient haplotype is reconstructed as a mosaic of the donor haplotypes, switching from one donor to another at points that behave like recombination events.

## 16.3 Genome-wide estimates of sharing: the co-ancestry matrix

To obtain genome-wide estimates of sharing (Lawson et al. 2012, PLoS Genetics):

- each individual *i* is allowed to **copy from every other individual j ≠ i**;
- each individual *i* is **painted using all the other individuals as “donors”**;
- for each pair we calculate **y<sub>ij</sub>**, the **DNA segments of individual i painted by individual j**.

The result is the **co-ancestry matrix**, which describes the **extent of haplotype sharing between each couple of individuals**. Each element x<sub>ij</sub> is an **estimate of the total segments (chunks) of genome i that are copied from/shared with the corresponding region of genome j**; rows are recipients and columns are donors, and the matrix is usually shown as a heat map (high sharing in dark red along the diagonal blocks of related individuals).

![[SATAUMV-image83.png|369]]

Two matrices are produced:

- **chunk-count matrix**: the average **number** of haplotype chunks;
- **chunk-length matrix**: the average **length** of haplotype chunks,

> that an individual (row) received from each donor (column).

## 16.4 fineSTRUCTURE: haplotype-based clustering

**fineSTRUCTURE** is a **model-based clustering algorithm** used to identify **fine-scale population structure** from dense sequencing or SNP-chip data. It takes the output of ChromoPainter (the **chunk-count matrix**) and uses a **Bayesian Markov Chain Monte Carlo (MCMC)** approach to **iteratively group individuals into population clusters based on haplotype sharing**. The workflow is:

![[SATAUMV-image84.png|335]]Compared with other approaches:

- it does **not simply calculate genetic distances** between individuals, but uses a **statistical model to evaluate whether individuals assigned to the same cluster have similar copying patterns**;
- it does **not need the number of clusters to be specified a priori**, as in conventional clustering approaches (e.g. K in ADMIXTURE, section 14.5): the algorithm **explores different possible clusters and assignments of individuals** and, after many iterations, identifies the configurations that **better explain the observed copying patterns**.

In short, fineSTRUCTURE uses the **copying profiles** to identify individuals with **similar patterns of sharing**, rather than simply clustering them on the basis of their **allele frequencies**.

**How the method works.** fineSTRUCTURE takes the ChromoPainter co-ancestry matrix and iteratively groups individuals into genetic population clusters based on shared ancestry:

- **initial configuration**: start with an initial assignment of individuals into clusters (the number K of clusters is not fixed in advance);
- **calculate the likelihood**: evaluate how well the proposed cluster configuration explains the observed ChromoPainter copying patterns. In Bayes’ theorem, the **likelihood** is the probability of observing the given data (or evidence) assuming a specific hypothesis;
- **explore alternative cluster configurations**: test changes such as moving individuals to different clusters, splitting clusters or merging them;
- **identify genetic clusters**: select the configuration with the **highest posterior probability**, i.e. the clustering that best explains the observed haplotype-sharing patterns.

The output is typically a **dendrogram** that displays the grouping of individuals into **genetically homogeneous clusters**. Its branching structure represents **similarities in copying profiles** and the inferred sharing patterns: individuals with similar copying profiles tend to be grouped together. On the slide, the fineSTRUCTURE model applied to the whole world gives a tree in which the colors are continents and the labeled populations are shown.

**Assignment probabilities** give an idea of the **confidence** of assigning each individual to a certain cluster.

## 16.5 Examples of clustering dendrograms

In both examples the fineSTRUCTURE algorithm identifies genetic clusters in an **entirely unsupervised way**, based **exclusively on patterns of haplotype sharing** among individuals.

**Italy** (Sazzini et al. 2020, BMC Biology): **38 high-coverage whole-genome sequences** from representative Italian populations, together with **69 individuals from 35 European and Mediterranean populations**, for **6,993,871 SNVs**. The fineSTRUCTURE tree (with the posterior support of each node) separates two main groups of clusters:

- one with **Bedouin, Near East, North Africa, South and North Caucasus, Crete** and **S_ITA**: the **southern Italian** genomes cluster in this part of the tree;
- one with **East/North Europe, Central/West Europe, Basque, Sardinia** and **N_ITA together with Iberia/C_Balkans**: the **central/northern Italian** genomes cluster in this part of the tree.

On the tree only **assignment probability values \< 1** are reported: branches without a value actually have a probability of 1. For example, the node of the southern Italian cluster has a value of 0.80 and the node grouping the central/northern Italian genomes a value of 0.96.

**Mexico** (Ojeda-Granados et al. 2022, Molecular Biology & Evolution): **271 individuals from 15 Native Mexican populations**, **3,981,990 SNVs**. The circular fineSTRUCTURE dendrogram identifies three main groups matching geography:

- **Northern Mexico (NMC)**: SER and TAR, which are clearly distinct from each other (**SER vs TAR F<sub>ST</sub> = 0.075**, P \< 10⁻⁶);
- **Central Mexico (CMC)**: HUI, NAH, NAJ/NAP, PUR, NAP, NAJ;
- **Southern Mexico (SMC)**: ZAP, MAZ, TRQ, TOT, MYA, LAC, TZT, TOJ; **TOT**, from central-east Mexico, clusters with the southern populations.

![[SATAUMV-image85.png|426]]The differentiation between the groups is significant: NMC vs CMC F<sub>ST</sub> = 0.024, NMC vs SMC F<sub>ST</sub> = 0.030 and CMC vs SMC F<sub>ST</sub> = 0.007 (all P \< 10⁻⁶), so the northern populations are the most differentiated.

## 16.6 GLOBETROTTER: haplotype-based testing and dating of admixture

**GLOBETROTTER** is a haplotype-based method that **identifies, describes and dates admixture events** occurring in a target population, by analyzing the **length of unbroken DNA segments** shared across the genome. Main methodological considerations:

- **Phased data**: phased data are used to first **paint** the genomes of individuals from a putative admixed population against the haplotypes of a set of reference populations using **CHROMOPAINTER** (section 16.2);
- **Ancestry source modeling**: it does **not rely on predefining reference populations** acting as surrogates of the admixing sources, but **models the genetic makeup of the target population as a mixture of haplotypes shared with different reference populations**;
- **Source inference**: it infers the **surrogate reference populations** that best represent the genetic makeup of the original admixing sources and estimates their **ancestry contributions**.

![[SATAUMV-image86.png|378]]**Example (simulation).** (A) An admixture event **30 generations ago** between Brahui (80%) and Yoruba (20%) produces admixed individuals carrying DNA segments from each source; the true sources are **unsampled**. (B) The CHROMOPAINTER painting shows the haplotype segments (“chunks”) shared with all possible reference populations (**raw painting**); model fitting narrows the donor set largely to Central-South Asia and Africa, giving a **“cleaned” painting**. (C) GLOBETROTTER’s **source inference** identifies **Balochi** and **Mandenka** as the sampled populations with the greatest similarity to the true sources, with inferred contributions of about 80% and 20%.

Two further features:

- **Dating admixture**: the software calculates **coancestry curves**, a measure of how often a pair of haplotype chunks separated by a distance x come from the given reference populations. In theory, the ancestry chunks inherited from each source have an **exponential distribution** of lengths, which produces an **exponential decay** of the coancestry curves. The **rate of decay equals the time in generations since admixture**, allowing the date to be estimated: a **steeper decay corresponds to an older admixture**;
- **Complex admixture**: it can infer **multiple waves of admixture**, including different pulses over time, and can detect admixture **even between closely related reference populations**.

In the example, the coancestry curve (black line) is the relative probability (y-axis) that two chunks of a target individual’s genome, separated by a given genetic distance (x-axis, 0–30 cM), are copied from ![[SATAUMV-image87.png|427]]**Balochi** (surrogate of Brahui) and **Mandenka** (surrogate of Yoruba). The curve closely fits an exponential with a rate corresponding to **30 generations (95% CI: 27–33)**, the simulated date, while curves for 7 generations (decaying too slowly) and 150 generations (decaying too fast) do not fit.

Note — the principle is the same as ALDER (sections 15.3–15.4): both date admixture from the exponential decay of a signal with genetic distance, but ALDER uses LD between SNPs weighted by allele-frequency differences, whereas GLOBETROTTER uses the haplotype chunks of the painting.

## 16.7 GLOBETROTTER results

The possible GLOBETROTTER results are:

- **uncertain** → admixture is detected, but it is difficult to identify the sources;
- **one-date** → a **single date** of admixture between **two sources**;
- **one-date-multiway** → a **single date** of admixture between **more than two sources**;
- **multiple-dates** → **two or more distinct dates** of admixture between two or more sources;
- **unclear signal** → no coancestry curve provides a very good fit to the data, suggesting that the admixture signal, if any, is very unclear or non-existent.

**Example — sub-Saharan Africa** (Busby et al. 2016, eLife, “Admixture into and within sub-Saharan Africa”): genome-wide data and haplotype-based analyses were used to characterize the genetic structure and admixture of **48 sub-Saharan African groups** (**4,216 individuals**, **328,176 high-quality common SNPs**). The fineSTRUCTURE tree groups the populations by region and language family (Central West and West Africa \[Niger-Congo\], East Africa \[Nilo-Saharan, Afroasiatic, Niger-Congo\], South Africa \[Niger-Congo, Khoesan\]). GLOBETROTTER dates the admixture events (approximate values read from the plot):

- **East African** Afroasiatic groups: Wolayta, Afar, Tigray and Amhara show a **single event** dated roughly between 200 BCE and 400 CE; **Oromo** and **Somali** show **two events** (multiple-dates), a recent one (about 1800 and 1500 CE) and an older one (about 300 and 900 BCE);
- **southern African** Khoesan groups: Karretjie and ≠Khomani show a **single recent event** (about 1800 CE), while the **Nama** show two events (about 1800 CE and 400 CE).

---
> [[SATAUMV 15 - Testing and dating population relationships and admixture|← Testing and dating population relationships and admixture]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 17 - Summary of the main points|Summary of the main points →]]
