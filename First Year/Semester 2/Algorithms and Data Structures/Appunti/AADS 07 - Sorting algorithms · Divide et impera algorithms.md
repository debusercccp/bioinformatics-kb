---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 7
tags: [note, aads]
---

> [[AADS 06 - Sorting algorithms · The sorting problem + Incremental algorithms|← Sorting algorithms · The sorting problem + Incremental algorithms]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 08 - Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting|Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting →]]

# Divide et impera algorithms

*Divide et impera*: divide the problem into smaller sub-problems, conquer them recursively, combine their solutions. More efficient than incremental algorithms.

### 5.3.1 MergeSort (von Neumann, 1945)

1.  **Divide:** split A\[1..n\] into A<sub>1</sub> = A\[1..q\] and A<sub>2</sub> = A\[q+1..n\], q = ⌊(1 + n)/2⌋.
2.  **Conquer:** sort A<sub>1</sub> and A<sub>2</sub> recursively (an array of size 1 is sorted).
3.  **Combine:** merge the two sorted arrays.

<!-- -->

    1: function mergesort(int A[1, ⋯, n], int p, int r)
    2:     if p < r then
    3:         q = ⌊(p + r)/2⌋
    4:         mergesort(A, p, q)
    5:         mergesort(A, q + 1, r)
    6:         ▷ here A[p, ⋯, q] and A[q + 1, ⋯, r] are sorted
    7:         merge(A, p, q, r)

First call mergesort(A, 1, n). Partitioning is easy, merging is the hard part.

     1: function merge(int A[1, ⋯, n], int p, int q, int r)
     2:     let B[1, ⋯, r − p + 1] be a new array
     3:     i = p                      ▷ index over A[p, ⋯, q]
     4:     j = q + 1                  ▷ index over A[q + 1, ⋯, r]
     5:     k = 1                      ▷ index over B
     6:     while i ≤ q and j ≤ r do
     7:         if A[i] ≤ A[j] then
     8:             B[k] = A[i]; i = i + 1
    10:         else
    11:             B[k] = A[j]; j = j + 1
    13:         k = k + 1
    14:     while i ≤ q do             ▷ append the rest of A[i, ⋯, q]
    16:         B[k] = A[i]; k = k + 1; i = i + 1
    19:     while j ≤ r do             ▷ append the rest of A[j, ⋯, r]
    20:         B[k] = A[j]; k = k + 1; j = j + 1
    23:     for k = 1, ⋯, r − p + 1 do  ▷ copy B back into A[p, ⋯, r]
    24:         A[p + k − 1] = B[k]

The test A\[i\] ≤ A\[j\] (and not \<) makes mergesort **stable**; it is **not in place** (extra array B; an in-place merge is much more complex). The second and third while loops are never both executed. In Python, q = p + (r − p)//2 avoids overflow of p + r in old languages; // is integer division.

**Cost.** merge is linear in r − p + 1 (each iteration advances i or j; then the copy). Recurrence T(n) = 2T(n/2) + Θ(n): α = β = 1 ⇒ **Θ(n log n)**, independently of the initial order (best = average = worst).

### 5.3.2 QuickSort (Hoare, 1959)

1.  **Divide:** partition A into A\[1..q−1\] and A\[q+1..n\] such that every key in the first part is ≤ A\[q\] and every key in the second is \> A\[q\] (A\[q\] is the **pivot**).
2.  **Conquer:** sort the two parts recursively.
3.  **Combine:** nothing to do, the array is already sorted.

<!-- -->

    1: function quicksort(int A[1, ⋯, n], int p, int r)
    2:     if p < r then
    3:         q = partition(A, p, r)
    4:         ▷ ∀ i ≤ q − 1, A[i] ≤ A[q] and ∀ i ≥ q + 1, A[i] > A[q]
    5:         quicksort(A, p, q − 1)
    6:         quicksort(A, q + 1, r)

    1: function partition(int A[1, ⋯, n], int p, int r) → int
    2:     x = A[r]                    ▷ deterministic choice of the pivot
    3:     i = p − 1
    4:     for j = p, ⋯, r − 1 do
    5:         if A[j] ≤ x then
    6:             swap(A, i + 1, j)
    7:             i = i + 1
    8:     swap(A, i + 1, r)           ▷ move the pivot to A[i + 1]
    9:     return i + 1                ▷ pivot index

partition always costs Θ(r − p + 1); it is in place but **not stable**. Quicksort is the standard sorting algorithm in many libraries. Class note: *for quicksort remember what it does and the result (the idea), not necessarily the pseudocode.*

The running time depends on how balanced the partitions are.

- **Worst case**: one part has size 0, the other n − 1 (e.g. a sorted array with the last element as pivot). T(n) = T(n − 1) + T(0) + n; by iteration T(n) = T(n − i) + i + Σ<sub>k=0..i−1</sub> (n − k), ending at i = n: T(n) = 1 + n + n(n + 1)/2 = **Θ(n<sup>2</sup>)**, like insertion and selection sort.
- **Best case**: two halves of size n/2. T(n) = 2T(n/2) + n ⇒ **Θ(n log n)**, like mergesort.
- **Average case**: in general T(n) = T(i) + T(n − i − 1) + n. Assuming all partitions are equally likely, T(n) = (1/n) Σ<sub>i=0..n−1</sub> \[T(i) + T(n − i − 1)\] + n = (2/n) Σ<sub>i=0..n−1</sub> T(i) + n. Multiply by n: nT(n) = 2Σ<sub>i=0..n−1</sub> T(i) + n<sup>2</sup> (1); write it for n − 1: (n − 1)T(n − 1) = 2Σ<sub>i=0..n−2</sub> T(i) + (n − 1)<sup>2</sup> (2); subtract (2) from (1) to remove the summation: nT(n) − (n − 1)T(n − 1) = 2T(n − 1) + 2n − 1, i.e. nT(n) = (n + 1)T(n − 1) + 2n − 1. Divide by n(n + 1): T(n)/(n + 1) ≤ T(n − 1)/n + 2/(n + 1). Iterating: T(n)/(n + 1) ≤ T(1)/2 + 2 Σ<sub>k=3..n+1</sub> 1/k ≤ 1/2 + 2 ln n. Hence T(n) ≤ (n + 1)(1/2 + 2 ln n) = **O(n log n)**. (Class note: *since the best case is pseudolinear, the average case cannot be faster than that.*)

**Choice of the pivot.** With the last element as pivot, the balance depends on the input order: nearly sorted arrays lead to the worst case, and in practice they are more likely than random ones. The fix is **randomization**:

    1: function rpartition(int A[1, ⋯, n], int p, int r) → int
    2:     i = random(p, r)            ▷ random choice of the pivot
    3:     swap(A, i, r)
    4:     return partition(A, p, r)

With a random pivot all partitions are equally likely whatever the input, so the expected cost is O(n log n).

**Sorting in Python.** sorted() and sort() used QuickSort (up to 1.6), SampleSort (2.0–2.2), **TimSort** (2.3–3.10) and PowerSort (from 3.11). TimSort combines MergeSort and InsertionSort: it finds already sorted runs, extends short runs with InsertionSort up to a minimum size, and merges runs of similar size with MergeSort (stable). Worst and average O(n log n), best O(n) on nearly sorted arrays.

---
> [[AADS 06 - Sorting algorithms · The sorting problem + Incremental algorithms|← Sorting algorithms · The sorting problem + Incremental algorithms]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 08 - Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting|Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting →]]
