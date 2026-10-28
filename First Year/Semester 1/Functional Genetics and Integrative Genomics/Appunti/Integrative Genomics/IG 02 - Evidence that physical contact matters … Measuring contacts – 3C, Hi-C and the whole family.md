---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 2
tags: [note, ig]
---

> [[IG 01 - Lecture notes – key facts … Enhancer–promoter crosstalk|← Lecture notes – key facts … Enhancer–promoter crosstalk]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 03 - TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter|TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter →]]

# Evidence that physical contact matters

![[IG-image3.png|371]]As we said before: there is strong evidence in support of physical **contact** between enhancers and promoters, as shown by the **Blobel experiments** on the Hbb locus. Many studies show that enhancer–promoter contacts form **together with gene expression**, but a correlation cannot say what is the **cause** and what is the **consequence**: the forced looping experiments are the **direct evidence** that a contact can cause transcription.

### Forced looping at the Hbb locus

In the **Hbb locus**, the **LCR is far from the Hbb gene**. **LDB1** is fused to **zinc-finger proteins** designed to **bind the LCR** (L-ZF) and the **Hbb promoter** (P-ZF): since LDB1 **self-associates**, the two regions are **brought together** (forced chromatin looping), and **Hbb is transcribed** even though Hbb and LCR are 40–60 kb distant, and **even without GATA1**, the erythroid TF that normally brings LDB1 to the locus. This suggests a **therapeutic idea**: rerouting the LCR towards the **γ-globin** gene (HBG), which is silenced after birth, could compensate for β-thalassemia and sickle cell disease.

### LCR = enhancer cluster (super-enhancer).

### Reversible induced contacts (dCas9)

Contacts can also be induced in a **reversible way** by targeting **dCas9** to the two regions with specific **sgRNAs**:

- **Chemically induced looping**: dCas9 is fused to **PYL1** at one site and to **ABI1** at the other, and the addition of abscisic acid (**ABA**) makes **PYL1** and **ABI1 dimerize**, which forms the **loop**; when **ABA is removed**, the **loop is lost**.
- **Light-induced looping**: dCas9 is **fused to CIBN** at both sites, and **blue light** makes **CRY2 bind the two CIBN**, which forms the **loop**; in the **dark the loop is lost**.

### How do contacts act on output?

- Transcription happens in **bursts**. Forced looping raised **burst fraction** (how many alleles transcribe), not burst size.
- Contacts persist during transcription (Cd47, Kit): the E–P complex may travel with Pol II, or sit at stable transcription factories while the gene body is reeled through.
- **Non-contact modes** exist: *Shh* in the developing brain, and the EDN1 locus, show expression without detectable promoter contact. Possibly too rare to detect, or eRNAs/other mechanisms are involved.

## 4. The prototypic *Shh* enhancer: ZRS

Shh encodes a ligand involved in **developmental processes**. Shh is a **morphogen** used in **brain and limb development**: it is produced as a **precursor**, which is cleaved and modified with **cholesterol**, and then secreted through **Disp1**. When Shh is **absent** or **sequestered**, Ptch1 is active and inhibits Smo, so the pathway is **inactive**; when Shh is **present**, it binds Ptch1 (with the co-receptors Boc/Cdo), which is inactivated, so Smo is active and the pathway is **activated** through a **G-protein**, and the **Gli** transcription factors activate their target genes. Hhip binds Shh too.

The Shh locus carries **multiple enhancers** (spread over about **900 kb**), and the **ZRS** enhancer (**zone of polarizing activity regulatory sequence**) is responsible for **limb bud determination**. The ZRS is bound by the **activators** ETS1/GABPa and by the **repressors** ETV4/ETV5, which **restrict Shh expression** to the ZPA, so the hand develops normally.

The **ZRS** is located inside the Lmbr1 gene (in an **intron**), about 1 Mb away from Shh (~850 kb in the mouse), but in the same TAD, as shown by the **Hi-C contact map** of the locus, which contains the genes Rbm33, Shh, Rnf32 and Lmbr1. Mice with a **knockout of the ZRS** have **truncated limbs**, because Shh is lost in the limb bud, while the neighboring genes are not affected. **Mutations** in the **ZRS** also cause **extra digits** (polydactyly) in **humans** and in cats (like the six-toed cats of Hemingway): a **point mutation changes which TF sites the ZRS reads and gives an ectopic expression of Shh**. On the contrary, the **python ZRS** lacks a 17-bp TF binding site and cannot sustain limb development (mice carrying the python ZRS have truncated limbs).

The ZRS and the Shh promoter are **close in space also in cells that do not express Shh**, but the proximity is highest (\< 200 nm) in the ZPA, where Shh is on: so, **proximity is permissive, but not sufficient** for the activation.

## 5. Measuring contacts: 3C, Hi-C and the whole family

One-line answer: 3C and Hi-C do not look at DNA, they count **how often** two pieces of DNA were stuck together in the nucleus; TADs are the **squares** that this counting reveals, and the proof that they matter comes from experiments that break or move them (section 6).

### Step 1. How 3C measures contact between two loci

- ![[IG-image4.png|376]]**Crosslink.** Formaldehyde fixes cells, gluing together DNA segments that are physically close (through the proteins between them). This freezes the 3D arrangement at one moment.
- **Cut.** A restriction enzyme cuts the DNA into fragments (a few kb). Crosslinked fragments **stay held together** in complexes.
- **Ligate under dilution.** DNA ligase joins ends. At low concentration, ends that are crosslinked together **ligate to each other** far more often than to random fragments. A new hybrid molecule forms piece of locus A joined to piece of locus B.
- **Reverse the crosslinks** and purify the DNA.
- **Detect the hybrid.** PCR with one primer in A and one in B (3C = “one vs one”). The amount of product is proportional to how often A and B were close in the cell population.
- **Control.** The same PCR on a random-ligation library (naked DNA) corrects for primer efficiency and distance, so an E–P signal is compared against background.

