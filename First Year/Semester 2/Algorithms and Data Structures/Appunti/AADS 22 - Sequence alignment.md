---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 22
tags: [note, aads]
---

> [[AADS 21 - String matching|← String matching]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 23 - Suffix data structures|Suffix data structures →]]

# Sequence alignment

**⚠ Non nei topics:** *questo argomento non compare nel programma ufficiale del corso (pagina UniBo A.A. 2026/27, riportata nel vault); è presente nelle slide e negli esami passati.*

*Reference: Durbin et al., “Biological Sequence Analysis”, Ch. 2 and 6; Gusfield, Ch. 11 and 14.*

In bioinformatics, sequence alignment compares biological sequences to identify regions of similarity, which may reflect functional, structural or evolutionary relationships. It lines up two or more sequences allowing **matches**, **mismatches** (substitutions) and **gaps** (insertions/deletions, indels), scored by a scoring scheme.

Classes: **pairwise** (two sequences) vs **multiple** (more than two); **global** (the whole sequences) vs **local** (subsequences).

## 15.1 Global alignment

**Problem.** Given X = x<sub>1</sub> … x<sub>m</sub> and Y = y<sub>1</sub> … y<sub>n</sub> (typically of similar length, hundreds or thousands of residues), return the alignment that maximizes a similarity score (an optimization problem).

A global alignment X’, Y’ inserts gaps (–) in arbitrary positions of X and Y so that (1) \|X’\| = \|Y’\| = k, and (2) there are no gap–gap columns. The score is Σ<sub>i=1..k</sub> σ(x’<sub>i</sub>, y’<sub>i</sub>), e.g. σ = +1 for a match, −1 for a mismatch, −2 for a gap.

*Example:* X = GATCGGCAT, Y = CAATGTGAATC; one alignment of length 12 has 6 matches, 2 mismatches and 4 gaps: score 6·1 + 2·(−1) + 4·(−2) = −4.

**How many alignments?** We consider only “non-boring” alignments: a gap cannot be aligned with a gap, and alignments that differ only in the order of adjacent gaps in the two sequences carry the same information and count as one. Even so, their number grows exponentially (in the order of Σ<sub>k</sub> C(m, k)·C(n, k)), so enumeration is impossible: we use dynamic programming.

### 15.1.1 Needleman–Wunsch (DP for global alignment)

The problem has optimal substructure. Let A\[i, j\] be the score of the best alignment between X\[1..i\] and Y\[1..j\]; the optimum is A\[m, n\].

- A\[0, 0\] = 0; A\[i, 0\] = i·d (i gaps to align ε with X\[1..i\]); A\[0, j\] = j·d.
- A\[i, j\] = max{ A\[i − 1, j − 1\] + σ(x<sub>i</sub>, y<sub>j</sub>) (⇖ x<sub>i</sub> with y<sub>j</sub>), A\[i − 1, j\] + d (↑ x<sub>i</sub> with a gap), A\[i, j − 1\] + d (← y<sub>j</sub> with a gap) },

where σ is the similarity function (match reward / mismatch penalty) and d \< 0 the gap penalty. A path matrix B stores the chosen move (⇖ match/mismatch, ↑ and ← gap, × stop) to rebuild the alignment by following the arrows from (m, n) back to (0, 0). Ties are broken in the order ⇖, ↑, ← (as in the exam solutions).

     1: function GA(String X, String Y, Function σ, Real d) → (Matrix, Matrix)
     2:     m = |X|, n = |Y|
     3:     A[0..m][0..n], B[0..m][0..n]
     4:     A[0, 0] = 0, B[0, 0] = ×
     5:     for i = 1, ⋯, m do A[i, 0] = i·d, B[i, 0] = ↑
     6:     for j = 1, ⋯, n do A[0, j] = j·d, B[0, j] = ←
     7:     for i = 1, ⋯, m do
     8:         for j = 1, ⋯, n do
     9:             match = A[i − 1, j − 1] + σ(X[i], Y[j])
    10:             gapx = A[i − 1, j] + d
    11:             gapy = A[i, j − 1] + d
    12:             A[i, j] = max{match, gapx, gapy}
    13:             B[i, j] = arrow of the maximum (⇖, ↑, ← in this priority)
    14:     return (A, B)

