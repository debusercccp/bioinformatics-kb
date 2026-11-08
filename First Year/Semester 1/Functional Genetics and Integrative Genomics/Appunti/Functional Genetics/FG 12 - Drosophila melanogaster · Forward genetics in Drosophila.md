---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/Functional_Genetics/FunctionalGen_common.docx"
order: 12
tags: [note, fg]
---

> [[FG 11 - Drosophila melanogaster · The fly as a model organism|← Drosophila melanogaster · The fly as a model organism]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 13 - Drosophila melanogaster · Reverse genetics in Drosophila|Drosophila melanogaster · Reverse genetics in Drosophila →]]

*Approfondimento: [[FGx 02 - Balancer chromosomes – step by step|Balancer chromosomes – step by step]] · [[FGx 03 - Breaking, switching on, switching off – step by step|Breaking, switching on, switching off – step by step]]*

# Forward genetics in Drosophila

Forward genetics goes **from phenotype to gene**: mutagenise at random, screen for a phenotype, then identify the gene responsible. In the fly the classic toolkit is **chemical mutagenesis with EMS**, **balancer chromosomes** to keep the new recessive mutations, and the **saturation screen** of Nüsslein-Volhard and Wieschaus; **insertional mutagenesis with the P element** adds a molecular tag that makes the mutated gene easy to clone, and **enhancer traps** use the same random insertions to find genes by their expression pattern.

### The mutagens

The logic is the one introduced in Module 1: a **wide range of mutagens** is used to induce mutations at a rate much higher than the spontaneous one, and **a given mutagen increases the rate of some kinds of mutation but not others**. The three classes are physical, chemical and biological (insertional).

**Physical mutagens (radiation).**

- **X-rays:** Muller's work on *Drosophila* (1926–1927) showed that exposure to X-rays causes mutations, particularly in gametes. X-rays mainly induce **double-stranded chromosome breaks** and large-scale "chromosome mutations" or rearrangements: **deletions, duplications, inversions**.

- **γ-rays:** induce genomic rearrangements.

- **UV light:** produces **thymine dimers**, which may be repaired incorrectly.

**Chemical mutagens.** The discovery of chemical mutagenesis is due to **Charlotte Auerbach (1899–1994)**, who from 1940 in Edinburgh studied in *Drosophila* the biological effects of **mustard gas**. Flies were exposed under extremely dangerous conditions and the number of mutations in treated flies was compared with untreated controls; mustard gas proved highly effective at producing mutations. The results were sent to the government agency in March 1942 but **publication was not permitted until after the end of the war**, because of concerns about their use as a weapon.

**EMS (ethyl methanesulfonate)** is the chemical mutagen actually used in fly screens. It is an **alkylating agent** and mainly induces **single base changes, i.e. point mutations**: -\> Predictable base substitutions.

**Why are EMS mutations so predictable?** EMS is **not targeted to a gene or a position**: it hits random sites across the genome. What is predictable is the **type of change**, and that comes from its chemistry. (1) EMS only **transfers an ethyl group to single atoms of individual bases**; it does not break the DNA backbone, so it gives **point mutations, not deletions**. (2) It ethylates several atoms, but **only those involved in base pairing cause mutations**. The most frequent adduct, **N7-ethylguanine**, sits in the major groove, outside the Watson–Crick interface, so it does not change pairing (at most it causes depurination). The mutagenic one is **O⁶-ethylguanine**: the O⁶ is part of the G–C pairing face, and once ethylated the base pairs with **T** instead of C. (3) O⁶-ethylG is still a purine and T is a pyrimidine, so the pair keeps normal purine–pyrimidine geometry: the polymerase accepts it and the result can only be a **transition, never a transversion**. Over two rounds of replication: **G:C → (O⁶-etG):T → A:T**. (4) Because this lesion dominates, the **large majority of EMS mutations are G:C → A:T**. You can even predict which codons can become stop codons, e.g. **TGG (Trp) → TAG/TGA (stop)** or **CAA/CAG (Gln) → TAA/TAG (stop)**.

The atoms involved are:

- it **ethylates DNA principally at oxygens**, such as the **O⁶ of guanine**: O⁶-ethylguanine pairs with thymine, giving the **transition C:G → T:A**;

- it ethylates the **O⁴ of thymine** (whose pairing partner becomes G): **transition A:T → G:C**;

- it also ethylates nitrogen positions, mostly **N7 of guanine**.

