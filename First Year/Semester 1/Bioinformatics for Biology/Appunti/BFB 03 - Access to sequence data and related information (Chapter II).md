---
course: "[[Bioinformatics for Biology]]"
module: "[[Bioinformatics for Biology]]"
source: "MCB/BFB/Bioinformatics_For_Biology.docx"
order: 3
tags: [note, bfb]
---

> [[BFB 02 - The practical hardware needs of biology (Chapter I)|← The practical hardware needs of biology (Chapter I)]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]] · [[BFB 04 - Pairwise sequence alignment (Chapter III)|Pairwise sequence alignment (Chapter III) →]]

# Access to sequence data and related information (Chapter II)

## 3.1 A global and redundant technostructure

Sequence databases are organised as an international, deliberately redundant infrastructure: the **International Nucleotide Sequence Database Collaboration (INSDC)**, formed by three partners that mirror each other’s content.

| Institution | Location | Main resources |
|:---|:---|:---|
| **NCBI** — National Center for Biotechnology Information | Bethesda, Maryland, USA | PubMed (publications), Entrez (Gene, Nucleotide, Protein), SRA (bulk NGS data), GEO (processed data), Taxonomy Browser, Books |
| **EBI** — European Bioinformatics Institute (part of EMBL, European Molecular Biology Laboratory) | Hinxton, UK (EBI) and Heidelberg, Germany (EMBL) | Ensembl (genes and genomes), ENA (European Nucleotide Archive, bulk data), EGA (European Genome-Phenome Archive), BioMart (sequence ID conversion) |
| **DDBJ** — DNA Database of Japan | Mishima, Shizuoka, Japan | Japanese node of the collaboration |

Redundancy here is a feature, not a defect: each node holds a copy of the nucleotide records submitted to any of the three, which guarantees persistence and geographic availability.

## 3.2 The NCBI sequence database: nr and RefSeq

The NCBI sequence database, formerly known as **Entrez**, is organised in two main collections that differ in *how* the sequences got in. This distinction is the central concept of the chapter.

|  | **nr** | **RefSeq** |
|:---|:---|:---|
| Name | non-redundant sequences | reference sequences |
| Content criterion | Anything submitted by recognised institutions | Manually curated records |
| Proteins | ~1,100,000,000 | 495,290,394 |
| Nucleotides | ~130,000,000 | 86,067,871 |
| Organisms | ~580,000 | 184,752 |

### 3.2.1 nr — non-redundant sequences

- **What it is**: the archival, submission-driven collection. Any sequence submitted by a recognised institution ends up here, with no curation of its biological content.
- **Why “non-redundant”**: identical sequences submitted multiple times are collapsed into a single entry (so the *sequence* is not duplicated), but this is a technical de-duplication only. It does **not** mean that one gene has one record: the same gene can be represented by many different, partially overlapping, differently annotated submissions.
- **Consequences**: nr is much larger than RefSeq (an order of magnitude more proteins), it is far more heterogeneous in quality, and it includes record types that are intrinsically fragmentary, such as **ESTs** (Expressed Sequence Tags — snapshots of many short, \< 1000 nt, mRNA/cDNA sequences).
- **Who submits**: individual labs, sequencing projects, and third-party databases whose identifiers appear inside nr (e.g. SwissProt IDs such as `O14896`).
- **When to use it**: whenever you want maximum sensitivity and coverage — all the evidence available, including poorly annotated organisms, partial sequences and sequences from under-studied species. It is the default target database for a BLAST search (“search the appropriate non-redundant BLAST database”).

### 3.2.2 RefSeq — reference sequences

- **What it is**: an expertly curated collection that provides, for a given gene/transcript/protein/genome, *the* stable, agreed-upon “reference” version of the sequence, with its own accession number.
- **Curation**: records are manually reviewed, which is why RefSeq contains roughly a third fewer organisms than nr and far fewer records: curation does not scale the way submission does.
- **Properties that matter in practice**: one reference record per biological entity (non-redundant in the *biological* sense, not merely at the level of identical strings); consistent annotation across species; stable identifiers that can be cited in a paper and resolved years later; explicit links between the nucleotide record and the protein it encodes (`NM_` ↔ `NP_`).
- **When to use it**: whenever you need a defined, citable, unambiguous sequence — designing primers, choosing a canonical transcript, comparing orthologues across species, reporting a variant’s coordinates, building a reproducible pipeline.

### 3.2.3 RefSeq accession number formats

RefSeq identifiers encode the *type* of molecule in the two-letter prefix, which makes them self-documenting:

| Prefix | Content | Example |
|:---|:---|:---|
| `NC_######` | Complete genome / chromosome | `NC_045512.2` (SARS-CoV-2 genome), `NC_000001.10` (human chromosome 1) |
| `NT_######` | Genomic contig |  |
| `NM_######` | Protein-coding nucleotide (mRNA / transcript) | `NM_006744.2`, `NM_001206696` |
| `NR_######` | Non-coding nucleotide |  |
| `NP_######` | Protein associated to an `NM_` record | `NP_006735`, `NP_000509.1` (human beta globin) |
| `YP_######` | Protein **not** associated to an `NM_` record | `YP_009724390.1` (SARS-CoV-2 spike glycoprotein) |
| `XM_######` | Predicted nucleotide (computationally derived) |  |
| `XP_######` | Predicted protein (computationally derived) |  |

