---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 21
tags: [note, aads]
---

> [[AADS 20 - Hard problems – P, NP, NP-complete, NP-hard|← Hard problems – P, NP, NP-complete, NP-hard]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 22 - Sequence alignment|Sequence alignment →]]

# String matching

**⚠ Non nei topics:** *questo argomento non compare nel programma ufficiale del corso (pagina UniBo A.A. 2026/27, riportata nel vault); è presente nelle slide e negli esami passati.*

*Reference: CLRS Ch. 32 (exact matching); Gusfield, “Algorithms on Strings, Trees and Sequences” (approximate matching).*

String matching is the problem of searching a pattern in a string; it is central in many fields (text editors, search engines, bioinformatics). Two classes: **Exact String Matching (ESM)**, where every character must match, and **Approximate String Matching (ASM)**, where P may appear “more or less” in S, with errors (useful for DNA/RNA/protein sequences, where mutations and sequencing errors happen).

**Notation.** S = s<sub>1</sub> … s<sub>n</sub>; \|S\| = n; S\[i\] = s<sub>i</sub>; S\[i..j\] = s<sub>i</sub> … s<sub>j</sub> (1 ≤ i ≤ j ≤ n); ε is the empty string (S\[k\] = ε for k ∉ \[1, n\]). Strings are **1-based**. m = \|P\|, n = \|S\|, and normally m ≪ n.

## 14.1 Exact string matching

Related problems: *decision* (is P in S?), *counting* (number of occurrences), *search* (first or all occurrences). We solve the counting problem; the others need small modifications. Example: P = ACGTACT, S = ACGGTACGTACGTACT ⇒ count = 1.

### 14.1.1 Brute force

Slide P over S and compare all characters.

     1: function BF-ESM(String P, String S) → int
     2:     m = |P|, n = |S|
     3:     k = 0                               ▷ number of matches
     4:     for j = 0, ⋯, n − m do              ▷ n − m + 1 positions
     5:         i = 1
     6:         while i ≤ m and P[i] == S[j + i] do
     7:             i = i + 1
     8:         if i == m + 1 then
     9:             k = k + 1
    10:     return k

The for loop runs n − m + 1 times, the while loop O(m): **worst case O(m(n − m + 1)) = O(mn)**. The bound is tight: with P = A<sup>m−1</sup>C and S = A<sup>n</sup> (k = 0), or P = A<sup>m</sup> and S = A<sup>n</sup> (k = n − m + 1), BF checks exactly m(n − m + 1) pairs. Lower bound Ω(n + km), with k the number of occurrences (each full match costs Θ(m)).

### 14.1.2 Knuth–Morris–Pratt (1977)

Brute force forgets everything when it moves to the next position and goes back and forth on S. KMP remembers previous matches and mismatches, so it **never goes backwards on S**: after a mismatch, the pattern itself tells where the next comparison should start. Example: P = ACGTACT on S = ACGGTACGTACGTACT; after matching ACGTAC and failing on T, we know the last AC matched, and AC is also a prefix of P, so we continue comparing P\[3\] with the current character of S. Upon a mismatch, a **failure function** F gives the new position in P.

**Prefix-suffix function.** X\[i\] = length of the longest **proper** prefix of P\[1..i\] that is also a proper suffix of P\[1..i\] (a proper prefix/suffix is any prefix/suffix except P itself).

**Failure function** F\[1..m + 1\], computed from X:

- F\[1\] = 0;
- F\[i\] = X\[i − 1\] + 1 if P\[X\[i − 1\] + 1\] ≠ P\[i\];
- F\[i\] = F\[X\[i − 1\] + 1\] otherwise (if the character we would restart from is the same one that just failed, we already know it fails, so we jump further).

F\[i\] is the position of P to compare next after a mismatch on P\[i\]; F\[i\] = 0 means “advance on S and restart from P\[1\]”; F\[m + 1\] is used after a full match.

*Example P = ACGTACT:*

| i   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|:----|:----|:----|:----|:----|:----|:----|:----|-----|
| P   | A   | C   | G   | T   | A   | C   | T   |     |
| X   | 0   | 0   | 0   | 0   | 1   | 2   | 0   |     |
| F   | 0   | 1   | 1   | 1   | 0   | 1   | 3   | 1   |