![[FG-image22.png|453]]

*Why this matters:* because EMS gives point mutations rather than deletions, it produces an **allelic series** — null, hypomorphic and occasionally antimorphic alleles of the same gene — which is precisely what Müller's classification needs in order to be applied (see Module 1).

**Biological (insertional) mutagens:** transposable elements, retroviruses, etc. They produce fewer events, but each insertion **tags the gene** and makes it easy to clone (see *Insertional mutagenesis: the P element*, below).

### EMS mutagenesis in practice

1.  **Males are fed a solution of 25 mM EMS in 1% sucrose.**

    - **Lower doses (7.5–10 mM)** are used to **minimize the introduction of multiple lethal hits** per chromosome, i.e. when searching for a new mutation and the treated chromosome is to be made **homozygous**.

    - **Higher doses** are used when **isolating new alleles** of existing mutations, i.e. when the treated chromosome will be tested **in trans**.

2.  **Treated males are mated to females.**

**Why males?**

- Mature **sperm is quite sensitive to mutagens**.

- Treated males are **still capable of coupling**.

- **One male will mate with many females**, so a single treated genome can be propagated into many lines.

![[FG-image23.png|341]]**The general scheme of a chemical-mutagenesis screen** (Hales et al., *Genetics* 2015) is: (A) males eat food with the mutagen; (B) each developing sperm carries a **different** new mutation; (C) the males are crossed to wild-type females; (D) the offspring each carry different mutations; (E) the offspring are outcrossed separately; (F) inbred lines of the new mutations are established; (G) the homozygotes, **if alive**, are tested for the phenotype of interest.

The weak point of this scheme is step (F): a newly induced recessive mutation is invisible in the heterozygote and is lost by recombination unless it is protected. This is what balancer chromosomes are for.

### Balancer chromosomes

**Identified by H. J. Muller in 1918.** A balancer is a chromosome engineered (or found) so that it can carry a mutagenized homologue through the generations **without ever recombining with it**.

![[FG-image24.png|254]]**Properties:**

1.  **Multiple, overlapping inversions** (paracentric and pericentric) within the same chromosome. They **cannot pair normally with their homologue during meiosis**, and when recombination does occur it generates **lethal aneuploidy** — so no recombinant gametes survive. The practical effect is that the mutagenised chromosome is kept **intact**.

2.  **One or more recessive lethal (or sterile) mutations**, which prevent the survival of balancer homozygotes, so the balancer cannot become fixed.

3.  **One or more dominant visible markers** (e.g. **Curly**, *Cy*), which allow the researcher to follow the balancer in crosses by eye.

4.  **Recessive visible mutations** that can be useful in crosses (e.g. eye-colour markers).

**Why one inverted chromosome is enough.** Recombination is not a property of one chromosome but of the pair, because it requires base-by-base alignment. If only one homologue carries an inverted block, the synaptonemal complex can match the corresponding sequences only by forming an inversion loop: a single abnormal chromosome distorts the geometry of both, so the effect is **dominant** in a mechanical sense.

**What happens to the recombinants.** Recombination is not prevented: the recombinant gametes simply never become flies. A crossover inside the loop does happen, and its products depend on where the centromere lies. In a **paracentric** inversion (centromere outside the inverted block) it gives one **dicentric chromatid**, which is stretched into an anaphase bridge and breaks, and one **acentric fragment**, which is not segregated and is lost. In a **pericentric** inversion (centromere inside the block) it gives chromatids carrying **a duplication of one segment and a deletion of another**. Either way the recombinants are aneuploid and lethal, so the only viable gametes are the parental ones: the intact balancer or the intact mutagenised chromosome.

**Why the marker must be dominant.** It is a necessity, not a convenience. The balancer is homozygous lethal by construction, so the only genotype in which it is ever seen alive is the balancer/homologue heterozygote. A recessive marker would be masked by the wild-type allele on the other chromosome and would show only in the (dead) homozygote. Hence dominant markers: in Müller's terms, gain-of-function alleles (hypermorphs or neomorphs) or antimorphs.

Additional points from the lecture:

- Each *Drosophila* chromosome has its own set of balancers, **except chromosome 4**.

- The **X chromosome** balancers do not carry lethal recessive markers.

- **Balancer chromosomes are lethal in homozygosity.**