Two rules to retain:

- `N` as first letter = the record is supported by curated evidence; `X` = the record is a prediction, usually produced by an automated annotation pipeline.
- The suffix after the dot is the **sequence version** (`NC_045512.2` is the second version of that record). The accession stays stable while the version increments whenever the sequence itself is corrected or updated, so citing accession *plus* version is what makes an analysis reproducible.

### 3.2.4 Reading an accession number: nr vs RefSeq vs other databases

| Accession      | Collection | Type                               |
|:---------------|:-----------|:-----------------------------------|
| `NC_000001.10` | RefSeq     | Chromosome                         |
| `NM_001206696` | RefSeq     | Transcript sequence                |
| `NP_006138.1`  | RefSeq     | Protein                            |
| `CH471100.2`   | nr         | DNA sequence                       |
| `AI687828.1`   | nr         | Expressed sequence tag (EST)       |
| `CAA18545.1`   | nr         | Protein                            |
| `O14896`       | nr         | Protein, SwissProt identifier      |
| `1KT7`         | PDB        | Protein Data Bank structure record |

The practical heuristic: a two-letter prefix followed by an underscore (`NC_`, `NM_`, `NP_`, `XM_`…) means RefSeq; anything else — letter-digit combinations without the underscore — comes from the archival submission flow (nr) or from a specialised external database (PDB, SwissProt).

## 3.3 Hands-on: querying the NCBI databases

Entry point: `https://www.ncbi.nlm.nih.gov/`. Searching the accession number `NC_045512.2` returns the SARS-CoV-2 reference genome, whose record page carries date, authors, length, protein locations and translations.

Out-of-the-box analyses available directly from a nucleotide record page:

- **Run BLAST** — search for similar sequences.
- **Pick Primers** — design primers for PCR or RT-PCR.
- **Highlight Sequence Features** — coding sequences (CDS), genes, and other annotations.
- **Find in this Sequence** — search for a pattern, e.g. `ATGTTTGTT` (the spike’s starting codons).

### 3.3.1 Limiters and Boolean logic

NCBI Gene (formerly Entrez Gene) is a sub-database reached at `/gene`. A bare keyword search is almost always too broad: searching `Sars-cov-2` also returns records that merely resemble the virus, e.g. the human ACE2 receptor.

Queries are refined with **\[limiters\]** (Organism, Author, Gene Name, Chromosome, Molecular weight, Sequence Length, Title, …) and with **Boolean operators**:

- `"Sars-cov-2"[Organism]` → the genes of that virus only (11 genes plus a placeholder entry).
- `"Sars-cov-2"[Organism] AND S[Gene Name]` → the spike gene alone.
- `Sars-cov-2[Organism] AND membrane` → the 5 genes coding for viral membrane proteins (Membrane, Spike, Envelope, Nucleocapsid, ORF1ab).

Effect of the operators, with platypus as the example: `Platypus AND membrane` → ~5,000 hits; `Platypus NOT membrane` → ~26,000; `Platypus OR membrane` → over 8 million. Limiters narrow further: `Platypus` → 31,446 hits, `Platypus[Organism]` → 31,254, `Platypus NOT Platypus[Organism]` → 192 (records that mention platypus without being platypus records). Combined: `Platypus[Organism] AND 1[Chromosome]` → ~2,500.

Rules for building queries:

- `AND`, `OR`, `NOT` **must be capitalised**.
- Quotation marks search an exact phrase.
- Boolean operators are processed left to right; parentheses group terms so they are processed as a unit. `globin AND promoter OR enhancer` → ~31,000 results, while `globin AND (promoter OR enhancer)` → just 66.
- An asterisk truncates a query: `globin` → 6,777 results in NCBI Nucleotide, `glob*` → 490,358 (including *Chaetomium globosum* and the word “global”).
- Numeric ranges work inside limiters: `500000:999999[Molecular weight]`, `010000:050000[MOLWT] AND "pevsner j"[Author]`, `30000:50000[Sequence Length]`.
- Organisms can be specified by name or taxonomy ID, equivalently: `Human[Organism]`, `"Homo sapiens"[Organism]`, `txid9606[Organism]`.
- The **query builder** at `/gene/advanced` composes complex expressions, e.g. `((Platypus[Organism]) AND Enzyme[Title]) NOT 5[Chromosome]`.

### 3.3.2 Exercises from the book (Ch. 2)

- Find chicken ACE2 in NCBI Protein using a filter on the organism, then restrict by molecular weight (`2000:10000[molwt]`) or by sequence length (`30000:50000[Sequence Length]`).
- Titin (`NP_596869.4`) is the longest human protein, 34,423 amino acids, against an average of ~500.
- Human beta hemoglobin protein is `NP_000509`. To find the chimpanzee orthologue, either query `chimpanzee[Organism] AND hemoglobin[Title]`, or BLAST the chimpanzee proteome using the human protein ID as query — a good illustration that database querying and sequence similarity search are two complementary routes to the same answer.

## Collegamenti
- [[SATAUMV 09 - Technologies for genomic data generation and data formats]] — FASTQ/SAM/VCF e tecnologie di sequenziamento

---
> [[BFB 02 - The practical hardware needs of biology (Chapter I)|← The practical hardware needs of biology (Chapter I)]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]] · [[BFB 04 - Pairwise sequence alignment (Chapter III)|Pairwise sequence alignment (Chapter III) →]]
