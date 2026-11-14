---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_common.docx"
order: 21
tags: [note, fg]
---

> [[FG 20 - Danio rerio · Modeling cancer in zebrafish|← Danio rerio · Modeling cancer in zebrafish]] · [[Functional Genetics|↑ Functional Genetics]]

# Optogenetics

*Turning a gene into a switch for living cells* — from the eyespot of a green alga to the 2026 Nobel Prize.

### Why this lecture, this year (2026)

- The **2026 Nobel Prize in Physiology or Medicine** was awarded jointly to **Karl Deisseroth** (HHMI/Stanford), **Peter Hegemann** (Humboldt University, Berlin) and **Georg Nagel** (University of Würzburg).

- Citation: *“for their discoveries concerning light-gated ion channels and optogenetics”*, announced on 5 October 2026 at the Karolinska Institutet.

- **Hegemann and Nagel** discovered and characterized **channelrhodopsin** in a single-celled alga; **Deisseroth** turned it into a **light-controlled switch for nerve cells**.

### ![[FG-image64.png|292]]The logic: functional genetics needs to READ and to WRITE

- Genomics delivers **candidates** (a variant, a gene, a cell type): that is a **correlation**.

- A **causal** claim needs **perturbation** — loss and gain of function — **at the timescale on which the phenotype actually happens**.

- Two complementary classes of genetically encoded tools: **READ = indicators** (GCaMP for Ca²⁺, neurotransmitter sensors, voltage sensors — a fluorescent protein reports a cellular variable); **WRITE = actuators** (channelrhodopsins and pumps — light imposes a change on the cell).

- Both are **single transgenes**, and both inherit the **specificity of the regulatory elements** placed in front of them. **This is why optogenetics belongs in a genetics course.**

### Four ways to perturb, and the resolution each one buys

| **Approach** | **What is changed** | **Onset** | **Reversible** | **Precision** |
|----|----|----|----|----|
| CRISPR knock-out / knock-in | The gene product itself | Days – generations | No | Organism; tissue with conditional alleles |
| RNAi / morpholino knockdown | Transcript level (partial) | Hours – days | Transient | Tissue, dose-dependent |
| Chemogenetics (DREADD + ligand) | Excitability, via a designer GPCR | Minutes | Yes (hours) | Genetically defined population |
| Optogenetics (opsin + light) | Membrane potential, directly | Milliseconds | Yes (ms) | Genetically defined population, down to single cells |

The gain in **temporal and cellular precision** is the whole point — paid for with a **harder expression-targeting problem** and a **new set of artefacts**.

### Origin: a green alga that swims towards light

- ***Chlamydomonas reinhardtii***, a unicellular alga, steers by light with an **“eyespot”**: phototactic and photophobic responses within **milliseconds**.

- **Harz & Hegemann (Nature, 1991)** recorded **light-regulated ion currents** directly at the eyespot membrane — far too fast for a classical second-messenger cascade.

- **Inference**: in this organism, **light absorption and ion conduction might be carried out by the same protein**. Animal rhodopsins never work that way.

### The molecule: channelrhodopsin — one gene, one protein, one function

- ![[FG-image65.png|333]]**Seven-transmembrane** protein with **retinal** covalently bound as its chromophore. **Photon → retinal isomerization → conformational change → a pore opens.**

- Ions then move **passively**, down their electrochemical gradient — **no ATP, no G protein, no accessory subunit**.

- Vertebrate tissue already contains **enough retinal** (a vitamin A derivative), so no cofactor has to be supplied.

- Consequence: **transferring a single cDNA is sufficient to make any excitable cell light-controllable**.

> **Focus — Type I vs type II rhodopsins. Type II (animal) = GPCR cascades; type I (microbial) = light-driven pumps/channels, usable as single-gene tools.**

### 2005: putting the gene into a neuron

- ![[FG-image66.png|348]]**Boyden, Zhang, Bamberg, Nagel & Deisseroth** delivered **ChR2–YFP** to cultured hippocampal neurons with a **lentiviral vector**.

- **Blue light pulses** evoked action potentials with **millisecond precision** — **one flash, one spike** — with no chemical added.

- Within about two years the same gene was working in ***C. elegans*, *Drosophila*, mouse and zebrafish**, and in vivo through implanted optical fibers.

- Because expression is **genetically targeted**, light acts **only on the cells that transcribe the construct**, even when they are intermingled with cells that do not.

### ![[FG-image67.png|214]]The toolbox: drive or silence

