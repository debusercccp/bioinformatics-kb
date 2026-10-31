---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "lecture + course material"
order: 22
tags: [note, fg, crispr, genome-editing]
aliases:
  - CRISPR
  - Cas9
  - HDR
---

> [[FG 21 - Danio rerio · Optogenetics|← Danio rerio · Optogenetics]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 23 - Balancer chromosomes – step by step|Balancer chromosomes — step by step →]]

# CRISPR-Cas9 — step by step

*Mechanism companion to [[FG 19 - Danio rerio · CRISPRCas9 – from gene to disease model|CRISPR/Cas9: from gene to disease model]] · schematic, not to scale*

## 1. Origin: adaptive immunity in bacteria

In bacteria CRISPR is an adaptive immune system: it stores a memory of the phage and uses it on the second infection.

1. **First infection.** The phage injects its DNA into the bacterium.
2. **Spacer acquisition.** A fragment of phage DNA is inserted into the CRISPR locus as a new spacer between two repeats. Carried out by Cas1 and Cas2.
3. **Transcription into crRNA.** The CRISPR locus is transcribed and yields crRNAs, one per spacer.
4. **Complex with tracrRNA and Cas9.** The crRNA together with the tracrRNA forms a complex with Cas9.
5. **Second infection: cleavage.** Cas9 recognises the matching foreign DNA and cuts it. The bacterium is resistant to that virus.

**Remember**

- The locus alternates repeats and spacers: each spacer is the memory of one infection.
- In the lab crRNA and tracrRNA are fused into a single synthetic sgRNA.
- History: Francis Mojica proposed CRISPR arrays as a bacterial immune defence; Doudna and Charpentier proposed their use for editing (Nobel 2020).

## 2. Finding the target: Cas9 searches for the PAM, not for the guide

Cas9 does not scan the genome looking for the guide sequence. It looks for the PAM. Only afterwards does it attempt base pairing.

1. **Search.** Guide-loaded Cas9 samples the DNA and detaches almost immediately nearly everywhere.
2. **PAM docking.** It stops at 5′-NGG-3′, read in the major groove by Arg1333 and Arg1335, which hydrogen-bond the two guanines.
3. **Unwinding and seed.** Only after the PAM does Cas9 destabilise the duplex immediately upstream and attempt pairing with the guide, from PAM-proximal to PAM-distal. The first ~10–12 nt are the seed.
4. **R-loop.** If the seed pairs, pairing propagates to a complete R-loop: guide paired to the target strand, the other strand displaced.

**Four cases**

| Case | Outcome |
| --- | --- |
| PAM present, seed paired | R-loop completes, cleavage can occur |
| No PAM | No cleavage, whatever the homology. This is also why the bacterial CRISPR locus does not cut itself: it contains the spacers but not their PAMs |
| Mismatch in the seed | The complex detaches within milliseconds and resumes the search |
| PAM-distal mismatch | Often tolerated: the R-loop completes anyway and cleavage happens at the wrong site. This is where off-targets come from |

**Remember**

- No PAM, no cut, whatever the homology.
- Seed mismatches abolish cleavage; PAM-distal mismatches are often tolerated — hence off-targets.
- The protospacer is 20 bp long and is defined by the spacer of the guide.

## 3. The cut: HNH and RuvC cleave the two strands

Once the R-loop is complete, the two nuclease domains cut almost together and leave blunt ends.

1. **Complete R-loop.** The starting point is the end of the previous step.
2. **HNH rearranges.** HNH changes conformation and comes into contact with the target strand.
3. **Allosteric checkpoint.** That movement acts as a control: it is what licenses RuvC as well.
4. **Near-simultaneous cleavage.** HNH cuts the target strand, RuvC the displaced strand.
5. **Blunt DSB 3 bp from the PAM.** A double-strand break with blunt ends, 3 bp upstream of the PAM. The position is predictable, and this is what makes precise insertions designable.

**Remember**

- Cas9 only cuts. The outcome depends on how the cell repairs.
- The predictability of the cut site is what allows precise knock-ins to be designed.

## 4. Repair without a template: NHEJ

With no template the cell rejoins the ends in an error-prone way and leaves small insertions or deletions.

1. **Two blunt ends.** The starting point is the cut.
2. **Error-prone rejoining.** The ends are ligated without a template.
3. **Small indel.** A small insertion or deletion remains at the junction.
4. **Reading frame.** If the indel is not a multiple of 3, the frame shifts and the downstream codons change.
5. **Premature stop and NMD.** A premature stop codon usually appears: the mRNA undergoes nonsense-mediated decay and function is lost.

**Indel size**

- **1 nt indel** — not a multiple of 3: the reading frame shifts, downstream codons change, and a premature stop usually appears. Gene disrupted.
- **3 nt indel** — a multiple of 3: the frame is preserved, one amino acid is lost or gained. The protein often still works, at least partly.

**Remember**

