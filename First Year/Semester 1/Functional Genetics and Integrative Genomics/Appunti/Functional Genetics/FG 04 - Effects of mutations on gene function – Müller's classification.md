---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 4
tags: [note, fg]
---

> [[FG 03 - Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele)|← Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele)]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 05 - Where do we measure gene function|Where do we measure gene function →]]

# Effects of mutations on gene function: Müller's classification

**H. J. Müller (1932, Nobel Prize 1946)** classified alleles according to what they do to gene activity.

- **Loss-of-function (LOF)** – usually **recessive** to wild type

  - Complete loss: **amorph (null, KO)**

  - Partial loss: **hypomorph**

- **Gain-of-function (GOF)** – usually **dominant**

  - **Hypermorph**

  - **Neomorph**

  - **Antimorph (dominant negative)** – conceptually odd because it *reduces* wild-type activity but behaves like a gain of function (it is dominant)

**How do we distinguish them in practice?** With **gene dosage tests**: each class behaves in a characteristic way when the relative dosage of wild-type and mutant gene is changed. The standard tool is a **deficiency (Df)**, a chromosomal deletion that removes the whole locus, so *m/Df* has only one copy of the mutant allele (hemizygous), and *extra copies of the wild-type locus* (duplication/transgene).

**In short:** put the allele **over a deficiency (Df)** and **over extra wild-type copies**, and check whether the phenotype gets worse, better or stays the same. That pattern identifies the class (see the summary table below).

### Amorph (null, complete LOF)

- Eliminates normal gene function; generally recessive.

- The amorphic phenotype directly indicates the **stage or tissue that first requires the gene product**.

- Testing whether a gene is essential requires a null allele.

- **Dosage logic:** *null/null = null/Df = Df/Df* – no change in phenotype when placed over a deficiency, because there is no activity left to remove.

![[FG-image5.png|461]]

### Hypomorph (partial LOF, "weak" or "leaky" allele)

- **Decreased** normal gene function; generally recessive.

- **Dosage logic:** *hypomorph/hypomorph \< hypomorph/Df \< Df/Df* (in terms of residual activity: the phenotype gets **more severe** over a deficiency, because you halve the amount of the weak product).

- Rescued by extra wild-type copies.

![[FG-image6.png|454]]

### Hypermorph (GOF, increased wild-type activity)

- **Increased activity of the normal function**; usually dominant.

- Causes: promoter mutations increasing transcription, constitutively active or more stable gene products, receptor mutations that increase affinity for the ligand.

- **Dosage logic:** *hypermorph/hypermorph \> hypermorph/+ \> hypermorph/Df ≈ +/+*: the phenotype is **suppressed over a deficiency** (fewer mutant copies = less excess activity) and **enhanced by extra wild-type copies**.

- Caveat: hypermorphs may not exist for all genes, because some processes are relatively insensitive to the dose of a gene product.

![[FG-image7.png|449]]

### Neomorph (GOF, new function)

- **Novel gene function or novel phenotype**; typically dominant.

- Phenotype: altered activity, **qualitatively different** from wild type, or **ectopic expression** caused by a control-region mutation.

- **Dosage logic:** *neomorph/neomorph = neomorph/Df*: **not ameliorated when hemizygous** and **not affected by changing the dose of the WT allele** (the new activity is independent of the normal one).

- **Example (ectopic expression):** a gene normally active in the forelegs is repressed in the antenna by a repressor element in its regulatory region. A mutation destroying that repressor site leaves the coding region intact but the gene is now expressed in the antenna as well → a leg-like structure in the wrong place. The same protein, in the wrong cell/tissue/stage, creates a new phenotype.

![[FG-image8.png|462]]

### Antimorph (dominant negative)

- The mutant product **antagonizes the wild-type product**: in effect it **decreases wild-type activity** and is typically **dominant**.

- Often indicates a protein that **forms dimers or multimers**: the mutant subunit gets incorporated into the complex and poisons it.

- **Worked example – a dimeric receptor tyrosine kinase.** The wild-type receptor forms a **homodimer** after ligand binding, which activates the kinase and signaling. A dominant-negative receptor (e.g. one lacking a functional kinase domain) still dimerizes with the wild-type receptor but the dimer cannot signal.

  - In a **WT/DN heterozygote** with equal amounts of both subunits, only (½)² = **¼ of dimers are fully functional → 25% activity**.

  - In a **WT/null heterozygote** the null allele simply makes no protein → **~50% activity**, which is often enough to produce a response.

  - Therefore **a dominant-negative allele can be more severe than a knock-out allele.**

