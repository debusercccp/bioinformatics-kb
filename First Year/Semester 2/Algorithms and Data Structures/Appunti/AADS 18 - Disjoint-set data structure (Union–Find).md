---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 18
tags: [note, aads]
---

> [[AADS 17 - Algorithmic techniques|← Algorithmic techniques]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 19 - Graphs – representation, connected components, minimum spanning trees|Graphs – representation, connected components, minimum spanning trees →]]

# Disjoint-set data structure (Union–Find)

**⚠ Non nei topics:** *questo argomento non compare nel programma ufficiale del corso (pagina UniBo A.A. 2026/27, riportata nel vault); è presente nelle slide e negli esami passati.*

*Reference: CLRS Ch. 21.*

## 11.1 Definition and operations

A disjoint-set data structure maintains a collection S = {S<sub>1</sub>, …, S<sub>k</sub>} of **disjoint** dynamic sets (no element belongs to more than one set), e.g. S = {{1, 2}, {3, 4, 7}, {5}}. It is used for very specific problems: connected components of a graph, Kruskal’s algorithm, equivalence relations; in bioinformatics, for example, grouping proteins from pairwise protein–protein interactions (PPI).

Each set is identified by a **representative** ρ ∈ S<sub>i</sub>: any element, or a specific one (e.g. the minimum or the maximum, for integers). Every find on the same set must return the same representative; the representative may change after a union.

- **make-set(x):** create the singleton {x} (x must not belong to any other set).
- **find-set(x):** return a reference to the representative of the set containing x. With S = {{1, 2}, {8}, {3, 5}} and the minimum as representative, find-set(2) returns 1.
- **union(x, y):** replace S<sub>x</sub> and S<sub>y</sub> (disjoint, i.e. find-set(x) ≠ find-set(y)) with S<sub>x</sub> ∪ S<sub>y</sub>. Example: union(1, 5) gives {{1, 2, 3, 5}, {8}}.

With n disjoint sets, after n − 1 unions only one set remains. Costs are analyzed for a sequence of **m operations, n of which are make-set** (so m ≥ n and there are at most n − 1 unions).

## 11.2 Linked-list implementation

Each set is a linked list; each node x has x.elem, x.next and x.set (a pointer to the set object, which holds head and tail). The representative is the first node.

- make-set(x): a new list with one node, O(1).
- find-set(x): follow x.set and return the head, O(1).
- union(x, y), naive: append L<sub>y</sub> to L<sub>x</sub> and update the set pointer of every node of L<sub>y</sub>: Θ(\|L<sub>y</sub>\|) = O(n). A sequence of n unions can cost Θ(n<sup>2</sup>) (when \|L<sub>x</sub>\| = 1 and \|L<sub>y</sub>\| = n − 1 each time).

**Weighted-union heuristic:** append the shorter list to the longer one, cost Θ(min(\|L<sub>x</sub>\|, \|L<sub>y</sub>\|)). **Theorem:** a sequence of m operations, n of them make-set, costs O(m + n log n). *Sketch:* make-set and find-set are O(1) (O(m) in total); each time the set pointer of an element is updated, the element joins a set at least twice as big, so after k updates its set has ≥ 2<sup>k</sup> members; since sets have at most n members, each element is updated at most log n times: O(n log n) for all unions.

## 11.3 Disjoint-set forests (Galler and Fisher, 1964)

Each set is a rooted tree; each node contains an element and a pointer to its parent; the root is the representative and points to itself.

- make-set(x): a one-node tree, O(1).
- find-set(x): follow parents up to the root (the **find path**): O(h) = O(n).
- union(x, y): make the root of one tree point to the root of the other: O(1) if the roots are known, otherwise O(n) because of the find-set calls.

Without heuristics this is no better than linked lists with weighted union (a tree can degenerate into a chain). Two heuristics keep the trees low:

**Union by rank** (Tarjan and van Leeuwen, 1984). Every node keeps a **rank**, the height of its subtree (or an upper bound of it). In a union the root with smaller rank points to the root with larger rank, and the rank does not change; if the ranks are equal, one root is appended to the other and the new root’s rank increases by 1. (Equivalent idea: union by size.)

**Path compression** (McIlroy and Morris, 1970s). During find-set(x), every node on the find path is made to point directly to the root, so future finds on those nodes take O(1). Path compression changes only parent pointers, **not the ranks**: after compression the rank is no longer the exact height but an upper bound (updating exact heights would need the children of each node, while we only have parent pointers).

The forest can be implemented as an array (or a dictionary, if the elements are not integers) of nodes with fields elem, parent, rank:

    1: function make-set(DS D, elem x)
    2:     D[x].elem = x
    3:     D[x].parent = D[x]
    4:     D[x].rank = 0

    1: function find-set(DS D, elem x) → elem
    2:     if D[x].parent ≠ D[x] then
    3:         y = find-set(D, D[x].parent.elem)
    4:         D[x].parent = D[y]                   ▷ path compression
    5:     return D[x].parent.elem

    1: function union(DS D, elem x, elem y)
    2:     u = find-set(D, x)
    3:     v = find-set(D, y)
    4:     if u ≠ v then
    5:         link(D, u, v)

    1: function link(DS D, elem x, elem y)        ▷ x, y are roots
    2:     if D[x].rank > D[y].rank then
    3:         D[y].parent = D[x]
    4:     else
    5:         D[x].parent = D[y]
    6:         if D[x].rank == D[y].rank then
    7:             D[y].rank = D[y].rank + 1

Note the convention used at the exam: with equal ranks, the root of the **first** argument goes under the root of the **second**, whose rank grows by one.

## 11.4 Costs

