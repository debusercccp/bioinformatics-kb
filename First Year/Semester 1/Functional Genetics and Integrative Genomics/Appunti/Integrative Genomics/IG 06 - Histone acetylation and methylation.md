---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 6
tags: [note, ig]
---

> [[IG 05 - Chromatin and remodeling|← Chromatin and remodeling]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 07 - Histone variants, the histone code and epigenetic memory|Histone variants, the histone code and epigenetic memory →]]

# Histone acetylation and methylation

### What can be modified

| **Residue / base** | **Modifications** |
|:---|:---|
| Lysine | Methylation, acetylation, ubiquitination, sumoylation, ADP-ribosylation |
| Arginine | Methylation |
| Serine, threonine | Phosphorylation |
| DNA (cytosine) | C5-methylcytosine (5mC), C5-hydroxymethylcytosine (5hmC) (section 14) |

Most marks sit on the **N-terminal tails** that protrude from the nucleosome core, where enzymes and readers can reach them; a few are in the globular core (e.g. H3K56ac, H3K79me).

- **H3:** acetylation at K9, K14, K18, K23; methylation at K4, K9, K27, K36, K79 (lysine) and R2, R17, R26 (arginine); phosphorylation at S10, S28.
- **H4:** S1 phosphorylation, R3 methylation, acetylation at K5, K8, K12, K16; K20 methylation.
- **H2A:** S1 phosphorylation, K5/K9 acetylation, K119 ubiquitination (PRC1, repression). **H2B:** K5, K12, K15, K20 acetylation, K120 ubiquitination (transcription elongation).

### Histone acetylation

- ![[IG-image17.png|324]]**Chemistry:** KATs/HATs transfer an acetyl group from **acetyl-CoA** to the ε-NH₃⁺ of lysine → **acetyl-lysine**, which is neutral. HDACs remove it (classes below).
- **Effect 1, charge:** the basic tails bind DNA **phosphates** and the acidic patch of neighboring nucleosomes. Acetylation **neutralizes them and weakens these contacts**. Deacetylated chromatin (HDAC) forms compact arrays with the tails on the DNA; acetylated chromatin (HAT) has spaced nucleosomes and an open fibre, so factors can reach the DNA. H4K16ac alone is enough to block compaction of the fibre in vitro.
- **Effect 2, readers:** acetyl-lysine is bound by **bromodomains** (BRD4, TAF1, GCN5, CBP/p300, BRG1 of SWI/SNF), which **bring coactivators, remodelers and elongation factors** (BRD4 → P-TEFb, section 10).
- **Targeting:** HATs and HDACs have no sequence specificity; TFs recruit them. **Activators bring coactivator HATs** (GCN5/SAGA, CBP/p300); **repressors bring corepressor HDAC complexes** (Sin3, NuRD, NCOR/SMRT–HDAC3).
- **Where:** promoters (H3K9ac, H3K14ac, together with H3K4me3) and active enhancers (**H3K27ac** with H3K4me1; sections 2 and 10). Turnover is fast (minutes), so acetylation **follows the activity of the TFs that recruit the enzymes**.

#### **Sir proteins and yeast replicative ageing**

- **Bud scars:** each division leaves a chitin scar on the mother cell wall, so the number of scars **gives the replicative age**; a cell with ~25 scars is old.
- **Bud position:** as described in the lecture, each new bud forms **180**° opposite the previous one (bipolar budding, typical of diploids; haploids bud axially, next to the previous scar).
- **Longevity genes:** mutants of certain genes, notably the SIR genes, can increase or decrease lifespan (sir2 deletion shortens it, an extra SIR2 copy extends it). These genes are linked to **silencing at telomeres** (and at HM loci and rDNA).

#### **Histone acetyltransferases (HATs / KATs)**

- Main families: **GNAT** (GCN5/KAT2A, PCAF/KAT2B), **MYST** (TIP60, MOF, HBO1, MOZ, MORF), **CBP/p300**, and the putative **NCOA** family (SRC1, SRC3/ACTR, CLOCK).
- Many HATs carry a reader domain next to the HAT domain: **bromodomain** (GNAT, CBP/p300) or **chromodomain** (some MYST members, e.g. TIP60, MOF).
- **Conservation:** GCN5, HAT1 and ELP3 are conserved from yeast and plants to humans; CBP/p300 and the NCOA family are absent from *S. cerevisiae* (metazoan HATs).
- **HATs act in complexes**, and the complex sets the histone target: e.g. GCN5 in **SAGA** (yeast) / **STAGA–TFTC** (human) acetylates H3 (and H2B);
- **GCN5 does more than acetylation:** it can also transfer other acyl groups (e.g. propionyl, butyryl, succinyl), so one enzyme can write several kinds of histone mark.
- **67 new marks:** a mass-spectrometry paper identified 67 new histone modifications, including lysine crotonylation (Tan et al., Cell 2011); for most of them the function is unknown.
- **Self-maintenance:** a diacetylated tail keeps a **bromodomain-containing HAT (or reader) bound close by**; the enzyme **acetylates neighboring nucleosomes**, which helps keep the state through the cell lineage.

