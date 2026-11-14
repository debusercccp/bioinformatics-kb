---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 5
tags: [note, ig]
---

> [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|← Genomic imprinting + Enhancer RNAs (eRNAs)]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 06 - Histone acetylation and methylation|Histone acetylation and methylation →]]

# Chromatin and remodeling

### The historical logic

- Biochemistry of the ’80s–’90s: in vitro reconstitution defined the activators and the pre-initiation complex (PIC, section 2).
- Problem: transcription in vitro is **inhibited when the template is nucleosomal** rather than naked DNA, because the histones cover the promoter and the TF sites, so Gal4, the PIC and Pol II cannot reach the DNA. Chromatin is therefore not neutral: it is a **regulated barrier** (“the chromatin player”, Kornberg) and the histones are **regulatory elements**, not only packaging.
- Histones: small (10–23 kDa), basic, highly conserved proteins (packaging and nucleosome structure below).

### ![[IG-image13.jpeg|188]]PIC and nucleosome packing

**Gal4**: one of the major TFs in yeast.

- *Gal4/PIC reconstitution.* In vitro steps in the figure: (i) **Gal4 binds its sites** upstream of a TATA promoter; (ii) incubate with Gal4 and TFIID (TBP); (iii) wash; (iv) add the other factors and RNA polymerase; (v) add NTPs; (vi) assay the transcript by primer extension. Reading: pre-binding by Gal4 is needed to recruit the machinery, and Gal4 also supports **re-initiation** (the scaffold left on the promoter fires again).
- *Nucleosome.* Core octamer: two each of H2A, H2B, H3, H4. Linker histone H1 seals the entry/exit DNA; the figure shows fully folded, partially folded and unfolded fiber states. ~2 m of DNA per diploid cell must fit a ~90 fL nucleus (~6 µm diameter).

Naked DNA does not exist in vivo. And the chromatin is organized in fractals.

> “The Gal4 transcription factor is a positive regulator of gene expression of galactose-induced genes. This protein represents a large fungal family of transcription factors, Gal4 family, which includes over 50 members in the yeast *S. cerevisiae* e.g. Oaf1, Pip2, Pdr1, Pdr3, Leu3.” — From Wikipedia, The Free Encyclopedia \<3

### The mechanism of mating-type switching (gene conversion)

The yeast silent mating-type cassettes are the system in which the link between **histone hypoacetylation** and **silencing** was first shown.

**Paper — Braunstein et al., 1993** (Genes Dev 7:592–604): the paper that tied silencing to the histones — the silent mating-type cassettes and the telomeric regions of yeast carry nucleosomes with strongly reduced acetylation of the H2B, H3 and H4 tails, and the hypoacetylated domain has the same extent as the silenced one and depends on the SIR genes.

Yeasts have sexual dimorphism: we have the **α** strain and the **a** strain. If you have **haploid** cells, they must have the **opposite** mating type and they reproduce forming a **diploid** cell with an undefined gender (2 **α** and 2 **a**). Then, once they form the spore, the diploid cells do **meiosis**, and they give birth to 2 **α** cells and 2 **a** cells.

If a haploid yeast cell (e.g., type **a**) needs to switch to the opposite mating type (**α**), it undergoes a directional genetic conversion at the active MAT locus (playback slot). The cell maintains two silent, inactive storage cassettes (HMLα and HMRa) located elsewhere on the chromosome.

The HO endonuclease is a site-specific DNA endonuclease (encoded by the HO gene) that makes a **single double-strand break** at the MAT locus (playback slot), starting the switch. It is expressed only in mother cells, in late G1, so only mother cells switch mating type.

This switch is a specialized form of gene conversion that unfolds in specific biochemical steps:

1.  **Cleavage:** The HO endonuclease recognizes a specific DNA sequence at the active MAT locus (playback slot) and induces a double-strand break (DSB).
2.  **Resection:** The broken DNA ends undergo a 5′→3′ resection to create single-stranded tails.
3.  **Strand invasion:** Driven by a recombinase (such as Rad51), the single-stranded tail invades the opposite silent cassette to use it as a template.
4.  **Overwriting:** The genetic information from the silent cassette is copied and substituted into the MAT locus (playback slot). This is a **non-reciprocal transfer**: the donor cassette remains **completely unchanged**, while the old MAT (playback slot) sequence is permanently overwritten.

