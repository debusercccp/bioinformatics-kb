---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 5
tags: [note, ig]
---

> [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|← Genomic imprinting + Enhancer RNAs (eRNAs)]] · [[Integrative Genomics|↑ Integrative Genomics]]

# Chromatin and remodelling

### The historical logic

- Biochemistry of the ’80s–’90s: in vitro reconstitution defined activators and the pre-initiation complex (PIC). Example: **Gal4** must **pre-bind its sites to recruit the machinery and helps re-initiation**.
- Problem: transcription **in vitro is inhibited when the template is nucleosomal** rather than naked DNA. So chromatin is not neutral; it is a regulated barrier (“the chromatin player”, Kornberg).
- Histones: small (10–23 kDa), basic, highly conserved; they pack ~2 m of DNA into a nucleus of ~90 fL (~6 µm diameter). Nucleosome = DNA wrapped around a histone octamer.

### PIC and nucleosome packing

**Gal4**: one of the major TFs in yeast.

- ![[IG-image14.jpeg|188]]*Gal4/PIC reconstitution.* In vitro steps in the figure: (i) **Gal4 binds its sites** upstream of a TATA promoter; (ii) incubate with Gal4 and TFIID (TBP); (iii) wash; (iv) add the other factors and RNA polymerase; (v) add NTPs; (vi) assay the transcript by primer extension. Reading: pre-binding by Gal4 is needed to recruit the machinery, and Gal4 also supports **re-initiation** (the scaffold left on the promoter fires again).
- *Hierarchy of packaging.* DNA double helix (2 nm) → nucleosome “beads on a string” (~11 nm) → 30-nm fibre → ~300-nm looped fibre → ~700-nm condensed fibre → ~1,400-nm metaphase chromosome.
- *Nucleosome.* Core octamer: two each of H2A, H2B, H3, H4. Linker histone H1 seals the entry/exit DNA; the figure shows fully folded, partially folded and unfolded fibre states. ~2 m of DNA per diploid cell must fit a ~90 fL nucleus (~6 µm diameter).
- *Structural methods.* A cryo-EM slide and EM class averages with angular reconstitution of the 70S ribosome (*Structure* 1995) show how large complexes such as nucleosomes and remodellers are resolved. They are method illustrations, not part of the regulatory argument.

Naked DNA does not exist in vivo. And the chromatin is organized in fractals.

> “The Gal4 transcription factor is a positive regulator of gene expression of galactose-induced genes. This protein represents a large fungal family of transcription factors, Gal4 family, which includes over 50 members in the yeast *S. cerevisiae* e.g. Oaf1, Pip2, Pdr1, Pdr3, Leu3.” — From Wikipedia, The Free Encyclopedia \<3

### The mechanism of mating-type switching (gene conversion)

Yeasts have sexual dimorphism: we have the **α** strain and the **a** strain. If you have haploid cells, they must have the opposite mating type and they reproduce forming a diploid cell with an undefined gender. Then, once they form the spore, the diploid cells do meiosis, and they give birth to 2 **α** cells and 2 **a** cells.

If a haploid yeast cell (e.g., type a) needs to switch to the opposite mating type (α), it undergoes a directional genetic conversion at the active MAT locus. The cell maintains two silent, inactive storage cassettes (HMLα and HMRa) located elsewhere on the chromosome.

This switch is a specialized form of gene conversion that unfolds in specific biochemical steps:

1.  **Cleavage:** The HO endonuclease recognizes a specific DNA sequence at the active MAT locus and induces a double-strand break (DSB).
2.  **Resection:** The broken DNA ends undergo a 5′→3′ resection to create single-stranded tails.
3.  **Strand invasion:** Driven by a recombinase (such as Rad51), the single-stranded tail invades the opposite silent cassette to use it as a template.
4.  **Overwriting:** The genetic information from the silent cassette is copied and substituted into the MAT locus. This is a non-reciprocal transfer: the donor cassette remains completely unchanged, while the old MAT sequence is permanently overwritten.

#### **Directionality and the Recombination Enhancer (RE)**

To successfully switch to the opposite sex, the recombinase must actively choose the correct silent cassette. This choice is dictated by the Recombination Enhancer (RE):

- In MATa cells, the RE strongly biases the repair machinery to use the HMLα cassette (~85–90% of the time) rather than HMRa (~10–15%).
- If the RE is deleted (REΔ), this directionality flips almost entirely, resulting in the cell choosing HML only ~5–10% of the time and incorrectly choosing the already-matching HMR ~90–95% of the time.

#### **Gene conversion in meiosis**

Mating type switching is a form of **gene conversion**: a **double-strand break** is **repaired** by copying the information of a **homologous donor**. In **meiosis**, the break is made by a **Spo11 homodimer**, the 5′ ends are resected (5′→3′ resection), the 3′ end invades the homologous chromosome (strand invasion) and, after further processing, the **copied region gives non-Mendelian ratios in the spores**, such as 5:3 and 6:2 instead of 4:4 \[note: the ratios refer to the 8 spores of an octad (e.g. in *Sordaria* or *Neurospora*), so 6:2 is a conversion of a whole chromatid and 5:3 a conversion of a single strand (post-meiotic segregation)\]; this happens because gene conversion is a **non-reciprocal transfer of information**.