To prove that Locus A and Locus B **were in contact**, you must prove that the **ligation junction exists**.

*Primer placement:* you design one unidirectional primer specific to Locus A, placed just upstream of its restriction cut site, and a second unidirectional primer specific to Locus B, placed just downstream of its cut site.

*The amplification strategy:*

- If the DNA never looped and never crosslinked, Locus A and Locus B remain far apart. The primers face in the “wrong” (opposite) directions, and the PCR fails.
- If the DNA was in contact and successfully ligated, Locus A and Locus B are now fused. Crucially, because they were ligated head-to-head, the two primers are now brought close together and are pointing towards each other across the new ligation junction.

*Weakness:* you need to know in advance which two loci to test.

### Step 2. How the family scales up

- **4C:** one bait (viewpoint, e.g. a promoter) vs all other regions: circularize the hybrids, inverse PCR, sequencing.
- **5C:** many vs many: ligation-mediated amplification of a chosen region.
- **Hi-C:** all vs all, no prior choice.
- **Capture Hi-C / promoter-capture Hi-C:** Hi-C library enriched with probes for all promoters, so every promoter’s partners are found at high resolution. This is the method used to link enhancers to genes.
- **ChIA-PET / HiChIP:** add an immunoprecipitation (e.g. CTCF, H3K27ac, YY1) so only contacts mediated by that protein are read.

> ![[IG-image5.png|496]]

### Step 3. How Hi-C gives a genome-wide map (unbiased)

![[IG-image6.png|247]]**Hi-C maps all the contacts of the genome**, and the results are shown as **contact maps**, i.e. **heatmaps** in which each pixel is the contact frequency between two regions (**the intensity of the pixel is directly proportional to the interaction frequency**). The **signal** is **strongest** along the **diagonal**, because regions close on the linear DNA contact each other more often (the contact frequency falls steeply with the genomic distance, as described by the **scaling** or **P(s) curve**); the **squares along the diagonal are domains** that interact mostly inside themselves (**TADs**), and the **dots** outside the diagonal are **loops between two specific sites**. Contacts can also be shown in a **circular plot**, in which the **lines connect interacting regions**.

![[IG-image7.png|283]]🡺 https://github.com/debusercccp/clew-hic

In the **Hi-C protocol**, the crosslinked DNA is **digested** with an enzyme, the **ends are filled in with biotin and ligated**, and then the DNA is **fragmented**, and the **biotinylated junctions are pulled down** and **amplified** for **sequencing**. The junctions are pulled down with **streptavidin**, which removes the huge amount of non-chimeric DNA, and with **paired-end sequencing** each read pair corresponds to **one contact**, with one end from each of the two pieces of DNA. The Hi-C **reads** (FASTQ) are then **analysed** with the Distiller pipeline (mapping, filtering, balancing), which produces:

- **Stats**, i.e. mapping statistics and the cis/trans ratio;
- **Pairs** (Sample.nodups.pairs.gz), used for scaling plots;
- **Coolers** (Sample.1000.cool, Sample.1000.mcool), which can optionally be converted to C-world.

![[IG-image8.png|433]]

### Step 4. Reading the Hi-C map

- **Strong diagonal:** loci close on the linear genome always contact most; frequency falls steeply with distance (the scaling or P(s) curve).
- ![[IG-image9.png|389]]**Compartments (plaid pattern):** large regions that contact other regions of the same type. A compartment is A (active, gene-rich, open) or B (inactive, closed). Found by the first principal component of the correlation matrix.
- **TADs (triangles/squares on the diagonal):** blocks where loci contact each other much more inside the block than with loci just outside. Typically, submegabase. The edge is a **boundary**.
- **Loops (dots at the corner of a TAD or square):** a single pair of loci with a specific, strong contact, usually two convergent CTCF sites with cohesin.

### Step 5. How TADs are called from the map

- Slide a small window along the diagonal and count contacts that cross each position: the **insulation score**. A dip (a local minimum) means few contacts cross there, so it is a **boundary**.
- Alternatively, the **directionality index** (Dixon et al. 2012): each bin is compared for upstream vs downstream bias; the bias flips sign at a boundary, and a hidden Markov model joins the biased stretches into domains.
- TADs are nested (sub-TADs inside TADs), so the call depends on resolution and algorithm. Boundaries are enriched for CTCF, cohesin and active (housekeeping) genes, and TADs are largely conserved between cell types and even species, unlike compartments.

### Step 6. Why the experiments combine different methods

- Since **Hi-C is a population average** of millions of fixed cells, contact is a **frequency**, not a movie, and it is **not a proof of regulation**.
- Crosslinking and ligation can create **artefacts**, so the key contacts are validated with **DNA-FISH**, live imaging and super-resolution microscopy.
- The test of function is always a **perturbation**: CRISPR deletion or inversion of a boundary, forced looping as for Hbb, degron removal of CTCF/cohesin, followed by **RNA-seq** or a **reporter read-out**.

---
> [[IG 01 - Lecture notes – key facts … Enhancer–promoter crosstalk|← Lecture notes – key facts … Enhancer–promoter crosstalk]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 03 - TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter|TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter →]]