*Example* (slides): X = AAAC, Y = AGC, σ = ±1, d = −2: A\[4, 3\] = −1, e.g. AAAC / –AGC.

## 15.2 Semiglobal alignment

Different problems need different alignments: searching a gene inside a chromosome (the short sequence should align inside the long one, with free gaps at its ends) or finding overlapping reads in a sequencing project (the end of one read overlaps the beginning of the other). With global alignment, X = CAGCACTTGGATTCTCGG and Y = CAGCGTGG have optimal score −12; an alignment placing Y inside X looks much more interesting but scores −19, because of the many end gaps; ignoring the initial and final gaps of Y’ its score would be 3.

**Semiglobal alignment** does not penalize gaps at the beginning and/or at the end of the sequences. Same recurrence as global alignment, different initialization and output:

| Do not penalize gaps at the… | then |
|:---|:---|
| beginning of X | A\[0, j\] = 0 for j = 1..n |
| beginning of Y | A\[i, 0\] = 0 for i = 1..m |
| end of X | best score = max{A\[i, n\] : i = 1..m} (max of the last column) |
| end of Y | best score = max{A\[m, j\] : j = 1..n} (max of the last row) |

There are 2<sup>4</sup> − 1 = 15 semiglobal variants (beginning/end of X/Y, each penalized or not; the 16th combination is the global alignment). Approximate string matching (previous chapter) is a semiglobal problem: free gaps at the beginning and end of S.

**Personal note (GA_penalties): linear-memory semiglobal alignment.** The exam coding exercises (2023/07/24 Ex. 6, 2024/07/26 Ex. 5) ask for the pseudocode computing only the optimal score, and the highest mark goes to implementations using **linear memory**: since row i depends only on row i − 1, a 2 × (n + 1) matrix suffices, indexed by i mod 2.

*Variant 1: no penalty for gaps at both ends of both sequences* (2023/07/24):

     1: function SGA(String X, String Y, Function σ, Real d) → Real
     2:     m = |X|, n = |Y|
     3:     let A[0..1][0..n] be a new matrix          ▷ 2 × n matrix
     5:     for i = 0, 1 do A[i, 0] = 0
     6:     for j = 0, ⋯, n do A[0, j] = 0
     8:     score = 0
     9:     for i = 1, ⋯, m do
    10:         for j = 1, ⋯, n do
    11:             match = A[(i − 1) mod 2, j − 1] + σ(X[i], Y[j])
    12:             gapx = A[i mod 2, j − 1] + d
    13:             gapy = A[(i − 1) mod 2, j] + d
    14:             A[i mod 2, j] = max{match, gapx, gapy}
    15:         score = max(score, A[i mod 2, n])       ▷ best on the last column
    17:     for j = 1, ⋯, n do score = max(score, A[m mod 2, j])   ▷ best on the last row
    18:     return score

*Variant 2: no penalty for gaps at the beginning of both sequences* (2024/07/26): same initialization with zeros, no maximum over the last row/column, return A\[m mod 2, n\].

*Variant 3: no penalty for gaps at the end of both sequences:* initialize A\[0, j\] = j·d and the first column with i·d, keep the maximum of the last column during the loop (maxi) and of the last row at the end (maxj), return max{maxi, maxj}. Careful: in the 2-row version the column-0 value must be set at every row, A\[i mod 2, 0\] = i·d, inside the loop over i.

<figure>
![[AADS-rId201.jpg|475]]
<figcaption aria-hidden="true"><p>Original note: the three linear-memory variants</p></figcaption>
</figure>

<figure>
![[AADS-rId204.jpg|475]]
<figcaption aria-hidden="true"><p>Variant 2</p></figcaption>
</figure>

<figure>
![[AADS-rId207.jpg|475]]
<figcaption aria-hidden="true"><p>Variant 3</p></figcaption>
</figure>

## 15.3 Local alignment (Smith–Waterman)

**Problem.** Given X and Y, find the optimal alignment between a substring X\* of X and a substring Y\* of Y. It generalizes semiglobal alignment. Goal: find local regions of highest similarity (e.g. conserved domains). Local alignment suits low-similarity sequences (or sequences of different length sharing only a conserved region); global alignment suits high-similarity sequences of comparable length. *Example:* X = CGTCCGAAGGGATGA, Y = TCCGAATTAG: the local alignment isolates TCCGAA.