##### **CBP/p300**

- Two large paralogs (**CBP 2,441 aa**, **p300 2,414 aa**) with high identity in the functional domains (up to 93%). Domains: **CH1 (TAZ1)**, **KIX** (binds phosphorylated CREB), **bromodomain**, **HAT domain**, **CH2** (PHD), **CH3** (TAZ2/ZZ; ADA2 homology); nuclear-receptor interaction at the N-terminus, SRC-1 at the C-terminus.
- They bind **hundreds of partners**: nuclear receptors, CREB, p53, STATs, JUN/FOS, MYB, NF-κB p65, HIF1, MYOD, GATA1, YY1, the basal factors TBP and TFIIB, and viral oncoproteins (E1A, SV40 T antigen, HPV E6/E7, HTLV Tax). So CBP/p300 are **coactivators and integrators**: they bridge many TFs to the basal machinery and acetylate histones (H3K27ac, link to enhancers in sections 2 and 10) and non-histone proteins.
- **Rubinstein–Taybi syndrome:** point mutations or microdeletions in **CREBBP** or **EP300** (haploinsufficiency); intellectual disability, broad thumbs and big toes, characteristic face. It shows that the **dose** of a coactivator matters.
- **Link to \[VB25\]:** for p300/CBP, PROTAC degradation works better than enzymatic inhibitors; KAT2A null vs catalytic-dead mice are compared in section 16.

#### **Histone deacetylases (HDACs)**

- ![[IG-image18.png|339]]**Zn²⁺-dependent HDACs:** **Class I** (HDAC1, 2, 3, 8; Rpd3-like, nuclear, ubiquitous), **Class IIa** (HDAC4, 5, 7, 9; shuttle between nucleus and cytoplasm, tissue-specific), **Class IIb** (HDAC6, two catalytic domains, cytoplasmic, tubulin deacetylase; HDAC10), **Class IV** (HDAC11).
- **Class III = sirtuins** (Sir2-like): **NAD⁺-dependent**, so deacetylation is coupled to the metabolic state of the cell.
- **Reaction:** acetyl-lysine + NAD⁺ → lysine + nicotinamide + 2′-O-acetyl-ADP-ribose. Some sirtuins instead transfer the ADP-ribose to the protein (mono-ADP-ribosyltransferase). The bacterial homolog CobB regulates acetyl-CoA synthetase.
- **Inhibitors and selectivity:** SAHA (vorinostat), TSA, PXD101 (belinostat), LBH589 (panobinostat), LAQ824 → pan-inhibitors (classes I, II, IV); valproic acid, butyrate, trapoxin → classes I and IIa; MS-275 (entinostat) → HDAC1–3; depsipeptide (romidepsin) → HDAC1–2; SB-379872-A → HDAC8; tubacin → HDAC6.
- **Therapy link:** a TF complex (TFC) at an HDAC-sensitive promoter recruits an HDAC, and the promoter is silent. An HDAC inhibitor lets a HAT act instead: histones are acetylated, transcription turns on and leads to cell-growth arrest, differentiation and apoptosis. This is the rationale for HDAC inhibitors in cancer (limits in section 16). It also shows the order of events: chromatin relaxation (acetylation, remodeling) comes before TFs can act on their sites.
- **Link to \[VB25\]:** HDAC3 is essential for development mainly as a scaffold rather than as an enzyme (section 16).

### Histone methylation