#### **Directionality and the Recombination Enhancer (RE)**

To successfully switch to the opposite sex, the recombinase must actively choose the correct silent cassette. This choice is dictated by the Recombination Enhancer (RE):

- ![[IG-image14.png|310]]In **MATa** cells, the RE strongly biases the repair machinery to use the **HMLα cassette** (~85–90% of the time) rather than HMRa (the cassette) (~10–15%).
- If the RE is **deleted** (REΔ), this directionality flips almost entirely, resulting in the cell choosing HML (the cassette) only ~5–10% of the time and incorrectly choosing the already-matching HMR (the cassette) ~90–95% of the time.

#### **Gene conversion in meiosis**

Mating type switching is a form of **gene conversion**: a **double-strand break** is **repaired** by copying the information of a **homologous donor**. In **meiosis**, the break is made by a **Spo11 homodimer**, the 5′ ends are resected (5′→3′ resection), the 3′ end invades the homologous chromosome (strand invasion) and, after further processing, the **copied region gives non-Mendelian ratios in the spores**, such as 5:3 and 6:2 instead of 4:4 \[note: the ratios refer to the 8 spores of an octad (e.g. in *Sordaria* or *Neurospora*), so 6:2 is a conversion of a whole chromatid and 5:3 a conversion of a single strand (post-meiotic segregation)\]; this happens because gene conversion is a **non-reciprocal transfer of information**.

### Genetics of SWI/SNF (Herskowitz)

The link between **chromatin** and **transcription** came from **yeast genetics** (**Ira Herskowitz**, 1946–2003, UCSF):

- **SWITCH = SWI**: mutants that cannot switch mating type because they cannot transcribe the HO gene. HO is the endonuclease that starts switching: it makes the double-strand break at MAT (playback slot), and switching then happens by gene conversion from HML or HMR (the cassettes); without HO the break is never made.
- **SUCROSE NON-FERMENTING = SNF**: mutants that **cannot use/ferment sucrose** as a carbon source, because they are **defective** in the transcription of the genes that produce the **enzymes to catabolize sucrose** (e.g. SUC2, which encodes the invertase).

These two classes of mutant phenotypes fall in the **same complementation group**; in other words, they are caused by the **same mutated genes**: SWI and SNF mutants partly overlap, e.g. SWI2 = SNF2, and their products form the same complex (SWI/SNF). So, the **same genes** control the transcription of **unrelated targets**, which means that they are **general regulators** of transcription. Suppression screens reveal that **suppressor mutations** occur **within histone genes**, and amino acid **substitutions** in histones **H3** and **H4 relieve the requirement** of swi2/snf2 for transcription.

#### **The SWI phenotype and suppressor genetics**

The biology of the SWI/SNF regulatory complex was mapped using **suppressor screens**, a genetic logic tool used to prove that **two proteins physically interact**:

**Logic of genetic interaction (charge example):**

- gene A product (+Lys) and gene B product (–Asp) **interact**;
- mutating A (→ Glu) **breaks the interaction** (Glu–Asp repel);
- a **suppressor mutation in B** (→ Arg, +) restores it;
- so a suppressor in a different gene suggests that the two proteins physically interact (the suppressor alone usually gives a defect of its own).

### Step by step: SWI/SNF remodeling