A\[i, j\] = score of the best alignment between a suffix of X\[1..i\] and a suffix of Y\[1..j\]:

- A\[i, 0\] = A\[0, j\] = 0 (gaps at the beginning are not penalized);
- A\[i, j\] = max{ A\[i − 1, j − 1\] + σ(x<sub>i</sub>, y<sub>j</sub>), A\[i − 1, j\] + d, A\[i, j − 1\] + d, **0** };
- the optimal score is **max<sub>i,j</sub> A\[i, j\]** (gaps at the end are not penalized); trace back from that cell and **stop at a 0** (×): when the local score would become negative we restart.

Local alignments emerge only with negative mismatch and gap penalties (otherwise the whole sequences always win).

*Example* (slides): X = TGCA, Y = AGC, σ = ±1, d = −2: max A = A\[3, 3\] = 2, local alignment GC / GC.

**Remarks.** Global alignment: Needleman–Wunsch (1970), one of the first applications of DP to protein sequences (cubic in its original formulation). Local alignment: Smith–Waterman (1981). Both cost **Θ(mn) time and space**. Optimizations: O(mn/log<sup>2</sup> n) time (“four Russians”), O(m + n) space (divide and conquer, Hirschberg). A quasi-quadratic cost is still too high for database searches, where heuristics (BLAST, FASTA) are used; NW and SW are used when high-quality alignments are needed. The short notes: global alignment aligns the *entire* sequences from start to end; local alignment aligns the *best-matching substrings*, allowing a “restart at 0”.

## 15.4 Scoring: substitution matrices and gap penalties

**Substitution matrix.** The scoring must reflect biological similarity. Protein sequences: standard matrices **PAM** and **BLOSUM** (a different likelihood score for every pair of amino acids). Genomic sequences: different reward/penalty ratios depending on conservation: 1/−1 for ~75% conserved sequences, 1/−2 for ~95%, 1/−3 for highly conserved (~99%).

**Gap penalty.** Needed to avoid useless gaps. Interpretation: in spell checking a gap is a misspelling (discourage large gaps); in biology a gap is a mutation (indel), and one long indel is more likely than many short ones (discourage many short gaps). There is no universally best model.

- **Constant:** d for every gap, whatever its length. Favors large gaps (a long gap costs as much as a short one): not reasonable in practice.
- **Linear:** L·d for a gap of length L. Favors short gaps but discourages too many gaps: the model used so far, not the best for biological sequences.
- **Affine:** d<sub>o</sub> + L·d<sub>e</sub> (opening penalty d<sub>o</sub>, extension penalty d<sub>e</sub>, with \|d<sub>e</sub>\| \< \|d<sub>o</sub>\|): opening a gap is expensive, extending it is cheap. Good compromise.
- **Convex** (e.g. logarithmic in L): each extra position costs less than the previous one; a good model for biology.

Any general gap function can be handled by DP in O(mn(m + n)); convex gaps in O(mn log(m + n)) (not easy); **affine gaps cost no more than linear ones: O(mn)**.

**Global alignment with affine gaps (Gotoh, 1982).** For each (i, j) we must remember whether a gap is open, so A is split into three matrices:

- M\[i, j\]: best score of X\[1..i\] vs Y\[1..j\] with x<sub>i</sub> aligned to y<sub>j</sub>;
- X\[i, j\]: best score with y<sub>j</sub> aligned to a gap after x<sub>i</sub> (gap in X);
- Y\[i, j\]: best score with x<sub>i</sub> aligned to a gap (gap in Y).

M\[i, j\] = σ(x<sub>i</sub>, y<sub>j</sub>) + max{M\[i − 1, j − 1\], X\[i − 1, j − 1\], Y\[i − 1, j − 1\]}; X\[i, j\] = max{M\[i, j − 1\] + d<sub>o</sub> + d<sub>e</sub>, X\[i, j − 1\] + d<sub>e</sub>, Y\[i, j − 1\] + d<sub>o</sub> + d<sub>e</sub>}; Y\[i, j\] = max{M\[i − 1, j\] + d<sub>o</sub> + d<sub>e</sub>, Y\[i − 1, j\] + d<sub>e</sub>, X\[i − 1, j\] + d<sub>o</sub> + d<sub>e</sub>}; optimal score max{M\[m, n\], X\[m, n\], Y\[m, n\]}. Three matrices instead of one: still Θ(mn).

