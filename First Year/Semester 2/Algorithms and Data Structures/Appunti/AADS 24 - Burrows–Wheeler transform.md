---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 24
tags: [note, aads]
---

> [[AADS 23 - Suffix data structures|← Suffix data structures]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 25 - Sequence assembly|Sequence assembly →]]

# Burrows–Wheeler transform

**⚠ Non nei topics:** *questo argomento non compare nel programma ufficiale del corso (pagina UniBo A.A. 2026/27, riportata nel vault); è presente nelle slide e negli esami passati.*

*Reference: Burrows and Wheeler (1994); Ferragina and Manzini (2000); Langmead’s lecture notes.*

## 17.1 Motivation

String matching on biological sequences must be efficient in **time** (searches are repeated many times) and in **memory** (sequences are huge). A suffix array needs at least n log(n\|Σ\|) bits: n log n bits for the n indices plus n log \|Σ\| bits for S. For the human genome (about 6.1·10<sup>9</sup> bp with the two strands) this is tens of gigabytes. The BWT allows indices that are both compressed and searchable.

## 17.2 Definition

The **Burrows–Wheeler Transform** maps a string S to another string BWT(S) of the **same length** that is easier to compress. It is not a compression algorithm itself: it reorders the characters so that equal characters tend to appear in runs, which compress well (e.g. a<sup>m</sup>b<sup>n</sup> can be stored as (a, m, b, n) instead of m + n characters, run-length encoding). If S has many repeated substrings, BWT(S) has many runs of repeated characters.

**Computing BWT(S)** (naive algorithm):

1.  append the terminator: S = S\$, where \$ ∉ Σ is smaller than every character (it appears only once);
2.  build the matrix M of all the cyclic rotations of S (n × n, Θ(n<sup>2</sup>));
3.  sort the rows of M lexicographically (O(n<sup>2</sup> log n) with comparisons, Θ(n<sup>2</sup>) with radix sort);
4.  **BWT(S) is the last column L of M.**

<!-- -->

    1: function BWT(String S) → String
    2:     let B be an empty matrix
    3:     for i = 0, ⋯, n − 1 do
    4:         B[i + 1] = S[i + 1..n] · S[1..i]      ▷ i-th cyclic rotation
    5:     sort lexicographically the rows of B
    6:     return the last column of B

*Example:* S = BANANA\$. Sorted rotations: \$BANANA, A\$BANAN, ANA\$BAN, ANANA\$B, BANANA\$, NA\$BANA, NANA\$BA. First column F = \$AAABNN, last column **L = BWT(S) = ANNB\$AA**.

**BWT and suffix array.** Sorting the rotations of S\$ is the same as sorting its suffixes, so BWT\[i\] = S\[SA\[i\] − 1\] if SA\[i\] \> 1, and \$ if SA\[i\] = 1 (the character preceding the i-th smallest suffix). For BANANA\$, SA = \[7, 6, 4, 2, 1, 5, 3\] gives BWT = S\[6\] S\[5\] S\[3\] S\[1\] \$ S\[4\] S\[2\] = A N N B \$ A A. Hence the BWT can be computed in Θ(n) through a suffix array built from a suffix tree.

## 17.3 Inverse transform

The BWT is **reversible** (otherwise lossless compression would be impossible).

**Naive inversion:** start from an empty matrix B and repeat n times: prepend L as a new first column, then sort the rows lexicographically. After n steps B is the sorted rotation matrix, and S is the row ending with \$. Cost O(n<sup>3</sup> log n) time (O(n<sup>3</sup>) with radix sort), Θ(n<sup>2</sup>) memory; BWT(S) naively costs O(n<sup>2</sup> log n) (Θ(n<sup>2</sup>) with radix sort) and Θ(n<sup>2</sup>) memory. Both can be done in Θ(n) time and space without building the matrices.

**LF property.** The i-th occurrence of a character c in the last column L corresponds to the i-th occurrence of c in the first column F (they are the same character of S). Reason: the rows starting with c are sorted by what follows c, and the rows ending with c are sorted by the same strings.

**LF mapping.** LF\[i\] = the position in F of the character L\[i\]. It can be computed in Θ(n + \|Σ\|) without the matrix: let C(c) be the number of characters of S smaller than c, and P(k) the number of occurrences of L\[k\] in L\[1..k\] (its rank); then **LF\[k\] = C(L\[k\]) + P(k)**. F is just the characters of S sorted.

*Example* S = BANANA\$: L = ANNB\$AA, F = \$AAABNN, C(\$) = 0, C(A) = 1, C(B) = 4, C(N) = 5, LF = \[2, 6, 7, 5, 1, 3, 4\].

**Inverse with LF in Θ(n):** row 1 starts with \$, so L\[1\] is the last character of S before \$. Follow k = LF\[k\] from k = 1, reading L\[k\], until L\[k\] = \$; the characters read are S in reverse order.

     1: function INV-BWT(String L, int LF[1, ⋯, n]) → String
     2:     S[1..n]                         ▷ the inverted string
     3:     S[n] = $
     4:     i = n − 1
     5:     k = 1
     6:     while L[k] ≠ $ do
     7:         S[i] = L[k]
     8:         k = LF[k]
     9:         i = i − 1
    10:     return S

*Example:* L = ANNB\$AA, LF = \[2, 6, 7, 5, 1, 3, 4\]: k = 1 → 2 → 6 → 3 → 7 → 4 → 5 (stop, L\[5\] = \$); reading L: A, N, A, N, A, B; reversed with \$ at the end: BANANA\$.

## 17.4 Exact string matching with the BWT (backward search)

