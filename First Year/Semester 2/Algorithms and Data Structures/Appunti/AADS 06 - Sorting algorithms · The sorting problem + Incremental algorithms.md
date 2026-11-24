---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 6
tags: [note, aads]
---

> [[AADS 05 - Recurrence relations|← Recurrence relations]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 07 - Sorting algorithms · Divide et impera algorithms|Sorting algorithms · Divide et impera algorithms →]]

# The sorting problem

**Input:** a sequence of n numbers \[a<sub>1</sub>, …, a<sub>n</sub>\]. **Output:** a permutation p of the indices such that a<sub>p(1)</sub> ≤ a<sub>p(2)</sub> ≤ ⋯ ≤ a<sub>p(n)</sub>. Example: \[7, 32, 88, 21, 92, −4\] → \[−4, 7, 21, 32, 88, 92\].

Each element of the array has a **key** (comparable with \<, =, \>; an integer, a string, …) and possibly a **value** associated with it. We sort with respect to the key, not the value; often the array contains only keys.

Two properties of sorting algorithms:

- **in place:** the algorithm sorts inside the input array, with no extra array as additional memory;
- **stable:** elements with the same key appear in the output in the same order as in the input.

Any non-stable algorithm can be made stable by sorting on the pair (key, index), where index is the original position: e.g. (10, 2) \< (10, 6).

**Array.** A group of elements of the same type accessed by index (from 1 in pseudocode). Access costs O(1) for every element. Arrays have fixed size: enlarging one means creating a new array and copying all elements. A\[i, ⋯, j\] denotes the sub-array A\[i\], …, A\[j\].

Three families: **incremental** (SelectionSort, InsertionSort), **divide et impera** (MergeSort, QuickSort), **non-comparative** (CountingSort, RadixSort).

## 5.2 Incremental algorithms

They build the sorted sequence one element at a time: starting from a sorted prefix A\[1..k\], extend it to A\[1..k+1\]. Both are in place.

### 5.2.1 SelectionSort

At each step i = 1, …, n − 1: find the position j of the minimum key in A\[i..n\] and swap A\[j\] with A\[i\].

     1: function selectionsort(int A[1, ⋯, n])
     2:     for i = 1, ⋯, n − 1 do
     3:         m = minindx(A, i)        ▷ search min in A[i, ⋯, n]
     4:         swap(A, i, m)            ▷ swap A[m] with A[i]
     6: function minindx(int A[1, ⋯, n], int i)
     7:     for j = i + 1, ⋯, n do
     8:         if A[j] < A[i] then
     9:             i = j
    10:     return i
    12: function swap(int A[1, ⋯, n], int i, int j)
    13:     tmp = A[i]
    14:     A[i] = A[j]
    15:     A[j] = tmp

The swap makes this implementation **not stable** (in the class example two equal 7s are exchanged in order by a swap). Cost: at step i the search costs Θ(n − i), the swap O(1). Both loops are always fully executed, so best, average and worst case coincide:

Σ<sub>i=1..n−1</sub> (n − i) = Σ<sub>i=1..n−1</sub> i = n(n − 1)/2 = **Θ(n<sup>2</sup>)**.

(Class note: *there is no difference between best and worst case because the algorithm always scans a quadratic number of elements.*)

<figure>
![[AADS-rId92.jpg|212]]
<figcaption aria-hidden="true"><p>SelectionSort cost annotated in class</p></figcaption>
</figure>

In Python the swap is written compactly as `A[i], A[j] = A[j], A[i]`; the code is almost identical to the pseudocode (indices from 0).

### 5.2.2 InsertionSort (Mauchly, 1946)

At each step i = 2, …, n, A\[1..i−1\] is sorted; insert A\[i\] in its correct position in A\[1..i\] (the way we sort playing cards). **Stable**, in place.

    1: function insertionsort(int A[1, ⋯, n])
    2:     for i = 2, ⋯, n do
    3:         j = i
    4:         while j > 1 and A[j] < A[j − 1] do
    5:             swap(A, j, j − 1)
    6:             j = j − 1

The for loop is always fully executed; the while loop may not be executed at all.

- **Worst case** (array sorted in reverse): the while loop runs i − 1 times at iteration i: Σ<sub>i=2..n</sub> (i − 1) = n(n − 1)/2 = Θ(n<sup>2</sup>).
- **Best case** (already sorted): the while loop never runs: Σ<sub>i=2..n</sub> 1 = n − 1 = Θ(n). (Notes: *n − 1, but we write n because the −1 gives no asymptotic contribution.*)
- **Average case**: assuming the while loop runs (i − 1)/2 times on average, Σ (i − 1)/2 = n(n − 1)/4 = Θ(n<sup>2</sup>), the same as the worst case.

**Nearly sorted arrays.** If A is sorted except for its k smallest keys, the while loop runs only for those k elements, at most n times each: Θ(n) + O(nk) = O(nk). If k = O(1) the cost is Θ(n). The same holds for arrays sorted except for k = O(1) keys. Nearly sorted arrays are common in practice. (Visualization: see-algorithms.com/sorting/InsertionSort.)

---
> [[AADS 05 - Recurrence relations|← Recurrence relations]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 07 - Sorting algorithms · Divide et impera algorithms|Sorting algorithms · Divide et impera algorithms →]]