*Linear vs affine example:* X = GGACTTTTCA, Y = GGACTATATATCA, σ = ±1. With linear d = −2 the optimal alignment scatters many single gaps (intuitively not good); with affine d<sub>o</sub> = −2, d<sub>e</sub> = −1 the gaps are grouped into a few longer ones, which is biologically more realistic.

## 15.5 Multiple sequence alignment (MSA)

**Problem.** Given m \> 1 sequences X<sub>1</sub>, …, X<sub>m</sub> of similar length, return the best alignment among all of them: gaps are inserted so that all sequences have the same length n ≥ max\|X<sub>i</sub>\|, and no column contains only gaps. It generalizes global alignment (m = 2) and highlights conserved positions across a family of sequences. An objective function is needed; the usual one is the **sum-of-pairs (SP) score**: for each column, the sum of σ over all pairs of sequences (gap–gap counts 0), summed over the columns.

**DP for MSA.** The global DP extends to m sequences: with m sequences of length n the score matrix has (n + 1)<sup>m</sup> cells. For m = 3, A\[i, j, k\] is the maximum over the 2<sup>3</sup> − 1 = 7 combinations of advancing or not on each sequence (A\[i − 1, j − 1, k − 1\] + SP(x<sub>i</sub>, y<sub>j</sub>, z<sub>k</sub>), A\[i, j − 1, k − 1\] + SP(–, y<sub>j</sub>, z<sub>k</sub>), …). Each cell considers 2<sup>m</sup> − 1 predecessors and computes an SP score of O(m<sup>2</sup>): **O(m<sup>2</sup> 2<sup>m</sup> n<sup>m</sup>)**, exponential in m.

**Complexity.** MSA with SP score is **NP-hard**: the decision version (is there an MSA with SP score ≥ k?) is in NP (an alignment can be checked in polynomial time) and is NP-complete by reduction from known NP-complete problems (e.g. independent set).

**Star alignment heuristic.** (1) Choose a center sequence X<sub>c</sub>; (2) compute the m − 1 global alignments between X<sub>c</sub> and every other X<sub>i</sub>; (3) merge them into a multiple alignment, following the rule “once a gap, always a gap”: gaps inserted in the center in one pairwise alignment are propagated to all the other sequences. To choose the center, compute all m(m − 1)/2 pairwise global alignments and take the sequence maximizing the sum of its scores against all the others. Cost: O(m<sup>2</sup>n<sup>2</sup>) for the pairwise alignments, plus the merge. Not optimal, but with some provable properties (under suitable scores its SP score is within a factor 2 of the optimum).

*Slides example:* five sequences, σ = ±1, d = −2; the table of the 10 pairwise scores gives sums 2 (X<sub>1</sub>), 1 (X<sub>2</sub>), −11 (X<sub>3</sub>), −3 (X<sub>4</sub>), −17 (X<sub>5</sub>): X<sub>1</sub> is the center.

**Other approaches.** Exact and efficient MSA is still open; most practical tools use **progressive alignment**: build a guide tree, align the closest sequences first and progressively add more distant ones (requires guide-tree construction and the extension of global alignment from sequences to alignments/profiles).

## 15.6 Exam exercises on sequence alignment

**Exam 1 July 2026, Ex. 5: X = PLANET, Y = PLATE, σ = ±1, d = −2.**

1)  Global alignment (rows X, columns Y):

| A   |     | P   | L   | A   | T   | E   |
|-----|:----|:----|:----|:----|:----|:----|
|     | 0   | −2  | −4  | −6  | −8  | −10 |
| P   | −2  | 1   | −1  | −3  | −5  | −7  |
| L   | −4  | −1  | 2   | 0   | −2  | −4  |
| A   | −6  | −3  | 0   | 3   | 1   | −1  |
| N   | −8  | −5  | −2  | 1   | 2   | 0   |
| E   | −10 | −7  | −4  | −1  | 0   | 3   |
| T   | −12 | −9  | −6  | −3  | 0   | 1   |

