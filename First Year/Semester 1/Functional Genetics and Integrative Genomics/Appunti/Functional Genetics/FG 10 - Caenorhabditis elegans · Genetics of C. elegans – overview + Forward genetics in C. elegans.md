---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 10
tags: [note, fg]
---

> [[FG 09 - Introduction to Caenorhabditis elegans|← Introduction to Caenorhabditis elegans]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 11 - Caenorhabditis elegans · Reverse genetics in C. elegans|Caenorhabditis elegans · Reverse genetics in C. elegans →]]

# Genetics of C. elegans: overview

### Overview of *C. elegans* Genetics and Gene Targeting

**Genomic milestones (*Science*, Dec 1998 – "*C. elegans*: Sequence to Biology").** *C. elegans* was the first multicellular organism to have its entire genome sequenced:

- **Genome size:** 97 Mb

- **Protein-coding genes:** ~19,100 (~1 predicted gene per 5 kb)

- **Gene structure:** ~5 introns/gene

- **Functional coverage:** ~3,400 / 19,100 mutant alleles; ~2,400 / 19,100 characterized by RNAi

### Main genetic approaches in *C. elegans*:

- **1. Generation of mutants (random or site-specific)** to study gene function.

- **2. Generation of transgenics** to study gene expression.

- **3. Generation of random mutants (Forward genetics):** **A) Chemical mutagenesis (EMS)** and **B) Insertional mutagenesis** (transposons).

- **4. Generation of site-specific mutants/knockdowns (Reverse genetics):** **RNAi** and **CRISPR/Cas9**.

## Forward genetics in *C. elegans*

Forward genetics goes **from phenotype to gene**: the whole animal is mutagenised at random (chemically with EMS, or by transposon insertion), the progeny are screened for a phenotype, and the affected gene is then identified by complementation, mapping and rescue.

### Chemical mutagenesis with EMS

![[FG-image15.png|244]]**Chemical mutagenesis workflow (Forward genetics with EMS).** The entire organism ($P_{0}$ wild-type hermaphrodite, $+ / +$) is exposed to a mutagenic compound—**ethyl methanesulfonate (EMS)**—which induces point mutations in the germ cells (egg and sperm):

- $P_{0}$ **(**$+ / +$**)** $\rightarrow$ $F_{1}$ **(**$m/ +$**):** Self-fertilization of mutagenized $P_{0}$ adults generates heterozygous $F_{1}$ hermaphrodites.

- $F_{1}$ **(**$m/ +$**)** $\rightarrow$ $F_{2}$**:** Self-fertilization of $F_{1}$ heterozygotes yields Mendelian segregation in the $F_{2}$ progeny: **25%** $+ / +$, **50%** $m/ +$, and **25% homozygous mutant (**$m/m$**)**, which are isolated for **phenotype analysis**.

**Why it works.** New mutations are almost always **recessive**, so they are invisible in the F1 (m/+). **Hermaphrodite self-fertilisation** makes them homozygous automatically in the **F2**, with no crosses needed.

**Step-by-step EMS mutagenesis protocol ("In detail..."):**

1.  Expose $P_{0}$ adults to **50 mM EMS for 4 hours**, followed by a **4-hour recovery**.

2.  Transfer **10** $P_{0}$ **adults per plate across 10 plates** (Plates no. 1–10).

3.  Remove the $P_{0}$ adults after **~6 hours**, leaving **~100** $F_{1}$ **eggs** per plate.

4.  Incubate for **3 days** to obtain **~100** $F_{1}$ **adults**.

5.  Allow the $F_{1}$ adults to self-fertilize and **lay eggs for 20 hours**, then **wash off the** $F_{1}$ **adults**, leaving **~2,000** $F_{2}$ **eggs** stuck to the bacteria.

6.  Incubate for **3 days** to obtain **2,000** $F_{2}$ **worms** (= 20 $F_{2}$s from every $F_{1}$), screen for the phenotype of interest, and **clone individual** $F_{2}$ **mutants** onto separate plates to establish homozygous $F_{3}$ lines.

**Why 20 F2 per F1:** each F2 worm has a **1/4** chance of being m/m, so the chance of getting at least one homozygote among 20 siblings is **1 − (3/4)^20 ≈ 99.7%**. Practically no mutation is lost.

### From mutation to gene – once a mutation has been isolated, how do we identify the affected gene?

1.  **Complementation analysis:** Cross different mutant strains to define whether they affect the same gene (non-complementation) or different genes (complementation).

> **How to read it:** cross two recessive mutants. If m1/m2 is **mutant** → **same gene** (neither chromosome provides a working copy). If m1/m2 is **wild type** → **different genes** (each parent supplies the working copy the other lacks).

2.  **Mapping and cloning of the gene:** Use classical genetic mapping or molecular techniques to identify the mutated gene.

3.  **Transformation:** Perform functional validation of the candidate gene through **rescue experiments** (restoring the wild-type phenotype with a wild-type gene copy) or expression studies.

> **Key point:** **rescue is the definitive proof**. If adding a wild-type copy of the candidate gene restores the normal phenotype, it is the right gene.

4.  **Microinjection:** Direct delivery of cloned DNA with a fine glass needle into *C. elegans* gonads to generate transgenic lines.

---
> [[FG 09 - Introduction to Caenorhabditis elegans|← Introduction to Caenorhabditis elegans]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 11 - Caenorhabditis elegans · Reverse genetics in C. elegans|Caenorhabditis elegans · Reverse genetics in C. elegans →]]
