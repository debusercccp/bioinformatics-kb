---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 9
tags: [note, aads]
---

> [[AADS 08 - Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting|← Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 10 - Elementary data structures · Data structures, prototype and implementation + The Dictionary|Elementary data structures · Data structures, prototype and implementation + The Dictionary →]]

# Summary

| Algorithm | Best | Average | Worst | In place | Stable |
|:---|:---|:---|:---|:---|:---|
| SelectionSort | Θ(n<sup>2</sup>) | Θ(n<sup>2</sup>) | Θ(n<sup>2</sup>) | yes | no |
| InsertionSort | Θ(n) | Θ(n<sup>2</sup>) | Θ(n<sup>2</sup>) | yes | yes |
| MergeSort | Θ(n log n) | Θ(n log n) | Θ(n log n) | no | yes |
| QuickSort | Θ(n log n) | O(n log n) | Θ(n<sup>2</sup>) | yes | no |
| CountingSort | Θ(n + k) | Θ(n + k) | Θ(n + k) | no | yes (keys+data version) |
| RadixSort | Θ(d(n + k)) | Θ(d(n + k)) | Θ(d(n + k)) | no | yes |

n = number of elements, k = range of the key values (of a digit for RadixSort), d = maximum number of digits of a key. Summary from the short notes: incremental sorts are simple; divide et impera sorts are more complex but more efficient; non-comparative sorts use extra information on the keys (digits, bits, bounded range) to place items directly, often in O(n), at the price of extra memory and assumptions on the keys.

## 5.7 Exercises (from the slides)

**Ex. 1. MergeSort vs CountingSort** on n integers in \[1, k\]. MergeSort Θ(n log n) independently of k; CountingSort Θ(n + k): Θ(n) if k = O(1), Θ(log n) or Θ(n), and Θ(n<sup>2</sup>) if k = Θ(n<sup>2</sup>). CountingSort is better in all cases except k = Θ(n<sup>2</sup>), where MergeSort wins.

**Ex. 2. Top-k items** of an unsorted list of n prices, placed in the first k slots. Solution 1: reverse-sort with MergeSort, Θ(n log n). Solution 2: k selection steps:

    1: function topk(Array A[1, ⋯, n], int k)
    2:     for i = 1, ⋯, k do
    3:         j = index of the max value in A[i, ⋯, n]
    4:         swap(A, i, j)

Cost Σ<sub>i=0..k−1</sub> Θ(n − i) = Θ(nk − k<sup>2</sup>/2) = O(nk). If k = O(1) topk is linear (better); if k = Θ(log n) both are Θ(n log n); if k = Θ(n) MergeSort is better (topk becomes quadratic).

**Ex. 3. Three-way MergeSort** (split into thirds, sort recursively, merge A<sub>1</sub> with A<sub>2</sub> and then with A<sub>3</sub>). The two merges cost (2/3)n + n = (5/3)n = Θ(n); T(n) = 3T(n/3) + n, α = β = 1 ⇒ Θ(n log n): asymptotically equivalent, with higher hidden constants.

**Ex. 4. First m elements sorted, last n unsorted.** Sort the last n with MergeSort and merge:

    1: function newsort(Array A[1, ⋯, m + n], int m)
    2:     mergesort(A, m + 1, m + n)
    3:     merge(A, 1, m, m + n)

Cost Θ(n log n + m + n) = Θ(n log n + m), better than Θ((m + n) log(m + n)): if n = O(1), Θ(m); if n = O(log m), Θ(m) (log m · log log m = O(m)); if n = O(m), Θ(m log m).

**Ex. 5. QuickSelect** (k-th smallest element, average O(n)):

    1: function quickselect(Array A[1, ⋯, n], int k, int p, int r) → int
    2:     q = partition(A, p, r)
    3:     if q == k then
    4:         return A[q]
    5:     else if q < k then
    6:         return quickselect(A, k, q + 1, r)
    7:     else
    8:         return quickselect(A, k, p, q − 1)

