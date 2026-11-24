---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 23
tags: [note, aads]
---

> [[AADS 22 - Sequence alignment|← Sequence alignment]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 24 - Burrows–Wheeler transform|Burrows–Wheeler transform →]]

# Suffix data structures

**⚠ Non nei topics:** *questo argomento non compare nel programma ufficiale del corso (pagina UniBo A.A. 2026/27, riportata nel vault); è presente nelle slide e negli esami passati.*

*Reference: Gusfield, “Algorithms on Strings, Trees and Sequences”, Ch. 5–7; Langmead’s lecture notes.*

Dynamic programming is versatile for string comparison but costs quadratic time: acceptable for a few comparisons, not for many searches. In bioinformatics we often store a long, known, fixed string S (a genome, a protein database) and run many queries on it. It pays to **preprocess S once** into a data structure (an **index**) that makes queries faster than DP and uses little memory. Typical queries, for a pattern P much smaller than S: is P a substring of S (ESM decision)? how many times does P occur (counting)? is P a suffix of S? what is the longest common substring of P and S? what is the longest repeated substring of S?

Key observation: **every substring of S is a prefix of some suffix of S**. Index all suffixes S\[i..n\] and substring problems become prefix problems.

## 16.1 Suffix tries

(Fredkin, Thue, de la Briandais, around 1960.) Let Σ be a finite alphabet and S = S’\$ with S’ ∈ Σ\* and \$ ∉ Σ a terminator that does not appear in the alphabet (it marks where a suffix ends; it is lexicographically smaller than every character). The **suffix trie** SuffTrie(S) is a tree such that: each edge is labeled with a character; edges leading to leaves are labeled \$; every path from the root to a leaf spells a suffix of S, and every suffix corresponds to exactly one such path; the edges leaving a node have distinct labels. Only non-empty suffixes are considered. Example: S = abaaba\$.

**Queries (with the trie already built), m = \|P\|, n = \|S\|:**

- *ESM decision:* follow the path of P from the root: if all the characters of P are consumed the answer is yes; if some character has no matching edge, no. Cost O(m) with an array of \|Σ\| + 1 child pointers per node, O(\|Σ\|m) with a first-child/next-sibling representation. (Compare BF O(mn), KMP O(m + n), DP Θ(mn).)
- *Counting:* follow P and count the leaves of the subtree below the end of the path: O(N) with N the number of nodes, O(m) if each node stores its number of leaves.
- *Is P a suffix of S?* Yes iff the P-path ends at a node with a \$-child (leading to a leaf).
- *Approximate matching with edit distance ≤ k:* Ukkonen’s algorithm, about O(mk), much better than quadratic DP.
- *Longest repeated substring:* the deepest node with at least two leaves below it.

**Suffix links.** A suffix link connects the node representing a string aw (a ∈ Σ, w ∈ Σ\*) to the node representing w (one character less): e.g. the node for “BAN” links to the node for “AN”. Every node represents a prefix of some suffixes and has a suffix link to another node; the suffix link of a leaf (a suffix) always points to another leaf (the next shorter suffix).

*Longest common substring between P and S:* walk down the trie following P; when no edge matches P\[i\], save the current node u and continue matching P\[i + 1\] from u’s suffix link (“backtracking” without restarting from the root); when P is consumed, the longest common substring is the deepest saved node. Cost O(m) (DP would cost O(mn)).

**Construction.** Scan S left to right: SuffTrie(S\[1..i\]) is obtained from SuffTrie(S\[1..i−1\]) by appending S\[i\] to all its suffixes, which is done by following suffix links. Let CurrentSuffix be the node of the longest suffix S\[1..i−1\]; repeat until CurrentSuffix is the root or already has an edge labeled S\[i\]: (1) add a child labeled S\[i\] to CurrentSuffix; (2) CurrentSuffix = CurrentSuffix.suffixlink. The new suffix links are set while adding the new nodes. Example: with S = abbacabaa, from SuffTrie(abba) we add c to abba, bba, ba, a and the root, obtaining the suffixes abbac, bbac, bac, ac, c.

**Size.** A suffix trie can have **Θ(n<sup>2</sup>) nodes**, and building it costs O(n<sup>2</sup>). Example: S = a<sup>n/2</sup>b<sup>n/2</sup>: the root, one path of n/2 nodes labeled a, and n/2 + 1 paths labeled with b’s, each with n/2 nodes: 1 + n/2 + (n/2 + 1)(n/2) = Θ(n<sup>2</sup>).

## 16.2 Suffix trees

(McCreight, 1976.) A **suffix tree** is a compressed suffix trie: paths without branches (chains of single-child nodes) are merged into a single edge, and each edge label is stored as a range i:j of S (the substring S\[i..j\]) instead of the characters. Example: in the suffix tree of abaaba\$ the edge labels are ranges such as 7:7 (\$), 5:6, 4:7. Queries follow the edges character by character as before, in O(\|query\|) time regardless of the size of S.

**Space Θ(n):** there are n leaves (one per suffix); each internal node has at least 2 children, so there are fewer than n internal nodes and O(n) edges; each edge stores a range in O(1) space (assuming indices take O(1) words). **Construction Θ(n):** Ukkonen’s algorithm (1995), similar to the trie construction with suffix links plus optimizations. Drawback: the hidden constant is large (many pointers per node), so suffix trees take a lot of memory in practice.

From the short notes: in a suffix trie pattern P occurs in T iff we can follow P from the root, but memory is large; the suffix tree compresses single-child paths into edges labeled by (start, end) indices and still represents all suffixes as root-to-leaf paths; suffix links make linear-time (Ukkonen-style) construction possible, avoiding re-walking from the root after each extension.