- **Dosage logic:** usually **rescued by increasing the WT dose**, usually **not enhanced by a deficiency**. Many antimorphic phenotypes **depend on the presence of a wild-type allele**; homozygotes may show no phenotype or a different one.

![[FG-image9.png|424]]

### Summary table

| Class | Effect on gene activity | Typical dominance | Phenotype over a deficiency | Extra wild-type copies |
|:---|:---|:---|:---|:---|
| **Amorph (null)** | Activity abolished | Recessive | Unchanged (already zero) | Rescue |
| **Hypomorph** | Activity reduced, not abolished | Recessive | More severe | Rescue |
| **Hypermorph** | Activity increased | Often dominant | Less severe | Phenotype enhanced |
| **Neomorph** | New or ectopic activity | Dominant | Unchanged | Unchanged |
| **Antimorph (dominant negative)** | Interferes with the wild-type product | Dominant | Unchanged or milder | Rescue / suppression |

### Molecular manipulation of embryos: "pasting, painting and cutting" (Xenopus eye example)

- **Pasting (gain of function):** injection of mRNA encoding the **Frizzled 3 receptor** into an 8-cell *Xenopus* embryo → formation of an **ectopic eye**.

- **Painting (readout):** immunolocalisation of **Pax6** (ganglion and amacrine cells) and **rhodopsin** (photoreceptors) shows that the ectopic eye has the layered retinal organisation of a normal eye (L = lens).

- **Cutting (loss of function):** injection of RNA encoding a **dominant-negative Frizzled 3** (receptor blockade) → the eye does **not** develop.

**Type of intervention:** **microinjection of in vitro-synthesised mRNA** into blastomeres = **transient** gain (Frizzled 3) or loss (dominant negative) of function. The RNA is translated and then degraded; **nothing is integrated into the genome**, so it is **not transgenesis** and is not inherited. Painting is only a **readout** (immunostaining), not a perturbation.

- Logic: sufficient (gain) *and* necessary (loss) → strong evidence for function.

### Explants

- A specific group of cells is cut out and cultured **without the influence of surrounding cells**, in a neutral environment or with added signals.

- Neutral environment: the explant becomes **epidermis** by default.

- Example (animal cap of *Xenopus*, Kimelman 2006): the same tissue gives different fates depending on the **dose of Activin** and other factors: high Activin (100 ng/ml) → heart and cartilage; 10–50 ng/ml → notochord (with retinoic acid → pronephros); 5–10 ng/ml → muscle; very low Activin plus IL-3 → lymphocytes, plus Scf → erythrocytes, plus Ang2 → vascular tissue.

- Message: cell fate depends on **signal identity and concentration**, not only on the cell's intrinsic genome.

**Type of intervention:** **microsurgery + in vitro culture**, with or without added signalling molecules (Activin, retinoic acid, cytokines). **No genetic modification**: only the environment of the cells is changed.

### Transplants

- They show the **fate of a group of cells and their influence on neighbouring cells**.

- Types: **homospecific** (same species), **heterospecific** (different species), **heterochronic** (different age), **heterotopic** (different region of the same embryo).

- Classic example: transplanting the **dorsal lip of the blastopore** of a non-pigmented *T. cristatus* embryo into the ventral side of a pigmented *T. taeniatus* gastrula induces a **secondary axis and a second embryo** (the organiser). The pigment difference lets you see which tissues come from the donor and which from the host.

- Molecular version: injecting RNA for **chordin** (an organiser-secreted factor) is sufficient to induce a secondary axis.

**Type of intervention:** **microsurgical grafting** between embryos, producing a **chimera** (cells of two individuals/species, told apart by pigment). **No genetic modification**. The molecular version is **RNA microinjection**: transient, as in the eye example.

### Knock-out and knock-in in mice

- Study a gene's role by producing animals that **lack** it. Based on **homologous recombination** in **embryonic stem (ES) cells**.

- Procedure: targeted ES cells are injected into blastocysts → implanted in foster mothers → **chimeric mice** → mated with normal mice → if the targeted cells contributed to the germline, offspring carry the modification (**gene-targeted mice**).

**Why ES cells.** **Homologous recombination is rare**, so it is done in cultured cells, where the few correctly targeted clones can be selected. ES cells are **pluripotent**: injected into a blastocyst they can colonise the **germline of the chimera**, which then transmits the modification to its offspring. HR works well in yeast and mouse ES cells, poorly in worm and fly, which is why those organisms rely on **CRISPR** and **transposons**.

