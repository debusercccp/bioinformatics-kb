---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_common.docx"
order: 13
tags: [note, fg]
---

> [[FG 12 - Drosophila melanogaster · Forward genetics in Drosophila|← Drosophila melanogaster · Forward genetics in Drosophila]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 14 - Danio rerio · Zebrafish as a model organism|Danio rerio · Zebrafish as a model organism →]]

*Approfondimento: [[FGx 03 - Breaking, switching on, switching off – step by step|Breaking, switching on, switching off – step by step]]*

# Reverse genetics in Drosophila

Reverse genetics goes **from gene to phenotype**: start from a known gene, change it or its expression on purpose, and look at the consequence. In the fly this rests on **transgenesis** — getting a construct into the germ line, at random with the P element or at a defined landing site with ΦC31 — and on **binary expression systems** (GAL4/UAS and its derivatives) that decide **where and when** the transgene is on, for gain of function (ectopic expression) or loss of function (UAS-RNAi).

### Transgenesis

#### P-element-mediated germline transformation

- A **vector transposon** carries the **gene of interest (goi)** and a **marker**, between the inverted repeats, on a plasmid. Being **non-autonomous**, it needs **transposase in *trans***.

- A **helper plasmid** supplies the **transposase** but **lacks the inverted repeats**, so it is itself **immobile** — a stable transposase source that cannot integrate.

- The two plasmids are **co-injected into the posterior pole of a pre-cellular embryo**, where the **pole cells** (the future germ line) are forming, in a ***w⁻/w⁻* (white-eyed) background**.

- Transposition occurs in the nuclei that will become germ cells; about **15% of injected embryos** give **G0 adults that are germline chimeras**.

- The G0 flies are **backcrossed to the *w⁻/w⁻* stock**. In the progeny, **white-eyed flies** come from non-transformed germline cells, whereas **red-eyed flies carry the donor DNA in all their cells** — a true transgenic line. **10–20% transformants** is the usual yield.

- The transgene inserted into the genome is then **stably inherited** in subsequent generations.

**Limit:** insertion is **random**, so each line has the transgene in a different chromatin context (**position effects**) and two constructs cannot be compared directly. This is the problem **ΦC31** solves.

> **Paper — Rubin & Spradling, 1982** (Science 218:348–353): The founding paper of fly transgenesis: *rosy*⁺ cloned in a P element and injected with a transposase source into *rosy* embryos gave stable transformants with fully restored eye colour (20–50% of injected embryos). The helper was then a complete P element (or dysgenic embryos), which could itself jump; the wings-clipped helper came later.

![[FG-image35.png|394]]

**Marker genes for *Drosophila* transgenesis.** Two strategies:

- **Screening:**

  - **rescue of a visible mutant phenotype** that minimally affects viability — adult **eye-colour markers** (*white*, *rosy*, *rough*) and the adult **body-colour marker** *yellow*. All of these **require the corresponding mutant lines** as a background.

  - **fluorescent-protein-based markers**, e.g. **3xP3-EGFP**, driven by an artificial eye promoter — these do not require a mutant background.

- **Selection:** ***hs-neo*** (neomycin phosphotransferase, G418 resistance); ***hs-opd*** (organophosphate-degrading gene, an insecticide-selectable marker using paraoxon); ***Adh*** (the enzyme of ethanol catabolism), which again requires the corresponding mutant strain.

#### ΦC31 integrase-mediated transgenesis

P-element insertion is **random**, so two transgenic lines are never strictly comparable: **each insertion sits in a different chromatin context** (**position effects**). The ΦC31 system solves this by integrating constructs **at defined genomic docking sites**.

- The integrase of the *Streptomyces* phage **ΦC31** mediates a **sequence-directed recombination** between the bacterial attachment site **attB** and the phage attachment site **attP**.

- A **preplaced recipient site (*attP*)**, previously installed in the genome by transposon-mediated germline transformation, acts as the **landing site** in the *Drosophila* genome.

- A **donor plasmid** containing the transgene and the ***attB*** sequence is **co-injected with ΦC31 integrase mRNA** into *attP*-containing recipient embryos → **site-specific insertion** of the transgene into the *attP* site.

- The reaction produces the **hybrid sites *attL* and *attR***, which **prevent further integrase-catalyzed movement** of the integrated transgene: the event is irreversible. This is what **distinguishes ΦC31 from Cre/loxP or FLP/FRT**, where the recombinase catalyzes both integration and excision.

