---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "lecture + course material"
order: 23
tags: [note, fg, drosophila, balancers]
aliases:
  - Balancers
  - Balancer chromosomes
  - CyO
---

> [[FG 22 - CRISPR-Cas9 – step by step|← CRISPR-Cas9 — step by step]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 24 - Breaking, switching on, switching off – step by step|Breaking, switching on, switching off — step by step →]]

# Balancer chromosomes — step by step

*Mechanism companion to [[FG 13 - Drosophila melanogaster · Forward genetics in Drosophila|Forward genetics in Drosophila]] · schematic, not to scale*

## 1. The problem: a new mutation gets lost

After mutagenesis each treated chromosome carries a new recessive mutation. The weak point of the whole scheme is not making the mutation — it is **keeping** it.

1. **A mutagenised chromosome.** The new recessive mutation sits on one chromosome, heterozygous with the normal homologue.
2. **Invisible in the heterozygote.** The wild-type allele on the other chromosome covers it: the fly looks wild type and the mutation cannot be scored.
3. **Meiosis reshuffles.** The two homologues pair and recombine.
4. **The original chromosome is gone.** The products are reshuffled, so the starting combination — that mutation on that chromosome — is broken up.
5. **Protection is needed.** This is what balancers are for: they carry a mutagenised homologue through the generations without ever recombining with it.

**Remember**

- The weak point of a mutagenesis screen is the stage at which lines are established: a newly induced recessive mutation is invisible in the heterozygote and is lost by recombination unless it is protected.
- Balancers were identified by **H. J. Muller in 1918**.

## 2. The properties: four things on one chromosome

A balancer is a chromosome built (or found) so that it carries the mutagenised homologue forward without ever giving viable recombinants.

1. **A chromosome like any other.** Same chromosome, same centromere; what changes is how it is organised inside.
2. **Multiple, overlapping inversions.** Paracentric and pericentric, on the same chromosome. They cannot pair normally with the homologue in meiosis, and when recombination does happen it produces lethal aneuploidies.
3. **A recessive lethal.** One or more recessive lethal (or sterilising) mutations, so balancer homozygotes do not survive and the balancer cannot become fixed.
4. **A dominant visible marker.** E.g. **Curly** (*Cy*), which lets you follow the balancer through crosses by eye.
5. **Recessive visible markers.** E.g. eye-colour markers, useful in crosses.

**Remember**

- In short: **inversions** → no viable recombinants, so the mutagenised chromosome stays intact; **recessive lethal** → balancer homozygotes die; **dominant marker** → you can tell by eye who carries it.
- Every fly chromosome has its own set of balancers, **except the fourth**.
- **X-chromosome balancers do not carry recessive lethal markers.**
- Example: the ***SM*** balancer of the second chromosome, with a paracentric inversion (22D–34A, 42A–58A) and a pericentric one (21A/22A–60F/60B), marked with *Cy* (curly wings) and a recessive lethal. ***CyO***, "Curly of Oyster", is the standard second-chromosome balancer.

## 3. The inversion loop: why one inverted chromosome is enough

Recombination is not a property of one chromosome but of the **pair**: it requires base-by-base alignment.

1. **Two homologues, one inverted.** One carries an inverted block, the other does not.
2. **Pairing requires homology.** The synaptonemal complex aligns corresponding sequences, base by base.
3. **The only way is the loop.** To match the sequences, the pair can synapse only by forming an **inversion loop**.
4. **The effect is dominant.** A single abnormal chromosome distorts the geometry of both — dominance in a mechanical sense.

**Remember**

- The inversions are multiple and overlapping precisely so that they cover the whole length of the chromosome, leaving no uncovered region where a crossover could still give viable products.

## 4. The recombinants: what happens to them

Recombination is not prevented: the recombinant gametes simply never become flies.

| Inversion type | Centromere | Products of a crossover inside the loop |
| --- | --- | --- |
| **Paracentric** | outside the inverted block | one **dicentric** chromatid and one **acentric** fragment: the dicentric is stretched into an anaphase bridge between the two poles and breaks, the acentric is not segregated and is lost |
| **Pericentric** | inside the inverted block | chromatids carrying a **duplication** of one segment and a **deletion** of another |

1. **The crossover inside the loop.** It does happen.
2. **The recombinant products.** They depend on where the centromere lies relative to the inverted block.
3. **Aneuploid either way.** In both cases the recombinant products are aneuploid and lethal.
4. **The filter acts downstream.** The only viable gametes are the parental ones: either the intact balancer or the intact mutagenised chromosome.

**Remember**

- Practical effect: the mutagenised chromosome stays intact, generation after generation.
- Recombination is not physically prevented — the recombinant gametes simply do not become flies.

## 5. The dominant marker: why it must be dominant

Not a convenience: a necessity that follows from how the balancer is built.

