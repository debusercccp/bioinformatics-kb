---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 19
tags: [note, fg]
---

> [[FG 18 - Danio rerio · Reporter lines – making gene expression visible|← Danio rerio · Reporter lines – making gene expression visible]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 20 - Danio rerio · Modelling cancer in zebrafish|Danio rerio · Modelling cancer in zebrafish →]]

# CRISPR/Cas9: from gene to disease model

### How we can study gene function with zebrafish

Before genome editing the options were **random gene disruption** (ENU), **knockdown by morpholinos** and **knockdown by RNA interference** (modified miRNA hairpins). The knockdowns **transiently suppress protein levels**, give **no complete ablation of the gene** and have **off-target effects**. Targeted genome editing came with **ZFN** (zinc-finger nucleases), **TALEN** (transcription activator-like effector nucleases) and then **CRISPR-Cas9**.

**Focus — ZFN and TALEN.** Both fuse a programmable **DNA-binding domain** (zinc fingers, ~3 bp each; TALE repeats, 1 bp each) to the **FokI** nuclease domain, which cuts only as a dimer: two proteins must bind on opposite strands to make a double-strand break. Each new target requires a new protein, which is why the RNA-guided CRISPR system replaced them.

### ![[FG-image60.png|290]]CRISPR-Cas9 in zebrafish

- Zebrafish was the **first vertebrate** in which CRISPR/Cas9 was shown to **efficiently edit the genome in vivo** (Hwang et al., 2013).

- **Guide RNA** (crRNA + tracrRNA): a short synthetic RNA with a **scaffold** sequence needed for Cas binding and a user-defined **~20-nt spacer** that defines the genomic target. **Target sequence: 20 bp.**

- A **CRISPR-associated endonuclease** (Cas protein).

- An **in vitro complex of guide RNA and Cas9 protein** (RNP) is **microinjected into one-cell-stage embryos**.

- CRISPR knockout zebrafish are **extremely popular** and model many diseases. Since 2004, about **28,000 articles** on CRISPR/Cas, **\>1000 in zebrafish**. History: **Francis Mojica** proposed CRISPR arrays as part of a **bacterial immune defence**; **Doudna & Charpentier** proposed gene-editing applications (**Nobel Prize 2020**).

**Focus — What happens after the cut.** Cas9 cuts 3 bp upstream of an **NGG PAM**. In the embryo the break is repaired mostly by **NHEJ**, which leaves small **indels**; an indel that is not a multiple of 3 causes a **frameshift** and usually a premature stop codon → nonsense-mediated decay → loss of function. Precise changes need a repair template (HDR) or the newer editors.

### CRISPR tools answer different questions

| **Tool** | **Question** | **How** |
|----|----|----|
| Cas9 knockout | What happens when gene function decreases? | Double-strand break → indels |
| dCas9 regulation (CRISPRa, CRISPRi, epigenome editing) | What happens when expression changes? | Catalytically dead Cas9 fused to an activator, repressor or chromatin modifier; no DNA break |
| Precise editing (base editing) | What does a specific variant do? | Nickase Cas9 fused to a deaminase (e.g. A→G) |

![[FG-image61.png|513]]

*CRISPR tools answer different questions (Sander & Joung, 2014).*

### CRISPRi and a worked example: doxorubicin cardiotoxicity

**CRISPRi** (CRISPR interference): **dCas9**, usually fused to a repressor domain, is guided to the promoter/start of a gene and **blocks transcription** → a **knockdown without changing the DNA**. If dCas9 is expressed from a tissue-specific promoter, the knockdown is restricted to that tissue.

**The problem.** **Doxorubicin** (Dox) remains an essential component of many anticancer regimens, but causes **severe cardiotoxicity**. The heart contains cardiomyocytes, **endothelial cells**, fibroblasts and cardiac progenitors; **endothelial cells are affected** by Dox through:

- **reduced regenerative ability** of progenitors;

- **impaired VEGF signalling** or aberrant activation of the **TGF-β** pathway;

- **impaired autophagy** via Atg7;

- **cellular senescence**.

![[FG-image62.png|687]]

**The experiment** (Graziani et al., *EMBO Reports* 2026): “**Endothelial RRM2B-dependent mitochondrial DNA signalling drives doxorubicin cardiotoxicity**”.

- ***rrm2b*** and ***sting*** were down-regulated by **CRISPRi in endothelial cells**; efficiency was verified on sorted cells.

- **Readout: heart rate**, in DMSO vs Dox-treated larvae.

- **Result**: endothelial *rrm2b* or *sting* down-regulation **prevents the development of the cardiotoxic phenotype** after exposure to Dox at **3 dpf**.

**Focus — The logic.** RRM2B is a ribonucleotide-reductase subunit that supplies dNTPs for **mitochondrial DNA**; STING is the adaptor of the cGAS–STING pathway that senses **DNA in the cytosol** and triggers an inflammatory response. Knocking down either one in the endothelium alone is enough to protect the heart, so the pathway acts in the **endothelium**, not in the cardiomyocytes — a cell-type-specific conclusion that a whole-body knockout could not give.

### F0 crispants: rapid functional screening

![[FG-image63.png|328]](See also Crispants in Module 1.)

- **Cas9 RNPs** injected at the one-cell stage.

- **Several target sites within one gene**: with **three synthetic guides, \>90% of F0 embryos are biallelic knockouts** in the tested assays (Kroll et al., 2021; readout: loss of pigment in *slc24a5* crispants).

- **Phenotyping in the injected generation** — no need to raise stable lines.

- Experiments completed **before independent feeding** (typically **\<5 dpf**) generally **do not require an animal-experimentation project authorisation** under EU legislation.

**Focus — Why several guides.** One guide gives each cell a random mix of in-frame and frameshift indels, so a single-guide F0 is a **mosaic** that keeps some function. With three guides on the same gene, the probability that every allele in a cell remains functional becomes very small, so the F0 behaves almost like a null mutant.

---
> [[FG 18 - Danio rerio · Reporter lines – making gene expression visible|← Danio rerio · Reporter lines – making gene expression visible]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 20 - Danio rerio · Modelling cancer in zebrafish|Danio rerio · Modelling cancer in zebrafish →]]