- **Depolarize** — **cation channels** (ChR2 and relatives): Na⁺ and H⁺ flow in, the cell fires.

- **Hyperpolarize** — three physical mechanisms: **inward Cl⁻ pumps** (**NpHR**, halorhodopsin from *Natronomonas pharaonis*); **outward H⁺ pumps** (**Arch**, archaerhodopsin-3); **anion channels** (**GtACR1/2** from *Guillardia theta*) — large currents, efficient silencing.

- **Interpret with care**: silencing a projection is **not equivalent to deleting a gene**, and in **axon terminals** a chloride conductance can be **depolarizing** rather than inhibitory.

**Choosing an actuator** — pick by **which ion moves**, **on/off kinetics**, **single-channel conductance** and **peak wavelength**:

| **Actuator** | **Peak (~nm)** | **Type / note** |
|----|----|----|
| ChR2 (H134R) | 470 | Cation channel, Na⁺/H⁺ influx — activates |
| Chronos | 500 | Fast kinetics — activates |
| ChRmine | 520 | Large photocurrent, red-shifted — activates |
| Chrimson / ChrimsonR | 590 | Red-shifted — activates |
| GtACR2 | 470 | Anion channel — silences |
| GtACR1 | 515 | Anion channel — silences |
| Arch (Arch-3) | 566 | Outward H⁺ pump — silences |
| NpHR (eNpHR3.0) | 589 | Inward Cl⁻ pump — silences |
| Jaws | 632 | Cl⁻ pump, deep tissue — silences |

**Red-shifted** tools penetrate tissue better and can be separated spectrally from green indicators. **Two well-separated colors = independent control of two populations in the same animal.**

### Worked example: read and write in the same zebrafish larva

- **Tg(elavl3:nlsGCaMP6s)** — a pan-neuronal nuclear calcium indicator: the **READ** channel.

- **Gal4s1171t; UAS:ChR2–mCherry** — a restricted neuronal population carrying the actuator: the **WRITE** channel.

- **Cross the two lines**, and a single larva lets you **image the whole brain while stimulating a genetically defined subset**. mCherry marks the ChR2-expressing cells; the traces show which identified neurons respond to each stimulation pulse.

- Practical obstacle: **spectral crosstalk** — the blue light that excites GCaMP also opens ChR2. Solutions: **red-shifted actuators** or **two-photon excitation** (e.g. Dal Maschio et al., 2017, two-photon holographic optogenetics).

**Read and write in the same animal: a two-transgene cross**

![[FG-image68.png|374]]• Tg(elavl3:nlsGCaMP6s) —a pan-neuronal nuclear calcium indicator: the READ channel.

• Gal4ˢ¹¹⁷¹ᵗ; UAS:ChR2–mCherry —a restricted neuronal population carrying the actuator: the WRITE channel.

• Cross the two lines and a single larva lets you image the whole brain while stimulating a genetically defined subset.

• In the image: mCherry marks the ChR2-expressing cells; the traces show which identified neurons respond to each stimulation pulse (orange lines).

• The practical obstacle is spectral crosstalk —the blue light that excites GCaMP also opens ChR2. Solutions: red-shifted actuators, or two-photon excitation.

> **Focus — Why the zebrafish larva is ideal for this. Transparent, with a small brain imaged whole, and compatible with hundreds of Gal4 lines.**
>
> **From the bench to the clinic.** Sahel et al. (*Nat. Med.*, 2021) reported **partial recovery of visual function** in a blind patient with retinitis pigmentosa after gene therapy with the red-shifted channelrhodopsin **ChrimsonR** into retinal ganglion cells, combined with light-stimulating goggles — the first clinical use of optogenetics.

### Take-home messages

- **Optogenetics is a genetics method.** The optics is the easy half; the hard half is expressing **the right actuator in the right cells at the right level**.

- A **single microbial gene** is enough because a **type I rhodopsin is both the photoreceptor and the ion channel**, and vertebrates already supply retinal.

- The 2026 Nobel Prize rewards a chain that began with **how a green alga swims towards light** — a reminder of the value of basic, curiosity-driven research.

- **Indicators (read) + actuators (write)** convert a correlational activity map into a **causal, quantitative circuit model**.

- Interpretation stands or falls on **controls**: **opsin-negative animals**, **verified expression**, **calibrated light**, and the distinction between **sufficiency and necessity**.

---
> [[FG 20 - Danio rerio · Modeling cancer in zebrafish|← Danio rerio · Modeling cancer in zebrafish]] · [[Functional Genetics|↑ Functional Genetics]]
