---
course: "[[Statistical Approaches to Assess Human Molecular Variability]]"
module: "[[Statistical Approaches to Assess Human Molecular Variability]]"
source: "MCB/SATAUMV/Statistical_approaches.docx"
order: 5
tags: [note, sataumv]
---

> [[SATAUMV 04 - Generating diversity – mutation|← Generating diversity – mutation]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 06 - Eliminating diversity – genetic drift|Eliminating diversity – genetic drift →]]

# Generating diversity: recombination

## 5.1 Mechanism and role

- **Recombination** is the **reciprocal exchange of DNA segments between pairs of homologous chromosomes during meiosis** (crossing over between paired homologous chromosomes in prophase I, followed by the two meiotic divisions that produce haploid daughter cells).
- It is a direct consequence of **sexual reproduction**.
- It plays a fundamental role in creating **new combinations of genetic variants** from one generation to the next, thus contributing to genetic variation. Unlike mutation, it does not create new alleles; it reshuffles existing ones.

## 5.2 Haplotypes

A **haplotype** is the combination of allelic states for a set of polymorphic sites along the same DNA molecule. Recombination generates **new haplotypes** (new combinations of alleles on the same DNA).

- **4 SNPs** with **no recombination** give **5 haplotypes (ht1–ht5)**, all due to mutations. Alleles are coded 0 (ancestral) and 1 (derived).
- A **single recombination spot** between SNP2 and SNP3 produces **4 recombinant haplotypes (ht6–ht9)**, for example crossing ht1 with ht3 gives ht6.

![[SATAUMV-image4.png|249]]

![[SATAUMV-image5.png|364]]

## 5.3 Linkage disequilibrium (LD)

Linkage disequilibrium (LD) is simply the term for when the alleles stick together more often than expected by pure mathematical chance. **LD is the non-random association of alleles at different loci.**

Consider two loci, A and B. If there is no association between them (**linkage equilibrium**), the frequency of haplotype AB should equal the product of the frequencies of A and B:

![[SATAUMV-image6.png|229]]

*P<sub>AB</sub> = P<sub>A</sub> × P<sub>B</sub>*

The deviation from this expectation is the coefficient of linkage disequilibrium:

*D = P<sub>AB</sub> − P<sub>A</sub> × P<sub>B</sub> = (P<sub>AB</sub> · P<sub>ab</sub>) − (P<sub>Ab</sub> · P<sub>aB</sub>)*

*(observed AB frequency minus the AB frequency expected under equilibrium)*

Graphically, under linkage equilibrium the area of each haplotype square equals the product of the allele frequencies; under linkage disequilibrium the haplotype areas depart from those products.

![[SATAUMV-image7.png|220]] ![[SATAUMV-image8.png|222]]

## 5.4 Measures of LD

| **Measure** | **Definition** | **Interpretation** |
|:---|:---|:---|
| D (Lewontin and Kojima, 1960) | *D = P<sub>AB</sub> − P<sub>A</sub>P<sub>B</sub>* | Raw deviation from equilibrium. Depends on allele frequencies, so hard to compare across pairs of loci. |
| D′ (Lewontin, 1964) | *D′ = D / D<sub>max</sub>*, where *D<sub>max</sub> = min(P<sub>A</sub>P<sub>b</sub>, P<sub>a</sub>P<sub>B</sub>)* if *D \> 0*, and *min(P<sub>A</sub>P<sub>B</sub>, P<sub>a</sub>P<sub>b</sub>)* if *D \< 0* | \|D′\| = 1 means **complete LD**: no recombination between the loci (in the sample). |
| r² (Hill and Robertson, 1968) | *r² = D² / (P<sub>A</sub>P<sub>a</sub>P<sub>B</sub>P<sub>b</sub>)* | r² = 1 means **perfect LD**: complete LD **and** identical allele frequencies at the two loci. |

*Note:* the slide writes r² = D / √(P<sub>A</sub>P<sub>a</sub>P<sub>B</sub>P<sub>b</sub>). That expression is r (the correlation coefficient); r² is its square, as written in the table above.

## 5.5 Genome-wide patterns of LD

- Alleles on **different chromosomes** segregate randomly during meiosis.
- **Closely linked loci** on the same chromosome are not independent, because recombination between them occurs infrequently. Linked loci therefore share a **common evolutionary heritage** (for example the **hitchhiking effect**: a neutral variant linked to a selected one changes frequency with it).
- LD is high between close SNPs and lower between distant ones.
- Recombination is **not uniformly distributed** along the genome: LD shows a **discontinuous, block-like structure** with **recombination hotspots** between blocks.
- **YRI** (African), **CEU** (European) and **CHB and JPT** (East Asian). The African sample shows less extensive LD blocks than the non-African samples, consistent with the longer history and larger effective size of African populations and with the bottlenecks that accompanied the dispersal out of Africa.

## 5.6 LD decay

**Recombination progressively breaks haplotypes** over subsequent generations, so LD decays. The slide illustrates a new mutation (N → D) that initially sits on a single haplotype background; after 10 and 90 generations recombination has replaced the surrounding segments, leaving the mutation associated with an ever-smaller block of its original haplotype.

*D<sub>t</sub> = (1 − r)<sup>t</sup> × D₀*

*(r = recombination fraction between the loci, t = generations)*

![[SATAUMV-image9.png|624]]

| **Recombination fraction** | **Behaviour of LD (graph with D₀ = 0.25)** |
|:---|:---|
| r = 0 | No recombination: D stays constant at 0.25 (complete linkage). |
| r = 0.01 | Very slow decay, D is still close to 0.2 after 25 generations. |
| r = 0.05 | Moderate decay, D falls to about 0.07 after 25 generations. |
| r = 0.1 | Faster decay, D falls to about 0.02 after 25 generations. |
| r = 0.5 (unlinked loci) | Rapid decay: D is essentially 0 within about 5–10 generations. |

Worked example: for r = 0.01 and t = 100 generations, D₁₀₀ = (0.99)¹⁰⁰ × D₀ ≈ 0.366 × D₀, so about 37% of the initial LD remains. The smaller r is, the longer LD persists, which is why tightly linked variants stay associated for many generations.

---
> [[SATAUMV 04 - Generating diversity – mutation|← Generating diversity – mutation]] · [[Statistical Approaches to Assess Human Molecular Variability|↑ Statistical Approaches]] · [[SATAUMV 06 - Eliminating diversity – genetic drift|Eliminating diversity – genetic drift →]]