1. **The balancer is homozygous lethal.** By construction. So the only genotype in which it is ever seen alive is the balancer/homologue heterozygote.
2. **A recessive marker would be masked.** The wild-type allele on the other chromosome would cover it.
3. **It would show only in homozygotes.** And that homozygote is dead, so the marker would be invisible forever.
4. **Hence dominant.** In Müller's terms these are gain-of-function alleles (hypermorphs or neomorphs) or antimorphs.

**Remember**

- The molecularly clearest case is **Stubble** (*Sb*, third chromosome): a transmembrane serine protease whose mutant subunit poisons the complex it joins — a dominant negative. It gives short, thick bristles in the heterozygote.
- See [[FG 04 - Effects of mutations on gene function – Müller's classification|Müller's classification]] for the categories.

## 6. The balanced stock: a stock that maintains itself

This is what "balanced stock" means: the marker never disappears and never becomes homozygous.

| Cross | Progeny |
| --- | --- |
| **mut/CyO × mut/CyO** | *CyO*/*CyO* die, and mut/mut die if the mutation is lethal: only mut/*CyO* survive. The stock maintains itself and the mutation stays protected |
| **Cy/+ × Cy/+** | ¼ *CyO*/*CyO* (dead), 2/4 *Cy*/+ (Curly), ¼ +/+ (wild type) → among the survivors, **2/3 Curly and 1/3 wild type** |

1. **The two parents.** Both heterozygous for the balancer.
2. **The four combinations.** One quarter per square.
3. **Balancer homozygotes die.** Because of the recessive lethal.
4. **What is left.** The surviving class is always the heterozygote.

**Remember**

- *Cy* is dominant and homozygous lethal, which is why it neither disappears nor becomes fixed in a balanced stock.
- The same 2/3 : 1/3 ratio is what a **complementation test** reads out: all survivors Curly → same gene; 2/3 Curly and 1/3 wild type → different genes.

## 7. The Nüsslein-Volhard and Wieschaus screen

EMBL Heidelberg, 1979–1980: a saturation screen for the zygotic genes that control the embryonic body plan.

1. **P.** EMS-treated males (*cn bw sp*) crossed to females carrying the *CyO* balancer (*Cy pr cn²*/*pr cn*).
2. **F1.** Balanced males carrying one mutagenised chromosome over the balancer are selected. Each one carries a different chromosome, recognisable by eye colour (bright red vs orange). Each male is crossed individually to *CyO* females.
3. **F2.** ¼ *CyO*/*CyO* (lethal), ¼ balancer over the non-mutagenised chromosome, ½ carrying the mutagenised one. A single pair of balanced siblings is intercrossed.
4. **F3.** The stock segregates balancer homozygotes (they die as larvae), the balanced mutant stock (viable, the line that is kept) and homozygotes for the mutagenised chromosome.
5. **The cuticle.** Those homozygous embryos are the ones collected. The first-instar larval cuticle is a rigid, reproducible map of the body plan, and a dead embryo preserves it, so even a lethal mutant can be scored.

**Remember**

- **Why F3 and not F2 as in the worm:** the fly does not self-fertilise. One generation is needed to put each mutagenised chromosome over the balancer (F1) and one to build a balanced sibling stock (F2); only their intercross gives homozygous embryos (F3).
- To tell the F2 classes apart: extra visible markers, especially eye colours, or **DTS** (dominant temperature-sensitive) lethal mutations, which kill the unwanted class at the restrictive temperature.
- A mutation that abolishes a gene with a **specific role in patterning** leaves almost everything else normal — which is why the gene's normal role can be reconstructed from the defect.
- ~27,000 balanced lines were built by hand to recover 139 loci; most loci were hit more than once, which is the evidence for saturation.

## 8. Side effects: the breakpoints make themselves felt

The physical construction of a balancer and its dominant marking are not entirely independent.

1. **Inversion breakpoints.** They can generate dominant phenotypes on their own.
2. **Inside a gene.** If a breakpoint falls inside a gene, that gene becomes haploinsufficient.
3. **Or by position effect.** A euchromatic gene moved next to heterochromatin is silenced.
4. **Patchy and clonal.** This is **position-effect variegation** (PEV): the eye becomes mottled.

**Remember**

- Three facts worth keeping together: balancers are homozygous lethal; every chromosome has its own set except the fourth; X balancers carry no recessive lethal.
- The same position effect is the reason random P-element insertions give variable expression, and the reason ΦC31 landing sites were chosen in open chromatin — see [[FG 14 - Drosophila melanogaster · Reverse genetics in Drosophila|Reverse genetics in Drosophila]].

---
> [[FG 22 - CRISPR-Cas9 – step by step|← CRISPR-Cas9 — step by step]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 24 - Breaking, switching on, switching off – step by step|Breaking, switching on, switching off — step by step →]]
