---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/FGIG/IG/IntegrativeGen_RS.docx"
order: 4
tags: [note, ig]
---

> [[IG 03 - TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter|← TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 05 - Chromatin and remodelling + Cautions and corrections to keep in mind|Chromatin and remodelling + Cautions and corrections to keep in mind →]]

# Genomic imprinting

For most of our genes, we express both alleles simultaneously (biallelic expression) — one inherited from the Father (F) and one from the Mother (M). However, a small subset of genes (less than 1%) undergoes genomic imprinting.

- **Mechanism:** Imprinting is an epigenetic phenomenon (primarily driven by DNA methylation at specific Imprinting Control Regions, ICRs). It prevents the expression of one allele in a parent-of-origin-specific manner.
- **Maintenance:** This epigenetic silencing is established in the germline (sperm or egg). When the zygote is formed, one of the two alleles is already silenced. Crucially, this imprinted state is maintained clonally in all somatic cells of the developing organism. Every cell in your body will keep that specific parental allele silenced.

### Loss of Imprinting (LOI)

“Loss of Imprinting” is not the normal physiological process, but rather a pathological epigenetic error (frequently observed in cancer).

- In LOI, the cell loses epigenetic marks (like DNA methylation) that were keeping the imprinted allele silenced.
- As a result, a gene that should be expressed from only one allele is now abnormally expressed from both alleles (aberrant biallelic expression), leading to an overproduction of the gene product (often a growth factor, driving tumor formation).

## 10. Enhancer RNAs (eRNAs)

Enhancer elements are **transcribed**. Enhancers:

- Are **modestly conserved** across **species** on the basis of DNA sequence analyses;
- Are marked by **high chromatin accessibility** (DNase hypersensitive sites);
- Have a high ratio of **specific histone marks** (H3K4me1, H3K4me3, H3K27ac) \[note: more precisely, active enhancers have a **high H3K4me1:H3K4me3 ratio** together with H3K27ac, since H3K4me3 is typical of promoters\];
- Show the presence of **RNA Pol II** (assembly of the transcriptional machinery complex);
- Favour the **pause release of RNA Pol II** through **enhancer–promoter looping**.

Enhancers can give rise to **non-coding RNAs** (**eRNAs**), a **novel layer** of the enhancer function. eRNAs are not universally necessary, but they do **contribute to maintaining enhancer activity (the degree of necessity differs by locus)**; they are **bidirectionally transcribed**, and their expression **positively correlates** with the **mRNAs encoded by nearby genes** (so the eRNA level marks the **activation of the enhancer**, even if this correlation does not prove causality). According to the professor, most eRNAs derive from **lncRNAs** \[note: more precisely, the definitions of eRNA and lncRNA (\> 200 nt) overlap, and the review treats the enhancer-derived lncRNAs together with the eRNAs\], and they are **very poorly conserved** between species. eRNAs have a **low abundance** and are **unstable**, **nuclear**, **chromatin-bound** and very **tissue-specific**.

### The two types of eRNA

| **Feature** | **1D-eRNA** | **2D-eRNA** |
|:---|:---|:---|
| Length | Long, from 500 to over 2000 nt | Short, typically \< 150 nt |
| Transcription | Unidirectional | Bidirectional |
| Processing | Spliced and polyadenylated | Not spliced and not polyadenylated |
| Function | In trans (e.g. on another chromosome) | In cis (on the nearby promoter) |

### What eRNAs do, mechanism by mechanism

![[IG-image11.png|548]]

In more detail, **YY1 binds** the enhancer DNA, **drives** the eRNA transcription and also **binds** the nascent eRNA, which increases the YY1 occupancy at the enhancer (**positive feedback loop**). In the **pause release**, Pol II is held near the promoter by **NELF/DSIF**; a stimulus (e.g. neuronal activity or the androgen receptor) induces the eRNA, which binds NELF and acts as a **decoy**, so NELF dissociates and Pol II enters elongation (in prostate cancer, the **KLK3 eRNA** also activates P-TEFb); this is probably a **contributor** rather than the **only determinant**, since the pause release is also needed to produce the eRNAs. eRNAs bind **CBP** and stimulate its acetyltransferase activity (more H3K27ac), and BRD4 binds both acetylated histones and eRNAs through its bromodomains, so the eRNA reinforces the BRD4 retention (e.g. the SNAI1 eRNA); m6A-eRNAs read by **YTHDC2** engage **MLL1**, which increases H3K4me3 and accessibility at super-enhancers in pancreatic cancer (PDAC). In looping, eRNAs bind **cohesin** (RAD21, SMC3), **CTCF** (CCAT1-L at the MYC locus) or **Mediator** (MED1), and the knockdown of the eRNA with **ASOs** loosens the loop and lowers the target transcription. The condensates formed by m6A-eRNAs and YTHDC1 are abolished when m6A is removed with dCas13d–FTO. Finally, the **HOXD eRNA** binds PRC2-covered CpG islands, removes **EZH2** and activates glioma driver genes.

