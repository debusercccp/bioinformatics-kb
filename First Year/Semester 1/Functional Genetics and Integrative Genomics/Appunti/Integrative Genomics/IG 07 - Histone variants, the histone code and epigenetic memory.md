---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Integrative Genomics]]"
source: "MCB/Functional_Genetics/IntegrativeGen_RS.docx"
order: 7
tags: [note, ig]
---

> [[IG 06 - Histone acetylation and methylation|← Histone acetylation and methylation]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 08 - DNA methylation + Methods – from one locus to the whole epigenome|DNA methylation + Methods – from one locus to the whole epigenome →]]

# Histone variants, the histone code and epigenetic memory

### Histone variants

Canonical histones are replication-dependent; variants are deposited by specific chaperones and change the properties of the nucleosome.

- **H2A:** **H2A.X** (accumulates at DNA damage, recruits repair proteins after phosphorylation = γH2A.X); **H2A.Z** (transcription initiation, heterochromatin organisation, genome stability); **macroH2A** (vertebrates; silenced regions, blocks recruitment of transcription machinery and remodellers, **related to X chromosome**); **H2A.J** (senescent cells, inflammatory genes); **H2A.Bbd** (testis, brain; less compaction); **H2A.L.2** (histone-to-protamine transition); **TH2A/TH2B** (gametes; help reprogramming to pluripotency).
- **H3:** **H3.3** (replication-independent; deposited where nucleosomes are lost by transcription: active genes, promoters, but also telomeres, imprinted genes, heterochromatin); **H3T/H3.4** (testis, entry into meiosis); **CENP-A/CenH3** (marks the **centromere**, needed for the kinetochore); **H3.X/H3.Y** (primate-specific, active TSSs).
- **H4:** H4.7/H4.G (nucleolus, less compact rDNA chromatin). **H1:** H1.0 (terminally differentiated cells), H1.1–H1.5 (replication-dependent, peak in S phase), H1.6/H1.7/H1.9 (testis), **H1.8 = H1oo** (oocytes), H1.10 (nucleolus).
- Beyond Ac/Me/P/Ub, tails also carry SUMOylation, citrullination, ADP-ribosylation, biotinylation, proline isomerisation and acylations linked to metabolism (propionylation, butyrylation, crotonylation, **lactylation**).

### Seeing modifications in the cell

- **ChIP:** formaldehyde crosslink → lysis and sonication → antibody on protein A/G beads → wash → reverse crosslink, digest proteins → purify DNA → qPCR at one locus or sequencing genome-wide (section 15).

> ![[IG-image23.png|539]]

- **Co-immunolocalisation:** double immunofluorescence with DAPI. H3K4me3 overlaps with H3K9ac and RNA Pol II (active, euchromatic); H4K20me3 overlaps with H3K9me3 in DAPI-dense heterochromatic foci; H3K4me3 and H3K9me3 do not overlap.

> **Sonication** = high-frequency ultrasound (~20 kHz) delivered by a probe or water-bath sonicator (e.g. Bioruptor, Covaris); the sound waves create **cavitation bubbles** in the liquid that collapse and generate shear forces, **breaking chromatin into random fragments**. Fragment size is tuned by power, number of cycles and duration; samples are kept cold (on/off pulses on ice) because heat can reverse crosslinks and damage epitopes. Unlike MNase, which cuts preferentially in linker DNA, sonication shears largely sequence-independently, but open chromatin breaks more easily than compact heterochromatin.

### Trithorax vs Polycomb and bivalent promoters

- **Trithorax group (TrxG):** MLL with WDR5, ASH2L, RBBP5 writes **H3K4me3**; UTX removes H3K27me3 → gene **ON**.
- **Polycomb group (PcG):** **PRC2** (EZH2, EED, SUZ12, JARID2) writes **H3K27me3**, together with HDACs → gene **OFF**.
- **ESC → neural progenitor (NPC) → neuron:** developmental genes are **bivalent** in ESCs (H3K4me3 + H3K27me3 = OFF but poised). Pluripotency genes: ON in ESCs, then OFF with DNA methylation. Proneural genes: bivalent → ON in NPCs (H3K4me3 only) → OFF in neurons. Neuronal genes: bivalent in ESCs and NPCs → ON in neurons. Other-lineage genes: lose H3K4me3, keep H3K27me3 and/or gain DNA methylation → permanently OFF. Link to the poised state in section 2.

