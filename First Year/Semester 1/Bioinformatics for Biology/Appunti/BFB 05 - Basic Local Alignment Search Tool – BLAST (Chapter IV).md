---
course: "[[Bioinformatics for Biology]]"
module: "[[Bioinformatics for Biology]]"
source: "MCB/BFB/Bioinformatics_For_Biology.docx"
order: 5
tags: [note, bfb]
---

> [[BFB 04 - Pairwise sequence alignment (Chapter III)|← Pairwise sequence alignment (Chapter III)]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]]

# Basic Local Alignment Search Tool — BLAST (Chapter IV)

## 5.1 What BLAST is

BLAST allows rapid comparison of a query sequence against another sequence or against an entire database — the case where Smith–Waterman is far too slow. Features:

- Fast, accurate, accessible (web and Linux command line).
- **Heuristic**: it uses shortcuts to reach a solution, and is therefore *not* guaranteed to find the best solution, unlike Smith–Waterman. In practice it almost always does.
- An alternative fast heuristic is the FASTA algorithm.
- It became the most optimised tool in existence largely because it is backed by NCBI.

## 5.2 The heuristics

- The sequences are split into short **words**.
- BLAST finds matches between the words of the query (computed on the fly) and the words of the database — which, being gigantic, has its words precomputed and indexed.
- When a match is found, BLAST tries to **extend** it in both directions.
- The original BLAST did not allow gaps; current versions do.

## 5.3 The Expect value (E)

The Expect value describes the **number of hits one can expect to see by chance** when searching a database of a particular size. The lower the E value, the more significant the alignment.

- Higher matching scores yield lower E values.
- **Larger databases yield higher E values**: the same alignment with the same score has E = 6e-7 against a small database and E = 9e-5 against a large one. Significance is therefore a property of the alignment *and* of the database searched, not of the alignment alone.
- A different alignment gives a different score and hence a different E value (score 23.1 → 6e-7; score 18.9 → 1e-5, same database).

Rules of thumb:

| E value          | Interpretation                                       |
|:-----------------|:-----------------------------------------------------|
| E = 1            | Not a significant match                              |
| E = 1e-2 (0.01)  | Possible remote homology                             |
| E = 1e-3 (0.001) | Remote homology                                      |
| E = 1e-10        | Homology accepted even by the most pedantic reviewer |

## 5.4 Running a BLAST search

**Step 1 — the query sequence.** Nucleotide or protein, any length, given either as an accession number or as text (plain or FASTA format). A whole study can originate from a single sequence: one review started from `NP_004955.2` (human HDAC1).

**Step 2 — choose the program.** The choice encodes which molecule the query and the database are, and how many translation combinations must be tried:

| Program   | Query      | Database   | Combinations |
|:----------|:-----------|:-----------|:-------------|
| `blastn`  | Nucleotide | Nucleotide | 1            |
| `blastp`  | Protein    | Protein    | 1            |
| `blastx`  | Nucleotide | Protein    | 6            |
| `tblastn` | Protein    | Nucleotide | Many         |
| `tblastx` | Nucleotide | Nucleotide | 36           |

The combinatorics come from the genetic code. DNA/RNA can be translated in **six reading frames** (3 forward, 3 reverse), which is where the 6 of `blastx` comes from, and 6 × 6 = 36 for `tblastx`. In the reverse direction, back-translating a protein is massively degenerate: the two residues R-F (arginine, phenylalanine) correspond to 12 possible nucleotide sequences (`CGU UUU`, `CGU UUC`, `CGC UUU`, … `AGG UUC`).

**Step 3 — choose a database.** Separate lists for protein and nucleotide databases; this is where the nr / RefSeq distinction of §3.2 becomes an operational choice. The standard instruction “search the appropriate non-redundant BLAST database” means nr.

**Step 4 — extra options.** You can choose the organism to search, turn filtering on or off, change the substitution matrix, change the expect (E) threshold, change the word size, and change the output format. Search parameters exposed by BLASTP include max sequences, max matches, short-query adjustment, word size, expect threshold, scoring matrix, gap costs, mask and filter. Varying filtering and compositional adjustments can greatly change the alignment itself — e.g. BLASTP of human insulin (`NP_000198`) against a *C. elegans* RefSeq database.

## 5.5 Reading the output

Four output tabs:

- **Descriptions** — the list of sequences matching the query, with links to the NCBI entries, bit score, E value and download options.
- **Graphic Summary** — cartoon-style summary where colour codes the alignment score and the length of the horizontal bar codes the length of the alignment.
- **Alignments** — the text-based alignments themselves.
- **Taxonomy** — which taxonomic groups are represented among the matches.

Multiple alignment views are also available.

**The dot-plot** is a graphical summary of a pairwise alignment in which each dot represents a match between amino acids or nucleotides. A protein against itself produces a perfect diagonal. A human cytoglobin against a large snail globin (which contains many globin repeats) produces matches in about a dozen locations, and the absence of dots for human residues 160–190 shows that the last 30 amino acids are not present in the snail protein. Dot-plots are therefore the fastest way to see repeats, domain duplications and truncations.

## 5.6 Exercises

Using `NP_004955.2` (human histone deacetylase 1) as query against the appropriate non-redundant database: limit the search to green plants, set maximum target sequences to 5000, set a stringent expect threshold (1e-10 or less), then compare the number of hits obtained with different matrices (BLOSUM45, more sensitive, vs BLOSUM90, more severe) and inspect all four output tabs.

Questions from the book (Ch. 3, pp. 114–115), with the reasoning rather than just the key:

- *Orthologs are defined as* homologous sequences in different species that share an ancestral gene (option c describes paralogs; option b describes analogy/structural similarity).
- *Which BLOSUM or PAM matrix suits two distantly related proteins?* BLOSUM45 or PAM250 — low BLOSUM number and high PAM number both mean “tolerant of divergence”.
- *A global algorithm such as Needleman–Wunsch* finds the optimal alignment by finding the optimal subpath that defines the best alignment — i.e. dynamic programming, not exhaustive search.
- Single-letter amino acid codes worth memorising from the exercise: N asparagine, Q glutamine, W tryptophan, C cysteine, F phenylalanine, A alanine.

---
> [[BFB 04 - Pairwise sequence alignment (Chapter III)|← Pairwise sequence alignment (Chapter III)]] · [[Bioinformatics for Biology|↑ Bioinformatics for Biology]]
