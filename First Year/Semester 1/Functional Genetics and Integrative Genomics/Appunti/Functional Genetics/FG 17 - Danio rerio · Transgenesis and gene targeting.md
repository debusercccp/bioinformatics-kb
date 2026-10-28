---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 17
tags: [note, fg]
---

> [[FG 16 - Danio rerio · Forward genetics in zebrafish + Reverse genetics in zebrafish|← Danio rerio · Forward genetics in zebrafish + Reverse genetics in zebrafish]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 18 - Danio rerio · Reporter lines – making gene expression visible|Danio rerio · Reporter lines – making gene expression visible →]]

# Transgenesis and gene targeting

### Transgenesis

- An **additional gene** (e.g. a reporter) driven by **regulatory elements**.

- The regulatory elements can be **tissue-specific promoters**, **enhancers**, or elements **sensitive to specific signalling pathways**.

- Possibility of **spatially restricted and time-controlled** strategies (conditional systems).

### Transgenesis, gene trap and enhancer trap: the use of transposons

- **Pseudotyped retroviruses** (genome of Moloney murine leukaemia virus + envelope glycoprotein of vesicular stomatitis virus) were used in zebrafish. **Problem**: handling viruses in the laboratory.

- **Transposons** were known and active in *Drosophila* (P element), but not in vertebrates.

- Three strategies solved the problem: the **synthetic transposon Sleeping Beauty (SB)**; **invertebrate transposons** Tc3 (*C. elegans*) and Tc1/*mariner* (*Drosophila*); a **vertebrate transposon from medaka (*O. latipes*): Tol2**, which is also active in amphibians and mice.

### ![[FG-image55.png|282]]The Tol2 system

- Identified as an **insertion in the tyrosinase gene** of medaka, causing **albinism**.

- **Short terminal inverted repeats (TIRs)**, flanked by **8-bp direct repeats** (the target-site duplication).

- Belongs to the **hAT family** (e.g. *Ac* in maize).

- Present in two out of ten *Oryzias* species (*O. latipes*, Japan, and *O. curvinotus*, China).

- Non-autonomous, defective variants exist; **Tol2-tyr is autonomous** and is **active also in zebrafish**.

**Full-length vs minimal vector** (Kawakami, 2007). The full-length element contains the **transposase coding sequence** between the TIRs. The **minimal Tol2 vector** keeps only about **200 bp and 150 bp of DNA from the left and right ends**; between them it can carry a DNA fragment of interest with its **promoter**.

*Tol2 transgenesis: transposase mRNA + transposon plasmid co-injected; excision, integration and germline transmission.*

**How it is done:**

- the cloned Tol2 cDNA is **transcribed in vitro** → **transposase mRNA**;

- it is **co-injected into fertilised eggs** with a **plasmid carrying the transposon vector** (e.g. with GFP);

- the transposase **excises** the transposon from the plasmid (detectable by PCR only when transposase mRNA is co-injected) and **integrates** it into the genome;

- the injected **founder** has a mosaic germ line; crossed to wild type, it gives **F1 embryos expressing GFP**, and the insertions are identified by Southern blot.

**Focus — Why the transposase comes as mRNA.** This is the same binary logic as the P-element vector plus helper plasmid in *Drosophila*: the transposase is supplied only transiently, so once the transposon has jumped into the genome no enzyme is left to remobilise it, and the insertion is stable.

### Tol2 Gateway: an upgrade

![[FG-image56.png|401]]

*Tol2kit / multisite Gateway assembly (Kwan et al., 2007).*

A **four-vector system** (Kwan et al., 2007): **(1) 5′ entry clones** (promoters), **(2) middle entry clones** (coding sequences), **(3) 3′ entry clones** (tags, polyA), **(4) destination vector** (with the Tol2 arms). The three entry clones are assembled into the destination vector by site-specific recombination.

- **Advantages**: it simplifies the generation of expression constructs thanks to an **extensive library of existing building blocks** (entry clones), with **high transgenesis efficiency**.

**Focus — The “green heart” marker.** Destination vectors often carry a second cassette, **cmlc2:EGFP**, which labels the heart. Transgenic embryos can then be selected by eye within two days, even when the transgene of interest is not yet expressed or is not fluorescent.

### Yield in transgenesis

| **Method** | **Transgenesis yield** | **Notes** |
|----|----|----|
| Classical: injection of linearised plasmids | ~5% (rarely up to 25%) | Concatemers, mosaicism, silencing over generations |
| Tol2 system | 12.5%, ~50% after improvements | Usually single, stable insertions (by F5): no concatemers, no silencing, no rearrangements |
| I-SceI meganuclease | ~30% |  |

---
> [[FG 16 - Danio rerio · Forward genetics in zebrafish + Reverse genetics in zebrafish|← Danio rerio · Forward genetics in zebrafish + Reverse genetics in zebrafish]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 18 - Danio rerio · Reporter lines – making gene expression visible|Danio rerio · Reporter lines – making gene expression visible →]]