## 16.3 Suffix arrays

(Manber and Myers, 1990.) The **suffix array** SA of S is the array of the starting positions of all suffixes of S, **sorted lexicographically**. Memory Θ(n) like suffix trees, but with a much smaller constant: we store only S and an array of n indices.

*Example:* S = cattcat\$ has suffixes 1 cattcat\$, 2 attcat\$, 3 ttcat\$, 4 tcat\$, 5 cat\$, 6 at\$, 7 t\$, 8 \$. Sorted: \$, at\$, attcat\$, cat\$, cattcat\$, t\$, tcat\$, ttcat\$, so **SA = \[8, 6, 2, 5, 1, 7, 4, 3\]**.

**Construction.**

- Naive: sort the n suffixes with an optimal comparison sort, Θ(n log n) comparisons, each costing O(n) ⇒ O(n<sup>2</sup> log n).
- With RadixSort (suffixes as keys of at most n characters over Σ): O(n(n + \|Σ\|)), quadratic when \|Σ\| is small with respect to n (typical for nucleotide sequences).
- **Linear time Θ(n)** from a suffix tree: build it with Ukkonen’s algorithm with the edges leaving each node sorted by label and the leaves labeled with the starting index of their suffix, then output the leaf labels with an in-order (left-to-right) visit: Θ(n) + Θ(n). (Direct linear-time algorithms also exist.)

**ESM on suffix arrays.** All suffixes starting with P are **contiguous** in SA. Binary search for the first and the last suffix starting with P, as in a binary search over numbers but comparing strings lexicographically (⪯ instead of ≤): an arithmetic comparison costs O(1), a lexicographic comparison O(min(\|X\|, \|Y\|)) = O(m). Hence **O(m log n)**: O(log n) comparisons of O(m) each. The number of occurrences is the distance between the two positions found. *Example:* searching P = tcat in cattcat\$: the binary search over SA converges on position 7 of SA, the suffix starting at 4 (tcat\$): one occurrence.

## 16.4 Summary: exact string matching

| Approach | Preprocessing | Memory | ESM counting (worst case) | Total |
|:---|:---|:---|:---|:---|
| Brute force | – | – | O(mn) | O(mn) |
| KMP | Θ(m) | Θ(m) | Θ(n) | Θ(m + n) |
| DP (ASM) | – | Θ(mn) | Θ(mn) | Θ(mn) |
| Suffix trie | O(n<sup>2</sup>) | O(n<sup>2</sup>) | O(m) | O(n<sup>2</sup> + m) |
| Suffix tree | Θ(n) | Θ(n) | O(m) | O(n + m) |
| Suffix array | Θ(n) (via suffix tree) | Θ(n) | O(m log n) | O(n + m log n) |

With an index the preprocessing is paid once, and each new query costs only O(m) or O(m log n), independently of n (or almost). Suffix trees are the fastest; suffix arrays are the most memory-efficient.

## 16.5 Exam exercises on suffix data structures

**Exam 28 June 2024, Ex. 5: S = AAACCC\$.** Suffix trie: from the root, edges \$, A, C; the A-branch continues with A (then A–C–C–C–\$ and C–C–C–\$) and C–C–C–\$; the C-branch with \$ and C (then \$ and C–\$). Suffix links for the leaves connect each suffix leaf to the leaf of the next shorter suffix (AAACCC\$ → AACCC\$ → ACCC\$ → CCC\$ → CC\$ → C\$ → \$). Suffix tree (unary paths compressed):

    root ─ $ ─────────────── 7
         ├ A ─┬ A ─┬ ACCC$ ── 1
         │    │    └ CCC$ ─── 2
         │    └ CCC$ ──────── 3
         └ C ─┬ $ ─────────── 6
              └ C ─┬ $ ────── 5
                   └ C$ ───── 4

Suffix array: sorted suffixes \$ (7), AAACCC\$ (1), AACCC\$ (2), ACCC\$ (3), C\$ (6), CC\$ (5), CCC\$ (4): **SA = \[7, 1, 2, 3, 6, 5, 4\]**.

**Exam 16 December 2024, Ex. 5: S = AAAAAA\$.** Every node on the A-path has two children (A and \$), so there are no unary paths to compress: **the suffix trie and the suffix tree coincide**. The root has children \$ (suffix 7) and A; each node A<sup>k</sup> (k = 1..5) has children \$ (suffix 7 − k) and A; the node A<sup>6</sup> has only the \$ child (suffix 1). Suffix links of the leaves: A<sup>k</sup>\$ → A<sup>k−1</sup>\$. Suffix array: \$ (7), A\$ (6), AA\$ (5), AAA\$ (4), AAAA\$ (3), AAAAA\$ (2), AAAAAA\$ (1): **SA = \[7, 6, 5, 4, 3, 2, 1\]**.

**Exam 15 December 2025, Ex. 1:** complexity of calling ESM on the m prefixes of P with a suffix trie (O(n<sup>2</sup> + m<sup>2</sup>)) or a suffix array (O(n + m<sup>2</sup> log n)); see the recurrence relations chapter.

### 16.5.1 Past exam exercises on this topic

5)  Ex. 6 2023/01/16; (E) Ex. 6 2024/01/15; (E) Ex. 5 2024/02/12; (E) Ex. 6 2024/04/24; (E) Ex. 5 2024/06/28; (E) Ex. 5 2024/12/16.

---
> [[AADS 22 - Sequence alignment|← Sequence alignment]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 24 - Burrows–Wheeler transform|Burrows–Wheeler transform →]]