F\[6\] = F\[X\[5\] + 1\] = F\[2\] = 1 because P\[6\] = P\[2\] = C: if P\[6\] already mismatched, P\[2\] would mismatch too. F\[7\] = X\[6\] + 1 = 3 because P\[7\] = T ≠ G = P\[3\]: a mismatch on P\[7\] means we matched P\[5..6\] = AC = P\[1..2\], so we restart from P\[3\]. A human-friendly way to compute F\[i\]: slide P under itself and find the first shift where the characters before position i still match and the character at the new position differs from P\[i\].

     1: function KMP-FF(String P) → Array
     2:     m = |P|
     3:     F[1, .., m + 1]                     ▷ failure function array
     4:     F[1] = 0
     5:     i = 2                               ▷ current character index
     6:     j = 1                               ▷ prefix length + 1
     7:     while i ≤ m do
     8:         if P[i] == P[j] then
     9:             F[i] = F[j]
    10:         else
    11:             F[i] = j
    12:             while j > 0 and P[i] ≠ P[j] do
    13:                 j = F[j]
    14:         i = i + 1
    15:         j = j + 1
    16:     F[i] = j                            ▷ F[m + 1]
    17:     return F

(KMP-FF does not need X explicitly.)

     1: function KMP-ESM(String P, String S) → int
     2:     m = |P|, n = |S|
     3:     F = KMP-FF(P)
     4:     k = 0, i = 1, j = 1                 ▷ i on P, j on S
     5:     while j ≤ n do
     6:         if i == 0 then                  ▷ restart P on the next character
     7:             i = 1, j = j + 1
     8:         else if P[i] == S[j] then
     9:             i = i + 1, j = j + 1
    10:             if i == m + 1 then          ▷ full match
    11:                 k = k + 1
    12:                 i = F[m + 1]
    13:         else
    14:             i = F[i]                    ▷ mismatch: use the failure function
    15:     return k

**Complexity.** j (on S) is never decremented: Θ(n) increments. i may be decremented (F\[i\] \< i), but every decrement of i must be preceded by an increment (which also increments j), so there are at most n decrements: at most 2n steps, **KMP-ESM scan Θ(n)**. In KMP-FF, i is incremented m − 1 times and j can decrease at most as many times as it was increased: **KMP-FF Θ(m)**. Total **Θ(m + n)** in every case. F depends only on P, so it can be computed once and reused to search the same pattern in many strings.

*BF vs KMP*, P = AAAAAAC, S = A<sup>14</sup> (X = 0 1 2 3 4 5 0; F = 0 0 0 0 0 0 6 1): BF compares 7 characters at each of the 8 positions; KMP compares the first six A’s once, and after each mismatch on C restarts from P\[6\] (F\[7\] = 6), checking only one A and the C at each new position.

## 14.2 Approximate string matching

Given a query P (m) and a text S (n), m ≤ n: ESM asks whether P is a substring of S; **ASM asks for the minimum number of changes to apply to P so that the result P’ is a substring of S**. Related, but computationally very different problems.

A **k-approximation** of P in S is a string P’ that occurs in S and can be obtained from P with 0 ≤ k ≤ m edit operations: **substitution** (p<sub>i</sub> replaced), **insertion** (a new character added), **deletion** (p<sub>i</sub> removed). ASM returns a k-approximation with the minimum k (the edit distance between P and P’); there may be several. We want the minimum k, not the longest P’.

*Example:* P = AATAGG, S = AAAATTGA: minimum k = 2, e.g. AATAGG → (G→A) AATAGA → (A→T) AATTGA = P’, or AATAGG → (G→T) AATATG → (delete A) AATTG = P’’.

### 14.2.1 Dynamic programming formulation

Let D\[i, j\] be the minimum k of a k-approximation of P\[1..i\] ending at position j of S. If p<sub>i</sub> = s<sub>j</sub> the characters match and D\[i, j\] = D\[i − 1, j − 1\]; otherwise D\[i, j\] is the best among D\[i − 1, j − 1\] + 1 (substitution of p<sub>i</sub>), D\[i − 1, j\] + 1 (deletion of p<sub>i</sub>), D\[i, j − 1\] + 1 (insertion of a character after p<sub>i</sub>). Optimal substructure holds, and the sub-problems overlap.