**In short:** **attB × attP → attL + attR**, which the integrase no longer recognizes → the insertion is **irreversible** and **always at the same site**.

> **Focus — The enzyme and the chemistry. A serine recombinase that joins attB × attP by subunit rotation, with no Holliday junction and no host factors.**
>
> **Why it is irreversible, and how it differs from Cre and FLP.** Recombination produces the hybrid sites **attL** and **attR**, chimeras of the two parental ones, which the integrase alone does not recognize as substrates: catalyzing the reverse reaction requires a separate phage cofactor, the **RDF** (recombination directionality factor, gp3), which is absent from the system. This is the opposite of **Cre/loxP** and **FLP/FRT**, where the two sites are **identical** and the product is still a substrate: the reaction is at equilibrium and, for reasons of local concentration, excision dominates over integration. Hence Cre and FLP are used to **remove** DNA and ΦC31 to **insert** it.
>
> **A detail on the landing site.** 3xP3 is an artificial promoter (three Pax6 sites upstream of a minimal TATA) driving RFP in the eyes; being floxed, the marker can be removed with Cre after integration, which matters because two fluorescent markers in the same animal are hard to tell apart. Supplying the integrase as **injected mRNA** has the advantage of being transient: the enzyme disappears and cannot catalyse anything else.

**The widely used system (Bischof et al., PNAS 2007).** The donor is **pUASTattB**, carrying the *white* marker, a loxP site, the UAS–MCS–SV40 cassette and *attB*. The host stock carries a **loxP–3xP3-RFP–loxP–*attP*** landing site, where the **artificial 3xP3 promoter** drives strong RFP expression in the eyes and is **flanked by loxP sites**, so the marker can be removed later by **Cre-mediated excision**. The integrase itself is supplied by a transgenic stock expressing **ΦC31 integrase in the germ cells** from the ***nanos*** (or ***vasa***) promoter.

> **Paper — Bischof et al., 2007** (PNAS 104:3312–3317): Improved ΦC31 transgenesis by encoding the integrase in the host genome under **nanos** or **vasa** control (germline only, no mRNA to inject) and by providing many mapped attP landing sites that can be modified in situ.

**Advantages:**

- Every transgene sits in **the same genomic context**: no concerns about position effects, expression levels between constructs can be considered equal, and constructs modified in different ways can be **compared directly**.

- The **rate of integration is higher** than with P-element transposase.

- **Chromosome mapping is not required.**

- A **large collection of lines with precisely mapped *attP* sites** on the four major chromosomes is available, already tested for accessibility and expression behaviour.

> **Focus — ΦC31 and the silencing problem. Random P insertions can be silenced by heterochromatin; ΦC31 attP sites (attP2, attP40) lie in open chromatin and give reliable, comparable expression.**

#### The GAL4/UAS binary system

- It enables **precise regulation** of transgene expression.

- It uses the **GAL4 transcription factor of *S. cerevisiae***, which binds the **UAS (Upstream Activating Sequence)**. Neither exists in the fly, so the system is orthogonal to fly biology.

- Developed by **Andrea Brand and Norbert Perrimon in 1993**, and it can be used for **ectopic expression** of a gene.

![[FG-image36.png|354]]

**The GAL4 protein.** GAL4 (881 aa) is the yeast activator of the galactose-induced genes. It binds DNA as a **dimer** on a **17 bp site** (the UAS, found between *GAL10* and *GAL1*) through a **zinc-finger DNA-binding domain** (residues 1–65), with a dimerisation domain (65–94) and two activation regions (148–196 and 768–881; GAL80 binds residues 851–881). Variants used in flies include optimized UAS sequences and **GAL4-VP16**, a stronger hybrid activator (GAL4 DNA-binding domain fused to the acidic activation domain of herpes simplex VP16).

> **Focus — Domain map in detail. DBD 1–65 (Zn₂Cys₆), dimerisation 65–94, activation 148–196 and 768–881, GAL80 site 851–881.**
>
> **The UAS itself.** It is a **17 bp palindromic site** (consensus CGG-N₁₁-CCG): each CGG half-site is contacted by one monomer, and the 11 central bp act as a spacer fixing the geometry of the dimer.
>
> **Why the system is orthogonal.** Neither GAL4 nor UAS exists in **Drosophila**. GAL4 on its own has no endogenous targets in the fly, so the driver line is phenotypically neutral; and UAS on its own is not recognised by any fly factor, so the responder line is silent. This is precisely what allows **lethal or toxic constructs** to be kept as stocks: they exist, but they are off until you cross them.
>
> **A stronger variant.** GAL4-VP16 fuses the GAL4 DNA-binding domain to the acidic activation domain of herpes simplex VP16, giving a much stronger activator — at the cost of greater toxicity.

