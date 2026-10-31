---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "lecture + course material"
order: 24
tags: [note, fg, drosophila, p-element, gal4-uas, rnai]
aliases:
  - P element
  - GAL4/UAS
  - RNAi step by step
---

> [[FG 23 - Balancer chromosomes – step by step|← Balancer chromosomes — step by step]] · [[Functional Genetics|↑ Functional Genetics]]

# Breaking, switching on, switching off — step by step

*Mechanism companion to [[FG 13 - Drosophila melanogaster · Forward genetics in Drosophila|Forward genetics in Drosophila]], [[FG 14 - Drosophila melanogaster · Reverse genetics in Drosophila|Reverse genetics in Drosophila]] and [[FG 11 - Caenorhabditis elegans · Reverse genetics in C. elegans|Reverse genetics in C. elegans]] · P element, GAL4/UAS, RNAi*

## 1. P element — structure: what the element looks like

The autonomous element is **2907 bp**: two ends that get cut, internal sites where the transposase binds, and in between the transposase gene itself.

1. **An element inside the genome.** The P element is the transposon that made the fly an organism you can not only break but also build.
2. **31 bp terminal inverted repeats.** The substrate for cleavage.
3. **11 bp internal inverted repeats.** The actual transposase binding sites.
4. **ORF in exons 0, 1, 2, 3.** In the middle lies the transposase gene, in four exons.
5. **IVS3.** The third intron is the one that decides everything: it is removed only in the germ line.
6. **8 bp duplication.** The element is flanked by an 8 bp duplication of the insertion site — the molecular signature of the event, and the proof that insertion goes through a staggered cut.

**Remember**

- The terminal 31 bp are **cut**; the internal 11 bp **bind** the transposase. Two different things.
- Key idea: transposon and transposase can be **separated**. Both transgenesis and insertional mutagenesis follow from this.
- Insertion is **not random**: it prefers the 5′ regions of genes (promoters and first introns), with hotspots and coldspots. This is why no collection of P insertions saturates the genome, and why **piggyBac** and **Minos**, with complementary preferences, came later.

## 2. P element — soma or germ line: why it only jumps in the germ line

The same transcript gives two different proteins, depending on whether IVS3 is removed or not.

| Element | Splicing of IVS3 | Consequence |
| --- | --- | --- |
| **Autonomous element** | removed only in the germ line; in the soma **PSI** (P-element Somatic Inhibitor, hnRNP-like) together with **hrp48** binds exonic sequences upstream of the splice site and blocks removal | germline transposition only |
| **Δ2-3(99B)**, the classic jumpstarter | IVS3 already deleted **at the DNA level** | transposase made constitutively, soma included, without depending on splicing; having lost its inverted repeats it is not a valid substrate for itself and cannot move |

1. **Primary transcript.** Contains three introns.
2. **The first two introns.** Removed in all cells.
3. **In the soma: PSI blocks.** Removal of IVS3 is prevented.
4. **In the germ line: IVS3 is removed.** Nothing blocks splicing there.
5. **Two different proteins.** Soma: IVS3 retained, truncated ORF, **66 kDa repressor**. Germ line: complete ORF, active **87 kDa transposase**.

**Remember**

- This is why the P element is a **germline** mutagen and not a somatic one.
- It is also the molecular basis of **hybrid dysgenesis**: P males × M females. The maternal M cytoplasm has neither the repressor nor the piRNAs that silence the element, so transposition explodes in the germ line of the progeny — sterility, mutations, chromosome breaks.

## 3. P element — cut-and-paste

The transposase, as a multimer, binds the internal 11-mers, brings the two ends together and cuts. The element **moves**; it does not copy itself.

1. **Binding to the 11-mers.** The transposase binds as a multimer at both ends.
2. **Synapsis.** The two ends are brought together and paired.
3. **Staggered cut.** The cuts are staggered and leave **17-nucleotide 3′ extensions** on the element.
4. **Insertion elsewhere.** The excised element inserts at another site through an 8 bp staggered cut.
5. **8 bp duplication.** Once filled in by the polymerase, that cut generates the target-site duplication.
6. **The donor site.** Excision leaves a double-strand break that the cell must repair.