### Genetics of SWI/SNF (Herskowitz)

The link between **chromatin** and **transcription** came from **yeast genetics** (**Ira Herskowitz**, 1946–2003, UCSF):

- **SWITCH = SWI**: mutants that **block mating type switching**, because they are **defective** in the transcription of the **site-specific HO recombinase** required for mating type switching \[note: HO is a site-specific endonuclease, not a recombinase: it makes a double-strand break at the MAT locus, which is then repaired with the silent copy of the other mating type\]; **without HO**, the **double-strand break** is never made.
- **SUCROSE NON FERMENTING = SNF**: mutants that **cannot use/ferment sucrose** as a carbon source, because they are **defective** in the transcription of the genes that produce the **enzymes to catabolize sucrose** (e.g. SUC2, which encodes the invertase).

These two classes of mutant phenotypes fall in the **same complementation group**; in other words, they are caused by the **same mutated genes**: SWI and SNF mutants partly overlap, e.g. SWI2 = SNF2, and their products form the same complex (SWI/SNF). So, the **same genes** control the transcription of **unrelated targets**, which means that they are **general regulators** of transcription. Suppression screens reveal that **suppressor mutations** occur **within histone genes**, and amino acid **substitutions** in histones **H3** and **H4 relieve the requirement** of swi2/snf2 for transcription.

#### **The SWI phenotype and suppressor genetics**

The SWI mutants (named because they cannot switch mating types) fail to execute this process because they **cannot transcribe the HO gene**. Without the HO endonuclease, the initial double-strand break is never made.

The biology of the SWI/SNF regulatory complex was mapped using suppressor screens, a genetic logic tool used to prove that two proteins physically interact:

- **Wild type:** both gene products work normally (m+, s+) to form an active complex.
- **First mutation (m):** mutating one gene breaks the interaction, rendering the complex inactive.
- **Second mutation (s — suppressor):** a subsequent mutation in a second interacting gene (e.g., a structural change in a histone) compensates for the first defect. This restores the interaction or bypasses the need for the first gene entirely, restoring activity. (Note: the suppressor mutation alone in a wild-type background would typically render the complex inactive.)

![[IG-image15.png|602]]

**Logic of genetic interaction (charge example):**

- gene A product (+Lys) and gene B product (–Asp) interact;
- mutating A (→ Glu) breaks the interaction (Glu–Asp repel);
- a **suppressor mutation in B** (→ Arg, +) restores it;
- so a suppressor in a *different* gene suggests the two proteins physically interact. Applied here: SWI/SNF works on histones/nucleosomes; histone mutations compensate for lack of SWI/SNF.

**How does a suppressor screen work?** It generally follows these steps:

- *Create or identify a mutant:* researchers begin with a cell carrying a mutation that produces a recognizable defect, such as an inability to switch mating types.
- *Introduce additional mutations:* they expose the cells to mutagens or use another mutagenesis strategy to generate mutations in other genes.
- *Select for restored function:* they look for cells in which the original defect has been partially or completely rescued.
- *Identify the suppressor gene:* they determine which additional mutation is responsible for the restoration.
- *Study the relationship between the genes:* they investigate how the two genes contribute to the same biological process.

### Step by step: SWI/SNF remodelling

- **Targeting.** A sequence-specific TF (the slides show **c-Myc and p53**) binds its site and recruits the SWI/SNF (BAF) complex: ATPase **BRG1** plus BAF250, BAF170, BAF155, BAF60, BAF57, BAF53, hSNF5/BAF47.
- **ATP hydrolysis.** BRG1 uses ATP → ADP + Pi.
- **Remodelling.** The energy repositions the nucleosome (sliding, histone ejection or exposure of DNA), disrupting histone–DNA contacts.
- **Access.** DNA that was wrapped becomes accessible; further TFs, the PIC and Pol II can bind.
- **Outcome.** The promoter/enhancer becomes open (DNase-hypersensitive) and transcription proceeds.

The next step: once the nucleosomes are moved, **TBP/TFIID, other general factors and Pol II assemble** at the exposed promoter (the PIC), which closes the loop. Typical teaching figure: c-Myc/p53 recruit the complex; BRG1 hydrolyses ATP (ADP + Pi); the nucleosome next to the TF site is repositioned; the PIC forms.

### How it was shown biochemically (Peterson lab figures)