- **Targeting.** A sequence-specific TF (e.g. **c-Myc and p53**) binds its site and recruits the SWI/SNF (BAF) complex: ATPase **BRG1** plus BAF250, BAF170, BAF155, BAF60, BAF57, BAF53, hSNF5/BAF47.
- **ATP hydrolysis.** BRG1 uses ATP → ADP + Pi.
- **Remodeling.** The energy repositions the nucleosome (sliding, histone ejection or exposure of DNA), disrupting histone–DNA contacts.
- **Access.** DNA that was wrapped becomes accessible; further TFs, the PIC and Pol II can bind.
- **Outcome.** The promoter/enhancer becomes open (DNase-hypersensitive) and transcription proceeds.
- **ATP dependence**: remodeling requires ATP hydrolysis and not only ATP binding (the evidence is in “How it was shown biochemically” below).
- **Sliding vs looping:** two models for how SWI/SNF makes nucleosomal DNA behave like naked DNA. Sliding: the **octamer moves along the DNA in cis and uncovers the site**. Looping: the ATPase pumps DNA into the nucleosome, forming a small loop that travels around the octamer and transiently exposes the DNA without moving the octamer.
- **Conservation and cancer:** SWI/SNF is highly conserved among species, and its subunits are mutated in many human cancers (e.g. SMARCB1/SNF5 in rhabdoid tumors, ARID1A, SMARCA4/BRG1).

### How it was shown biochemically (Peterson lab figures)

![[IG-image15.png|366]]**Paper — Côté et al., 1994** (Science 265:53–60): the source of these figures. The purified SWI/SNF complex is made of **10 subunits** and contains the SWI1, SWI2/SNF2, SWI3, SNF5 and SNF6 gene products; it **has DNA-stimulated ATPase activity but no helicase activity**, and it stimulates the binding of GAL4 derivatives to nucleosomal DNA 10- to 30-fold in a reaction that requires ATP hydrolysis but is independent of the activation domain. A mutant SWI2 subunit abolishes the stimulation, the histone-binding protein nucleoplasmin increases it, and a direct ATP-dependent interaction between the complex and nucleosomal DNA was detected: so the primary role of SWI/SNF is to promote activator binding to nucleosomal DNA.

- **Purification** of the complex through successive columns: Ni2+-NTA (affinity), Mono-Q (ion exchange), Superose 6 (size exclusion/gel filtration) — purification of SWI2-HA-6HIS-tagged SWI/SNF.
- **EMSA** (Electrophoretic Mobility Shift Assay gel shift): a **labeled probe** is **incubated** with a **protein** and the complexes are **separated on a native gel**: the **free probe runs fast**, the **probe** bound by the **protein runs slower** (**shift**), and the addition of an **antibody** against the protein **slows it further** (**supershift**). An unlabeled specific competitor abolishes the shift, while a mutant or non-specific competitor doesn’t.

#### What is a DNA footprint?

A **DNA footprint** is the stretch of DNA that a bound **protein** protects from cleavage or chemical attack. It shows **where** the protein sits, at nucleotide resolution, and, if the protein is titrated, **how tightly** it binds. EMSA (above) only says that a complex **forms**; footprinting says **where**.

- **Probe:** a DNA fragment (a few hundred bp) labeled at **one end only** (³²P or a fluorophore), so every band on the gel is defined by its distance from that end.
- **Binding:** the probe is incubated with increasing amounts of protein, on naked DNA or on a reconstituted nucleosome.
- **Partial digestion:** a small dose of DNase I for a short time, so that each molecule is cut on average **once**, at a random position (single-hit conditions).
- ![[IG-image16.png|259]]**Reading:** without protein the cuts **give a continuous ladder**; with the protein bound, DNase I cannot reach the DNA underneath and the bands of that region disappear: **the gap is the** **footprint**. Bands at the edges can become stronger (**hypersensitive** sites), because the protein bends or distorts the DNA.
- **Titration:** the protein concentration at which the footprint appears is a measure of affinity (half-protection ≈ Kd).
- **On a nucleosome:** DNA wrapped on the octamer is cut only where its minor groove faces outwards, about every 10 bp; a positioned nucleosome therefore gives a typical **10-bp periodic ladder**. If this pattern disappears or changes, the nucleosome has been remodeled.
- **Other probes:** hydroxyl radicals (cut at every nucleotide, sequence-neutral, finer resolution), DMS (methylates guanine N7; contact Gs are protected or enhanced), exonuclease III (maps the borders of the bound protein). **In vivo footprinting:** cells are treated with DMS or DNase I and the result is read by ligation-mediated PCR. **Genome-wide:** in DNase-seq or ATAC-seq data a bound TF leaves a dip in cut density at its motif inside an accessible region (computational footprinting).
- **Footprinting vs DNase I hypersensitivity:** both use a nuclease to visualize DNA–protein interaction, but footprinting **maps the exact base pairs covered by a bound protein**, while the hypersensitivity assay **maps open chromatin regions** that are cut more easily.
- **One-base resolution:** the denaturing polyacrylamide gel separates fragments that differ by a single nucleotide; compared with the DNA control reaction, a bound protein that blocks cleavage appears as an empty window (missing bands) in the ladder.

