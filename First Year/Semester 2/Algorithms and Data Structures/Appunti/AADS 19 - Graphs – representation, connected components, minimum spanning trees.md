---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 19
tags: [note, aads]
---

> [[AADS 18 - Disjoint-set data structure (Union–Find)|← Disjoint-set data structure (Union–Find)]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 20 - Hard problems – P, NP, NP-complete, NP-hard|Hard problems – P, NP, NP-complete, NP-hard →]]

# Graphs: representation, connected components, minimum spanning trees

*Reference: CLRS Ch. 22 and 23.*

## 12.1 Definitions

A graph models relationships between objects (road maps, social networks, protein interaction networks, metabolic pathways…). A graph is a pair G = (V, E) of a set of **vertices** (nodes) and a set of **edges** (links); we write n = \|V\| and m = \|E\|.

- **Undirected:** edges have no direction (A — B); **directed** (digraph): edges are ordered pairs (A → B).
- **Weighted:** each edge has a cost/length w(u, v); **unweighted:** all edges equal.
- **Simple graph / multigraph:** whether multiple edges and self-loops are allowed.
- **Degree** δ(u): number of edges incident to u (in-degree and out-degree for directed graphs). **Adjacent** vertices are connected by an edge.
- **Path:** sequence of vertices connected by edges; **cycle:** a path that returns to its start.
- **Connected graph:** there is a path between any two vertices. **Connected component:** a maximal set of mutually reachable vertices (undirected).
- **Complete graph:** every pair of vertices is adjacent; m = n(n − 1)/2. In general m = O(n<sup>2</sup>).
- **Tree:** connected acyclic graph (n − 1 edges). **DAG:** directed acyclic graph.
- **Sparse** graph: m ≪ n<sup>2</sup>; **dense** graph: m ≈ n<sup>2</sup>.

## 12.2 Representation

**Adjacency list.** An array A\[1..n\] of pointers to linked lists; A\[v\] lists the vertices adjacent to v (for undirected graphs each edge appears in both lists; for weighted graphs each list node also stores the weight). Space Θ(n + m) (Θ(n + 2m) undirected), at most O(n<sup>2</sup>). Visiting the neighbors of u costs Θ(δ(u)) = O(n); checking whether (u, v) ∈ E costs O(δ(u)) = O(n). Ideal for **sparse** graphs.

**Adjacency matrix.** An n × n matrix with A\[u\]\[v\] = 1 if (u, v) ∈ E, 0 otherwise (or w(u, v) for weighted graphs; symmetric for undirected graphs). Space Θ(n<sup>2</sup>). Visiting the neighbors of u costs Θ(n); checking an edge costs O(1). Ideal for **dense** graphs.

**Pseudocode notation.** G.V and G.E are the vertex and edge sets. `for u ∈ G.V` costs Θ(n); `for (u, v) ∈ G.E` costs Θ(n + m) with adjacency lists and Θ(n<sup>2</sup>) with an adjacency matrix. G.A is the adjacency vector (G.A\[u\] is the list of u) or the adjacency matrix (G.A\[u\]\[v\]).

## 12.3 Connected components

A sub-graph G’ = (V’, E’) of an undirected graph G is a connected component iff for every u ∈ V’: (1) there is a path from u to every other v ∈ V’; (2) there is no path from u to any w ∈ V − V’. The problem is solved easily with disjoint sets: put adjacent vertices in the same set.

    1: function CC(Graph G) → DS
    2:     D = DS()                          ▷ disjoint-set data structure
    3:     for v ∈ G.V do
    4:         make-set(D, v)                ▷ each vertex is a singleton
    5:     for (u, v) ∈ G.E do
    6:         union(D, u, v)                ▷ adjacent vertices in the same set
    7:     return D                          ▷ each set is a connected component

    1: function sameCC(DS D, Vertex u, Vertex v) → bool
    2:     return find-set(D, u) == find-set(D, v)

CC performs n make-set and m union operations: O(n + m) with union by rank and path compression (α(n) ≈ constant); the edge loop costs Θ(n + m) with adjacency lists and Θ(n<sup>2</sup>) with an adjacency matrix. So CC costs **Θ(n + m)** (list) or **Θ(n<sup>2</sup>)** (matrix). sameCC costs O(log n) (two find-set; height ≤ log n with union by rank), O(1) amortized.

(Graph traversals, BFS and DFS, can compute the components as well; the course uses the disjoint-set version.)

## 12.4 Minimum Spanning Tree **\[Non nei topics\]**

**⚠ Non nei topics:** *l'MST e l'algoritmo di Kruskal non compaiono nel programma ufficiale del corso (pagina UniBo A.A. 2026/27, riportata nel vault), che cita solo i grafi; sono presenti nelle slide e negli esami passati.*

**Problem.** Given a connected, undirected, weighted graph G = (V, E) with w : E → ℝ, compute T ⊆ E such that: (1) T is a tree (connected and acyclic); (2) T connects all the vertices (spanning); (3) w(T) = Σ<sub>(u,v)∈T</sub> w(u, v) is minimum. A spanning tree on n vertices always has n − 1 edges. Applications: design of networks (electrical, telecommunication, road), clustering, approximation algorithms (see Δ-TSP). An MST always exists but may not be unique; **if all weights are distinct, the MST is unique**. Missing edges can be seen as having weight +∞.

### 12.4.1 Generic greedy algorithm

Grow T starting from ∅, adding one **safe edge** at a time. An edge (u, v) is safe for T if T ∪ {(u, v)} is still a subset of some MST.

    1: function Generic-MST(Graph G) → Set
    2:     T = ∅
    3:     while T is not a MST for G do
    4:         find a safe edge (u, v) ∈ G.E − T
    5:         T = T ∪ {(u, v)}
    6:     return T