- Example: the ***SM*** balancer of the 2nd chromosome, with a paracentric inversion (22D–34A, 42A–58A) and a pericentric inversion (21A/22A–60F/60B), marked with ***Cy*** (curly wings) and a recessive lethal (*let*). ***CyO*** ("Curly of Oyster") is the standard 2nd-chromosome balancer.

![[FG-image25.png|242]]

**Reading a balanced stock.** Because *Cy* is dominant and lethal when homozygous, a *Cy*/+ × *Cy*/+ cross gives **1/4 *Cy*/*Cy* (dead), 2/4 *Cy*/+ (Curly), 1/4 +/+ (wild type)**: of the surviving progeny, **2/3 are Curly and 1/3 are wild type**. A stock in which *Cy* never disappears and never becomes homozygous is therefore self-maintaining — this is what "a balanced stock" means. The same logic applies to a mutant stock: in mut/CyO × mut/CyO, CyO/CyO die and, if the mutation is lethal, mut/mut die too, so only mut/CyO survive — the stock maintains itself and the mutation stays protected.

**Side effects of the breakpoints.** The physical construction of a balancer and its dominant marking are not entirely independent: **inversion breakpoints can generate dominant phenotypes on their own**. If a breakpoint falls inside a gene, that gene becomes haploinsufficient; if it moves a euchromatic gene next to heterochromatin, the gene is silenced by position effect in a patchy, clonal way — position-effect variegation (PEV), e.g. a mottled eye.

**In short:** inversions → no viable recombinants, so the mutagenised chromosome stays intact; recessive lethal → balancer homozygotes die; dominant marker → you can tell by eye who carries it.

### The Nüsslein-Volhard and Wieschaus screen (1979–1980, EMBL Heidelberg)

**The question.** Which genes control the pattern of the embryo? The design is a **saturation screen**: identify **zygotic** genes, anywhere on each chromosome, that are involved in embryonic development and whose mutations affect the **cuticular phenotype** of the larvae.

**Why the cuticle.** The first-instar larval cuticle is a rigid, highly reproducible map of the body plan: acron, head, thorax (T1–T3), abdominal segments A1–A8, telson, with denticle belts in a precise pattern. A dead embryo preserves its cuticle, so **even a lethal mutant can be scored**, which is the key trick of the whole screen.

**The two kinds of outcome the screen distinguishes:**

- A mutation abolishing the function of a gene **essential for embryonic development** → abnormal development, lethality, a normal-looking unhatched embryo.

- A mutation abolishing the function of a gene with a **specific role in patterning** → most structures of the mutant embryo are normal and the **defects are limited to specific regions** of the body. Because of this, it is possible to **reconstruct the normal role of each gene** from the defect.

**The crossing scheme** (second chromosome, as an example):