D\[i, j\] = 0 if i = 0; i if j = 0; min{ D\[i − 1, j − 1\] + δ<sub>i,j</sub> (⇖ match/substitution), D\[i − 1, j\] + 1 (↑ deletion), D\[i, j − 1\] + 1 (← insertion) } otherwise, with δ<sub>i,j</sub> = 0 if p<sub>i</sub> = s<sub>j</sub>, 1 otherwise.

D\[0, j\] = 0 because the approximate occurrence may start anywhere in S; D\[i, 0\] = i (delete all of P\[1..i\]). To rebuild the solution we store the chosen operation in a table B: ⇖ match/substitution, ↑ deletion, ← insertion, × stop.

     1: function ASM(String P, String S) → (Matrix, Matrix)
     2:     m = |P|, n = |S|
     3:     B[0..m][0..n], D[0..m][0..n]
     5:     for i = 0, ⋯, m do D[i, 0] = i, B[i, 0] = ↑
     6:     for j = 0, ⋯, n do D[0, j] = 0, B[0, j] = ×
     8:     for i = 1, ⋯, m do
     9:         for j = 1, ⋯, n do
    10:             sub = D[i − 1, j − 1] + δ(i, j)
    11:             del = D[i − 1, j] + 1
    12:             ins = D[i, j − 1] + 1
    13:             D[i, j] = min{sub, del, ins}
    14:             if D[i, j] == sub then B[i, j] = ⇖
    15:             else if D[i, j] == del then B[i, j] = ↑
    16:             else B[i, j] = ←
    17:     return (B, D)

    1: function ASM-ED(Matrix D[0..m][0..n]) → int
    2:     k = D[m, 0]
    3:     for j = 1, ⋯, n do
    4:         k = min{D[m, j], k}               ▷ minimum of the last row
    5:     return k

     1: function ASM-PRINT(Matrix B, String S, int i, int j)
     2:     if B[i, j] ≠ × then
     3:         if B[i, j] == ⇖ then             ▷ match/substitution
     4:             ASM-PRINT(B, S, i − 1, j − 1)
     5:             print S[j]
     6:         else if B[i, j] == ← then        ▷ insertion
     7:             ASM-PRINT(B, S, i, j − 1)
     8:             print S[j]
     9:         else                             ▷ deletion
    10:             ASM-PRINT(B, S, i − 1, j)

The initial call is ASM-PRINT(B, S, m, j) for each j with D\[m, j\] = ASM-ED(D). Note the tie-breaking order (substitution, then deletion, then insertion), which decides the arrow when several moves give the same value.

**Complexity.** ASM Θ(mn) (fill both tables); ASM-ED Θ(n) (scan the last row); ASM-PRINT O(m + n) (i and/or j decrease at each step). ESM counting can be solved with ASM by counting the zeros in the last row of D: Θ(mn), no better than brute force. Memory optimizations: B is redundant (the arrows can be recomputed from D); for the distance alone two rows of length n + 1 suffice.

*Example P = AATAGG, S = AAAATTGA* (D, then B):

| D   |     | A   | A   | A   | A   | T   | T   | G   | A   |
|-----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|     | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| A   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 0   |
| A   | 2   | 1   | 0   | 0   | 0   | 1   | 2   | 2   | 1   |
| T   | 3   | 2   | 1   | 1   | 1   | 0   | 1   | 2   | 2   |
| A   | 4   | 3   | 2   | 1   | 1   | 1   | 1   | 2   | 2   |
| G   | 5   | 4   | 3   | 2   | 2   | 2   | 2   | 1   | 2   |
| G   | 6   | 5   | 4   | 3   | 3   | 3   | 3   | 2   | 2   |

| B   |     | A   | A   | A   | A   | T   | T   | G   | A   |
|-----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|     | ×   | ×   | ×   | ×   | ×   | ×   | ×   | ×   | ×   |
| A   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   |
| A   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   |
| T   | ↑   | ↑   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ←   | ↑   |
| A   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ↑   | ⇖   | ⇖   | ⇖   |
| G   | ↑   | ↑   | ↑   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ←   |
| G   | ↑   | ↑   | ↑   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   |

The minimum of the last row is k = 2, at columns 7 and 8. From (6, 8): AATTGA (G→A, A→T); from (6, 7): AATTG (G→T and deletion of an A).

## 14.3 Summary: exact string matching

