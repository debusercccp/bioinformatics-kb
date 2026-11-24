---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 20
tags: [note, aads]
---

> [[AADS 19 - Graphs – representation, connected components, minimum spanning trees|← Graphs – representation, connected components, minimum spanning trees]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 21 - String matching|String matching →]]

# Hard problems: P, NP, NP-complete, NP-hard

*Reference: CLRS Ch. 34–35.*

## 13.1 Types of problems and complexity classes

In complexity theory problems are grouped into resource-related **complexity classes** (time, memory); the Complexity Zoo lists 547 of them. We focus on P and NP.

- **Decision problem:** the answer is yes/no (is G a tree?). Most classes are defined for decision problems.
- **Optimization problem:** among all feasible solutions find the best one according to an objective function (MST, change making). Every optimization problem can be turned into a decision problem (is there a spanning tree of weight \< k? can W be changed with fewer than k coins?).
- **Counting problem:** how many solutions are there (how many MSTs?). **Function problem:** compute a value (the factorial). **Search problem:** find a specific solution in a search space.

**P** is the class of decision problems **solvable** in polynomial time (n, n<sup>2</sup>, n<sup>3</sup>, …): considered efficiently solvable. **NP** is the class of decision problems **verifiable** in polynomial time: if the answer is yes, a proposed solution can be checked in polynomial time. **P ⊆ NP**: solving implies verifying. Verifying is typically easier than finding (given a Sudoku, a filled grid is easy to check, finding one is hard).

**The P vs NP problem** (Cook, 1971): is P = NP? Equivalently: if a solution is easy to check, is it also easy to find? It is the most famous open problem in computer science (one of the Millennium Prize problems).

**Determinism vs non-determinism.** NP stands for *non-deterministic polynomial*. For SAT with n variables, a deterministic algorithm must evaluate up to 2<sup>n</sup> assignments, while a non-deterministic machine “guesses” an assignment in n steps (each branch of the computation lives in its own independent universe) and verifies it. NP = problems solvable in polynomial time by a non-deterministic machine.

**Polynomial-time verification.** A **verifier** (certifier, checker) is an algorithm that takes a problem instance P and a candidate solution S (the **certificate** or witness) and returns true iff S is a solution of P. It does not solve P, it checks a candidate. It is a polynomial verifier if its cost is polynomial in the input size. Example: verifying a Sudoku solution costs Θ(n<sup>2</sup>) (consistency with the puzzle, every row and every column contains 1, …, n); there is a huge number of candidates, which a non-deterministic algorithm could generate in O(n<sup>2</sup>) steps.

## 13.2 NP-complete and NP-hard problems

A decision problem P is **NP-complete** if:

1.  P ∈ NP (verifiable in polynomial time), and
2.  every problem in NP can be reduced to P in polynomial time.

A problem is **NP-hard** if it satisfies property 2, not necessarily property 1: at least as hard as the hardest problems in NP. NP-hard problems need not be in NP: they may be optimization problems, or not have efficiently verifiable certificates. NP-complete problems are “the hardest problems inside NP”.

**How to prove it in practice.** P is NP-complete if (1) a solution can be verified in polynomial time and (2) **a known NP-complete problem can be reduced to P in polynomial time** (if we could solve P fast, we could solve the known problem fast). P is NP-hard if a known NP-complete problem reduces to (the decision version of) P in polynomial time.

**Scenarios.** If any NP-complete/NP-hard problem had a polynomial algorithm, then all of NP would be polynomial: **P = NP** (revolutionary). If no NP-hard problem has a polynomial algorithm, P ≠ NP (the expected scenario). Consequences of P = NP: efficient solutions to many NP-hard problems, including many in computational biology; cryptography would need a complete overhaul (many protocols rely on P ≠ NP, e.g. hardness of integer factorization). Consequences of P ≠ NP: a proven limit on the power of computation, cryptography stays safe, and attention goes to heuristic and approximation algorithms. Either proof would likely need new mathematical techniques.

## 13.3 Four classic hard problems

For each of them verifying a solution is easy (polynomial) and finding one is hard (no polynomial algorithm is known); a brute-force exponential search has, as far as we know, “optimal” worst-case complexity.

**Boolean satisfiability (SAT).** Given a Boolean formula φ in conjunctive normal form (CNF), is there an assignment that makes φ true? CNF is an AND of clauses, each an OR of literals (a variable or its negation); every formula can be converted to CNF. Example: φ = (A ∨ ¬B ∨ C) ∧ (B ∨ ¬C) ∧ (¬A ∨ B ∨ ¬C) is satisfied by A = B = T, C = F. SAT was the **first problem proved NP-complete** (Cook–Levin theorem: given a non-deterministic Turing machine solving a problem in NP and an input x, one builds a formula satisfiable iff the machine accepts x; Karp, 1972–73, then reduced many problems to it). 3-SAT (three literals per clause) is NP-complete.

**Graph coloring.** Given an undirected graph and k, can the nodes be colored with m ≤ k colors so that adjacent nodes have different colors? Example: the map of Australia (regions = nodes, borders = edges) can be 3-colored, but not with m ≤ 2 colors.

