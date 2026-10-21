---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 5
tags: [note, fg]
---

> [[FG 04 - Effects of mutations on gene function – Müller's classification|← Effects of mutations on gene function – Müller's classification]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 06 - What is a model organism|What is a model organism →]]

# Where do we measure gene function?

### The core question

**The experimental system we choose decides which phenotypes can exist at all**. Choosing a system fixes the set of possible answers. The slides give two examples:

- In a **monolayer** culture there can be no neuronal migration, because there is nothing to migrate through (no three-dimensional tissue, no matrix, no other cells).

- A **40% change in enzyme kinetics** can be perfectly visible in a lysate, but in a whole animal it can be "buffered away" by compensatory mechanisms (alternative metabolic routes, homeostatic regulation) and produce no observable phenotype.

So no system is "the right one" in absolute terms: each is suited to some questions and blind to others. The lecture moves from the simplest and most controllable system (in silico) to the whole organism.

### The fundamental trade-off: control vs physiological relevance

**2D cell culture** is the most controllable and reproducible but the least physiological; **3D cultures** and **organoids** are intermediate; **microfluidic organ-on-a-chip devices** add flow and tissue–tissue interaction; **animal models** are the most physiologically relevant but the least controllable and reproducible. The more realism you gain, the more control you lose: it is the same trade-off we will meet again when choosing a model organism.

The sequence of systems is: **in silico → 2D → 3D → organoids → organ-on-chip → whole organism**.

### 2D and 3D cultures

Cells in a dish (2D) grow attached to a rigid plastic surface.

**2D culture**

- Soluble factors diffuse uniformly into the medium: **no gradient forms**.

- Cell organisation and polarity are "forced" by the flat support.

- Cells are exposed directly to the liquid interface.

- The high **stiffness** of the support makes cells spread out in a monolayer.

- Cell–cell interactions are restricted.

**3D culture**

- **Concentrated gradients** of soluble factors (oxygen, nutrients, morphogens) form, as in real tissues.

- Cells adhere to the **extracellular matrix (ECM)** through **integrin–matrix binding**.

- Cells are **embedded** in the matrix.

- **Cell–cell interactions** increase.

- Matrix fibrils limit cell spreading, so cells take a morphology closer to the one found in vivo.

*Further detail:* differences in morphology, signalling (integrins, mechanotransduction), gene expression and drug response between 2D and 3D are the reason a gene can look essential in 2D and not in 3D, or vice versa. A large 3D mass also has a hypoxic, nutrient-poor core, which 2D does not reproduce.

### 3D technology is evolving fast: how a 3D culture is made

There is also so-called **2.5D** culture, an intermediate (cells on a layer of matrix, or in medium containing matrix, but still essentially flat).

1.  **Anchorage independent (scaffold-free)**: cells aggregate with each other to form **spheroids and microtissues**. Three methods:

    - *hanging drop*: cells collect in a suspended drop;

    - *low attachment plate*: plates whose surface prevents adhesion, so cells aggregate;

    - *magnetic levitation*: cells made magnetic are lifted and aggregated with a magnet.

2.  **Anchorage dependent (scaffold-based)**: cells are embedded in a **hydrogel**.

    - *Biological hydrogels*: animal-derived (**collagen, Matrigel, gelatin**) or plant-derived (**alginate**).

    - *Synthetic hydrogels*: non-natural (**PEG** polyethylene glycol, **PLA** polylactic acid, **PGA** polyglycolic acid) or natural (**hyaluronic acid, peptides**).

3.  **Specialised 3D platforms**: **microfluidic devices** and **micropatterned plates**, up to **3D bioprinted** tissues (3D printing of cells and biomaterials).

*Further detail:* synthetic materials have the advantage of being defined and reproducible (tunable stiffness), whereas biological ones such as Matrigel (extracted from a murine tumour) are more "bioactive" but vary from batch to batch.

### Organoids and organ-on-chip

- **Organoids** are three-dimensional structures derived from stem cells that self-organise and partly reproduce the architecture and functions of an organ.

- **Organ-on-chip (OoC)** devices are **microfluidic**: small channels in which cells of a tissue grow, crossed by a flow of medium that simulates perfusion and mechanical stress. Several chips can be coupled:

  - **coupled single OoC chips**, linked by capillary connections;

  - a **multi-OoC plate**;

  - up to the concept of **Human-on-a-Chip**, in which brain, lung, heart, liver, gut, kidney and bone are connected by a circuit that mimics circulation.

- The **readouts** of an OoC are of two kinds. *Online/integrated*: integrated sensors (**TEER**, transepithelial electrical resistance, to assess barrier integrity; **MEA**, microelectrode arrays; cantilevers), online measurement of soluble analytes, and **live-cell imaging**. *Offline/endpoint*: analysis of soluble analytes by **LC/MS** or commercial kits, immunofluorescence, and, after lysis, extraction of nucleic acids and proteins for **Western blot, RT-PCR, NGS**.

### Stem cells and reprogramming: iPSCs

Building organoids and tissues requires stem cells. The transcription factors active during development (the example from the literature is the dorsal and ventral pancreatic bud, liver, stomach, intestine, common bile duct) can drive cells toward a specific fate.

The breakthrough is the **reprogramming of somatic cells into induced pluripotent stem cells (iPSCs)**:

- **Takahashi and Yamanaka (Cell, 2006)** showed that from mouse fibroblasts one can obtain cells with a gene expression profile and developmental potential similar to those of embryonic stem cells (ESCs), using only **four transcription factors: OCT3/4, SOX2, KLF4 and MYC (OSKM)**.

- The same factors are enough to generate **human iPSCs**.

- The factors can be introduced with **retroviral vectors** (or mRNA, proteins, plasmids).

**Type of intervention:** **transduction of somatic cells with retroviral vectors** carrying OSKM, i.e. **gene addition in cultured cells** (the vectors integrate into the genome). With mRNA, proteins or non-integrating plasmids, reprogramming is obtained **without permanent genetic modification**.

- iPSCs show the morphology, markers, and **DNA and histone methylation** typical of ESCs.

- Applications: **drug screening, disease modelling, regenerative medicine**.

In 2012 the **Nobel Prize in Physiology or Medicine** went to **John B. Gurdon** (nuclear transfer, experiments in amphibians) and **Shinya Yamanaka**. The conceptual meaning is **nuclear equivalence**: *all the genes in the genome are retained in every specialised cell type, even if silent and not used by that cell*. Specialisation is therefore epigenetic and regulatory, not a loss of DNA.

Here is a possible application of iPSCs to treat diabetes:

![[FG-image10.png|464]]

### How many organs does a human have? The limit of in vitro models

Anatomists estimate **70–80 organs**, grouped into about **ten systems**. The digestive system alone includes more than 12 organs (mouth with teeth and tongue, salivary glands, pharynx, oesophagus, stomach, segments of the small intestine, large intestine, liver, gallbladder, mesentery, pancreas, anal canal with anus). The point is that an organism is very complex and made of organs that talk to each other.

This leads to the question: **can computer models and cell cultures (3D cultures and organoids) replace animal research?** The answer is no, at least for now:

- such models cannot replicate the **complicated interactions** of the whole system: the nervous system, blood and brain chemistry, gland secretions and immune responses are **interrelated**, so it is impossible to explain or predict the course of a disease or the effect of a treatment without observing the whole organism;

- **final testing** depends on animal studies and in some cases is **required by law**;

- the best answer comes from using **animal and non-animal models together**.

---
> [[FG 04 - Effects of mutations on gene function – Müller's classification|← Effects of mutations on gene function – Müller's classification]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 06 - What is a model organism|What is a model organism →]]