Check 1 ≤ k ≤ n before running. Best case: T(n) = T(n/2) + n ⇒ Θ(n) (or the first pivot lands at k). Worst case: T(n) = T(n − 1) + n ⇒ Θ(n<sup>2</sup>). Average case, all partitions equally likely: T(n) = (1/(n − 1)) Σ<sub>i=1..n−1</sub> T(i) + n; multiply by n − 1, write for n − 1, subtract: (n − 1)T(n) − (n − 2)T(n − 1) = T(n − 1) + 2(n − 1), so T(n) = T(n − 1) + 2 and T(n) = T(1) + 2(n − 1) = Θ(n).

## 5.8 Exam exercises on sorting

**Exam 24 June 2022, Ex. 3 (solved in class): sorting n k-mers over {A, C, G, T}.** A lexicographic comparison of two strings of length k costs O(k).

- InsertionSort: O(n<sup>2</sup>) comparisons ⇒ O(kn<sup>2</sup>) (Σ<sub>i=2..n</sub> k(i − 1) = O(kn<sup>2</sup>)).
- MergeSort: Θ(n log n) comparisons ⇒ O(kn log n).
- RadixSort: Θ(k(n + \|Σ\|)) with d = k digits and \|Σ\| = 4 ⇒ Θ(kn).

If k = O(1): O(n<sup>2</sup>), O(n log n), Θ(n) ⇒ RadixSort. If k = O(n): O(n<sup>3</sup>), O(n<sup>2</sup> log n), Θ(n<sup>2</sup>) ⇒ RadixSort again.

<figure>
![[AADS-rId107.jpg|196]]
<figcaption aria-hidden="true"><p>Lexicographic comparison of two strings (class notes)</p></figcaption>
</figure>

<figure>
![[AADS-rId110.jpg|196]]
<figcaption aria-hidden="true"><p>Costs of the three algorithms on k-mers (class notes)</p></figcaption>
</figure>

**Exam 15 November 2024, Ex. 3: binary and all-zero arrays.** MergeSort is always Θ(n log n). Binary array: InsertionSort Θ(n<sup>2</sup>) (e.g. n/2 ones followed by n/2 zeros: each zero is shifted n/2 times, (n/2)(n/2)); QuickSort Θ(n<sup>2</sup>) (with only two values, partition almost always produces very unbalanced parts). All-zero array: InsertionSort Θ(n) (no shifts); QuickSort Θ(n<sup>2</sup>) (every A\[j\] ≤ x, so partitions are always totally unbalanced).

**Exam 13 February 2026, Ex. 3: repsort.** An array of n integers with only N distinct values. repsort scans A, storing in a hash table H the count of each value and in an array B the distinct values (steps 1–2), sorts B with mergesort (step 3), then rebuilds A by writing each B\[i\] cnt times (step 4). Average costs: steps 1–2 Θ(n) (hash operations O(1) on average), step 3 Θ(N log N), step 4 Θ(n). Total Θ(n + N log N), vs Θ(n log n) for mergesort:

- N = Θ(log n): Θ(n + log n log log n) = Θ(n) ⇒ repsort faster;
- N = Θ(√n): Θ(n + √n log n) = Θ(n) ⇒ repsort faster;
- N = Θ(n): Θ(n log n) ⇒ equivalent asymptotically, but repsort is slower in practice because of the overhead.

### 5.8.1 Past exam exercises on this topic

Sorting algorithms: (A) Ex. 3 2022/06/24 F; (A) Ex. 4 2022/11/30; (A) Ex. 4 2023/02/06; (A) Ex. 3 2023/06/29; (A) Ex. 1 2023/07/24 F; (A) Ex. 3 2023/12/01; (A) Ex. 3 2024/06/28; (A) Ex. 3 2024/11/15; (C) Ex. 2 2025/02/14 (requires algorithmic techniques); (A) Ex. 3 2026/02/13.

---
> [[AADS 08 - Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting|← Sorting algorithms · Lower bound for comparison sorting + Non-comparison sorting]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 10 - Elementary data structures · Data structures, prototype and implementation + The Dictionary|Elementary data structures · Data structures, prototype and implementation + The Dictionary →]]