The LF mapping allows searching P in S in time linear in m, proceeding **backwards** on P. The rows of M starting with a given string form a contiguous range \[first, last\]. Start with the range of the rows starting with P\[m\]: first = C(P\[m\]) + 1, last = C(next character after P\[m\]). Then for i = m − 1 down to 1, keep only the rows of the range whose L character is P\[i\] and map them through LF: they become the rows starting with P\[i..m\].

     1: function BWT-ESM(String P, String L, int LF[1, ⋯, n], Function C) → int
     2:     m = |P|
     3:     i = m − 1
     4:     c = P[m]
     5:     first = C(c) + 1
     6:     last = C(c + 1)                 ▷ C of the next character in the alphabet
     7:     while first ≤ last and i ≥ 1 do
     8:         c = P[i]
     9:         i = i − 1
    10:         first = min{LF[k] | L[k] = c, first ≤ k ≤ last}
    11:         last = max{LF[k] | L[k] = c, first ≤ k ≤ last}
    12:     if last < first then return 0
    14:     else return last − first + 1

*Example:* P = ANA in S = BANANA\$ (L = ANNB\$AA, LF = \[2, 6, 7, 5, 1, 3, 4\]). Start with c = A: first = C(A) + 1 = 2, last = C(B) = 4. c = N: the N’s in L\[2..4\] are at k = 2, 3, with LF 6, 7 ⇒ \[6, 7\]. c = A: the A’s in L\[6..7\] are at k = 6, 7, with LF 3, 4 ⇒ \[3, 4\]. Result: 4 − 3 + 1 = **2 occurrences**.

With the FM-index (rank counts stored at sampled positions), each step costs O(1) and the search costs **O(m)** after an O(n) preprocessing: total O(n + m), on a compressed index.

| Approach     | Preprocessing    | ESM counting | Total                |
|:-------------|:-----------------|:-------------|:---------------------|
| Brute force  | –                | O(mn)        | O(mn)                |
| KMP          | Θ(m)             | Θ(n)         | Θ(m + n)             |
| DP           | –                | Θ(mn)        | Θ(mn)                |
| Suffix trie  | O(n<sup>2</sup>) | O(m)         | O(n<sup>2</sup> + m) |
| Suffix tree  | O(n)             | O(m)         | O(n + m)             |
| Suffix array | O(n)             | O(m log n)   | O(n + m log n)       |
| BWT          | O(n)             | O(m)         | O(n + m)             |

**Concluding remarks.** Approximate matching can also be done on the BWT, and searches can run directly on the compressed string. The **FM-index** (Ferragina and Manzini, 2000) is a BWT-based structure that compresses the input string while still supporting fast substring queries; it is the core of read aligners such as Bowtie and BWA, and allows storing a human genome index in about 3 GB.

From the short notes: the BWT appends a unique smallest \$, lists all cyclic rotations, sorts them, and takes the last character of each; the output groups similar characters into runs, which compress well.

## 17.5 Exam exercises on the BWT

**Exam 1 July 2026, Ex. 6.**

1)  BWT of BONOBO\$. Rotations: BONOBO\$, ONOBO\$B, NOBO\$BO, OBO\$BON, BO\$BONO, O\$BONOB, \$BONOBO. Sorted:

| \#  | Sorted rotation | F   | L   | LF  |
|:----|:----------------|:----|:----|:----|
| 1   | \$BONOBO        | \$  | O   | 5   |
| 2   | BO\$BONO        | B   | O   | 6   |
| 3   | BONOBO\$        | B   | \$  | 1   |
| 4   | NOBO\$BO        | N   | O   | 7   |
| 5   | O\$BONOB        | O   | B   | 2   |
| 6   | OBO\$BON        | O   | N   | 4   |
| 7   | ONOBO\$B        | O   | B   | 3   |

**BWT(BONOBO\$) = OO\$OBNB**, LF = \[5, 6, 1, 7, 2, 4, 3\] (C(\$) = 0, C(B) = 1, C(N) = 3, C(O) = 4; e.g. L\[4\] is the third O ⇒ LF\[4\] = 4 + 3 = 7).

2)  Inverse of OKO\$COCTA. F = sorted characters = \$ACCKOOOT; C(\$) = 0, C(A) = 1, C(C) = 2, C(K) = 4, C(O) = 5, C(T) = 8.

| k   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
| F   | \$  | A   | C   | C   | K   | O   | O   | O   | T   |
| L   | O   | K   | O   | \$  | C   | O   | C   | T   | A   |
| LF  | 6   | 5   | 7   | 1   | 3   | 8   | 4   | 9   | 2   |

From k = 1: 1 → 6 → 8 → 9 → 2 → 5 → 3 → 7 → 4 (L\[4\] = \$, stop). Reading L: O, O, T, A, K, C, O, C. Reversed, with \$ appended: **BWT<sup>−1</sup>(OKO\$COCTA) = COCKATOO\$**.

**Typical requests:** compute BWT(S) through the sorted rotations; compute F and LF (with C and the ranks); invert a BWT with LF; run backward search for a pattern showing \[first, last\] at each step.

### 17.5.1 Past exam exercises on this topic

5)  Ex. 6 2022/06/24 F; (E) Ex. 6 2022/07/21; (E) Ex. 6 2022/10/28 F; (E) Ex. 6 2022/11/30 F; (E) Ex. 6 2023/01/16; (E) Ex. 6 2023/10/27; (E) Ex. 6 2024/02/12; (E) Ex. 6 2024/07/26; (E) Ex. 6 2024/12/16; (E) Ex. 6 2026/07/01.

---
> [[AADS 23 - Suffix data structures|← Suffix data structures]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 25 - Sequence assembly|Sequence assembly →]]