**Definitions.** A **cut** (S, V − S) is a partition of V. An edge **crosses** the cut if one endpoint is in S and the other in V − S. A cut **respects** a set of edges A if no edge of A crosses it. A **light edge** is a crossing edge of minimum weight.

**Theorem.** Let A be a subset of some MST T of G. If (S, V − S) is a cut that respects A and (u, v) is a light edge crossing it, then (u, v) is safe for A. *Proof sketch.* If (u, v) ∈ T we are done. Otherwise (u, v) forms a cycle with the path from u to v in T; this path contains an edge (x, y) crossing the cut, and (x, y) ∉ A because the cut respects A. Replacing (x, y) with (u, v) gives T’ = T − {(x, y)} ∪ {(u, v)}, a spanning tree with w(T’) ≤ w(T) because (u, v) is light: T’ is an MST containing A ∪ {(u, v)}.

### 12.4.2 Kruskal’s algorithm (1956)

An instance of Generic-MST that grows and merges a forest of trees by adding light edges. It is **greedy**: at each step it adds the edge of minimum weight that does not create a cycle, i.e. that connects two different trees (components). The MST problem has optimal substructure, and the theorem guarantees the greedy-choice property. Disjoint sets keep track of the trees.

     1: function Kruskal-MST(Graph G, w) → Set
     2:     D = DS()                          ▷ disjoint-set data structure
     3:     T = ∅
     4:     for v ∈ G.V do
     5:         make-set(D, v)                ▷ n single-vertex trees
     6:     S = sort(G.E, w)                  ▷ edges in increasing weight
     7:     for (u, v) ∈ S do
     8:         if find-set(D, u) ≠ find-set(D, v) then
     9:             T = T ∪ {(u, v)}          ▷ add the light edge
    10:             union(D, u, v)
    11:     return T

We can stop as soon as T has n − 1 edges. **Cost:** n make-set O(n); sorting the edges O(m log m) = **O(m log n)** (since m ≤ n<sup>2</sup>, log m ≤ 2 log n); the loop performs O(m) find-set/union, O(m α(n)). Total O(m log n), dominated by sorting.

Why choosing the cheapest edge that joins two components is safe (short notes): it is the cheapest way to reduce the number of components without creating a cycle; repeating it connects everything with minimum total weight.

**Slides example** (vertices a … i): the edges are taken in increasing order; (h, g) first, then (c, i), (g, f), (a, b), …; at step (f) the light edge (i, g) is discarded because find-set(i) = find-set(g) (it would close a cycle), and similarly (i, h) later. The result is T = {(a, b), (a, h), (c, d), (d, e), (c, f), (c, i), (f, g), (g, h)}, w(T) = 37; it is not unique, since (a, h) can be replaced by (b, c) (same weight 8).

**Other MST algorithms.** Prim’s algorithm (similar to Dijkstra’s shortest paths), also O(m log n); Fredman–Tarjan O(m + n log n) with Fibonacci heaps; Karger–Klein–Tarjan O(m + n) randomized; Fredman–Willard O(m + n), not based on comparisons.

## 12.5 Exam exercises on graphs

**Exam 13 February 2026, Ex. 4.** Undirected graph on A, B, C, D, E (edges with weight ≤ 0 not shown): A–D 4, A–B 4, D–C 4, B–C 4 (the outer square), A–E 6, D–E 6, B–E 2, C–E 2 (E is the center).

1)  Kruskal: sort the edges by weight; ties may be taken in any order.

<!-- -->

1.  (B, E), weight 2: B and E in different sets ⇒ added.
2.  (C, E), weight 2 ⇒ added.
3.  (A, B), weight 4 ⇒ added (A joins {B, C, E}).
4.  (A, D), weight 4 ⇒ added. Now T has 4 = n − 1 edges: stop. (Otherwise (B, C) and (C, D) would be rejected because they close cycles, as would the 6-edges.)

MST = {(B, E), (C, E), (A, B), (A, D)}, total weight 12.

2)  There are **three** distinct MSTs. Any MST contains the two 2-edges; A and D must then be attached with two 4-edges chosen among (A, B), (A, D), (C, D) ((B, C) would close a cycle with B–E–C): {(A, B), (A, D)}, {(A, B), (C, D)}, {(A, D), (C, D)}. Equivalently: adding (C, D) to the tree found creates a cycle, and removing either (A, B) or (A, D) gives the other two MSTs.

**Typical requests in (E) exercises:** run Kruskal showing the order in which edges are selected or discarded and the disjoint sets after each step; count the distinct MSTs (look at ties among the light edges); run CC/sameCC with the disjoint-set forest. (A) exercises may ask for the cost of an algorithm with adjacency lists vs adjacency matrix (e.g. 2024/12/16, Ex. 1).

### 12.5.1 Past exam exercises on this topic

5)  Ex. 4 2022/06/24 F; (E) Ex. 4 2022/10/28; (E) Ex. 4 2023/10/27; (E) Ex. 4 2024/01/15 F; (E) Ex. 4 2024/11/15; (A) Ex. 1 2024/12/16; (E) Ex. 4 2025/02/14; (E) Ex. 4 2026/02/13.

---
> [[AADS 18 - Disjoint-set data structure (Union–Find)|← Disjoint-set data structure (Union–Find)]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 20 - Hard problems – P, NP, NP-complete, NP-hard|Hard problems – P, NP, NP-complete, NP-hard →]]