- **Chemistry:** HMTs transfer a methyl group from **S-adenosyl-L-methionine (SAM)**, which becomes S-adenosyl-L-homocysteine (SAH). Lysine: mono-, di- or tri-methyl. Arginine (PRMTs): mono-methyl, then **symmetric** or **asymmetric** di-methyl.
- **No charge change** (unlike acetylation): methylation acts mainly by **recruiting readers**, and its meaning depends on the **residue** and the **degree of methylation**. Turnover is slower than for acetylation, which suits methylation to long-term states and epigenetic memory.
- **Active marks:** H3K4me3 (promoters), H3K4me1 (enhancers), H3K36me3 (bodies of transcribed genes), H3K79me. **Repressive marks:** H3K9me3 (constitutive heterochromatin, read by HP1), H3K27me3 (Polycomb, facultative heterochromatin), H4K20me3.
- **Erasers** (exam question): methylation was long thought permanent, because the methyl–lysine bond is very **stable** and methyl groups **turn over** at about the **same rate as the histones themselves** (removal only by histone exchange or dilution at replication); the demethylases found later are in the comparison table at the end of this section.
- Most lysine HMTases contain a **SET domain** (named after Su(var)3-9, Enhancer of zeste, Trithorax). Exception: **DOT1L** (H3K79) has no SET domain.

### Repression vs silencing

**Both switch a gene off**, but only silencing is strictly epigenetic, because it is inherited through cell division without the signal that started it.

**Repression** targets one gene (or a set of genes) carrying a binding site for a **sequence-specific repressor** at the promoter/enhancer, which recruits corepressors (HDAC, Sin3, NCOR/SMRT) for local deacetylation of a few nucleosomes; it is graded, reversible and continuously dependent on the signal, so **when the repressor leaves the gene turns on again** and the off state must be re-established in every cell cycle (e.g. HDAC-sensitive promoters, inducible genes).

**Silencing** instead targets a **chromatin region** and switches off **any gene placed there** (position effect): it **starts (nucleates) at** **specific DNA elements**, such as silencers in yeast, repetitive sequences or Polycomb response elements (PREs), and then **spreads along the chromatin fibre by a read–write loop** (a protein that reads the mark recruits the enzyme that writes it on the next nucleosome) until it reaches a **boundary**; the spread region is kept compact by structural heterochromatin proteins; it is self-maintaining, all-or-none and often variegated per cell, and is inherited through mitosis because the marks are copied in cis, like imprinting and CpG-island methylation in cancer. Silenced heterochromatin can be **constitutive** or **facultative**.

Experimentally, a repressed gene comes back when the repressor or signal is removed while a **silenced one stays off for several divisions**, and silencing affects any reporter moved into the region.

The two form a continuum: a repressor that recruits writers of self-propagating marks can turn a transient signal into a stable state, while poised (bivalent) genes sit in between, off but ready to be activated (section 13).

#### **Position-effect variegation (PEV) in Drosophila**

![[IG-image19.png|348]]PEV is the classic genetic model of heterochromatin-mediated **silencing**: a gene with an unchanged sequence is ON in some cells and OFF in others, only because of where **it sits relative to heterochromatin**.

##### **The phenomenon**

- **Discovery:** H. J. Muller (1930) obtained flies with mottled eyes among X-ray-induced chromosome rearrangements.
- **Classic allele:** *In(1)w*<sup>m4</sup> (white-mottled 4), an inversion of the X chromosome with **one breakpoint next to *white*** and the **other in the pericentric heterochromatin**. *white⁺* (needed for the red pigment of each ommatidium) and the nearby *roughest⁺* (*rst⁺*) are moved **from euchromatin** to the **border of heterochromatin**. The *white* sequence is intact; only its position has changed.
- **Phenotype:** the eye has red patches (*white* ON) and white patches (*white* OFF). Each patch is a **clone**: the ON/OFF choice is made in eye precursor cells during development and is then inherited by **all their descendants**. Early choices give large patches, late choices small ones.
- **Mechanism:** heterochromatin **spreads in cis** from the breakpoint into the neighboring euchromatin. How far it spreads differs from cell to cell (stochastic), so a gene **close to the breakpoint is silenced more often than a distant one**, and a distant gene is silenced only together with the closer ones (polarized spreading).
- **The silenced copy is real heterochromatin:** H3K9 methylation, HP1, compact and nuclease-resistant chromatin, late replication. The rearranged region can also be pulled into the heterochromatic compartment of the nucleus (chromocenter), so nuclear position contributes too.

##### **Modifiers: Su(var) and E(var)**

- ![[IG-image20.png|316]]Genetic screens for **dominant** modifiers of *w*<sup>m4</sup> found well over a hundred loci.

> **Su(var)** = suppressor of variegation: the mutation makes the eye redder (less silencing).
>
> **E(var)** = enhancer of variegation: the eye becomes whiter (more silencing).

