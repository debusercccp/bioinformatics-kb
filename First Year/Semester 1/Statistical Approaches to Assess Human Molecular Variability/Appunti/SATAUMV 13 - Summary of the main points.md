---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 13
tags: [note, sataumv]
---

> [[SATAUMV 12 - Summary statistics and genetic distances|← Summary statistics and genetic distances]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]]

# Summary of the main points

- Humans are 99.9% identical at the DNA level; most variation (about 85%) lies within populations, and SNPs are the most abundant variant type.
- Four genomic compartments follow different inheritance rules: autosomes (recombine), X (recombines in women only), Y (paternal, non-recombining) and mtDNA (maternal, non-recombining).
- Out-of-Africa expansion with serial founder effects, together with demography, adaptation and culture, explains much of current variation.
- HWE is the null model: p², 2pq, q². Departures from it reveal drift, non-random mating, mutation, gene flow or selection.
- **Mutation** creates new alleles but is a slow force; SNPs are mostly identical by descent and can be polarized into ancestral and derived states; finite-site models correct the underestimation of real changes.
- **Recombination** creates new haplotypes; LD (D, D′, r²) measures non-random association between loci and decays as (1 − r)<sup>t</sup>.
- **Genetic drift** arises from finite population size — the smaller the population, the stronger the drift — and progressively reduces within-population variability while increasing differentiation among populations; **bottlenecks**, **founder effects** and **inbreeding** all amplify drift, and population structure is measured by *F<sub>ST</sub> = (H<sub>T</sub> − H<sub>S</sub>) / H<sub>T</sub>*.
- **Gene flow** introduces alleles into populations where they were absent and reduces differentiation among populations, counterbalancing drift; even low migration rates rapidly make allele frequencies nearly identical. Its patterns are described by the **n-island**, **stepping-stone** and **isolation-by-distance** models.
- **Natural selection** (differential survival and reproduction of genotypes) changes allele frequencies in different directions: **negative** selection removes deleterious variants (lower diversity in exons, nsSNPs enriched at low frequency, background selection); **balancing** selection maintains polymorphism (heterozygote advantage, e.g. HbS and malaria); **positive** selection raises advantageous alleles and leaves **selective sweeps** (**hard**, **soft** or **polygenic**, increasingly difficult to detect as the diversity reduction becomes moderate); **adaptive introgression** brings selected alleles from archaic species.
- **Sanger sequencing** (chain termination with ddNTPs, up to ~1 kb, \> 99% accuracy), **SNP chips** (probes on beads; known, common SNPs; ascertainment bias) and **NGS** (massively parallel short reads; long reads in the third generation) are the main technologies for genomic data generation; NGS gives unbiased variant discovery but costs more and needs far more computation.
- NGS data flow: **FASTQ** (reads and Phred quality, Q = −10 log₁₀ P) → **SAM/BAM** (alignments, MAPQ, CIGAR) → **VCF** (REF/ALT, GT, AD, DP, GQ); SNP-chip data are stored in **PLINK** format (.ped/.map, or binary .bed/.bim/.fam).
- **Reference sequence:** the first human reference (2001) is a haploid mosaic of over 20 donors, with one individual contributing about 70%; GRC releases (hg19, hg38) progressively closed gaps and **T2T-CHM13** provided the first gapless assembly (except chromosome Y), while the **Human Pangenome** (47 phased diploid genomes in the 2023 draft, goal at least 350) is a graph model instead of a single sequence.
- **Population genomic databases:** **HGDP** (1,064 individuals, 52 populations), **HapMap** (270 individuals and 4 populations in phases I and II, about 1,300 samples and 11 populations in HapMap 3), **1KGP** (2,504 individuals, 26 populations, 84.7 million SNVs) and **SGDP** (300 genomes, 142 populations, 43X) are the public panels of worldwide variation; large biobanks (gnomAD, UK Biobank) have much larger samples but private or controlled access.
- **Quality control** is performed per individual (missingness with --mind, heterozygosity with --het, relatedness with --genome via PI_HAT = Z2 + 0.5·Z1, sex check) and per marker (missingness with --geno, HWE with --hwe, MAF with --maf); heterozygosity and missingness are best inspected jointly to detect contamination (high heterozygosity), inbreeding (low heterozygosity) and poor-quality samples (high missingness).
- **Dataset assembly** merges multiple QCed datasets with PLINK --merge/--bmerge (union by default; intersection via --extract); key issues are batch effects (detected by PCA or hierarchical clustering and removed), non-overlapping variant sets, and reference-genome inconsistencies (resolved by LiftOver and harmonization of rsIDs, chromosome coding and positions).
- **LD pruning** (--indep-pairwise window step r²) removes markers in high LD to leave approximately independent sites, producing plink.prune.in and plink.prune.out lists.
- **Phasing** reconstructs haplotypes from genotypes: trio-based phasing is accurate but requires family data; in unrelateds, Clark's parsimony and EM work for small numbers of tightly linked SNPs, while HMM-based methods using a reference panel are the standard for genome-wide data.
- **Imputation** predicts untyped variants by matching phased haplotypes to a dense reference panel, increasing marker density and power, but its accuracy depends on the representativeness of the panel and is lower for rare variants and underrepresented populations; phasing errors propagate into imputation.
- **Summary statistics** describe within-population variability: segregating sites (S) and number of haplotypes (k) depend strongly on sample size, while nucleotide diversity π = n/(n − 1) Σ xᵢxⱼdᵢⱼ and gene/haplotype diversity h = n/(n − 1)(1 − Σ pᵢ²) are corrected for it; computed in sliding windows they provide a genome-wide baseline for spotting unusually low or high diversity.
- **Distance matrices** (square, zero diagonal, symmetric, hence shown in triangular form) summarize pairwise differences; FST = (HT − HS)/HT = Var(p)/\[p̄(1 − p̄)\] is the most used **genetic distance** (Wright: \< 0.05 little, 0.05–0.15 moderate, 0.15–0.25 great, \> 0.25 very great differentiation).
- **Trees** are built with distance-based (UPGMA, NJ) or character-based (MP, ML, Bayesian) methods, by clustering or searching; UPGMA joins the closest pair and averages distances, giving an ultrametric tree, while NJ follows minimum evolution and gives an unrooted tree.
- **MDS** projects a distance matrix into 2–3 dimensions minimizing the stress S = Σ(Dᵢⱼ − dᵢⱼ)²; the **genome-wide FST distribution** is dominated by low values, and clustered outlier peaks mark highly differentiated regions.

---
> [[SATAUMV 12 - Summary statistics and genetic distances|← Summary statistics and genetic distances]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]]