**CLIQUE.** Given an undirected graph and k, is there a subset S of m ≥ k nodes such that every two nodes in S are adjacent? Verifier:

    1: function VerifyClique(Graph G, int k, Set S) → bool
    2:     if |S| < k then return false
    4:     for u ∈ S do                          ▷ each pair of distinct nodes in S
    5:         for v ∈ S − {u} do
    6:             if (u, v) ∉ G.E then return false
    8:     return true

Cost O(\|S\|<sup>2</sup>) with an adjacency matrix: polynomial. Brute force generates and verifies all 2<sup>n</sup> subsets of nodes:

     1: function clique(Graph G, int k, Set S) → bool
     2:     if |S| ≥ k and VerifyClique(G, k, S) == true then return true
     4:     else
     5:         for v ∈ G.V − S do
     6:             S = S ∪ {v}
     7:             if clique(G, k, S) == true then return true
     9:             else S = S − {v}
    11:     return false

MAX-CLIQUE (compute a maximum clique) is the optimization version.

*CLIQUE is NP-complete, by reduction from 3-SAT.* Given a CNF formula φ with k clauses of three literals, build a graph G with k clusters (one node per literal of each clause) and connect two nodes iff they belong to different clauses and are **not** a literal and its negation (they can be true together). Building G costs O(k<sup>2</sup>). φ is satisfiable iff there is a true literal in each clause iff G has a k-clique (choosing one compatible literal per clause). So CLIQUE is at least as hard as 3-SAT, hence NP-complete; consequently MAX-CLIQUE is NP-hard.

**Traveling Salesman Problem (TSP).** Given n cities, their distances and k, is there a tour of total length ≤ k that visits each city exactly once and returns to the origin? (Example: 7 cities in Tuscany.) Symmetric if w(u, v) = w(v, u), asymmetric otherwise. Θ(n) verifier, with D the distance matrix and S the certificate tour S\[1\] → ⋯ → S\[n\] → S\[1\]:

    1: function VerifyTSP(int D[1..n][1..n], int S[1..n], int k) → bool
    2:     δ = D[S[n], S[1]]                     ▷ closing edge S[n] → S[1]
    3:     for i = 2, ⋯, n do
    4:         δ = δ + D[S[i − 1], S[i]]
    5:     if δ > k then return false
    6:     return true

Brute force (BF-TSP) enumerates all n! permutations recursively, building S position by position from the set C of cities not yet used and updating the partial length δ; at the leaves (C = ∅) it adds the closing edge and compares with k.

## 13.4 How to deal with NP-hard problems

We must give up something:

- **Generality:** polynomial algorithms for **special cases**;
- **Optimality:** a polynomial solution “almost” optimal: **approximation algorithms**;
- **Efficiency:** exponential time, but cleverly pruning the search space: **branch & bound**;
- **Formality:** a polynomial algorithm that “seems” to give good solutions, without proof: **heuristics**.

**Special cases.** SAT is polynomial for 2-CNF formulas (NP-complete for 3-CNF). Graph coloring is polynomial with 2 colors (NP-complete already for 3). CLIQUE is polynomial on some graph classes (e.g. bipartite graphs). TSP is polynomial for some classes of distance matrices (e.g. Van der Veen matrices).

**Approximation algorithms.** For an optimization problem with non-negative cost c, an approximation algorithm finds in polynomial time a solution x’ with c(x’) ≤ ρ·c(x*), where x* is optimal and ρ \> 1 is the approximation ratio (factor).

*Δ-TSP (TSP with triangle inequality):* D\[i, j\] ≤ D\[i, k\] + D\[k, j\] for all i, j, k. Δ-TSP is NP-hard (its decision version is NP-complete) but it admits approximation algorithms. Model it on a complete weighted undirected graph G: a tour is a **Hamiltonian cycle** (a cycle visiting every node exactly once). Removing an edge from a Hamiltonian cycle gives a spanning tree, so **an MST costs no more than an optimal tour**. Algorithm: compute an MST T (Kruskal), do a pre-order visit of T from any root, H = \[a, b, c, h, d, e, f, g\] in the slides example, and return the tour that visits the nodes in that order and goes back to the start. A full walk of T costs 2w(T); skipping already visited nodes never increases the length thanks to the triangle inequality, so the tour has length ≤ 2w(T) ≤ 2·OPT: **a 2-approximation**. Cost: MST O(m log n) + visit O(n) = O(n<sup>2</sup> log n), since the graph is complete (m = Θ(n<sup>2</sup>)). Better approximations exist for Δ-TSP; but if P ≠ NP, the *general* TSP (without triangle inequality) admits no approximation algorithm at all, and many other problems do not either.