### The histone code hypothesis

Combinations of tail modifications, read by specific modules, specify distinct downstream events (Strahl & Allis; Jenuwein & Allis).

- Unmodified H3 → Sir3/Sir4/Tup1 → silencing. Acetylated H3 → bromodomain → transcription.
- H3 S10/S28 phosphorylation → condensins? → mitosis/meiosis. S10ph + K14ac → transcription. H3 methylation → transcription or silencing depending on the site.
- H4 K8/K16 acetylation → transcription; H4 K5/K12 acetylation (on new histones) → histone deposition. CENP-A phosphorylation → mitosis.
- **The “sun” picture:** the histone-code diagram puts the nucleosome at the centre with the histone tails radiating out like rays, each labelled with its modified residues and the enzymes that write them.
- **Still a lot to do:** most histone modifications have an unknown function, and the same enzymes also modify TFs and cofactors, so the code is far from being deciphered.
- **Code at work in the fly eye:** in PEV (section 12) the red/variegated eye comes from an inversion that takes white away from its normal control region and places it next to heterochromatin; SUV39 (H3K9 methyltransferase) and HP1 set how far heterochromatin spreads.
- **H3K27me3:** the Polycomb repression mark; PRC2 both writes it (EZH2) and reads it (EED), and this interaction maintains repression (below).

![[IG-image24.png|310]]**Slide: bivalent promoters resolve during neural differentiation.** The slide follows five classes of genes from embryonic stem cells (ESC) to neural progenitors (NPC) to neurons. Green lollipop = H3K4me3 (Trithorax, active), red triangle = H3K27me3 (Polycomb, repressive), pink star = DNA methylation (stable silencing). The point: in ESCs, developmental genes are bivalent (both marks, OFF but poised), and each differentiation step resolves bivalency in one of two directions.

- **Pluripotency genes (e.g. Oct4, Nanog):** ON in ESCs with H3K4me3 only. In NPCs they lose H3K4me3 and gain DNA methylation → OFF, and stay methylated and OFF in neurons. They are silenced permanently by DNA methylation, not by Polycomb.
- **Proneural genes:** bivalent and OFF in ESCs. In NPCs H3K27me3 is removed (K27 demethylases) and only H3K4me3 remains → ON. In neurons they are switched off again and DNA-methylated, because they are needed only at the progenitor stage.
- **Neuronal genes:** bivalent and OFF in ESCs and still bivalent (poised) in NPCs. Only in neurons is H3K27me3 removed → H3K4me3 alone → ON. Bivalency keeps them ready but silent until the right stage.
- **Other lineage genes A:** bivalent in ESCs and NPCs (OFF). In neurons they lose H3K4me3, keep H3K27me3 and gain DNA methylation → stably OFF.
- **Other lineage genes B:** bivalent in ESCs, but they lose H3K4me3 already in NPCs and become H3K27me3 + DNA methylation → OFF in NPCs and neurons. Genes of alternative fates are shut down earlier.
- **Take-home:** bivalent = OFF but poised. Loss of H3K27me3 → activation (Trithorax wins); loss of H3K4me3 → H3K27me3 alone, often followed by DNA methylation → long-term silencing (Polycomb wins). DNA methylation is the final lock (section 14), so the switch from Polycomb to DNA methylation turns flexible repression into stable silencing.

### Epigenetic memory through replication

- At the fork, parental modified nucleosomes are split between the two daughter strands and new, unmodified histones fill the gaps, so each daughter inherits ~half of the mark.
- **Read–write loop:** PRC2 reads H3K27me3 through **EED**, which allosterically stimulates **EZH2** to methylate neighboring nucleosomes; the mark is restored and spreads. Two models: the complex leaves the DNA at the fork and rebinds marked nucleosomes, or it is retained and transferred to the daughter strands.
- **Oncohistone H3.3 K27M** (pediatric diffuse midline glioma): the mutant tail binds and inhibits EZH2; PRC2 cannot spread, H3K27me3 is lost globally and silenced genes are activated.

---
> [[IG 06 - Histone acetylation and methylation|← Histone acetylation and methylation]] · [[Integrative Genomics|↑ Integrative Genomics]] · [[IG 08 - DNA methylation + Methods – from one locus to the whole epigenome|DNA methylation + Methods – from one locus to the whole epigenome →]]