- Example: **VDR (vitamin D3 receptor) KO mice** show a progressive visible phenotype (hair loss) at 8.5 months compared with wild type.

- A **knock-in** replaces/inserts a specific sequence (e.g. a reporter or a point mutation) in the endogenous locus.

**Type of intervention:** **gene targeting by homologous recombination in ES cells** → **chimera** → **germline transmission**. This is **true transgenesis**: a **stable, heritable** modification of a specific gene.

### CRISPR/Cas9

**In bacteria (natural function = adaptive immunity)**

- *1st infection:* a fragment of the phage DNA is acquired into the **CRISPR locus** as a new spacer between DNA repeats (Cas1/Cas2 mediate acquisition).

- *2nd infection:* the CRISPR locus is transcribed into **crRNAs**; together with the **tracrRNA** they form a complex with **Cas9**, which recognizes foreign DNA matching and **cleaves** it → resistance to the virus.

- A **single guide RNA (sgRNA)** directs Cas9 to a target next to a **PAM sequence** and makes a **double-strand break (DSB)**.

- Two repair outcomes:

  - **Non-homologous end joining (NHEJ):** error-prone; leaves small insertions/deletions → **disrupts the gene** (knock-out).

  - **Homology-directed repair (HDR):** uses a supplied **donor DNA** template → **precise correction or insertion** (knock-in).

**In short:** **Cas9 only cuts**; the outcome depends on how the cell repairs the cut. No template → **NHEJ** → indels → frameshift → **knock-out**. Template with homology arms → **HDR** → precise edit (**knock-in**, point mutation, GFP tag).

**Focus — How the target is actually found.** Cas9 does not scan for the guide sequence: it scans for the **PAM (5′-NGG-3′)**, read in the major groove by Arg1333 and Arg1335, which hydrogen-bond the two guanines. Only after engaging a PAM does Cas9 locally destabilize the duplex immediately upstream and attempt pairing with the guide, proceeding **PAM-proximal → PAM-distal**. If the first ~10–12 nt (the **seed region**) do not pair, the complex dissociates within milliseconds and resumes the search; if they do, pairing continues until a complete **R-loop** is formed.

**Focus — Two practical consequences.** First, **no PAM, no cut**, whatever the homology — which is also how the bacterial CRISPR locus protects itself, since it contains the spacers but not their PAMs. Second, mismatches in the seed abolish cleavage while PAM-distal mismatches are often tolerated, and that is exactly where **off-targets** come from.

**Focus — The cut itself.** Once the R-loop is complete, HNH undergoes a conformational rearrangement that brings it into contact with the target strand; this movement acts as an **allosteric checkpoint** that also licenses RuvC. The two domains cut almost simultaneously, generating a **blunt double-strand break 3 bp upstream of the PAM**. The position is predictable, and that predictability is what makes precise insertions designable.

### Morpholinos (knock-down)

- Antisense oligonucleotides that **do not modify DNA** but interfere with gene expression after binding RNA.

- They block **translation** (binding near the ATG start codon, preventing ribosome assembly) or **splicing** (binding a splice junction of the pre-mRNA, causing exon skipping/intron retention).

- Example: zebrafish *ambra1a* and *ambra1b* morphants (Benato et al., 2013) show clear developmental defects compared with WT at 2, 5 and 10 dpf.

- Knock-down = partial, often transient LOF; the complementary approach is **gain of function** by increasing expression of the gene.

**Why transient:** morpholinos **do not touch the DNA** and are **diluted at every cell division**, so they work best in early embryos (zebrafish, *Xenopus*).

### Crispants

- **F0 embryos are injected with multiple CRISPR-Cas9 guides** against the same target gene, producing mutations (frameshifts/truncated proteins or mutated essential residues) in many cells.

- This creates **genetic mosaicism from the F0 generation**, so the phenotype can be evaluated **immediately**, without waiting for several generations to establish a stable line.

**Trade-off:** you **save generations**, but the F0 is a **mosaic** (not every cell carries the same mutation), so the phenotype is **more variable** than in a stable mutant line.

---
> [[FG 03 - Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele)|← Reverse genetics + Gene mutation – molecular consequences (what is the nature of the allele)]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 05 - Where do we measure gene function|Where do we measure gene function →]]