#### **SWI/SNF promotes GAL4-AH binding to its own cognate site in the nucleosome**

![[IG-image17.png|277]]A nucleosome containing a GAL4 site was incubated with GAL4-AH, with or without SWI/SNF and ATP:

- GAL4-AH (GAL4 DNA-binding domain fused to an acidic activation helix) alone **binds the naked DNA** (G-AH/DNA band) but binds the nucleosome only **poorly**;
- **With SWI/SNF and ATP**, the G-AH/nucleosome complex **forms**, and it increases with the amount of SWI/SNF;
- **Without SWI/SNF**, much higher concentrations of GAL4-AH (30–100 nM) are needed to obtain the **same complex**.

The stimulation also appears at **lower GAL4-AH concentrations**, it requires a hydrolyzable ATP (because ATP-γ-S doesn’t work), and it occurs with different GAL4 derivatives: GAL4(1–94) (only the DNA-binding domain), GAL4-VP16 and GAL4-AH; **so SWI/SNF doesn’t need the activation domain of the factor**: it acts on the **nucleosome**, using the **energy of ATP hydrolysis**. However, the EMSA shows that a complex forms, but it doesn’t show where exactly the protein binds, nor whether the nucleosome has been rearranged: for this, the footprinting is needed.

**Footprinting result:** on naked DNA, GAL4-AH protects its site already at ~3–10 nM; on the nucleosome, only at 300–1,000 nM. With increasing SWI/SNF (1.5–6 µl) plus ATP, **the footprint on the nucleosomal GAL4 site appears at much lower GAL4-AH concentrations**, and only when SWI/SNF, GAL4-AH and ATP are all present. The 10-bp DNase I pattern of the nucleosome itself also changes: the nucleosome is really rearranged, not simply displaced, and GAL4-AH binds on it.

The same result is obtained in other conditions, where the GAL4 site is protected on the nucleosome only with SWI/SNF and ATP.

Finally, a SWI/SNF complex with a mutant SWI2 subunit (K798A, in the ATPase domain) is assembled normally and co-elutes on Superose 6, but it has a much lower ATPase activity than the wild type and doesn’t stimulate GAL4-AH binding to the nucleosome: so, the ATPase activity of SWI2 is necessary for the remodeling.

#### **How does SWI/SNF facilitate GAL4 binding?**

Two hypotheses: (I) SWI/SNF **changes the nucleosome** so that the GAL4 site becomes available for specific site recognition; (II) SWI/SNF **changes the conformation of GAL4** so that it binds better. The data support (I):

- **Not the transactivation domain:** the activation domain does not need to be activated; the DNA-binding domain alone (GAL4(1–94)) is stimulated, so **what matters is the binding of GAL4 to its site.**
- **Why we can infer that GAL4 does not change conformation (read it on the gel):** with SWI/SNF + ATP, the GAL4-AH footprint on the nucleosome covers the **same bands**, with the **same boundaries relative to the G+A ladder**, as on naked DNA. The protein makes the same contacts with the DNA, so its binding mode is **unchanged**; only the concentration needed drops. What changes is the nucleosome (its 10-bp DNase I pattern is altered), i.e. the **accessibility of the site**.
- **The energy goes to the nucleosome:** ATP-γ-S and the ATPase-dead K798A mutant do not stimulate binding, so simple contact between SWI/SNF and GAL4 is not enough.

---
> [[IG 04 - Genomic imprinting + Enhancer RNAs (eRNAs)|← Genomic imprinting + Enhancer RNAs (eRNAs)]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 06 - Histone acetylation and methylation|Histone acetylation and methylation →]]