For a sequence of m operations, n of which make-set:

- **Union by rank only:** O(m log n). *Sketch:* by induction on the number of unions, a tree with root x has at least 2<sup>x.rank</sup> nodes; since 2<sup>rank</sup> ≤ n, rank ≤ log n, so every find-set visits at most log n nodes.
- **Path compression only:** O(n + f(1 + log<sub>2+f/n</sub> n)), f = number of find-set operations (hard proof); amortized O(log n).
- **Union by rank + path compression** (Tarjan, 1975): **O(m α(n))**, where α(n) is the inverse Ackermann function. Amortized cost O(α(n)), just a bit worse than constant.

**Ackermann function** (1928): A(0, n) = n + 1; A(m, 0) = A(m − 1, 1) for m \> 0; A(m, n) = A(m − 1, A(m, n − 1)) for m, n \> 0. It is total and computable but not primitive recursive (it cannot be computed with for loops only, whose number of iterations is known before entering the loop). It grows incredibly fast: A(4, 2) = 2<sup>65536</sup> − 3 has 19 729 decimal digits. The inverse is defined as α(n) = min{m : A(m, m) ≥ n}; since A(4, 4) is astronomically large, **α(n) \< 5 for every practical n**, so α(n) can be treated as O(1).

From the short notes: path compression flattens the trees during finds, so later finds become cheaper on average; union by rank prevents trees from getting tall; together they make each operation almost constant time in practice.

## 11.5 Exam exercises on disjoint sets

These are (E) exercises: draw the forest after each operation, using union by rank and path compression. Procedure: for union(x, y) first run find-set on both (compressing their paths), then link the roots with the rank rule.

**Exam 28 June 2024, Ex. 4.** Set {1, …, 8}; make-set(1..8), then union(6, 7), union(5, 8), union(5, 6), union(1, 2), union(5, 7), union(5, 2), union(1, 3), union(1, 4). Notation: r(c<sub>1</sub>, c<sub>2</sub>, …) is a root with its children; \[rank\] is shown for roots of rank \> 0.

| Operation | Forest after the operation |
|:---|:---|
| make-set(1..8) | 1 2 3 4 5 6 7 8 (all rank 0) |
| union(6, 7) | 7(6) \[1\], 1, 2, 3, 4, 5, 8 |
| union(5, 8) | 7(6) \[1\], 8(5) \[1\], 1, 2, 3, 4 |
| union(5, 6) | roots 8 and 7 have equal rank: 8 goes under 7 ⇒ 7(6, 8(5)) \[2\], 1, 2, 3, 4 |
| union(1, 2) | 2(1) \[1\], 7(6, 8(5)) \[2\], 3, 4 |
| union(5, 7) | find-set(5) compresses 5 directly under 7 ⇒ 7(5, 6, 8) \[2\], 2(1) \[1\], 3, 4 |
| union(5, 2) | rank(2) = 1 \< rank(7) = 2 ⇒ 7(2(1), 5, 6, 8) \[2\], 3, 4 |
| union(1, 3) | find-set(1) compresses 1 under 7; 3 (rank 0) goes under 7 ⇒ 7(1, 2, 3, 5, 6, 8) \[2\], 4 |
| union(1, 4) | 7(1, 2, 3, 4, 5, 6, 8) \[2\] |

**Exam 21 July 2022, Ex. 4.** Set {1, …, 10}; union(1, 2), union(3, 4), union(2, 4), union(7, 8), union(7, 3), find-set(1), union(7, 6), union(3, 5).

| Operation | Forest after the operation |
|:---|:---|
| union(1, 2) | 2(1) \[1\] |
| union(3, 4) | 2(1) \[1\], 4(3) \[1\] |
| union(2, 4) | equal ranks ⇒ 4(2(1), 3) \[2\] |
| union(7, 8) | 8(7) \[1\] |
| union(7, 3) | rank(8) = 1 \< 2 ⇒ 4(2(1), 3, 8(7)) \[2\] |
| find-set(1) | path compression: 1 now points to 4 ⇒ 4(1, 2, 3, 8(7)) \[2\] |
| union(7, 6) | find-set(7) compresses 7 under 4; 6 goes under 4 ⇒ 4(1, 2, 3, 6, 7, 8) \[2\] |
| union(3, 5) | 4(1, 2, 3, 5, 6, 7, 8) \[2\]; singletons 9, 10 remain |

**Exam 26 July 2024, Ex. 1** (analysis with disjoint sets): see the chapter on recurrence relations. With union by rank and path compression a sequence of O(n) disjoint-set operations costs O(n α(n)) ≈ Θ(n).

**Class exercise: satisfiability of equality constraints.** Given n variables and constraints of the form x<sub>i</sub> = x<sub>j</sub> and x<sub>i</sub> ≠ x<sub>j</sub>, decide whether they can all be satisfied. Make a set for each variable; for every equality constraint call union(x<sub>i</sub>, x<sub>j</sub>); then for every inequality constraint check that find-set(x<sub>i</sub>) ≠ find-set(x<sub>j</sub>) (otherwise the constraints are contradictory). With m constraints the cost is O((n + m) α(n)).

### 11.5.1 Past exam exercises on this topic

5)  Ex. 4 2022/07/21 F; (E) Ex. 4 2023/06/29; (E) Ex. 4 2023/12/01; (E) Ex. 4 2024/04/24; (E) Ex. 4 2024/06/28; (A) Ex. 1 2024/07/26.

---
> [[AADS 17 - Algorithmic techniques|← Algorithmic techniques]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 19 - Graphs – representation, connected components, minimum spanning trees|Graphs – representation, connected components, minimum spanning trees →]]
