---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 1
tags: [note, aads]
---

> [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 02 - Introduction to algorithms – the Fibonacci example|Introduction to algorithms – the Fibonacci example →]]

# How these notes are organized

These notes merge into one linear text everything collected for the course *Algorithms and Data Structures for Computational Biology* (Prof. Pietro Di Lena, University of Bologna): the official slides (with the handwritten annotations taken in class), the detailed lecture transcripts (“stamp” notes), the personal lecture notes (ALGONOTES), the short summary notes (algos), the note on gap penalties in global alignment, the classification of past exam exercises, and the written exams with their official solutions (including the exams of 1 July 2026 and 13 February 2026). The reference textbook is Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (3rd edition, abbreviated CLRS); the corresponding chapters are pointed out at the start of each chapter.

The order follows the course: each chapter starts from the definitions, goes through the algorithms with pseudocode and cost analysis, then collects the remarks made in class and closes with the typical exam exercises on that topic, solved step by step. The exam is written: 2 hours, 4 exercises (two of 7 points and two of 9 points, max 32; rules of A.A. 2026/27); books, notes, electronic devices and AI are not allowed; every answer must be justified and all intermediate steps must be shown.

Exercises are classified, as in the official list, as **(A) Analysis** (compute a complexity, compare algorithms), **(C) Coding** (write pseudocode and analyze it) and **(E) Execution** (run an algorithm by hand on a given input). In the lists of past exercises, the mark **F** means that the exercise has already been done.

Conventions used throughout: arrays are indexed from 1 in pseudocode (as in the slides) unless stated otherwise; log means log<sub>2</sub>; n is the input size; NIL is the null pointer; ⌊x⌋ and ⌈x⌉ are floor and ceiling; in the path matrices of dynamic programming (string matching and alignment) the diagonal (up-left) arrow is written ⇖.

**Course map (and typical exam position)**

| \# | Topic | Typical exam exercise |
|:---|:---|:---|
| 1 | Introduction: the Fibonacci example | – |
| 2 | Asymptotic notation | part of Ex. 1 |
| 3 | Computational complexity, amortized analysis | Ex. 1 (A) |
| 4 | Recurrence relations | Ex. 1 (A) |
| 5 | Sorting algorithms | Ex. 1/3 (A) |
| 6 | Elementary data structures: list, stack, queue | Ex. 2 (C) |
| 7 | Trees and binary trees | Ex. 2 (C), Ex. 3 (A/E) |
| 8 | Binary search trees | Ex. 2–3 |
| 9 | Hash tables | Ex. 3–4 (E) |
| 10 | Algorithmic techniques | Ex. 2–3 (C/A) |
| 11 | Disjoint sets **\[Non nei topics\]** | Ex. 4 (E) |
| 12 | Graphs, connected components, MST **\[MST: non nei topics\]** | Ex. 4 (E) |
| 13 | Hard problems (P, NP) | Ex. 3–4 (A) |
| 14 | String matching (BF, KMP, approximate) **\[Non nei topics\]** | Ex. 5 (E) |
| 15 | Sequence alignment **\[Non nei topics\]** | Ex. 5–6 (E/C) |
| 16 | Suffix data structures **\[Non nei topics\]** | Ex. 5–6 (E) |
| 17 | Burrows–Wheeler transform **\[Non nei topics\]** | Ex. 6 (E) |
| 18 | Sequence assembly **\[Non nei topics\]** | Ex. 5–6 (E) |

---
> [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 02 - Introduction to algorithms – the Fibonacci example|Introduction to algorithms – the Fibonacci example →]]