| Approach | Preprocessing | ESM counting (worst case) |
|:---|:---|:---|
| Brute force | – | O(mn) |
| KMP | Θ(m) (failure function) | Θ(m + n) |
| Dynamic programming (ASM) | – | Θ(mn) |

(The table is completed with suffix data structures and the BWT in the next chapters.)

## 14.4 Exam exercises on string matching

**Exam 1 July 2026, Ex. 4: KMP with P = ANANAS, S = BANANASANDANANASJAM.**

1)  Prefix-suffix and failure function:

| i   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
|:----|:----|:----|:----|:----|:----|:----|-----|
| P   | A   | N   | A   | N   | A   | S   |     |
| X   | 0   | 0   | 1   | 2   | 3   | 0   |     |
| F   | 0   | 1   | 0   | 1   | 0   | 4   | 1   |

2)  Execution (✓ match, ✗ mismatch; the number is the position in S):

- P at 1: A✗(B, S1) ⇒ F\[1\] = 0, advance on S.
- P at 2: A✓ N✓ A✓ N✓ A✓ S✓ (S2–S7): **occurrence 1**; i = F\[7\] = 1.
- P at 8: A✓(S8) N✓(S9) A✗(D, S10) ⇒ F\[3\] = 0, advance.
- P at 11: A✓ N✓ A✓ N✓ A✓ S✓ (S11–S16): **occurrence 2**; i = F\[7\] = 1.
- P at 17: A✗(J) ⇒ advance. P at 18: A✓(S18) N✗(M, S19) ⇒ i = F\[2\] = 1. P at 19: A✗(M) ⇒ end.

3)  Two exact occurrences.

**Exam 14 February 2025, Ex. 5: P = ACACCAC, S = AAACCACACCACACC.** F = 0 1 0 1 3 0 1 3 (positions 1–8). The pattern slides as: AC (fail at S2), AC (fail at S3), ACA (fail), ACACCAC (full match at S7–S13), ACACC (fail at the end of S): **one** exact occurrence.

**Exam 14 February 2025, Ex. 6: ASM with P = ACCATA, S = ATTTGATA.**

| D   |     | A   | T   | T   | T   | G   | A   | T   | A   |
|-----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|     | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| A   | 1   | 0   | 1   | 1   | 1   | 1   | 0   | 1   | 0   |
| C   | 2   | 1   | 1   | 2   | 2   | 2   | 1   | 1   | 1   |
| C   | 3   | 2   | 2   | 2   | 3   | 3   | 2   | 2   | 2   |
| A   | 4   | 3   | 3   | 3   | 3   | 4   | 3   | 3   | 2   |
| T   | 5   | 4   | 3   | 3   | 3   | 4   | 4   | 3   | 3   |
| A   | 6   | 5   | 4   | 4   | 4   | 4   | 4   | 4   | 3   |

| B   |     | A   | T   | T   | T   | G   | A   | T   | A   |
|-----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|     | ×   | ×   | ×   | ×   | ×   | ×   | ×   | ×   | ×   |
| A   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   |
| C   | ↑   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ↑   | ⇖   | ↑   |
| C   | ↑   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ↑   | ⇖   | ⇖   |
| A   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   | ⇖   |
| T   | ↑   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ↑   | ⇖   | ↑   |
| A   | ↑   | ⇖   | ↑   | ⇖   | ⇖   | ⇖   | ⇖   | ↑   | ⇖   |

2)  k = 3 (last row, column 8). (c) Following the arrows from (6, 8), all diagonal: P’ = TTGATA, with ACCATA → (C→G) ACGATA → (C→T) ATGATA → (A→T) TTGATA.

**Exam 24 July 2025 and 15 December 2025, Ex. 1:** complexity of calling ESM on all prefixes of P (see the recurrence relations chapter).

### 14.4.1 Past exam exercises on this topic

5)  Ex. 5 2023/07/24 F; (E) Ex. 5 2023/10/27; (E) Ex. 5 2023/12/01; (E) Ex. 5 2024/04/24; (E) Ex. 5 2024/11/15; (E) Ex. 4 2024/12/16; (E) Ex. 5 2025/02/14; (E) Ex. 6 2025/02/14; (E) Ex. 4 2026/07/01.

---
> [[AADS 20 - Hard problems – P, NP, NP-complete, NP-hard|← Hard problems – P, NP, NP-complete, NP-hard]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 22 - Sequence alignment|Sequence alignment →]]