1.  **P:** EMS-treated males (*cn bw sp*) × females carrying the **CyO balancer** (*Cy pr cn²*/*pr cn*).

2.  **F1:** select **balanced males** carrying one mutagenized chromosome over the balancer (*cn bw* \* *sp* / *CyO*, where \* marks the new EMS-induced recessive lethal); each male carries a **different mutagenized chromosome**, recognizable by eye color (bright red vs orange). Cross each F1 male individually with *CyO* females.

3.  **F2:** 25% *CyO*/*CyO* (**lethal**), 25% balancer over the non-mutagenized chromosome, 50% carrying the mutagenized chromosome. A single F2 pair of **balanced siblings** is intercrossed.

4.  **F3:** the stock segregates balancer homozygotes (die as larvae), **balanced mutant stock** (viable, the line that is kept), and **homozygotes for the mutagenized chromosome** — these are the embryos that are collected and screened for the cuticular phenotype.

**Why F3 (and not F2 as in the worm):** the fly **cannot self-fertilize**. One generation is needed to put each mutagenized chromosome over the balancer (**F1**), one to build a balanced stock of siblings (**F2**); only their intercross produces homozygous embryos (**F3**).

![[FG-image26.png|402]]

**How to distinguish the classes in F2?** Two devices: (1) **additional visible phenotypic markers**, mainly eye colours; (2) **DTS (Dominant Temperature Sensitive) lethal mutations**, which kill the unwanted class at the restrictive temperature.

**The numbers** (from the three 1984 papers in *Wilhelm Roux's Archives*):

| Chromosome | Balanced stocks | Lethal hits | Mutants with embryonic phenotype | Loci (\>1 allele) | Loci (single allele) | Total loci |
|----|----|----|----|----|----|----|
| 1 (X) | 8,614 | 3,200 | 114 | 20 | 13 | 33 |
| 2 | 5,764 | 7,000 | 272 | 48 | 13 | 61 |
| 3 | 12,600 | 7,000 | 198 | 32 | 13 | 45 |
| **Total** | **26,978** | — | **584** | — | — | **139** |

So roughly **27,000 balanced lines** were built by hand to recover **139 loci**. The fact that most loci were hit **more than once** is what shows the screen was close to **saturation** for this class of phenotype.

**The result: three classes of segmentation mutants** (Nüsslein-Volhard & Wieschaus, *Nature* 287, 1980):

- **Gap genes** — gaps in the segmentation pattern, i.e. a **large deletion of a group of contiguous segments** (*Krüppel*, *knirps*).

- **Pair-rule genes** — **pattern deletion in alternating segments** (*even-skipped*, *odd-skipped*, *paired*, *runt*).

- **Segment-polarity genes** — **deletions associated with duplications within each segment** (*gooseberry*, *patch*).

Together with the **maternal-effect genes** recovered separately, these three zygotic classes make up the segmentation hierarchy treated in full below.

**The conceptual conclusion drawn in the paper:** for a given line, certain regions of the embryo are affected while other regions are normal; mutants usually affect **areas of the embryo rather than specific cell types**; and since the affected region ultimately gives rise to a variety of different cell types, these genes **define positions or spatial coordinates rather than tissues or organs**. This is the birth of the idea of a hierarchy of positional information.

> **Paper — Nüsslein-Volhard & Wieschaus, 1980** (Nature 287:795–801): 15 loci that alter the larval segment pattern, read as three levels of organisation: **gap** (3: *Krüppel*, *knirps*, *hunchback*), **pair-rule** (6, including *even-skipped*; *engrailed* was then placed here) and **segment polarity** (6, e.g. *wingless*, *hedgehog*, *patch*).
>
> **Paper — Wieschaus & Nüsslein-Volhard, 2016** (Annu. Rev. Cell Dev. Biol. 32:1–46): A personal account (~600 mutants in 120 genes) of why the undirected screen worked despite the fear of too many genes and messy phenotypes. A zygotic screen misses genes masked by **redundant** paralogues, **haplolethal** genes and genes with a **maternal contribution**.

### Complementation testing

Once a collection of recessive lethal mutations has been isolated, the first question is **how many genes** they represent. Two independently isolated recessive lethals, *let1* and *let2*, are crossed (each kept over *CyO*):

- If **all surviving progeny are Curly** — i.e. the *let1*/*let2* class dies — the two mutations **fail to complement**: they are **alleles of the same gene**.

- If the surviving progeny are **2/3 Curly and 1/3 wild type** — the *let1*/*let2* class is viable — **complementation occurs**: the two mutations affect **different genes**.

![[FG-image27.png|700]]**Logic:** in this cross let1/let2 is the **only class without CyO**. If it dies, neither chromosome carries a working copy of that gene → **same gene**. If it lives, each chromosome covers the other's defect → **different genes**.

### Maternal and zygotic genes

**The maternal genome controls early embryonic development in metazoans.**

- **Maternal products** (mRNAs and proteins) loaded into the egg during oogenesis control embryonic development after fertilisation.

- Gene regulation in the early embryo is **post-transcriptional rather than transcriptional**, and involves the spatial and temporal control of subcellular transcript localisation, transcript stability and translation.

- **The zygotic genome is transcriptionally inactive** at first.

After a species-dependent number of mitotic cycles, the **MZT (maternal-to-zygotic transition)** takes place. It has two components:

1.  **Degradation of a subset of maternal mRNAs**, driven by maternally encoded products themselves;

2.  **ZGA (zygotic gene activation)**, taking place with an increasing degree — transcriptional activators enhancing the efficiency of zygotic transcription, plus proteins and miRNAs enhancing the efficiency of maternal mRNA degradation.

The result is that **genetic control of development is transferred from the maternal to the zygotic genome**. This is a **fundamental process conserved in metazoans**: echinoderms (*Strongylocentrotus purpuratus*), nematodes (*C. elegans*), insects (*Drosophila melanogaster*), fish (*Danio rerio*), amphibians (*Xenopus laevis*), mammals (*Mus musculus*) and plants.

![[FG-image28.png|329]]**Maternal-effect genes.** A maternal-effect gene is one whose product is **supplied by the mother** during oogenesis: the phenotype of the offspring therefore depends on the **mother's genotype, not on its own**.

- *A/A* males × *A/A* females → the "A" gene product is loaded into the egg → **fertile**, normal embryos.

- *A/A* males × *a/a* females → no product is loaded during oogenesis → the embryos die **even though they are *A/a* heterozygotes**.

![[FG-image29.png|417]]The diagnostic test is the **reciprocal cross**:

- **Cross:** *A/a* males × ***a/a* homozygous mutant females** → **all offspring die**, whatever their own genotype (*a/A* and *a/a* alike).

- **Reciprocal cross:** *a/a* homozygous mutant males × *A/a* females → **viable offspring**, again whatever their genotype.

**The lethal phenotype of the zygote is determined by the mother's genotype.** This is the signature of a maternal-effect mutation and is how *bicoid*, *nanos* and the other axis-determining genes were recognized.

**Zygotic genes, by contrast,** are transcribed from the embryo's own genome. A recessive lethal mutation in a zygotic gene required for normal embryonic development behaves in a strictly Mendelian way: *a/A* × *a/A* → 1 *A/A* : 2 *a/A* (all normal) : 1 ***a/a*, which dies**. The Nüsslein-Volhard and Wieschaus screen was designed specifically to catch **this** class, which is why it screened F3 homozygous embryos.

### The segmentation hierarchy: the four classes of genes

- **Maternal genes:** expressed by the mother to establish the initial **anterior-posterior and dorsal-ventral axes** of the egg and early embryo.

- **Gap genes:** they establish a segmented **polar body plan along the anterior-posterior axis**. They divide the embryo into segments.

- **Pair-rule genes:** subdivide the broad regions into a peri**odic, alternating stripe pattern that defines the precursors of individual segments**.

- **Segment-polarity genes:** establish the **fine-scale polarity** and precise boundaries within each individual segment.

#### On top of the cascade: homeotic (Hox) genes

The four classes set the number and polarity of the segments, not what each one becomes: that is the job of the **homeotic genes** (**Edward Lewis**, the third 1995 laureate).

- **Transcription factors** that assign **identity** along the antero-posterior axis, switched on by gap and pair-rule genes and **maintained** by the Polycomb/trithorax system.

- Two clusters in *Drosophila*: the **Antennapedia complex** (anterior segments) and the **Bithorax complex** (posterior segments).

- **Mutant phenotype:** **homeotic transformation** — a correct structure in the wrong place. *Antennapedia* gain of function gives legs instead of antennae; *bithorax/postbithorax* gives a four-winged fly (neomorphs in Müller's classification).

- "**Triple collinearity**" (Module 1): chromosomal order = temporal order = body order, conserved from fly to vertebrates.

**Two points worth keeping.** The cascade **flows one way**, from a continuous maternal gradient to a discrete 14-stripe pattern, each level narrower but more precise. The first three levels act in a syncytium, where transcription factors diffuse; the fourth acts in a cellularised embryo and needs cell–cell signalling — which is why the segment-polarity genes became the conserved signalling pathways of all animals.

### Insertional mutagenesis: the P element

The P element is the transposon that turned *Drosophila* from an organism you could only **break** into one you could also **build**.

![[FG-image30.png|619]]

**Structure of the active (autonomous) P element.** It consists of **two 31 bp inverted repeats (IR)** surrounding an open reading frame — organised in exons 0, 1, 2 and 3 — encoding a **transposase**; internal 11 bp inverted repeats are also present, and the whole element is flanked by an **8 bp duplication of the genomic insertion site** generated on insertion.

> **Focus — In numbers. 2907 bp; the 31 bp terminal repeats are cut, the 11 bp internal repeats bind the transposase; 8 bp TSD.**
>
> **Why it transposes only in the germ line.** The primary transcript contains three introns. The first two are removed everywhere, but the third one (**IVS3**) is spliced **only in the germ line**. In somatic cells an hnRNP-like protein, **PSI (P-element Somatic Inhibitor)**, together with hrp48 binds exonic sequences upstream of the splice site and blocks removal of IVS3. The outcome: in the soma IVS3 is retained, the ORF is truncated and a **66 kDa repressor** is made; in the germ line IVS3 is removed, the ORF is complete and the active **87 kDa transposase** is made. This is why the P element is a germinal and not a somatic mutagen, and it is also the molecular basis of **hybrid dysgenesis** (P males × M females: the M maternal cytoplasm lacks the repressor and the piRNAs that silence the element, so transposition explodes in the germ line of the progeny → sterility, mutations, chromosome breaks).

| **Element** | **Splicing of IVS3** | **Consequence** |
|----|----|----|
| **Autonomous element** | removed only in the germ line; in the soma **PSI** (P-element Somatic Inhibitor, hnRNP-like) together with **hrp48** binds exonic sequences upstream of the splice site and blocks removal | germline transposition only |
| **Δ2-3(99B)**, the classic jumpstarter | IVS3 already deleted **at the DNA level** | transposase made constitutively, soma included, without depending on splicing; having lost its inverted repeats it is not a valid substrate for itself and cannot move |

> **Transposition mechanism: cut-and-paste.** The transposase, as a multimer, binds the internal 11-mers, synapses the two ends and cuts. The cuts are staggered, leaving **17-nucleotide 3′ extensions** on the element. The excised element is inserted elsewhere through an 8 bp staggered cut which, once filled in by the polymerase, generates the target-site duplication. The mechanism is **non-replicative**: the element moves, it does not copy itself.
>
> **What happens at the donor site.** Excision leaves a double-strand break that the cell must repair, in one of two ways:

| **Repair of the donor site** | **Outcome** |
|----|----|
| **Homologous recombination** | the cell repairs using the sister chromatid, which still carries the element, so the element reappears at the donor site: copy number *seems* to increase although the mechanism is conservative |
| **End joining** | a **footprint** remains — a few residual bp of the inverted repeats, often with a frameshift. This is the basis of **imprecise excision**, used historically to generate deletions from a known insertion |

> **Insertion bias.** Insertion is **not random**: the P element strongly prefers the 5′ regions of genes, promoters and first introns, with hotspots and coldspots. This is why no collection of P insertions saturates the genome, and why other transposons with different and complementary preferences — **piggyBac** and **Minos** — were introduced later.

**The key idea: transposon and transposase can be separated.** This gives a **binary system** that allows two things:

1.  **P-element-mediated transgenesis** (putting DNA in) — treated under *Reverse genetics*, below;

2.  **P-element-mediated mutagenesis** (breaking genes, with a tag) — treated here.

**In short:** both mobilize the same P element with the same mutator/transposase split, but transgenesis **delivers a cargo** — the gene of interest plus a marker — and the insertion site is incidental (reverse genetics); mutagenesis mobilizes a **marker-only element** so that it lands inside a gene and breaks it, and here the insertion site is the point, **the known P sequence serving as the molecular tag** used to identify the affected gene (forward genetics).

#### P-element-mediated mutagenesis

The same binary logic is used to **break** genes, using two transgenic lines in a *w⁻* background:

- a **P mutator element**: a non-autonomous element carrying a ***white⁺*** marker, on chromosome II;

- a **P jumpstarter element**: an immobile transposase source on chromosome III, marked with a **dominant marker M**. On its own neither line can move: the mutator has no transposase, the jumpstarter has no inverted repeats.

**The crossing scheme** (Cooley, Kelley and Spradling, *Science* 1988, "Insertional Mutagenesis of the *Drosophila* Genome with Single P Elements"):

1.  Cross the two lines. Select **F1 males** that are **red-eyed** (they carry the mutator) and carry the **dominant marker M** (they carry the jumpstarter). Only in these flies are mutator and transposase together, so **transposition occurs** — onto chromosomes I, II or III.

2.  Cross the F1 males with **white-eyed, balancer-bearing females**.

3.  Select **F2 progeny** that are **red-eyed** (they kept the element), **M⁻** (they have **lost the jumpstarter**, so the new insertion can no longer move) and **balanced**.

The result is that **new mutations are induced by transposition of the single P element**, and the "new" P element is **stable**: it allows **rapid mapping, cloning and complementation testing** of the affected gene. Separating mutator from jumpstarter is what converts a random jump into a permanent, inherited, **molecularly tagged allele**.

![[FG-image31.png|543]]

![[FG-image32.png|303]]

**How the flanking gene is identified.** Two classic methods:

- **Plasmid rescue.** The P construct is built to contain a **bacterial origin of replication (*ori*)** and a **resistance gene (*kan*ʳ)**. Genomic DNA is extracted and **digested with XbaI**; the fragments are **circularised with DNA ligase**; competent *E. coli* are transformed, so that only the fragments carrying *ori* and *kan*ʳ — that is, the element **plus its genomic flanks** — produce colonies; the plasmid DNA is recovered and characterised by **restriction digestion and sequencing**.

- ![[FG-image33.png|227]]**IPCR (inverse PCR).** Genomic DNA is digested, the fragments are **circularised**, and PCR is run with primers pointing **outwards** from the known P-element sequence; 30 cycles amplify across the circle, so the product contains the **unknown flanking genomic region**.

**Common logic:** both methods exploit the fact that the **P-element sequence is known**; it is used as a handle to recover the **unknown genomic DNA next to the insertion**.

> **Focus — Why plasmid rescue works. ori + kanʳ sit inside the element: digest, self-ligate at low DNA concentration, transform — only insertion-derived circles grow.**
>
> **Why inverse PCR works.** Primers pointing **outwards** from the known P-element sequence would amplify nothing on a linear template; on a circle they end up facing each other across the genomic flank, so the product contains exactly the unknown region. It is faster and scalable, and it is the method that allowed the large insertion collections to be mapped (Berkeley Drosophila Genome Project).

#### P elements as expression vectors: enhancer traps

**The question:** in which tissues is a specific gene expressed? **The construct:** a **reporter gene** placed under the control of the gene of interest's **promoter** — the reporter is then expressed wherever the original gene is expressed.

The **enhancer trap** turns this round: instead of choosing the promoter, the element is allowed to insert at random and **reports on whatever enhancer it lands near**.

**O'Kane and Gehring (*PNAS* 1987), "Detection in situ of genomic regulatory elements in *Drosophila*"** — the **PZ element**:

- the **P element promoter** is a **weak** promoter (the main transcription start site is 87 bp from the 5′ end of the element), too weak to drive expression on its own;

- the second exon of the P element is fused **in frame** to the 5′ end of the ***lacZ*** gene (a transposase–β-galactosidase fusion carrying a nuclear localisation signal);

- the element also carries the **trailer sequence and polyadenylation site of *hsp70***, *kan*ʳ and *ori* for plasmid rescue, and ***rosy⁺*** as a transformation marker.

![[FG-image34.png|527]]

When the element inserts near a **genomic enhancer (E)**, that enhancer acts on the weak P promoter and **drives *lacZ* in the enhancer's own pattern**. Staining for β-galactosidase then reveals the expression pattern directly in embryos, imaginal discs and adult tissues — and, because the element is also a mutagen and a molecular tag, **the same insertion gives the pattern, a mutant allele and a handle for cloning at once**.

**Why a weak promoter?** On its own the P promoter is too weak to drive detectable *lacZ* expression, so the reporter is switched on **only when a genomic enhancer acts on it**. The staining pattern therefore reports the trapped enhancer and nothing else; a strong promoter would give expression everywhere and hide it.

**Enhancer trap vs gene trap.** What the element traps is a **genomic enhancer next to the insertion point** and, with it, that **enhancer's expression pattern** — not the gene or the promoter. The two strategies differ in where the element must land:

| **Trap type** | **Requirement** |
|----|----|
| **Enhancer trap** | the element only needs to land **near** an enhancer: upstream of a gene, in an intron, even some distance away. The weak P promoter alone is not enough, so the staining reports the trapped enhancer and nothing else |
| **Gene trap** | the reporter has **no promoter of its own** and must insert **inside a transcribed gene**, in the right orientation — usually in an intron, with a splice acceptor — so that it is spliced into the endogenous transcript and reports that gene's expression |

**The two outcomes of an enhancer-trap insertion:**

1.  **Identifying expression patterns** — the reporter shows where and when the nearby enhancer/gene is active, and the line becomes a marker for that tissue (with GAL4 instead of *lacZ* it becomes a **driver line**, see pGAWB below).

2.  **Identifying the gene** — the insertion is a molecular tag (the flanking DNA is recovered by plasmid rescue or IPCR) and often **disrupts the nearby gene**, giving a mutant allele whose phenotype can be studied.

---
> [[FG 11 - Drosophila melanogaster · The fly as a model organism|← Drosophila melanogaster · The fly as a model organism]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 13 - Drosophila melanogaster · Reverse genetics in Drosophila|Drosophila melanogaster · Reverse genetics in Drosophila →]]
