---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/Functional_Genetics/FunctionalGen_common.docx"
order: 19
tags: [note, fg]
---

> [[FG 18 - Danio rerio · Reporter lines – making gene expression visible|← Danio rerio · Reporter lines – making gene expression visible]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 20 - Danio rerio · Modelling cancer in zebrafish|Danio rerio · Modelling cancer in zebrafish →]]

*Approfondimento: [[FGx 01 - CRISPR-Cas9 – step by step|CRISPR-Cas9 – step by step]]*

# CRISPR/Cas9: from gene to disease model

### How we can study gene function with zebrafish

Before genome editing the options were **random gene disruption** (ENU), **knockdown by morpholinos** and **knockdown by RNA interference** (modified miRNA hairpins). The knockdowns **transiently suppress protein levels**, give **no complete ablation of the gene** and have **off-target effects**. Targeted genome editing came with **ZFN** (zinc-finger nucleases), **TALEN** (transcription activator-like effector nucleases) and then **CRISPR-Cas9**.

> **Focus — ZFN and TALEN. DNA-binding domain + FokI dimer; one new protein per target, hence replaced by CRISPR.**

### ![[FG-image59.png|290]]CRISPR-Cas9 in zebrafish

- Zebrafish was the **first vertebrate** in which CRISPR/Cas9 was shown to **efficiently edit the genome in vivo** (Hwang et al., 2013).

- **Guide RNA** (crRNA + tracrRNA): a short synthetic RNA with a **scaffold** sequence needed for Cas binding and a user-defined **~20-nt spacer** that defines the genomic target. **Target sequence: 20 bp.**

- A **CRISPR-associated endonuclease** (Cas protein).

- An **in vitro complex of guide RNA and Cas9 protein** (RNP) is **microinjected into one-cell-stage embryos**.

- CRISPR knockout zebrafish are **extremely popular** and model many diseases. Since 2004, about **28,000 articles** on CRISPR/Cas, **\>1000 in zebrafish**. History: **Francis Mojica** proposed CRISPR arrays as part of a **bacterial immune defence**; **Doudna & Charpentier** proposed gene-editing applications (**Nobel Prize 2020**).

- Timeline: with CRISPR/Cas9 a homozygous mutant line (F2) can be obtained in about nine months.

> **Focus — What happens after the cut. NHEJ → indels → frameshift → loss of function; precise edits need HDR.**
>
> **Paper — Hwang et al., 2013** (Nat. Biotechnol. 31:227–229): The first CRISPR test in a whole organism: sgRNA and Cas9 mRNA co-injected into one-cell embryos gave indels at 8 of 10 sites (24–59% per embryo), as efficient as ZFNs and TALENs. Today Cas9 protein (RNP) is usually injected instead of mRNA to reduce mosaicism.

#### Origin: adaptive immunity in bacteria

In bacteria CRISPR is an adaptive immune system: it stores a memory of the phage and uses it on the second infection.

1.  **First infection.** The phage injects its DNA into the bacterium.

2.  **Spacer acquisition.** A fragment of phage DNA is inserted into the CRISPR locus as a new spacer between two repeats. Carried out by Cas1 and Cas2.

3.  **Transcription into crRNA.** The CRISPR locus is transcribed and yields crRNAs, one per spacer.

4.  **Complex with tracrRNA and Cas9.** The crRNA together with the tracrRNA forms a complex with Cas9.

5.  **Second infection: cleavage.** Cas9 recognises the matching foreign DNA and cuts it. The bacterium is resistant to that virus.

#### Finding the target: Cas9 searches for the PAM, not for the guide

Cas9 does not scan the genome looking for the guide sequence. It looks for the PAM. Only afterwards does it attempt base pairing.

1.  **Search.** Guide-loaded Cas9 samples the DNA and detaches almost immediately nearly everywhere.

2.  **PAM docking.** It stops at 5′-NGG-3′, read in the major groove by Arg1333 and Arg1335, which hydrogen-bond the two guanines.