**The two lines.**

1.  **Driver line:** carries the **GAL4** gene under the control of a **specific promoter or enhancer**. GAL4 is produced **only in the tissues and at the times when that promoter is active**, and **has no endogenous target genes** in the fly, so **it does nothing on its own**.

![[FG-image37.png|499]]

2.  **Responder line:** carries the **gene of interest downstream of UAS**. The gene is **inactive by default**, since UAS alone cannot drive expression.

![[FG-image38.png|512]]

**In short:** the **driver decides where**, the **responder decides what**. Neither does anything alone; crossing them switches the gene on **only in GAL4-expressing cells**. Because the responder is **silent in its own stock**, even toxic or lethal genes can be kept.

**The cross.** The progeny carry **both transgenes**: GAL4 is made in the driver's pattern, binds the UAS, and **activates the gene of interest in exactly those cells**.

> **Paper — Duffy, 2002** (Genesis 34:1–15): The GAL4 review this part follows: GAL4 activity rises with temperature (minimal at 16 °C, maximal at 29 °C), so expression can be tuned, and the responder can be a toxin (ricin A, reaper) for cell ablation. Some drivers and reporters have phenotypes of their own, so driver-only and responder-only controls are always needed.

![[FG-image39.png|472]]

**How many progeny express the gene?** If both parental lines are **heterozygous** for their transgene (e.g. kept over a balancer), only ½ × ½ = **¼ (25%)** of the progeny carry both GAL4 and UAS-gene and show the effect; with homozygous driver and responder stocks, all the progeny do.

**Advantages:**

- It is a **binary system**: responder and driver are kept in **separate parental lines**.

- The expression of **any responder** can be targeted in a variety of spatial and temporal patterns simply by **mating it with different GAL4 drivers**.

- Responder lines can be maintained **even for gene products that are lethal, toxic or reduce viability** when expressed — because in the parental stock they are silent.

- It is possible to study the effect of **cell- and tissue-specific ablation** on embryonic, larval and adult development.

**How to obtain GAL4 driver lines.** Two approaches:

1.  **Link a cloned, characterised promoter upstream of GAL4** and introduce the construct into flies by P-element-mediated germline transformation — cloning the desired promoter fragment into the **pPTGAL4** vector (11 kb; *mini-white* marker, MCS, *hsp70* TATA box, *gal4*, *hsp70* polyA). **Use it when** a characterised promoter is already available and you want expression in its known pattern.

2.  **Enhancer trapping**, with the **pGAWB** vector, an enhancer-trap GAL4 P-element transformation vector. Here *gal4* transcription is directed by the **weak promoter of the P-transposase gene**, and GAL4 is expressed from **its own AUG**, since its N-terminus directs both nuclear localisation and DNA binding. The element lands at random and reports whichever enhancer it falls near — exactly the enhancer-trap logic, but with GAL4 instead of *lacZ*, so the trapped pattern becomes **usable** rather than merely visible. **Use it when** you want to **discover new expression patterns** (new enhancers): a single screen yields many driver lines, each with a different pattern.

**How to obtain UAS responder lines.** By subcloning the gene of interest into the **pUAST** vector:

- **UAS:** 5 tandemly arrayed, optimised GAL4 binding sites — the UAS is **multimerised** so that several GAL4 dimers bind and expression is stronger;

- the ***hsp70* TATA box** and transcriptional start;

- a **polylinker** with unique restriction sites, into which the gene of interest is cloned downstream of UAS and upstream of the SV40 terminator;

- the **SV40 transcriptional terminator**;

- note that **pUAST functions only in somatic cells**.

The modern version is **pUASTattB**, the same cassette plus an ***attB*** site and *mini-white*, so that the responder can be integrated at a defined *attP* landing site by ΦC31 integrase.

> **Focus — Why pUAST does not work in the germ line, and what to use instead. Germline silencing and a weak hsp70 promoter; use pUASp (P transposase promoter + K10 3′UTR).**

![[FG-image40.png|354]]**Directed RNA interference.** The same binary system is used for **loss of function**: the responder carries an **inverted-repeat (IR) construct** — the gene of interest (GoI) in **sense and antisense orientation separated by an unrelated spacer** (the spacer overcomes the instability of symmetrical sequences) — downstream of 5× UAS. In the F1 of a cross with a GAL4 driver, the IR construct is transcribed in the GAL4-expressing cells and folds into an **RNA hairpin**; the resulting **dsRNA mediates gene-specific RNAi** exactly where the driver is active. This is how a tissue-specific knockdown is obtained in an animal where RNAi by feeding (as in *C. elegans*) does not work.