| Repair of the donor site | Outcome |
| --- | --- |
| **Homologous recombination** | the cell repairs using the sister chromatid, which still carries the element, so the element reappears at the donor site: copy number *seems* to increase although the mechanism is conservative |
| **End joining** | a **footprint** remains — a few residual bp of the inverted repeats, often with a frameshift. This is the basis of **imprecise excision**, used historically to generate deletions from a known insertion |

**Remember**

- The mechanism is **non-replicative**: the element moves, it does not copy itself.
- The 8 bp duplication is the signature of insertion.

## 4. P element — mutator × jumpstarter: two lines that do nothing on their own

Cooley, Kelley and Spradling (*Science* 1988): separating the transposon from the transposase turns a random jump into a stable, tagged allele.

1. **The two parental lines.** Both in a *w⁻* background. The first carries a **non-autonomous mutator** element with the *white⁺* marker, on chromosome II. The second carries an immobile **jumpstarter** (the transposase source) on chromosome III, tagged with a dominant marker **M**.
2. **On their own they cannot move.** The mutator has no transposase; the jumpstarter has no inverted repeats.
3. **F1: together.** Select F1 males with red eyes (they carry the mutator) and the M marker (they carry the jumpstarter). Only in these males are the two pieces together, so transposition happens.
4. **The jump.** The element lands on any chromosome: I, II or III.
5. **Cross to balancer females.** F1 males are crossed to white-eyed females carrying a balancer.
6. **F2: freezing the insertion.** Keep offspring that are red-eyed (they kept the element), **M⁻** (they lost the jumpstarter, so the new insertion can no longer move) and balanced.

**Remember**

- The result is a new allele, **stable and molecularly tagged**: it can be mapped, cloned and tested by complementation. Balancers are what keep it — see [[FG 23 - Balancer chromosomes – step by step|Balancer chromosomes — step by step]].
- The genomic DNA next to the insertion is recovered by **plasmid rescue** (*ori* and *kan*ʳ inside the construct) or by **inverse PCR**. In both cases the known P-element sequence is the handle used to pull out the unknown flank.
- Many ways to break a gene: the insertion can land in the enhancer, promoter, 5′ UTR, an exon, an intron or the 3′ UTR — how severe the allele is depends on where it lands.

## 5. P element — enhancer trap: the element that spies on enhancers

What the element traps is a **genomic enhancer** next to the insertion point and, with it, that enhancer's expression pattern. It does not trap the gene or the promoter.

| Trap type | Requirement |
| --- | --- |
| **Enhancer trap** | the element only needs to land **near** an enhancer: upstream of a gene, in an intron, even some distance away. The weak P promoter alone is not enough, so the staining reports the trapped enhancer and nothing else |
| **Gene trap** | the reporter has **no promoter of its own** and must insert **inside a transcribed gene**, in the right orientation — usually in an intron, with a splice acceptor — so that it is spliced into the endogenous transcript and reports that gene's expression |

1. **The PZ construct.** O'Kane and Gehring, 1987. The P element promoter is weak (main start site 87 bp from the 5′ end), and the second exon is fused in frame to *lacZ*, with a nuclear localisation signal.
2. **Random insertion.** The element lands near a genomic enhancer.
3. **The enhancer acts on the weak promoter.** That promoter is not enough on its own: the reporter switches on only if an enhancer helps it. This is what "trapping" means.
4. **Staining.** β-galactosidase shows the pattern directly, in embryos, imaginal discs and adult tissues.
5. **Three things at once.** The same insertion gives the pattern, a mutant allele and a handle for cloning.

**Remember**

- **Why a weak promoter:** a strong one would drive expression everywhere and hide the pattern.
- With **GAL4** instead of *lacZ* the trapped pattern is not only visible but usable — this is the **pGAWB** vector.
- The construct also carries the *hsp70* trailer sequence and polyadenylation site, *kan*ʳ and *ori* for plasmid rescue, and *rosy⁺* as a transformation marker.

## 6. GAL4/UAS — the driver decides where, the responder decides what

Brand and Perrimon, 1993. GAL4 is the yeast activator and UAS is its binding site; neither exists in the fly, so the system is orthogonal.