3.  **Unwinding and seed.** Only after the PAM does Cas9 destabilise the duplex immediately upstream and attempt pairing with the guide, from PAM-proximal to PAM-distal. The first ~10–12 nt are the seed.

4.  **R-loop.** If the seed pairs, pairing propagates to a complete R-loop: guide paired to the target strand, the other strand displaced.

**Four cases**

| **Case** | **Outcome** |
|----|----|
| PAM present, seed paired | R-loop completes, cleavage can occur |
| No PAM | No cleavage, whatever the homology. This is also why the bacterial CRISPR locus does not cut itself: it contains the spacers but not their PAMs |
| Mismatch in the seed | The complex detaches within milliseconds and resumes the search |
| PAM-distal mismatch | Often tolerated: the R-loop completes anyway and cleavage happens at the wrong site. This is where off-targets come from |

#### The cut: HNH and RuvC cleave the two strands

Once the R-loop is complete, the two nuclease domains cut almost together and leave blunt ends.

1.  **Complete R-loop.** The starting point is the end of the previous step.

2.  **HNH rearranges.** HNH changes conformation and comes into contact with the target strand.

3.  **Allosteric checkpoint.** That movement acts as a control: it is what licenses RuvC as well.

4.  **Near-simultaneous cleavage.** HNH cuts the target strand, RuvC the displaced strand.

5.  **Blunt DSB 3 bp from the PAM.** A double-strand break with blunt ends, 3 bp upstream of the PAM. The position is predictable, and this is what makes precise insertions designable.

#### Repair without a template: NHEJ

With no template the cell rejoins the ends in an error-prone way and leaves small insertions or deletions.

1.  **Two blunt ends.** The starting point is the cut.

2.  **Error-prone rejoining.** The ends are ligated without a template.

3.  **Small indel.** A small insertion or deletion remains at the junction.

4.  **Reading frame.** If the indel is not a multiple of 3, the frame shifts and the downstream codons change.

5.  **Premature stop and NMD.** A premature stop codon usually appears: the mRNA undergoes nonsense-mediated decay and function is lost.

**Indel size**

- **1 nt indel** — not a multiple of 3: the reading frame shifts, downstream codons change, and a premature stop usually appears. Gene disrupted.

- **3 nt indel** — a multiple of 3: the frame is preserved, one amino acid is lost or gained. The protein often still works, at least partly.

#### Repair with a template: HDR

With a donor DNA template the cell repairs by copying the supplied sequence.

1.  **Same cut, template present.** A donor DNA supplied by the experimenter is added alongside the cut.

2.  **Homology arms.** The donor carries two arms identical to the regions flanking the cut.

3.  **Alignment.** The arms anneal to the two ends and fix the position.

4.  **Copying.** The cell copies from the donor whatever lies between the arms.

5.  **Precise modification.** The intended change remains in the endogenous locus: an insertion, a fluorescent tag or a point mutation.

**Donor format**

- **ssODN**, 100–200 nt single-stranded oligo, homology arms of 30–60 nt per side: point mutations, SNPs, small epitope tags.

- **Plasmid** or linear PCR product, arms of 500–1000 bp: large inserts, GFP, cassettes with a selection marker.

- **Long ssDNA via AAV or Easi-CRISPR**: mouse embryos, inserts of a few kb with better efficiency than plasmid.

Donor ≠ delivery vector: lentivirus and AAV are how the components get into the cell, the donor is the template. AAV can do both, hence the ambiguity.

**Design points**

- The donor must be co-delivered with the RNP, not afterwards: if the template is not already present when the cut happens, the break is closed by NHEJ.

- **Mutate the PAM or the seed in the donor** (synonymous mutations, if coding). Otherwise the corrected allele is still a target and Cas9 re-cuts it. For the same reason the donor must not contain an intact guide site.

- Molar excess of donor over RNP.

Screening is mandatory: PCR across the junction (one primer inside the insert, one in the genome outside the arm), sequencing, FACS if there is a fluorophore, drug selection if there is a cassette.

