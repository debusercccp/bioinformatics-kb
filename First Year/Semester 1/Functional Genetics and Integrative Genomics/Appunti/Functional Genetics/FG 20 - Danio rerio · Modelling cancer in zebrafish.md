---
course: "[[Functional Genetics and Integrative Genomics]]"
module: "[[Functional Genetics]]"
source: "MCB/FGIG/FG/FunctionalGen_RS.docx"
order: 20
tags: [note, fg]
---

> [[FG 19 - Danio rerio · CRISPRCas9 – from gene to disease model|← Danio rerio · CRISPRCas9 – from gene to disease model]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 21 - Danio rerio · Optogenetics|Danio rerio · Optogenetics →]]

# Modelling cancer in zebrafish

| **Positives** | **Negatives** |
|----|----|
| Transparent embryos, rapid development | Few spontaneous tumours |
| Shared vertebrate organs | Short lifespan |
| Complex immune system | Simpler organs |
| Efficient CRISPR and transgenesis | Missing organs (mammary gland, prostate) |
| Transparent adults (casper) for imaging | Smaller genome (~50% of human) |
| Fluorescent reporter lines | Genome duplication |
| Conserved oncogenes (BRAF, NRAS) | Lower temperature (28 °C vs 37 °C) |
| Tumours resemble human ones | Limited antibodies |
| Chemical screens → clinical trials |  |

(White, *Nature Reviews Cancer*.)

### Xenotransplantation: injection sites

| **Site** | **Used for** |
|----|----|
| Blastula | Early embryonic stage; orthotopic tumour models (e.g. glioblastoma), migration and differentiation |
| Brain | Orthotopic brain tumours; invasion, angiogenesis, therapy response |
| Perivitelline space (PVS) | Angiogenesis, intravasation |
| Yolk sac | Survival, proliferation, migration |
| Duct of Cuvier | Circulation, invasion, metastasis |
| Intraperitoneal cavity (adult) | Long-term studies; immunocompromised lines |

![[FG-image64.png|602]]

*Injection sites for zebrafish xenografts.*

**Focus — Why larval xenografts work.** The **adaptive immune system is not functional until about 3–4 weeks** post-fertilisation, so human cells are not rejected and no immunosuppression is needed; a few hundred cells are enough, and the result (growth, invasion, response to a drug) is read within days. Larvae are usually kept at a compromise temperature of about 34–35 °C, between the fish optimum and that of human cells. Adult xenografts need immunodeficient lines.

### 

### Single-cell visualisation of the tumour microenvironment

- Reporter lines label the host: **Tg(fli1:eGFP)** vessels, **Tg(mpx:eGFP)** neutrophils, **Tg(mpeg1:mCherry)** macrophages.

- In **Tg(mpeg1:mCherry; tnfa:eGFP)**, macrophages that are **TNFα⁺** are **anti-tumoral, M1-like**, while **TNFα⁻** ones are **pro-tumoral, M2-like** — the polarisation can be followed in the same larva from day 1 to day 4 (Martínez-López et al., 2025; Póvoa et al., 2021).

**Key antibodies for immunofluorescence on xenografts** (Mendes et al., 2025):

- **Caspase-3** → **apoptosis**; used to assess therapy-induced cell death;

- **Ki-67** → **proliferation**; a **human-specific** antibody avoids cross-reaction with the zebrafish host;

- **Phospho-histone H3** → **mitotic activity**.

**Example: HP-NAP and melanoma** (Facchinello et al., 2022). The ***Helicobacter pylori* neutrophil-activating protein (HP-NAP)** reduces the growth of melanoma xenografts, and **macrophages are essential for its anti-tumour activity** (followed in *mpeg1:EGFP* larvae, 4 dpi).

**Future perspectives:** automated imaging and AI-based analysis; automated microinjection for xenograft models (Ding et al., 2025); high-throughput drug screening; CRISPR/Cas9 for novel targets and cancer models; humanised zebrafish models; **personalised medicine** (patient-derived xenografts to choose a treatment, at reduced cost); integration with omics and single-cell technologies.

### Take-home messages

| **1. Genetic engineering** | **2. Fluorescent reporters** | **3. Disease models & controls** |
|----|----|----|
| What we modify | What we observe | What we conclude |
| CRISPR/Cas9, mutant lines | Cell types, dynamic processes | Phenotypes, mechanisms |

**Precise perturbation + live imaging + rigorous controls = mechanistic insight.**

---
> [[FG 19 - Danio rerio · CRISPRCas9 – from gene to disease model|← Danio rerio · CRISPRCas9 – from gene to disease model]] · [[Functional Genetics|↑ Functional Genetics]] · [[FG 21 - Danio rerio · Optogenetics|Danio rerio · Optogenetics →]]