1. **Two separate lines.** The driver carries GAL4 under a specific promoter or enhancer; the responder carries the gene of interest downstream of the UAS.
2. **On their own they do nothing.** GAL4 has no endogenous targets in the fly, and no fly factor recognises the UAS.
3. **The cross.** The progeny carries both transgenes.
4. **GAL4 binds as a dimer.** The UAS is a 17 bp palindrome, consensus **CGG-N₁₁-CCG**: one monomer contacts each CGG half-site and the central 11 bp act as a spacer. The pUAST vector has **5 sites in tandem**, so more dimers bind and expression is stronger.
5. **On only there.** The gene switches on only in cells that produce GAL4.

| What the fly carries | What happens |
| --- | --- |
| **Both transgenes** | GAL4 is made in the driver pattern, binds the UAS and switches the gene on exactly in those cells. If both parental lines are heterozygous, only **¼** of the progeny carries both |
| **Driver only** | GAL4 is made in the pattern of its promoter but has no target genes in the fly: the driver line is phenotypically neutral |
| **Responder only** | no fly factor recognises the UAS, so the gene stays off — which is why **lethal or toxic constructs can be kept in stock** |
| **GAL4-VP16** | the GAL4 DNA-binding domain fused to the acidic activation domain of herpes simplex VP16: a much stronger activator, but more toxic |

**Remember**

- GAL4 is **881 aa**: DNA-binding domain aa **1–65**, a binuclear **Zn(II)₂Cys₆** zinc cluster (not a classical zinc finger); dimerisation **65–94**; two acidic activation regions **148–196** and **768–881**; GAL80 binds **851–881**.
- Driver lines are made in two ways: put an already characterised promoter upstream of GAL4 (**pPTGAL4**), or use enhancer trapping with **pGAWB** to discover new patterns.
- **pUAST works only in somatic cells.** For the germ line, **pUASp** is used, with the P transposase promoter and the *K10* 3′UTR.

## 7. GAL4/UAS — GAL80 and TARGET: adding the "when"

Many drivers are not strictly limited in time, and this often causes lethality before the stage of interest.

1. **Three transgenes.** The GAL4 driver, the UAS–gene X responder, and a third line with **GAL80<sup>ts</sup>** (GAL80 is the natural inhibitor of GAL4 in yeast).
2. **How it inhibits.** GAL80 binds residues **851–881** of GAL4, the terminal part of the second activation domain: GAL4 stays on the DNA but no longer recruits Mediator — inhibition by occlusion, not by competition.
3. **Temperature shift.** The **TARGET** system uses a temperature-sensitive GAL80, so temperature becomes the switch.
4. **Spatial and temporal together.** The driver gives the "where", temperature the "when" — and it works with any existing driver.

| Temperature | State |
| --- | --- |
| **18–19 °C** | GAL80<sup>ts</sup> is folded and blocks GAL4 → gene **OFF**. GAL4 activity is also minimal at 18 °C on its own, being a yeast protein |
| **29–32 °C** | GAL80<sup>ts</sup> is inactivated and can no longer bind GAL4 → gene **ON**. GAL4 is itself most active at 29 °C; induction is maximal around 32 °C |

**Remember**

- Mnemonic: **cold = GAL80<sup>ts</sup> works = OFF; warm = GAL80<sup>ts</sup> broken = ON.**
- Other routes to temporal control: GAL80 under a heat-shock promoter, **GeneSwitch** (GAL4 made inducible by RU486) and the hybrid UAS-GAL4-Tet system.
- For control **in clones**: **AyGAL4** — heat shock → FLP → excision of the STOP between the FRT sites → GAL4 expressed only in the cells where excision happened, and all their descendants.

## 8. GAL4/UAS — Tet: TetOFF, TetON and the hybrid

A chemical switch: a tetracycline-sensitive transactivator and its *tet*-O operator.

1. **The *tet*-O operator.** Sits upstream of the reporter gene and waits for its transactivator.
2. **The transactivator.** **tTA** is the bacterial repressor TetR fused to VP16; **rtTA** is the same TetR, mutated so that the logic is reversed.
3. **Giving the drug.** Tetracycline or doxycycline, fed to the animals.
4. **The switch flips.** The drug changes the conformation of TetR: in TetOFF, DNA binding is lost; in TetON, it is gained.

