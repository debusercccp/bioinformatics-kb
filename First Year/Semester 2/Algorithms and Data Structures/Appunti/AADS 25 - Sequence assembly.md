---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 25
tags: [note, aads]
---

> [[AADS 24 - Burrows–Wheeler transform|← Burrows–Wheeler transform]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 26 - Appendix – the written exam|Appendix – the written exam →]]

# Sequence assembly

**⚠ Non nei topics:** *questo argomento non compare nel programma ufficiale del corso (pagina UniBo A.A. 2026/27, riportata nel vault); è presente nelle slide e negli esami passati.*

*Reference: Compeau and Pevzner, “Bioinformatics Algorithms”, Ch. 3; Gusfield, Ch. 16.*

## 18.1 The problem

Sequence assembly aligns and merges DNA fragments to reconstruct the original sequence (a genome or a contig). Sequencing technologies cannot read a whole genome in one go, only short fragments (**reads**): the human genome has about 3 billion nucleotides per strand, ultra-short reads are 20–40 bp, typical reads 100–500 bp. Two strategies:

- **Mapping (reference-guided):** align the reads to a known reference genome and build the consensus. Works well when a close reference exists. Tools: suffix data structures, BWT (FM-index).
- **De novo:** no reference; reconstruct the sequence only from the overlaps between reads. Tools: graph-based approaches.

De novo assembly assumes that almost every position of the genome is covered by many reads and that many reads overlap. *Example:* the fragments ACCGTG, CGTGC, CTAC, TACCGT can be assembled as TACCGTGCTACCGTG; but how do we decide whether an assembly is good? We need a formal problem.

## 18.2 Shortest Common Superstring (SCS)

**Problem.** Given strings X<sub>1</sub>, …, X<sub>m</sub>, build the shortest string Y containing every X<sub>i</sub> as a substring. Without “shortest”, the concatenation is a solution (ACCGTG·CGTGC·CTAC·TACCGT = ACCGTGCGTGCCTACTACCGT, 21 characters), but it ignores overlaps; the shortest one exploits them. Example from the short notes: the reads ATT, TTA, TAC have the superstring ATTAC.

**Overlap graph.** A weighted, directed, complete graph G = (V, E, w) with V = {X<sub>1</sub>, …, X<sub>m</sub>}, an edge (X<sub>i</sub>, X<sub>j</sub>) for every i ≠ j (no self-loops), and

w(X<sub>i</sub>, X<sub>j</sub>) = max{\|Z\| : Z is a suffix of X<sub>i</sub> and a prefix of X<sub>j</sub>} (the overlap).

A superstring of X<sub>1</sub>, …, X<sub>m</sub> corresponds to a **Hamiltonian path** in the overlap graph (a path visiting every vertex exactly once): for P = P<sub>1</sub> → ⋯ → P<sub>m</sub> the superstring has length

ω(P) = Σ<sub>i=1..m</sub> \|P<sub>i</sub>\| − Σ<sub>i=1..m−1</sub> w(P<sub>i</sub>, P<sub>i+1</sub>).

Since Σ\|X<sub>i</sub>\| does not depend on the path, **the SCS is given by the Hamiltonian path of maximum weight** Σ w(P<sub>i</sub>, P<sub>i+1</sub>).

*Example:* X<sub>1</sub> = ACCGTG, X<sub>2</sub> = CGTGC, X<sub>3</sub> = CTAC, X<sub>4</sub> = TACCGT. Non-zero overlaps: w(X<sub>4</sub>, X<sub>1</sub>) = 5 (ACCGT), w(X<sub>1</sub>, X<sub>2</sub>) = 4 (CGTG), w(X<sub>3</sub>, X<sub>4</sub>) = 3 (TAC), w(X<sub>4</sub>, X<sub>2</sub>) = 3 (CGT), w(X<sub>3</sub>, X<sub>1</sub>) = 2 (AC), w(X<sub>2</sub>, X<sub>3</sub>) = 1, w(X<sub>3</sub>, X<sub>2</sub>) = 1. The path X<sub>4</sub> → X<sub>2</sub> → X<sub>3</sub> → X<sub>1</sub> has ω = 6 + 5 + 4 + 6 − 3 − 1 − 2 = 15 and gives TACCGTGCTACCGTG, a superstring but not the shortest.