> **Focus — Libraries and controls. VDRC and TRiP collections; control for off-targets with two independent lines or a rescue.**

#### Adding temporal control to GAL4: GAL80, TARGET and the rest

**The problem.** Many GAL4 drivers **lack absolute temporal and spatial specificity**, and this often results in **lethality before the developmental stage of interest** is reached. Several approaches add a further level of control.

**1. Temperature dependence of GAL4 activity.** GAL4 is a yeast protein and works poorly at low temperature: **at 18 °C its activity is minimal, at 29 °C maximal**, with "minimal" effects on viability and fertility. By **lowering the temperature it is possible to bypass lethal effects at early stages** and then obtain the stage of interest at higher temperature.

**2. GAL80.** A **third transgenic line** carries **GAL80** — the **natural inhibitor** of GAL4 in yeast — under the control of an **inducible promoter** (e.g. a heat-shock promoter).

![[FG-image41.png|392]]

- **In the absence of heat shock:** GAL4 is free, binds UAS → **Gene X is expressed**.

![[FG-image42.png|406]]

- **After heat shock:** GAL80 is expressed and **inhibits GAL4** → **Gene X is silenced**.

![[FG-image43.png|410]]

This **combines spatial and temporal control**: the driver decides ***where***, the heat shock decides ***when***.

> **Focus — How GAL80 actually inhibits. It masks the activation domain (851–881) without blocking DNA binding: GAL4 stays on the DNA but no longer recruits Mediator — inhibition by occlusion, not by competition.**

**3. The TARGET system (Temporal And Regional Gene Expression Targeting).** This is the version actually used, because it avoids heat shock altogether. The UAS–GAL4 pair is regulated by a **temperature-sensitive allele of GAL80 (GAL80<sup>ts</sup>)**, expressed from a **ubiquitous promoter**:

- ***tub-GAL80<sup>ts</sup>*** is a chimeric transgene: the **tubulin 1α promoter** drives ubiquitous, high-level expression of the **temperature-sensitive form of GAL80**.

- At **low (permissive) temperature, 18–19 °C**: GAL80<sup>ts</sup> is folded and **blocks GAL4** → **the gene is OFF**.

- At **high (restrictive) temperature, 29–32 °C**: GAL80<sup>ts</sup> is inactivated and **fails to inhibit GAL4** → **the gene is ON**.

**Mnemonic:** **cold** = GAL80<sup>ts</sup> works = gene **OFF**; **warm** = GAL80<sup>ts</sup> broken = gene **ON**.

![[FG-image44.png|271]] ![[FG-image45.png|274]]

It is therefore a **ternary system**:

- **Spatial:** a tissue-specific enhancer (a specific promoter or an enhancer trap) drives GAL4;

- **Temporal:** the timing of transcriptional activation of the gene of interest is controlled by **shifting the incubation temperature**;

- **Quantitative:** induction is **maximal at about 32 °C**, and at intermediate temperatures (e.g. 28 °C) **intermediate levels of activation** are obtained.

Its practical advantages are that it **works with any existing GAL4 driver and UAS responder**, and that **temperature is a rapid and easily controlled inducer**; the drawback is that **high temperatures can have undesired effects** on the induced flies.

**4. The GeneSwitch system.** GAL4 is modified into a **chimeric inducible protein** made of the **GAL4 DNA-binding domain**, the **p65 activation domain** and a **hormone receptor domain** (e.g. for estrogen or progesterone, typically RU486/mifepristone).

- **Without hormone:** inactive.

- **Hormone binding** induces a **conformational change → activation**.

The inducer here is a drug fed to the flies, which avoids both heat shock and temperature shifts.

**5. The Tet systems (TetOFF / TetON),** based on a **tetracycline-sensitive transactivator**.

- **TetOFF:** the expression of the transactivator (**tTA**) is driven by a specific promoter. **In the absence of tetracycline** the transactivator binds its operator (**tet-O**) and **activates** the reporter gene; **in the presence of tetracycline** the transactivator is **inactive → gene OFF**.

- **TetON:** uses the **reverse transactivator (rtTA)**, which is **inactive without tetracycline** and **active in its presence** — the logic is inverted.