| System | Logic |
| --- | --- |
| **TetOFF (tTA)** | a specific promoter drives tTA. Without tetracycline it binds *tet*-O and activates the reporter; tetracycline abolishes DNA binding → **drug = gene off** |
| **TetON (rtTA)** | a TetR mutant that binds *tet*-O **only** in the presence of doxycycline → **drug = gene on** |
| **GAL4-Tet hybrid** | the two systems in series: GAL4 controls expression of rtTA, which controls the reporter. The driver gives the "where", the drug the "when" |

**Remember**

- The other drug-based system is **GeneSwitch**: a chimeric GAL4 with the **p65** activation domain and a hormone receptor domain. Without ligand it is held inactive in a complex with **HSP90**; **RU486** fed to the flies triggers the conformational change, releases HSP90 and exposes p65.
- Drug-based systems avoid both heat shock and temperature shifts — but are slower than temperature.

## 9. RNAi — Dicer and RISC: the gene stays intact, the message does not

Discovered in *C. elegans* by Fire and Mello: a dsRNA matching the target gene causes that gene's mRNA to be degraded.

1. **dsRNA.** A double-stranded RNA matching the target sequence enters the cell and is recognised by **Dicer**, an RNase III endoribonuclease.
2. **Dicer cuts.** It binds the long dsRNA and cuts it into short double-stranded fragments of **21–23 nt**.
3. **siRNA and RISC.** The siRNA duplexes associate with proteins to form the **RISC** complex.
4. **The passenger strand.** Inside RISC the duplex is unwound; the sense strand is cleaved and discarded, and the antisense **guide** remains.
5. **Recognition.** The guide brings activated RISC to the target mRNA by sequence complementarity.
6. **mRNA cleavage.** RISC cleaves the mRNA: the transcript is degraded and the protein disappears — a **post-transcriptional** loss of function.

**Remember**

- In short: **dsRNA → Dicer → siRNA → RISC → cleavage of the matching mRNA.**
- The gene itself is not touched: RNAi gives a **knockdown** (partial, often transient), not a knockout.
- Fire et al. 1998 compared sense, antisense and sense + antisense RNA on genes with known phenotypes (*unc-22*, *fem-1*, *unc-54*, *hlh-1*). Only **double-stranded** RNA gave potent and specific interference.

## 10. RNAi — delivery: getting the dsRNA in

In the worm there are three routes, all starting from the same plasmid. The fly uses a different one.

1. **The L4440 plasmid.** The target gene segment is cloned between two **convergent T7 promoters**: transcription starts from both sides and yields a double strand.
2. **Delivery.** What changes between methods is only how the dsRNA reaches the cells.
3. **Phenotype.** Animals are observed and scored for the loss-of-function phenotype.
4. **The spacer.** In the fly IR construct, an unrelated spacer gets around the instability of symmetric sequences.

| Method | How it works |
| --- | --- |
| **Microinjection** | dsRNA made from L4440 by in vitro transcription with T7 polymerase, injected into the germ cells or gonad of adult hermaphrodites; the progeny is then examined. Highly reproducible between individuals, a few nanograms are enough — but laborious |
| **Soaking** | the same dsRNA, but embryos or worms are soaked directly in the solution in a tube, then transferred to a plate and observed |
| **Feeding (HT115)** | L4440 is transformed into *E. coli* **HT115**: **RNase III⁻**, so it does not degrade the dsRNA it makes, and carrying an **IPTG-inducible T7 polymerase**. Bacteria are plated with IPTG, the worms eat the lawn, phenotypes are scored. This is what makes genome-wide screens possible: one clone, one plate, one gene |
| **UAS-IR in the fly** | the responder carries the gene in sense and antisense orientation, separated by an unrelated spacer, downstream of 5×UAS. In the F1 of a cross with a GAL4 driver the construct is transcribed in GAL4-expressing cells and folds into a hairpin; the resulting dsRNA triggers RNAi exactly where the driver is active — a tissue-specific knockdown in an animal where RNAi by ingestion does not work |

**Remember**

- The proper control for RNAi is **two independent lines** against the same gene, or a rescue construct.
- Genome-wide collections of UAS-IR lines exist: **VDRC** and **TRiP**, the latter using miRNA-based constructs, more efficient and with fewer off-target effects.
- The known problem is **off-target knockdown** through partial homology, made worse by CAN/CAG repeats.

---
> [[FG 23 - Balancer chromosomes – step by step|← Balancer chromosomes — step by step]] · [[Functional Genetics|↑ Functional Genetics]]