| B   |     | P   | L   | A   | T   | E   |
|-----|:----|:----|:----|:----|:----|:----|
|     | ×   | ←   | ←   | ←   | ←   | ←   |
| P   | ↑   | ⇖   | ←   | ←   | ←   | ←   |
| L   | ↑   | ↑   | ⇖   | ←   | ←   | ←   |
| A   | ↑   | ↑   | ↑   | ⇖   | ←   | ←   |
| N   | ↑   | ↑   | ↑   | ↑   | ⇖   | ⇖   |
| E   | ↑   | ↑   | ↑   | ↑   | ⇖   | ⇖   |
| T   | ↑   | ↑   | ↑   | ↑   | ⇖   | ↑   |

Optimal global score A\[6, 5\] = **1**: X’ = PLANET, Y’ = PLATE– (3 matches, N/T mismatch, E/E match, T/gap: 3 − 1 + 1 − 2 = 1).

2)  Local alignment:

| A   |     | P   | L   | A   | T   | E   |
|-----|:----|:----|:----|:----|:----|:----|
|     | 0   | 0   | 0   | 0   | 0   | 0   |
| P   | 0   | 1   | 0   | 0   | 0   | 0   |
| L   | 0   | 0   | 2   | 0   | 0   | 0   |
| A   | 0   | 0   | 0   | 3   | 1   | 0   |
| N   | 0   | 0   | 0   | 1   | 2   | 0   |
| E   | 0   | 0   | 0   | 0   | 0   | 3   |
| T   | 0   | 0   | 0   | 0   | 1   | 1   |

| B   |     | P   | L   | A   | T   | E   |
|-----|:----|:----|:----|:----|:----|:----|
|     | ×   | ×   | ×   | ×   | ×   | ×   |
| P   | ×   | ⇖   | ×   | ×   | ×   | ×   |
| L   | ×   | ×   | ⇖   | ×   | ×   | ×   |
| A   | ×   | ×   | ×   | ⇖   | ←   | ×   |
| N   | ×   | ×   | ×   | ↑   | ⇖   | ×   |
| E   | ×   | ×   | ×   | ×   | ×   | ⇖   |
| T   | ×   | ×   | ×   | ×   | ⇖   | ↑   |

Maximum score **3**, reached twice: PLA / PLA (from A\[3, 3\]) and PLANE / PLATE (from A\[5, 5\]).

**Exam 15 January 2024, Ex. 5: star alignment of X<sub>1</sub> = TTACA, X<sub>2</sub> = AGA, X<sub>3</sub> = CTGA** (σ = ±1, d = −2).

1)  Pairwise global alignments: X<sub>1</sub>/X<sub>2</sub> score −3 (TTACA / ––AGA); X<sub>1</sub>/X<sub>3</sub> score −2 (TTACA / CT–GA); X<sub>2</sub>/X<sub>3</sub> score −1 (–AGA / CTGA).

2)  Sums: X<sub>1</sub>: −3 − 2 = −5; X<sub>2</sub>: −3 − 1 = −4; X<sub>3</sub>: −2 − 1 = −3 ⇒ the center is **X<sub>3</sub>**.

3)  Merge: X<sub>3</sub> received a gap in its alignment with X<sub>1</sub> (CT–GA), so that gap is propagated into X<sub>2</sub> (–AGA becomes –A–GA):

<!-- -->

    X3   C T - G A
    X1   T T A C A
    X2   - A - G A

SP score by column (gap–gap = 0): (C, T, –) = −1 − 2 − 2 = −5; (T, T, A) = 1 − 1 − 1 = −1; (–, A, –) = −2 + 0 − 2 = −4; (G, C, G) = −1 + 1 − 1 = −1; (A, A, A) = 3. **SP score = −8.**

### 15.6.1 Past exam exercises on this topic

5)  Ex. 5 2022/06/24 F; (E) Ex. 5 2022/07/21 F; (E) Ex. 5 2022/10/28; (E) Ex. 6 2023/02/06 F; (E) Ex. 5 2023/06/29; (C) Ex. 6 2023/07/24 F; (E) Ex. 5 2024/01/15; (C) Ex. 5 2024/07/26; (E) Ex. 6 2024/11/15; (E) Ex. 5 2026/07/01.

---
> [[AADS 21 - String matching|← String matching]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 23 - Suffix data structures|Suffix data structures →]]