**Building the overlap graph.** We need the *all-pairs prefix-suffix* problem: the longest suffix–prefix match for every ordered pair. For one pair it costs O(\|X<sub>i</sub>\| + \|X<sub>j</sub>\|) with a modified KMP-ESM (failure function of X<sub>j</sub>, scan X<sub>i</sub>); comparing X<sub>i</sub> against all the others costs Σ<sub>j≠i</sub> (\|X<sub>i</sub>\| + \|X<sub>j</sub>\|) = O(n), with n = \|X<sub>1</sub>\| + ⋯ + \|X<sub>m</sub>\|, so all pairs cost **Θ(mn)**. (Suffix trees can do it in O(n + m<sup>2</sup>).)

**Complexity.** The maximum-weight Hamiltonian path problem is NP-hard, hence **SCS is NP-hard**. Solution: a heuristic.

## 18.3 GREEDY-SCS

At each step choose the remaining edge of maximum weight, avoiding cycles and nodes that already have an outgoing (resp. incoming) edge. It is a modification of Kruskal’s algorithm in which the spanning tree must be a **path** (a list).

     1: function GREEDY-SCS(Graph G) → Array
     2:     D = DS()                          ▷ disjoint-set data structure
     3:     in[1, ⋯, |G.V|]                   ▷ incoming edges
     4:     out[1, ⋯, |G.V|]                  ▷ outgoing edges
     5:     n = 0                             ▷ number of selected edges
     6:     for v ∈ G.V do
     7:         make-set(D, v)
     8:         in[v] = out[v] = NIL
     9:     S = sort(G.E)                     ▷ decreasing weight
    10:     for (u, v) ∈ S do
    11:         if find-set(D, u) ≠ find-set(D, v) and out[u] == NIL and in[v] == NIL then
    12:             out[u] = v
    13:             in[v] = u
    14:             n = n + 1
    15:             union(D, u, v)
    16:         if n == |G.V| − 1 then break  ▷ the path covers all nodes
    17:     return out

The in\[\] and out\[\] arrays guarantee that each node has at most one incoming and one outgoing edge; the disjoint sets prevent cycles. The superstring is read by starting from the node with no incoming edge and following out\[\], overlapping consecutive strings.

**Cost** (as Kruskal): with n = \|V\| and n<sup>2</sup> edges (complete graph), sorting costs Θ(n<sup>2</sup> log n<sup>2</sup>) = Θ(n<sup>2</sup> log n); at most n + 3n<sup>2</sup> disjoint-set operations cost O(n<sup>2</sup> α(n)) = O(n<sup>2</sup>). Total **Θ(n<sup>2</sup> log n)** (plus building the graph).

**Quality.** GREEDY-SCS is not guaranteed to find the optimum, but (Blum et al., 1994) the computed superstring is in the worst case **less than 4 times longer** than the true SCS (conjectured factor 2).

*Example* (same reads): edges by decreasing weight: X<sub>4</sub> → X<sub>1</sub> (5) selected; X<sub>1</sub> → X<sub>2</sub> (4) selected; X<sub>4</sub> → X<sub>2</sub> (3) is ignored (X<sub>4</sub> already has an outgoing edge and X<sub>2</sub> an incoming one, and X<sub>4</sub>, X<sub>2</sub> are already in the same set: it would close a cycle); X<sub>3</sub> → X<sub>4</sub> (3) adds the last node: stop. Path X<sub>3</sub> → X<sub>4</sub> → X<sub>1</sub> → X<sub>2</sub>: CTAC + CGT + G + C = **CTACCGTGC** (9 characters), which in this case is the shortest common superstring.

## 18.4 Complications of de novo assembly

Mapping SCS to real DNA assembly assumes: no sequencing errors; repeats shorter than the reads; reads covering the whole genome; known read orientation (strand); no contamination. In practice:

- **Sequencing errors:** base-call errors (substitutions, insertions, deletions), more frequent towards the end of the reads (Phred quality scores in FASTQ files). Solution: approximate matching between reads (an *approximate* all-pairs prefix-suffix problem, affecting only the overlap-graph construction; with few errors suffix trees and BWT handle it at a slightly higher cost). After assembly, a **consensus** sequence obtained by majority voting filters the errors out. (Example: reads ACCGT, CGTGC, CTAC, TACCGT with an insertion, a substitution or a deletion still yield the consensus CTACCGTGC.)
- **Repeats:** long, (almost) identical sequences occurring many times lead to ambiguous assemblies; repeats of length L cannot be resolved with reads shorter than L. Repeats show up as cycles in the overlap graph; solution: ignore them and break the assembly into fragments (contigs).
- **Lack of coverage:** with few fragments, parts of the target are covered by no read (sequencing is random sampling). Uncovered regions are visible in the overlap graph; solution: sequence more fragments or break the assembly.
- **Unknown orientation:** a read may come from either strand, so both X and its reverse complement X̄ must be considered (X = ACTACG, X̄ = CGTAGT). Solution: add all reverse-complemented reads as nodes of the graph.
- **Contamination:** foreign DNA (microorganisms from reagents and lab materials) and chimeric reads (joining non-contiguous parts of the target). Solution: remove them before assembly: screen reads against well-known vector/bacterial genomes; detect chimeras in pre-processing.

**More on de novo assembly.** It is still an open challenge. Most current assemblers use **de Bruijn graphs**: reads are broken into k-mers, which are the nodes; an edge joins two k-mers if the corresponding (k + 1)-mer appears in some read, labeled with its number of occurrences; the assembly is a path in the graph (an Eulerian path, which unlike Hamiltonian paths can be found in polynomial time). Advantages: speed and simplicity (each node has at most \|Σ\| incoming and outgoing edges, e.g. 4 for DNA). Disadvantages: repeats still cannot be resolved, and information on read continuity is lost.

From the short notes: the exact SCS/maximum Hamiltonian path formulation is NP-hard, so real assemblers use heuristics or other models (de Bruijn graphs); the greedy algorithm is not guaranteed to be optimal but gives a good approximation.

## 18.5 Exam exercises on sequence assembly

**Exam 28 June 2024, Ex. 6.** X<sub>1</sub> = AAACCC, X<sub>2</sub> = ACCCAA, X<sub>3</sub> = CAAACC, X<sub>4</sub> = CCCAAA.

1)  Overlap graph (weight of X<sub>i</sub> → X<sub>j</sub>):

| from \\ to    | X<sub>1</sub> | X<sub>2</sub> | X<sub>3</sub> | X<sub>4</sub> |
|:--------------|:--------------|:--------------|:--------------|:--------------|
| X<sub>1</sub> | –             | 4             | 1             | 3             |
| X<sub>2</sub> | 2             | –             | 3             | 5             |
| X<sub>3</sub> | 5             | 3             | –             | 2             |
| X<sub>4</sub> | 3             | 1             | 4             | –             |

2)  GREEDY-SCS: X<sub>2</sub> → X<sub>4</sub> (5) selected; X<sub>3</sub> → X<sub>1</sub> (5) selected; X<sub>1</sub> → X<sub>2</sub> (4) selected: the path X<sub>3</sub> → X<sub>1</sub> → X<sub>2</sub> → X<sub>4</sub> covers all nodes, stop. (X<sub>4</sub> → X<sub>3</sub>, also weight 4, would close a cycle.) Superstring: CAAACC + C + AA + A = **CAAACCCAAA** (10 characters). There are two distinct SCS solutions; this is one of them.

### 18.5.1 Past exam exercises on this topic

5)  Ex. 5 2022/11/30; (E) Ex. 5 2023/02/06; (E) Ex. 6 2023/06/29; (E) Ex. 6 2023/12/01; (E) Ex. 6 2024/06/28.

---
> [[AADS 24 - Burrows–Wheeler transform|← Burrows–Wheeler transform]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 26 - Appendix – the written exam|Appendix – the written exam →]]