- No template → NHEJ → indel → frameshift → knock-out.
- An in-frame indel is one of the reasons F0 crispants are variable.

## 5. Repair with a template: HDR

With a donor DNA template the cell repairs by copying the supplied sequence.

1. **Same cut, template present.** A donor DNA supplied by the experimenter is added alongside the cut.
2. **Homology arms.** The donor carries two arms identical to the regions flanking the cut.
3. **Alignment.** The arms anneal to the two ends and fix the position.
4. **Copying.** The cell copies from the donor whatever lies between the arms.
5. **Precise modification.** The intended change remains in the endogenous locus: an insertion, a fluorescent tag or a point mutation.

**Donor format**

- **ssODN**, 100–200 nt single-stranded oligo, homology arms of 30–60 nt per side: point mutations, SNPs, small epitope tags.
- **Plasmid** or linear PCR product, arms of 500–1000 bp: large inserts, GFP, cassettes with a selection marker.
- **Long ssDNA via AAV or Easi-CRISPR**: mouse embryos, inserts of a few kb with better efficiency than plasmid.

Donor ≠ delivery vector: lentivirus and AAV are how the components get into the cell, the donor is the template. AAV can do both, hence the ambiguity.

**Design points**

- The donor must be co-delivered with the RNP, not afterwards: if the template is not already present when the cut happens, the break is closed by NHEJ.
- **Mutate the PAM or the seed in the donor** (synonymous mutations, if coding). Otherwise the corrected allele is still a target and Cas9 re-cuts it. For the same reason the donor must not contain an intact guide site.
- Molar excess of donor over RNP.
- Screening is mandatory: PCR across the junction (one primer inside the insert, one in the genome outside the arm), sequencing, FACS if there is a fluorophore, drug selection if there is a cassette.

**Remember**

- Template with homology arms → HDR → precise modification (knock-in, point mutation, GFP tag).
- HDR is restricted to S/G2 and is rare. In the embryo repair goes mostly through NHEJ, so HDR events have to be selected.
- In mouse, the classic knock-in is instead done by homologous recombination in ES cells, because the event is rare and must be selected in culture.

## 6. Beyond cutting: same targeting, different uses

The guide stays the same. What changes is what is attached to the Cas protein.

| Tool | Question it answers | How it works |
| --- | --- | --- |
| **Cas9 knock-out** | What happens if gene function is reduced? | Double-strand break and indels |
| **CRISPRi** | Same, without touching the DNA | Catalytically dead dCas9, usually fused to a repressor domain, targeted to the promoter or the start of the gene: transcription is blocked. A knockdown; with a tissue-specific promoter it stays confined to that tissue |
| **CRISPRa** | What happens if the gene is overexpressed? | The same dCas9 fused to an activator: expression increases, again with no DNA break |
| **Base editing** | What does a precise variant do? | Cas9 nickase fused to a deaminase converts one base (e.g. A→G) without a double-strand break |

1. **Same targeting.** The guide delivers the complex in the same way, under the same PAM constraint.
2. **The effector changes.** Active nuclease, dCas9 with a repressor or activator, or nickase with a deaminase.
3. **The question changes.** Knock-out, change in expression, or precise variant: the tool is chosen from the question.

**Remember**

- Example from the course: *rrm2b* and *sting* repressed with CRISPRi in endothelial cells, in the doxorubicin cardiotoxicity model.
- Before CRISPR: ZFN and TALEN, a DNA-binding domain fused to FokI, which cuts only as a dimer. Every new target required a new protein, which is why the RNA-guided system replaced them.
- If the goal is a single base, a separate donor can be avoided altogether: base editing converts the base in place, and prime editing carries the template inside the guide itself (pegRNA).

## 7. In vivo: F0 crispants are mosaics

Injecting the RNP into the one-cell embryo gives a phenotype immediately, but the animal is a mosaic.

1. **One-cell injection.** The guide + Cas9 complex, preassembled in vitro (RNP), is microinjected into the embryo at the one-cell stage, often with several guides against the same gene.
2. **Every cell repairs on its own.** Cas9 cuts and NHEJ repairs independently in each cell.
3. **Mosaic of alleles.** The same guide leaves different indels: in-frame or frameshift, mono- or biallelic, next to unmodified cells.
4. **Phenotype immediately, but variable.** Generations are saved, but the phenotype varies between individuals and between tissues.

**Remember**

- An F0 embryo must not be treated as a homozygous null.
- For solid conclusions: genotype the embryos (amplicon sequencing, editing efficiency), use several independent guides, and confirm in stable lines (F1 heterozygotes → F2 homozygotes).
- Zebrafish was the first vertebrate in which CRISPR/Cas9 showed efficient in vivo editing (Hwang et al., 2013).

---
> [[FG 21 - Danio rerio · Optogenetics|← Danio rerio · Optogenetics]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 23 - Balancer chromosomes – step by step|Balancer chromosomes — step by step →]]