- **Su(var)2-5 = HP1:** chromodomain that binds H3K9me2/3 and chromoshadow domain that dimerizes and binds partners. **Su(var)3-9 = H3K9 methyltransferase** (SET domain; homolog of human SUV39H1 and *S. pombe* Clr4). **Su(var)3-7:** zinc-finger protein that binds HP1 and heterochromatin.
- **Slide summary (IG4):** wild type → no variegation; *white*-mottled → variegation; *white*-mottled + *Su(var)205* (= *Su(var)2-5*, HP1 mutant) → variegation **suppressed**; *white*-mottled + HP1 overexpression → variegation **enhanced**.

##### **Dosage dependence: the key logic**

- **Haplo-suppressors / triplo-enhancers:** with one mutant copy (*Su(var)/+*) there is less protein, heterochromatin spreads less and the eye is redder; with an extra transgenic copy (*P\[Su(var)\]*) there is more protein, heterochromatin spreads further and the eye is whiter. The slide figure (Schotta et al. 2002) shows this for Su(var)3-9, Su(var)2-5 and Su(var)3-7.
- **Meaning:** heterochromatin proteins are **limiting** and assemble cooperatively, so the amount of protein decides how far the silent domain extends (mass action). This is why the modifiers are dominant.
- **Extra heterochromatin suppresses PEV:** the Y chromosome is almost entirely heterochromatic. *w*<sup>m4</sup> males without a Y (X/0) have strongly variegated, almost white eyes; adding a Y (or other heterochromatin) makes them redder, because the extra heterochromatin titrates the limiting proteins away from the *white* breakpoint.
- **Temperature:** high temperature during development suppresses variegation, low temperature enhances it.

##### **Molecular explanation**

- **Read–write loop:** the cycle that lets heterochromatin **spread along the fibre** and be rebuilt after division (memory, section 13). Step by step:

1.  HDACs **remove the acetyl** groups from the H3 tail.
2.  SU(VAR)3-9 (the “writer”) **methylates** H3K9.
3.  HP1 (the “reader”) binds the methyl mark through its **chromodomain**.
4.  HP1 **recruits more SU(VAR)3-9**, which **methylates the neighboring** nucleosome.
5.  The cycle repeats: heterochromatin advances along the fibre and, after cell division, is rebuilt.

- **Role of the chromodomain:** it is the link between the written mark (H3K9me) and the protein that silences and spreads. Without the chromodomain, HP1 **cannot find heterochromatin** and the loop breaks. This is seen in Su(var)3-9 null flies: H3K9 methylation is lost from the chromocenter, so HP1 has nothing to grab and is mislocalized (Schotta et al. 2002).
- **Link to \[R00\] (below):** the human homolog SUV39H1 is the first histone methyltransferase identified, specific for H3K9; this gives the biochemical basis of the Su(var)3-9 phenotype.

##### **Why PEV matters**

- It shows that expression depends on **chromatin context**, not only on DNA sequence, and that the OFF state is **clonally inherited** without any change in DNA: a textbook epigenetic phenomenon.
- The genes found in PEV screens are conserved: HP1 (human CBX5/CBX1/CBX3 = HP1α/β/γ), SUV39H1/2.
- **Same principle elsewhere:** telomere position effect in yeast (Sir proteins silence genes placed near telomeres), and variable or silenced transgenes in mammals depending on the integration site. This is why vectors for transgenesis and gene therapy use **insulators/boundary elements**.

### Experiment \[R00\]: SUV39H1 is a site-specific H3 methyltransferase

