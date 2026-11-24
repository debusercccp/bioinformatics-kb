---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 26
tags: [note, aads]
---

> [[AADS 25 - Sequence assembly|← Sequence assembly]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]]

# Appendix: the written exam

## Format and rules

Official rules (A.A. 2026/27): the written exam lasts **2 hours** and has **4 exercises** covering the whole syllabus: two of intermediate difficulty (7 points each) and two more demanding ones (9 points each), for a maximum of 32 points; the grade is out of 30, with honours above 30. Books, notes, electronic devices, any unauthorized material and AI are forbidden. Past exams (listed below) used a 3-hour format with up to 6 exercises: the typical structure below refers to them. Write clearly (unreadable text is ignored), write the solution right after the text of each exercise, put name, surname and student ID on every sheet, **show all intermediate steps** and **justify every answer**, and hand in every sheet.

Typical structure:

- **Ex. 1 (A, ~5 points):** complexity analysis of “mystery” functions (recurrences, master theorem, summations), sometimes combined with a data structure (hash table, disjoint sets, graphs, suffix structures, string matching).
- **Ex. 2 (C, ~7 points):** write pseudocode (usually recursive, on linked lists or trees, or with an algorithmic technique) and analyze its best and worst case.
- **Ex. 3–4 (A/E, ~5 points):** sorting comparisons, tree reconstruction from traversals, hash table operations, disjoint-set forests, Kruskal, hard problems.
- **Ex. 5–6 (E, ~5 points):** KMP or ASM tables, global/local/star alignment, suffix trie/tree/array, BWT and LF mapping, greedy SCS.

## Checklist from the lectures

- Start the complexity analysis from the innermost function; constants such as 2<sup>100</sup> are distractors.
- Count loop iterations exactly (n, n/2, log n) and use Θ when best and worst case coincide.
- For linked-list pseudocode: base case on NIL, return the new head, use L.next = f(L.next).
- In open addressing, deleted slots become DELETED, never NIL; insert may reuse them.
- In union by rank with equal ranks, the first root goes under the second (exam convention), whose rank grows.
- In DP tables write both the value matrix and the arrow matrix; break ties as ⇖, ↑, ←.
- In local alignment stop the traceback at 0 and report *all* optimal local alignments.
- For KMP report X and F (with F\[m + 1\]) and show every slide of the pattern, marking the compared characters.
- For the BWT show the sorted rotations, F, L and LF; for the inverse, the sequence k = LF\[k\] from k = 1.

## Past exams and their exercises

1)  analysis, (C) coding, (E) execution. All the exams listed (except the two of 2026, solved in the chapters) are in the collection of past exams with official solutions; the exams from June 2025 to January 2026 are in the collection but not yet in the classification list.

| Exam | Exercises by topic |
|:---|:---|
| 2022/06/24 | 1 Complexity (A); 2 Trees (C); 3 Sorting (A); 4 Graphs (E); 5 Alignment (E); 6 BWT (E) |
| 2022/07/21 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Trees (A); 4 Disjoint sets (E); 5 Alignment (E); 6 BWT (E) |
| 2022/10/28 | 1 Complexity (A); 2 Trees (C); 3 Trees (E); 4 Graphs (E); 5 Alignment (E); 6 BWT (E) |
| 2022/11/30 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Hash tables (E); 4 Sorting (A); 5 Assembly (E); 6 BWT (E) |
| 2023/01/16 | 1 Complexity (A); 2 Trees (C); 3 Trees (E); 4 Hard problems (A); 6 BWT (E) |
| 2023/02/06 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Hash tables (E); 4 Sorting (A); 5 Assembly (E); 6 Alignment (E) |
| 2023/06/29 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Sorting (A); 4 Disjoint sets (E); 5 Alignment (E); 6 Assembly (E) |
| 2023/07/24 | 1 Sorting (A); 2 Trees (C); 3 Lists/stacks/queues (E); 4 Hash tables (E); 5 String matching (E); 6 Alignment (C) |
| 2023/10/27 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Trees (A); 4 Graphs (E); 5 String matching (E); 6 BWT (E) |
| 2023/12/01 | 1 Complexity (A); 2 Trees (C); 3 Sorting (A); 4 Disjoint sets (E); 5 String matching (E); 6 Assembly (E) |
| 2024/01/15 | 1 Complexity (A); 2 Trees (C); 3 Hard problems (A); 4 Graphs (E); 5 Alignment (E); 6 Suffix structures (E) |
| 2024/02/12 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Trees (A); 4 Hash tables (E); 5 Suffix structures (E); 6 BWT (E) |
| 2024/04/24 | 1 Complexity (A); 2 Trees (C); 3 Trees (A); 4 Disjoint sets (E); 5 String matching (E); 6 Suffix structures (E) |
| 2024/06/28 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Sorting (A); 4 Disjoint sets (E); 5 Suffix structures (E); 6 Assembly (E) |
| 2024/07/26 | 1 Disjoint sets (A); 2 Lists/stacks/queues (C); 3 Trees (E); 4 Hash tables (E); 5 Alignment (C); 6 BWT (E) |
| 2024/11/15 | 1 Hash tables (A); 2 Techniques (C); 3 Sorting (A); 4 Graphs (E); 5 String matching (E); 6 Alignment (E) |
| 2024/12/16 | 1 Graphs (A); 2 Trees (C); 3 Techniques (A); 4 String matching (E); 5 Suffix structures (E); 6 BWT (E) |
| 2025/02/14 | 1 Complexity (A); 2 Techniques (C); 3 Lists/stacks/queues (E); 4 Graphs (E); 5 String matching (E); 6 String matching (E) |
| 2026/02/13 | 1 Complexity (A); 2 Lists/stacks/queues (C); 3 Sorting (A); 4 Graphs (E) |
| 2026/07/01 | 1 Complexity (A); 2 Techniques (C); 3 Trees (E); 4 String matching (E); 5 Alignment (E); 6 BWT (E) |

---
> [[AADS 25 - Sequence assembly|← Sequence assembly]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]]