- **Purification** of the complex through successive columns: Ni2+-NTA (affinity), Mono-Q (ion exchange), Superose 6 (size exclusion/gel filtration) — purification of SWI2-HA-6HIS-tagged SWI/SNF.
- **EMSA (gel shift):** a **labelled probe** is **incubated** with a **protein** and the complexes are **separated on a native gel**: the **free probe runs fast**, the **probe** bound by the **protein runs slower** (**shift**), and the addition of an **antibody** against the protein **slows it further** (**supershift**). An unlabelled specific competitor abolishes the shift, while a mutant or non-specific competitor doesn’t.
- **In vitro footprinting:** a **DNA fragment** labelled at one end is **digested by DNase I** with or without the DNA-binding protein, with about **one cut per molecule**; the fragments are **separated on a gel** next to the sequencing lanes, and the region bound by the protein is **protected from cleavage**, so it appears as a **gap** in the ladder (footprint).

#### **SWI/SNF promotes GAL4-AH binding to its own cognate site in the nucleosome**

A nucleosome containing a GAL4 site was incubated with GAL4-AH, with or without SWI/SNF and ATP:

- GAL4-AH alone binds the naked DNA (G-AH/DNA band) but binds the nucleosome only poorly;
- With SWI/SNF and ATP, the G-AH/nucleosome complex forms, and it increases with the amount of SWI/SNF (lanes 6 and 8);
- Without SWI/SNF, much higher concentrations of GAL4-AH (30–100 nM) are needed to obtain the same complex (lanes 10–11).

The stimulation also appears at lower GAL4-AH concentrations, it requires a hydrolysable ATP (because ATP-γ-S doesn’t work), and it occurs with different GAL4 derivatives: GAL4(1–94) (only the DNA-binding domain), GAL4-VP16 and GAL4-AH; so SWI/SNF doesn’t need the activation domain of the factor: it acts on the nucleosome, using the energy of ATP hydrolysis. However, the EMSA shows that a complex forms, but it doesn’t show where exactly the protein binds, nor whether the nucleosome has been rearranged: for this, the footprinting is needed.

DNase I footprinting confirms the result: on naked DNA, GAL4-AH protects its site already at low concentrations, while on the nucleosome it protects the site only at very high concentrations; with increasing amounts of SWI/SNF, the footprint on the nucleosomal GAL4 site appears at lower GAL4-AH concentrations. Also, the DNase I pattern of the nucleosome itself changes, which shows that the nucleosome is really rearranged, and not simply displaced, and that GAL4-AH binds on the nucleosome.

The same result is obtained in other conditions, where the GAL4 site is protected on the nucleosome only with SWI/SNF and ATP.

Finally, a SWI/SNF complex with a mutant SWI2 subunit (K798A, in the ATPase domain) is assembled normally and co-elutes on Superose 6, but it has a much lower ATPase activity than the wild type and doesn’t stimulate GAL4-AH binding to the nucleosome: so, the ATPase activity of SWI2 is necessary for the remodelling.

### Histone modifications

- Kornberg, Grunstein and Allis are the names on (nucleosome structure, histone function in transcription, histone acetylation and acetyltransferases).
- **General mechanism:** **acetylation** of lysine on histone tails (by HATs such as p300/CBP) neutralises the positive charge, loosens histone–DNA contact, and creates binding sites for **bromodomain readers** (BRD4); deacetylation by HDACs reverses this. H3K27ac and H3K4me1 therefore mark active enhancers, which links back to the enhancer sections above.
- *Table:* types of modification on core histones — lysine: methylation, acetylation, ubiquitination, sumoylation, ADP-ribosylation; arginine: methylation; serine and threonine: phosphorylation. DNA bases: C5-methylcytosine and C5-hydroxymethylcytosine.
- *Acetylation:* lysine’s side chain NH3+ is positively charged; **KATs** (histone acetyltransferases) convert it to acetyl-lysine (neutral), **HDACs** reverse it.
- *Chromatin architecture:* deacetylated nucleosomes (HDAC) form compact arrays with histone tails close to DNA; acetylation (HAT) spaces them out, loosening the fibre so factors can reach DNA.
- *Therapy link:* a TF complex (TFC) at an HDAC-sensitive promoter recruits an HDAC; the promoter is silent. An **HDAC inhibitor** lets a HAT act instead, histones acetylate, transcription turns on and leads to cell-growth arrest, differentiation and apoptosis — the rationale for HDAC inhibitors in cancer.

## 12. Cautions and corrections to keep in mind

- **eRNA “necessary”:** in the literature the necessity differs by locus; correlation of eRNA with mRNA is not causal.
- **Size of 2D-eRNAs:** \<150 nt in \[W26\], not \<500.
- **Histone mark ratio:** high H3K4me1/H3K4me3, not high H3K4me3.
- **Number of enhancers:** ~1,000,000 candidates (\[SF19\]) vs \>400,000 (ENCODE, \[W26\]).
- **“Contacts in all TADs”:** TAD boundaries are leaky; CTCF/cohesin removal changes few genes.
- **Mark-based enhancer calls overestimate real enhancers:** only ~12% of H3K27ac peaks work in an MPRA in hESCs, and 41–48% of candidate enhancers fail in VISTA in vivo assays \[SF19\].

---
> [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|← Genomic imprinting + Enhancer RNAs (eRNAs)]] · [[Integrative Genomics|↑ Integrative Genomics]]
