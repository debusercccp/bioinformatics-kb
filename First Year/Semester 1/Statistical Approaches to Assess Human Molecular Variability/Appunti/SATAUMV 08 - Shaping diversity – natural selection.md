---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 8
tags: [note, sataumv]
---

> [[SATAUMV 07 - Shaping diversity – gene flow|← Shaping diversity – gene flow]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 09 - Technologies for genomic data generation and data formats|Technologies for genomic data generation and data formats →]]

# Shaping diversity: natural selection

## 8.1 Natural selection and its genomic footprints

**Natural selection** is the **differential survival and reproductive success** of individuals with different **genotypes**. Present-day patterns of variation can be explained by the **interplay of demographic events** (drift, bottlenecks, founder effects, migration) **and selective pressures**.

- Populations facing different selective pressures respond differently, so allele frequencies change in **different directions**.
- The **genomic footprints** of selection are considerably variable, mainly according to the **typology**, **age** and **strength** of selection.

| **Type** | **Effect on allele frequencies** | **Effect on diversity** | **Example** |
|:---|:---|:---|:---|
| Negative (purifying) | Eliminates **deleterious** mutations | Lower diversity in functional regions; excess of rare non-synonymous variants | Missense and nonsense SNPs |
| Balancing | Keeps **several alleles** in the population | High polymorphism in the selected region | Sickle-cell allele (*HBB*) and malaria |
| Positive | Increases the frequency of **advantageous** alleles | Loss of variation around the selected allele (selective sweep) | Lactase persistence, skin pigmentation, high altitude |

## 8.2 Negative selection

**Negative selection** maintains the **genomic integrity of functional regions** by **eliminating deleterious mutations**. Deleterious variants are removed before they can reach high frequency, so they are seen mostly at low frequency.

- **Lower diversity in exons** than in neutral regions.
- A **different frequency spectrum** between **missense/nonsense** SNPs and **silent** SNPs, with an **enrichment of nsSNPs at low frequency**.
- **Background selection:** loss of neutral alleles that are in **LD** with deleterious ones (they are removed together with the deleterious allele).

Number of SNPs by class and minor allele frequency (MAF) bin, from the chart on the slide: the lowest-frequency bin is the most populated in every class, but its share (percentage of the SNPs of that class) increases from about **53%** for silent SNPs to about **63%** for missense and about **78%** for nonsense SNPs, while nonsense variants are **absent** from the most frequent bin. In other words, **non-synonymous variants are more frequent in the low allele frequency bins than synonymous ones** because negative selection tends to eliminate them before they reach high frequencies in the population.

![[SATAUMV-image17.png|512]]

## 8.3 Balancing selection

**Balancing selection** **maintains high polymorphism** in the selected region. The classical example is **sickle-cell anemia**: in the *HBB* gene (β-globin) a change at the **β6 position** replaces glutamate with valine, producing the mutated hemoglobin HbS and sickled red blood cells.

| **Genotype** | **Phenotype** |
|:---|:---|
| HbA HbA (homozygous) | Normal red blood cells. |
| HbS HbS (homozygous) | **Sickle cell** disease. |
| HbA HbS (heterozygous) | Some normal and some abnormal red blood cells: **resistant to malaria** (**heterozygote advantage**). |

- The geographic distribution of **red blood cell diseases** overlaps with that of **malaria**: *Plasmodium falciparum* in Africa and *Plasmodium vivax* outside Africa.
- **Balancing selection of heterozygotes:** carriers have **increased resistance to infection** and **milder symptoms**, so the allele is kept at appreciable frequency even though homozygotes are affected.
- Consequence: a **high incidence of recessive diseases** such as sickle-cell anemia (homozygous HbS allele of *HBB*) and the β- and α-thalassemias.

## 8.4 Positive selection

**Positive selection** favors the **increase in frequency of advantageous alleles**. The slide map links candidate genes to the selective pressures met during the dispersal of modern humans:

| **Trait / pressure** | **Genes on the map** | **Region on the map** |
|:---|:---|:---|
| Skin pigmentation | *SLC24A5*, *SLC45A2*, *TYR*, *MC1R* | Europe |
| Lactase persistence | *MCM6* | Northern Europe; East Africa and Arabian peninsula |
| Arctic environment | *CPT1A*, *LRP5*, *THADA*, *PRKG1* | Siberia |
| High-fat diet | *FADS* loci | Greenland |
| High altitude | *EGLN1*, *EPAS1*; *VAV3*, *ARNT2*, *THRB*; *EGLN1* | Tibet and Central Asia; Ethiopian highlands; Andes |
| Starchy food | *AMY1* | East Asia |
| Thick hair | *EDAR1* | East Asia |
| Trypanosome resistance | *APOL1* | West Africa |
| Malaria | *G6PD*, *HBB*, *GYPA*, *GYPB*, *GYPC* | Africa |
| Height | *CISH*, *DOCK3*, *STAT5*, *HESX1*, *POU1F1*; polygenic signal | Central Africa; Europe |
| Increased BMI | *CREBRF* | Polynesia |
| Toxic arsenic-rich environments | *AS3MT* | Andes (South America) |

## 8.5 Selective sweep

A **selective sweep** is the footprint left by positive selection: a **loss of genetic variation in the genomic region surrounding the beneficial allele** that has been positively selected.

- **Before selection**, chromosomes carry different combinations of variants and the beneficial allele is present on only one of them.
- **After selection**, the chromosomes carrying the beneficial allele have become frequent and look alike in the surrounding region, because linked variants are dragged along with the selected allele; the other haplotypes are lost.
- Recombination progressively breaks the association with distance, so the footprint is **localized** around the selected site (see LD in chapter 5).

![[SATAUMV-image18.png|440]]

## 8.6 Models of positive selection

The footprint depends on how many variants and genes are involved. Three models are considered:

- **Hard sweep model** (*1 variant, 1 gene*)
  - After a change in environment, a **new allele generated by mutation** is favored and, several generations later, it has replaced the previous neutral variation.
  - **Outstanding reduction** in the **genetic diversity** of the selected genomic region (a deep, wide valley along the locus).
  - The **most tested** model, but **not the most realistic** one according to *H. sapiens* demography (i.e. small N<sub>e</sub> + young age).
- **Soft sweep model** (*multiple variants, same gene*)
  - Several variants of the same gene are favored, either through **selection on different** *de novo* **mutations** or through **selection on standing variation** (alleles already present before the change).
  - Only a **moderate reduction in diversity** (a narrow dip), because several haplotypes carry the favored allele.
  - **Difficult to test:** often requires **functional data**.
- **Polygenic adaptation model** (*multiple variants, different genes*)
  - Favored alleles at several genes (e.g. genes A, B and C), usually acting on **standing variation**.
  - **Very difficult to test** because of the **moderate reduction in diversity** and the **small effect** of single genes/variants on the phenotype.
  - Footprint: small dips in diversity at several loci.

| **Model** | **Variants and genes** | **Diversity footprint** | **Testability** |
|:---|:---|:---|:---|
| Hard sweep | 1 variant, 1 gene | Outstanding reduction | Most tested; less realistic for humans |
| Soft sweep | Multiple variants, same gene (de novo or standing) | Moderate reduction | Difficult; often needs functional data |
| Polygenic adaptation | Multiple variants, different genes (standing variation) | Moderate reduction at several loci | Very difficult; small effect of each variant |

![[SATAUMV-image19.png|613]]

## 8.7 Adaptive introgression

**Adaptive introgression** is selection on alleles that entered a population by **admixture with archaic species**. It is **difficult to test selection on archaic species** and to **distinguish introgressed loci from ancestral polymorphisms**.

- In the slide scheme, the ancestors of East Asians lack the beneficial haplotype, which is carried by the **extinct Denisovans**; after admixture and selection it is present in **present-day Tibetans**.
- Functions reported as targets: **angiogenesis** (Tibetans), **immunity** and **pigmentation** (East Asians), **lipid catabolism** (Europeans).

![[SATAUMV-image20.png|511]]

Key messages: **negative** selection removes variation, **balancing** selection keeps it, **positive** selection raises advantageous alleles and leaves a **sweep**; the fewer the variants and genes involved, the **stronger the footprint** and the **easier the test**.

---
> [[SATAUMV 07 - Shaping diversity – gene flow|← Shaping diversity – gene flow]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 09 - Technologies for genomic data generation and data formats|Technologies for genomic data generation and data formats →]]