![[IG-image12.png|545]]

We already must figure out why lncRNAs are in the cytoplasm: most of the time, we see them associated with ribosomes. They may control the activity of the ribosomes, or they can be no longer long non-coding RNA, encoding for small proteins.

### Fixes from the paper \[W26\]

- **Size:** 2D-eRNAs are typically **\<150 nt**; 1D-eRNAs are 500 to \>2,000 nt.
- **Mark ratio:** active enhancers have a high **H3K4me1 : H3K4me3 ratio** plus H3K27ac.
- eRNAs are low abundance and unstable (NEXT/exosome decay), nuclear, chromatin-bound, very tissue-specific.
- Their definition overlaps with lncRNA (\>200 nt); the review treats enhancer-derived lncRNAs together with eRNAs.

### How can we prove that eRNAs are important?

- **siRNA:** small RNA that forms a dsRNA targeting RNA, loaded into the **RISC (RNA-induced silencing complex)** ⇒ not so efficient, because siRNAs remain in the cytoplasm whereas eRNAs are mostly nuclear.
- **Cas13**, which, unlike Cas9, targets RNA.

**How Cas13 knocks down an eRNA** (diagram of CRISPR-Cas13):

1.  ![[IG-image13.png|271]]A CRISPR array is transcribed into a pre-crRNA (repeats and spacers).
2.  Cas13 processes it into mature crRNAs, each carrying one spacer.
3.  The Cas13–crRNA complex scans RNA and base-pairs through the spacer with a complementary target RNA.
4.  Target recognition activates the RNase domains, which cut the target. Both cytoplasmic RNA and targeted RNA are cleaved.
5.  For eRNAs, the point is that Cas13d can be given a nuclear localization, so it reaches chromatin-bound transcripts that siRNA/shRNA (RISC, mainly cytoplasmic) miss; the DNA itself is not touched, so the enhancer stays intact (unlike Cas9 deletion). Cas13 can also cut collaterally and off-target, which \[W26\] lists as a limitation.

### Step by step: eRNA biogenesis and fate

- **Initiation.** TFs bind accessible enhancer DNA (sometimes after nucleosome remodelling) and recruit cofactors and Pol II; the cap-binding complex adds the m7G cap at the 5′ end.
- **Chromatin permission.** p300/CBP acetylate histones (H3K27ac); KDM6A/B remove H3K27me2/3; PRC1 can increase accessibility with ERα/BRD4. MLL and HDACs suppress eRNA transcription; enhancer DNA hypomethylation favours it.
- **Elongation.** BRD4 reads acetylated histones and helps Pol II elongate; a signal-dependent checkpoint is released when DNA-PKcs phosphorylates KAP1, freeing P-TEFb (CDK9) from 7SK snRNP.
- **Termination.** The **Integrator** complex (endonuclease INTS11) cleaves the nascent transcript at the 3′ end; WDR82 with CPF also releases eRNA from Pol II. Loss of either causes unprocessed eRNAs.
- **Decay.** The nuclear exosome targeting complex (NEXT) degrades the 3′ end; short 2D-eRNAs lack a poly(A) signal near the TSS, so they are degraded fast.
- **Modification.** m6A is added co-transcriptionally by **METTL3–METTL14–WTAP** (and removed by **ALKBH5**); m5C by PGC-1α/**NSUN7** stabilises eRNAs. p300 acetylates METTL3 to spatially limit m6A deposition.

---
> [[IG 03 - TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter|← TADs as facilitators of enhancer–promoter communication … Step by step – how an enhancer activates a promoter]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 05 - Chromatin and remodelling + Cautions and corrections to keep in mind|Chromatin and remodelling + Cautions and corrections to keep in mind →]]