> **Focus — How the Tet switch works. tTA is the bacterial repressor TetR fused to VP16; rtTA is the same TetR, mutated so that the logic is reversed. The drug (tetracycline or doxycycline, fed to the animals) changes the conformation of TetR, abolishing DNA binding in TetOFF and enabling it in TetON. tTA: drug = OFF; rtTA: doxycycline = ON.**

![[FG-image46.png|282]] ![[FG-image47.png|276]]

**6. The UAS-GAL4-Tet hybrid system.** A hybrid combining **UAS-GAL4** and **Tet**: GAL4 controls the expression of the **tetracycline-sensitive transactivator (rtTA)**, which in turn controls the reporter. The two systems are chained, so **spatial control comes from the GAL4 driver** and **temporal control from the drug**.

![[FG-image48.png|500]]

**7. The Hsp-FLP/FRT system — clonal analysis.** This is a different kind of control: instead of switching a gene on in a whole tissue, it switches it on **permanently in a few random cells and all their descendants**.

- It uses the **yeast FLP recombinase** under **heat-shock promoter** control.

- FLP promotes ***cis* recombination between FRT sequences**; if the FRTs are oriented **in the same direction**, the **intervening DNA is excised**.

![[FG-image49.png|452]]

The standard construct is **AyGAL4** ("Actin \> y⁺ \> GAL4"):

- **(A) Initial state:** transcription from the ubiquitous **Actin promoter** is **terminated at the *hsp70* transcriptional termination signal**, which sits between the two FRTs together with the marker gene *yellow*. GAL4 is therefore **not** made.

- **(B) Upon heat shock:** the *hsp70* promoter drives the ***flp*** gene; **Flippase catalyses recombination at the two FRT sequences** and removes the termination signal and the *yellow* marker.

- **(C) In clones:** the rearranged **Act5C promoter–GAL4** fusion now expresses GAL4, which activates the **UAS-*tau*** reporter. Only the cells that experienced recombination **and their progeny** express bovine Tau, revealed with an anti-Tau monoclonal antibody. Because **Tau is a microtubule-associated protein** distributed throughout the cytoplasm by slow transport, **the whole cellular structure and the innervation pattern of the labelled cells can be resolved**.

![[FG-image50.png|500]]

By tuning the **length of the heat shock** one controls how many clones are induced, so single labelled cells can be followed in an otherwise wild-type animal — the fly equivalent of the genetic mosaics mentioned in Module 1.

**In short:** heat shock → **FLP** → excision of the STOP between the **FRTs** → **GAL4 permanently on** in that cell and all its descendants → a **mosaic**: labelled (or mutant) clones inside an otherwise normal animal.

> **Focus — The most powerful use: FRT-mediated mitotic recombination. Homozygous mutant clones in a heterozygous animal; in MARCM only the mutant clone loses GAL80 and is labelled.**
>
> **Why UAS-tau as a reporter.** Tau is a microtubule-associated protein distributed by slow transport throughout the cytoplasm and along axons, so it fills the entire cellular morphology, arborisation included — unlike a soluble nuclear reporter, which only marks the cell body.
>
> **Paper — Pagliarini & Xu, 2003** (Science 302:1227–1231): Mosaic analysis applied to cancer: GFP-labelled *eyeless*-FLP clones expressing **RasV12** (benign on its own) became metastatic only when combined with loss of polarity genes (*scribble*, *lgl*, *dlg*).
>
> **Paper — Yamamura et al., 2021** (Cancer Sci. 112:505–514): The fly as a cancer model: from the first tumour suppressor (*lgl*) and cell competition to flies carrying patients’ mutation combinations for drug screens (dRet flies helped validate **vandetanib**).

### What makes a good expression system

The lecture closes with the four criteria against which all of the above should be judged:

1.  **Fast ON/OFF kinetics.**

2.  **Induction without side effects.**

3.  **Ability to control expression levels.**

4.  **A fully OFF state when not induced.**

No single system satisfies all four: heat shock is fast but has side effects and is leaky; TARGET is clean and works with every existing line but needs temperature shifts that are themselves not neutral; GeneSwitch and Tet are chemically inducible but slower. The choice, as with the choice of the model organism itself, is a **compromise dictated by the question**.

---
> [[FG 12 - Drosophila melanogaster · Forward genetics in Drosophila|← Drosophila melanogaster · Forward genetics in Drosophila]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 14 - Danio rerio · Zebrafish as a model organism|Danio rerio · Zebrafish as a model organism →]]