**Branch & bound (BAB).** A “smart” enumeration that simulates brute force but does not extend a partial solution S if it cannot lead to a better solution than the current best (or, in the decision version, to a solution within the bound k). A function lb(S) gives a sound **lower bound** on the cost of every complete solution S\* extending S: lb(S) ≤ c(S\*).

     1: function BAB(problem P, solution S, bound k) → bool
     2:     C = choices(P, S)                    ▷ problem-dependent choices
     3:     if C = ∅ then
     4:         if c(S) > k then return false else return true
     6:     else
     7:         for c ∈ C do
     8:             S = S ∪ {c}                  ▷ add c to the partial solution
     9:             if lb(S) ≤ k then            ▷ still worth expanding S?
    10:                 if BAB(P, S, k) == true then return true
    11:             S = S − {c}                  ▷ remove c
    12:         return false

A BAB implementation depends on the **branch** (how many choices/children are generated), the **bound** (how lb is computed and how tight it is; lb(S) = −∞ is always sound but reduces BAB to brute force) and the **visit order** of the search tree. *BAB for TSP:* branch on the n − \|S\| cities not yet in S\[1..i\]; lb(S) = δ + μ, where δ is the length of the path S\[1\] → ⋯ → S\[i\] and μ is the sum, over S\[i\] and every city not in S, of the cheapest edge leaving it towards a city not yet used (or back to S\[1\]): every complete tour must leave each of those cities once. BAB-TSP is BF-TSP with the test lb(S, δ, C) ≤ k before the recursive call. Worst case still exponential, but often much faster.

**Heuristic algorithms.** When optimal solutions are too expensive and no approximation algorithm exists, heuristics are “educated guesses”: no guarantee, but often good solutions in practice. Two families: **greedy** (always make the same greedy choice) and **local search** (start from a solution and improve it with small changes).

*Greedy TSP* (optimization version, complete weighted graph): sort the edges by increasing weight; scan them and add (u, v) if u has no outgoing edge yet, v has no incoming edge yet, and no cycle is formed (checked with disjoint sets); finally add the edge that closes the tour (between the only node without outgoing edge and the only node without incoming edge).

     1: function greedy-TSP(Graph G) → Array
     2:     D = DS()                              ▷ disjoint-set data structure
     3:     in[1..|G.V|], out[1..|G.V|]
     4:     n = 0                                 ▷ number of selected edges
     5:     for v ∈ G.V do
     6:         make-set(D, v)
     7:         in[v] = out[v] = NIL
     8:     S = sort(G.E)                         ▷ increasing weight
     9:     for (u, v) ∈ S do
    10:         if find-set(D, u) ≠ find-set(D, v) and out[u] == NIL and in[v] == NIL then
    11:             out[u] = v, in[v] = u, n = n + 1
    12:             union(D, u, v)
    13:     close the tour with the edge from the node with out = NIL to the node with in = NIL
    14:     return out

The in/out vectors make sure every node has exactly one incoming and one outgoing edge; cost dominated by sorting, O(n<sup>2</sup> log n).

**Conclusions.** Many interesting problems are hard and we do not know whether polynomial algorithms exist (and even if they did, we would be unlikely to find them). We must learn to recognize hard problems to avoid wasting time looking for polynomial algorithms, and attack them with special-case, approximation, branch & bound or heuristic algorithms. Sequence assembly (shortest common superstring) and multiple sequence alignment are examples from bioinformatics.

## 13.5 Exam exercises on hard problems

**Exam 15 January 2024, Ex. 3: longest path.** Decision version: given an undirected G and k \> 0, is there a simple path (all vertices distinct) of length ≥ k?

1)  It is in NP: given a list of nodes L = \[v<sub>1</sub>, …, v<sub>n</sub>\], check in polynomial time that \|L\| ≥ k (O(n)), that v<sub>1</sub> → ⋯ → v<sub>n</sub> is a path in G (O(n)), and that it has no repeated nodes (O(n log n): sort the labels and look for duplicates).

2)  NP-complete by reduction from Hamiltonian path (NP-complete): G with n nodes has a Hamiltonian path iff it has a simple path with n nodes, so

<!-- -->

    1: function hamiltonian-path(Graph G) → bool
    2:     return longest-path(G, |G.V|)

A polynomial algorithm for longest-path would give one for Hamiltonian path.

3)  The general (optimization) longest path problem is then NP-hard.

**Exam 16 January 2023, Ex. 4: the pairing problem.** Pair the i-th smallest of X with the i-th smallest of Y, rearranging only Y. (a) If the first array is sorted, after pairing the second is sorted too, so we can sort X with: create Y = \[1, …, n\] (Θ(n)) and call pairing(Y, X). (b) If pairing (which works by comparisons) ran in O(n), pairingsort would be a linear-time comparison sort, contradicting the Ω(n log n) lower bound. Hence **no worst-case linear-time pairing algorithm exists** (a reduction used to prove a lower bound).

### 13.5.1 Past exam exercises on this topic

1)  Ex. 4 2023/01/16; (A) Ex. 3 2024/01/15.

---
> [[AADS 19 - Graphs – representation, connected components, minimum spanning trees|← Graphs – representation, connected components, minimum spanning trees]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 21 - String matching|String matching →]]