### CRISPR tools answer different questions

| **Tool** | **Question** | **How** |
|----|----|----|
| Cas9 knockout | What happens when gene function decreases? | Double-strand break → indels |
| dCas9 regulation (CRISPRa, CRISPRi, epigenome editing) | What happens when expression changes? | Catalytically dead Cas9 fused to an activator, repressor or chromatin modifier; no DNA break |
| Precise editing (base editing) | What does a specific variant do? | Nickase Cas9 fused to a deaminase (e.g. A→G) |

![[FG-image60.png|513]]

*CRISPR tools answer different questions (Sander & Joung, 2014).*

The guide stays the same across all of these tools: what changes is what is attached to the Cas protein (active nuclease, dCas9 with a repressor or activator, or nickase with a deaminase), and the tool is chosen from the question.

### CRISPRi and a worked example: doxorubicin cardiotoxicity

**CRISPRi** (CRISPR interference): **dCas9**, usually fused to a repressor domain, is guided to the promoter/start of a gene and **blocks transcription** → a **knockdown without changing the DNA**. If dCas9 is expressed from a tissue-specific promoter, the knockdown is restricted to that tissue.

**The problem.** **Doxorubicin** (Dox) remains an essential component of many anticancer regimens, but causes **severe cardiotoxicity**. The heart contains cardiomyocytes, **endothelial cells**, fibroblasts and cardiac progenitors; **endothelial cells are affected** by Dox through:

- **reduced regenerative ability** of progenitors;

- **impaired VEGF signalling** or aberrant activation of the **TGF-β** pathway;

- **impaired autophagy** via Atg7;

- **cellular senescence**.

![[FG-image61.png|687]]

**The experiment** (Graziani et al., *EMBO Reports* 2026): “**Endothelial RRM2B-dependent mitochondrial DNA signalling drives doxorubicin cardiotoxicity**”.

- ***rrm2b*** and ***sting*** were down-regulated by **CRISPRi in endothelial cells**; efficiency was verified on sorted cells.

- **Readout: heart rate**, in DMSO vs Dox-treated larvae.

- **Result**: endothelial *rrm2b* or *sting* down-regulation **prevents the development of the cardiotoxic phenotype** after exposure to Dox at **3 dpf**.

> **Focus — The logic. Endothelium-only knockdown of rrm2b or sting protects the heart.**

### F0 crispants: rapid functional screening

![[FG-image62.png|328]](See also Crispants in Module 1.)

- **Cas9 RNPs** injected at the one-cell stage.

- **Several target sites within one gene**: with **three synthetic guides, \>90% of F0 embryos are biallelic knockouts** in the tested assays (Kroll et al., 2021; readout: loss of pigment in *slc24a5* crispants).

- **Phenotyping in the injected generation** — no need to raise stable lines.

> F0 animals are mosaics: Cas9 cuts and NHEJ repairs independently in each cell, so the same guide leaves different indels (in-frame or frameshift, mono- or biallelic) next to unmodified cells. The phenotype is immediate but varies between individuals and between tissues.

- Experiments completed **before independent feeding** (typically **\<5 dpf**) generally **do not require an animal-experimentation project authorisation** under EU legislation.

> **Focus — Why several guides. Three guides per gene make an F0 crispant behave almost like a null.**

**Remember**

- No PAM, no cut, whatever the homology.

- Seed mismatches abolish cleavage; PAM-distal mismatches are often tolerated — hence off-targets.

<!-- -->

- No template → NHEJ → indel → frameshift → knock-out.

<!-- -->

- Template + homology arms → HDR → precise edit (knock-in, point mutation, tag).

<!-- -->

- F0 crispants are mosaics, not homozygous nulls.

---
> [[FG 18 - Danio rerio · Reporter lines – making gene expression visible|← Danio rerio · Reporter lines – making gene expression visible]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 20 - Danio rerio · Modelling cancer in zebrafish|Danio rerio · Modelling cancer in zebrafish →]]