- **Idea:** human SUV39H1 (412 aa), homolog of Su(var)3-9 (fly) and Clr4 (S. pombe), has an N-terminal chromodomain and a C-terminal SET domain (flanked by pre-SET and post-SET). The SET domain weakly resembles a plant Rubisco methyltransferase, so it could be an HMTase.
- **Assay:** histones + S-adenosyl-\[methyl-¹⁴C\]-L-methionine → ¹⁴C-methyl-histone + SAH; SDS-PAGE (Coomassie for loading) and a fluorogram to see the radioactive histone.
- **(a) Co-IP:** myc-tagged full-length SUV39H1 immunoprecipitated from cells carries HMTase activity on **H3**; the chromodomain-only construct does not.
- **(b) Recombinant protein:** GST–Suv39h1 (aa 82–412) from E. coli methylates H3 dose-dependently; GST–chromodomain does not → the activity is intrinsic to the protein.
- **(c) Mutants:** deleting the NHSC or GEEL motifs, the post-SET tail or the pre-SET cysteines, or the point mutants H324K and C326A, abolishes activity; H320R is hyperactive (only 10% loaded).
- **Specificity of the family:** CLR4 and Suv39h2 fragments also methylate H3; the SET fragments of EZH2 and HRX/MLL are inactive here (EZH2 needs PRC2).
- **Which histone and which residue?** Only H3 is methylated (weak H1 signal), and among N-terminal peptides only the H3 peptide. Edman degradation of methylated H3(1–20) releases the radioactivity at cycle 9 → H3K9.
- **Edman degradation, step by step.** (1) Coupling: at mildly alkaline pH, phenyl isothiocyanate (PITC) labels the free α-amino group of the N-terminal residue (PTC-peptide). (2) Cleavage: anhydrous acid (TFA) cuts the bond after the labeled residue, which leaves and is converted into a stable PTH-amino acid. (3) The peptide, now one residue shorter, has a new free N-terminus, and the cycle repeats.
- **Reading the product:** each PTH-amino acid is identified by HPLC (retention time vs standards). In \[R00\] what matters is which cycle carries the radioactivity: for the H3(1–20) peptide (A-R-T-K-Q-T-A-R-K-S…) methylated with radiolabeled SAM, the big peak is at cycle 9 = K9; the small signal at cycle 10 is carry-over, since each cycle is slightly less than 100% efficient.
- **What Edman gives and its limits:** it reads from the N-terminus, so on a short, pure peptide it gives the exact position of the mark; it needs a free (unblocked) N-terminus and works for ~30–50 residues, because per-cycle losses add up.
- **Ser10 crosstalk (synthetic peptides).** S10ph blocks K9 methylation by SUV39H1 (≈ 0%), and K9me reduces S10 phosphorylation by Aurora (≈ 35%) → mutually exclusive marks: silencing (HP1) vs mitosis/activation.
- **Conclusion:** H3K9 methylation by SUV39H1 creates a binding site for the **HP1 chromodomain** → heterochromatin; this explains, at the molecular level, why Su(var)3-9 and HP1 are dose-dependent suppressors of PEV.

### Readers: domains that bind modified histones

| **Domain** | **Target** | **Function** |
|:---|:---|:---|
| Bromo | Acetylated histones | Transcription, repair, replication, condensation |
| Chromo | Methylated H3 (K9, K27, K36) | Silencing (HP1 on K9me3, Polycomb on K27me3) or activation |
| PHD | Methylated H3 (K4) | Activation |
| Tudor | Methylated H4 (K20), H3 (K4) | DNA repair, transcription |
| PWWP | Methylated histones/DNA? | Unclear |
| MBT | Methylated H4 (K20) | DNA repair |

- **Multivalent reading.**
  - *Intranucleosomal:* one protein reads two marks on the **same tail** (*cis*, e.g. the double bromodomain of TAF1, the TBP-associated factor of TFIID, on two acetyl-lysines of H4, which anchors TFIID at the promoter) **or on two tails of the same nucleosome** (*trans*, e.g. BPTF: PHD on H3K4me3 + bromodomain on H4ac); oligovalent complexes combine several readers.
  - *Internucleosomal:* HP1 dimers bridge H3K9me on **adjacent or distant nucleosomes**, which **compacts heterochromatin**.

### Acetylation vs methylation at a glance

| **Feature** | **Acetylation** | **Methylation** |
|:---|:---|:---|
| Donor | Acetyl-CoA | SAM (→ SAH) |
| Residues | Lysine | Lysine (me1/2/3), arginine (me1, me2s, me2a) |
| Charge | Neutralizes lysine (+ → 0) | Unchanged |
| Writers | HATs/KATs: GNAT, MYST, CBP/p300 | SET-domain HMTs, DOT1L, PRMTs |
| Erasers | HDACs (Zn²⁺), sirtuins (NAD⁺) | LSD1 (FAD), JmjC (Fe²⁺/α-KG); PADI4 for arginine |
| Readers | Bromodomain | Chromo, PHD, Tudor, MBT, PWWP |
| Output | Generally activating | Activating or repressive, depending on the site |
| Turnover | Fast, dynamic | Slower, more stable |

---
> [[IG 05 - Chromatin and remodeling|← Chromatin and remodeling]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 07 - Histone variants, the histone code and epigenetic memory|Histone variants, the histone code and epigenetic memory →]]
