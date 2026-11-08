---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/Functional_Genetics/FunctionalGen_common.docx"
order: 16
tags: [note, fg]
---

> [[FG 15 - Danio rerio · Embryonic development of zebrafish|← Danio rerio · Embryonic development of zebrafish]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 17 - Danio rerio · Transgenesis and gene targeting|Danio rerio · Transgenesis and gene targeting →]]

# Forward genetics in zebrafish

The forward-genetics approach in zebrafish is almost the same as in *Drosophila*.

**ENU three-generation screen.** An **ENU**-treated male (P) is crossed to a wild-type female. The **F1** fish are heterozygous for many independent mutations (+/m); each F1 is outcrossed to found an **F2 family**, in which half of the fish carry the mutation. Random **sibling matings in F2** (+/m × +/m) give **F3 clutches** in which **¼ of the embryos are homozygous** and can be screened for a phenotype — the same logic as the recessive screens in *Drosophila*.

**The Big Screen (1993).** Nüsslein-Volhard (Tübingen) and Driever (Boston) applied this scheme on a large scale and described about **4000 embryonic lethal mutants**, the vertebrate counterpart of the Heidelberg screen on the fly.

> **Focus — ENU and publication. Alkylating spermatogonial mutagen, mainly point mutations; both screens published in 1996 (Development).**
>
> **Paper — Driever et al., 1996** (Development 123:37–46): The Boston half of the Big Screen, the first large-scale vertebrate screen: 2,383 mutations, 695 kept and 220 loci defined, with only 1.5 alleles per locus, too few to estimate saturation (unlike the fly screen).

## Reverse genetics in zebrafish

### TILLING – Targeting Induced Local Lesions IN Genomes

- **First step**: creation of a **mutagenised population** (ENU).

- **Aim**: reduce the time and cost of mutation detection using DNA sequencing.

- A **high-throughput** approach to identify **SNPs and/or indels** in a gene (or genes) of interest within a mutagenised population.

- Large libraries have to be screened, but they give **several allelic series with random mutations** → a very good **genotype–phenotype correlation** (from hypomorphs to amorphs, cf. Müller’s classification).

- First organisms: *A. thaliana*, *D. melanogaster*. A large project on zebrafish was run in Holland (about **1 mutation / 230 kb**).

- **Disadvantage**: the mutations are **introduced randomly**.

**Which regions are analysed.** Lesions in the library are identified by analysing **PCR amplicons** spanning the genomic regions of interest — typically **early exons**, or exons coding **critical functional domains**, where a nonsense mutation would very likely be inactivating.

![[FG-image53.png|576]]

*Chemical mutagenesis screen (a) vs TILLING (b), with CelI mismatch detection (Renninger et al., 2010).*

**The procedure:**

- ENU-mutagenised males are crossed to wild-type females; from each **F1** fish **DNA is isolated** (fin biopsy) and sperm is usually cryopreserved.

- **1. PCR** of the gene of interest → **2. denaturation** → **3. re-annealing**: if the fish is heterozygous, wild-type and mutant strands pair into **heteroduplexes** with a mismatch.

- The endonuclease **CelI** cuts at the mismatch, and the cleavage products are seen on a gel. Alternatively, individual fish are **directly resequenced**.

- The identified carrier is **outcrossed** to wild type; heterozygous F2 siblings are incrossed and the **homozygous phenotype** is examined in F3.

**Key points:** zebrafish TILLING projects have identified **over 150 loss-of-function mutations** in genes never found in forward screens; TILLING is **complementary** to the other reverse-genetics approaches.

**Problems with TILLING.** A mutation found in a given F1 fish is **only one of many heterozygous mutations in its genome**. With a detected rate of **2–4 mutations per megabase**, each F1 fish carries an estimated **3–6000 ENU-induced mutations**. As a result, **a phenotype seen in a clutch from two heterozygous F2 fish may well be due to another, unscreened ENU mutation**.

> **Focus — How the background problem is handled. Outcross, then check co-segregation, complementation and mRNA rescue.**

### Targeted gene perturbation approaches

- **mRNA injection** — wild-type mRNA → **overexpression / rescue**; also **cross-species rescue** (e.g. the human mRNA rescuing the fish mutant).

- **Mutant mRNA injection** — **dominant-negative** effects (antimorphs).

- **Antisense approaches** — **morpholino** oligonucleotides (**knockdown**).

- **Transgenesis** — stable gene expression or **reporter lines**.

### ![[FG-image54.png|288]]Morpholinos (MO)

(See also the general morpholino section in Module 1.)

**Structure.** Morpholinos are a **synthetic derivative of DNA** with two major changes:

- a **six-membered morpholine ring** replaces the deoxyribose ring;

- a **non-ionic phosphorodiamidate linkage** replaces the anionic phosphodiester bond.

The bases are the standard nucleic-acid bases, so a MO pairs with its target RNA by normal Watson–Crick pairing.

**Main features:**

- length: **25 nucleotides**;

- activity: most effective up to about **50 hpf (*hours post-fertilization)***, still useful through about **4 dpf (*days post-fertilization)***;

- **translation-blocking** MO (blocks translation) or **splice-site** MO (blocks proper splicing of the pre-mRNA); they can also block miRNAs or their targets, and ribozyme activity;

- they **do not trigger degradation of the target** (unlike siRNA or phosphorothioates) but act by **steric blocking**: the RNA is inactive until it is degraded naturally, which also releases the MO;

- “Morpholino characteristics” (Gene Tools): **no enzymatic degradation**, **no innate immune response**, **no enzyme activity required**;

- open issues: **dosage**, and **off-target effects** → **neurotoxicity due to p53 activation**.

> **Focus — The two types in practice. Translation-blocking (5′ UTR/ATG, checked on protein) vs splice-blocking (exon–intron junction, checked by RT-PCR).**

**Example: decorin** (Zoeller et al., 2009). Decorin, a chondroitin-sulfate proteoglycan, regulates **collagen fibrillogenesis and cell growth**. Decorin morphants show a range of **truncated-body phenotypes**, classified as **mild, moderate or severe**. Two controls make the result credible:

- the **mismatch MO** (same sequence with a few mismatched bases) gives **no phenotype**;

- **rescue**: co-injecting the MO together with an **mRNA of the gene that the MO cannot bind** restores the normal phenotype.

| **Advantages** | **Disadvantages** |
|----|----|
| Fewer infrastructural needs than a classical mutagenesis screen | Incomplete knockdown |
| Very easy delivery (microinjection) | Occasional off-target, nonspecific deleterious effects |
| Highly effective up to ~4 dpf → study of gene function during embryonic development | Dilution over time → efficacy diminishes at later stages |
| Bypasses the lethality problem |  |
| “Caged” MOs: photoactivated to act in specific locations at specific times → conditional knockdowns |  |

> **Focus — Morphants vs mutants. About 80% of morphant phenotypes were not reproduced in mutants (Kok et al., 2015): validate with mutants and controls.**

---
> [[FG 15 - Danio rerio · Embryonic development of zebrafish|← Danio rerio · Embryonic development of zebrafish]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 17 - Danio rerio · Transgenesis and gene targeting|Danio rerio · Transgenesis and gene targeting →]]
