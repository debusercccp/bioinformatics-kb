---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 10
tags: [note, aads]
---

> [[AADS 09 - Sorting algorithms · Summary … Exam exercises on sorting|← Sorting algorithms · Summary … Exam exercises on sorting]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 11 - Elementary data structures · Lists|Elementary data structures · Lists →]]

# Data structures, prototype and implementation

A **data structure** defines how data is logically organized and which operations access and modify it; it describes the organization, not the type of data stored (a list can hold integers or strings).

- The **prototype** (abstract interface) describes the possible values and operations, hides the implementation details, and tells the user how to use the structure.
- The **implementation** realizes it in a programming language; it is not visible to the user and can have a huge impact on the running time.

## 6.2 The Dictionary

A general-purpose structure (associative array) that stores a set of **unique keys**, each associated with some data (data values may repeat). Keys can be integers, strings (lexicographic order), dates… Operations:

- search(Key k): return the data associated with k, or NIL;
- insert(Key k, Data d): add (k, d); if (k, d’) is already present, replace d’ with d;
- delete(Key k): remove the pair with key k.

### 6.2.1 Implementation on an unsorted array

D.A is the array, D.size the number of elements.

     1: function search(Dict D, Key k) → Data
     2:     i = linsearch(D.A, D.size, k)
     3:     if i ≠ −1 then return D.A[i].data
     5:     else return NIL
     8: function linsearch(<Key,Data> A[1, ⋯, m], int n, Key k) → int
     9:     for i = 1, ⋯, n do
    10:         if A[i].key == k then return i
    12:     return −1                         ▷ key k not found

     1: function insert(Dict D, Key k, Data d)
     2:     i = linsearch(D.A, D.size, k)
     3:     if i == −1 then
     4:         D.size = D.size + 1           ▷ possible overflow
     5:         i = D.size
     6:     D.A[i].key = k
     7:     D.A[i].data = d

     1: function delete(Dict D, Key k)
     2:     i = linsearch(D.A, D.size, k)
     3:     if i ≠ −1 then
     4:         D.A[i] = D.A[D.size]          ▷ move the last pair into the hole
     5:         D.A[D.size] = NIL
     6:         D.size = D.size − 1

All three operations are dominated by the linear search: O(n) average and worst case (O(1) best case).

### 6.2.2 Implementation on a sorted array

Keep the array sorted by key after every insertion and deletion.

- search: binary search, O(1) best, Θ(log n) worst, O(log n) average.
- insert: find the position with a modified binary search (binsearchpos), then shift right all pairs with key \> k and put (k, d) in the gap.

<!-- -->

    1: function binsearchpos(<Key,Data> A[1 ⋯ N], int n, Key k) → int
    2:     i = 1, j = n
    3:     while i ≤ j do
    4:         m = (i + j)/2
    5:         if A[m].key == k then return m
    6:         else if A[m].key < k then i = m + 1
    7:         else j = m − 1
    8:     return i          ▷ the only difference with binsearch

When the loop ends j = i − 1, and i is the position where k must be inserted. Insert costs Θ(n) worst case (shift of the whole array when inserting at the front), O(n) average (n/2 shifts on average), O(1) best case (no shift).

- delete: binary search then shift left all pairs with key \> k. Worst Θ(n), average O(n). Best case O(log n): if binary search stops after i steps, the shift touches about n/2<sup>i</sup> elements, total O(i + n/2<sup>i</sup>); the best and worst cases of the two parts are opposite, and the minimum is O(log n).

|                | search   | insert | delete |
|:---------------|:---------|:-------|:-------|
| Unsorted array | O(n)     | O(n)   | O(n)   |
| Sorted array   | O(log n) | O(n)   | O(n)   |

Sorted arrays speed up search, but both are **bounded-size** dictionaries; we need unbounded structures.

---
> [[AADS 09 - Sorting algorithms · Summary … Exam exercises on sorting|← Sorting algorithms · Summary … Exam exercises on sorting]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 11 - Elementary data structures · Lists|Elementary data structures · Lists →]]
