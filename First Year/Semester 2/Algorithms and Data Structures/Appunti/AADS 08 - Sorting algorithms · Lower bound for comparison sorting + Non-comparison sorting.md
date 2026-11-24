---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 8
tags: [note, aads]
---

> [[AADS 07 - Sorting algorithms · Divide et impera algorithms|← Sorting algorithms · Divide et impera algorithms]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 09 - Sorting algorithms · Summary … Exam exercises on sorting|Sorting algorithms · Summary … Exam exercises on sorting →]]

# Lower bound for comparison sorting

All the previous algorithms are **comparison sorts**. Any comparison sort can be described by a **decision tree**: each internal node compares two elements, an execution is a root-to-leaf path, the height of the tree is the number of comparisons in the worst case, and there must be at least n! leaves (one per permutation).

*Lemma.* A binary tree T<sub>k</sub> with k leaves in which every internal node has two children has height h(T<sub>k</sub>) ≥ log<sub>2</sub> k. *Proof by induction on k.* Base: h(T<sub>1</sub>) = 0 = log<sub>2</sub> 1. Step: let the subtrees have k<sub>1</sub> ≥ k<sub>2</sub> leaves, k = k<sub>1</sub> + k<sub>2</sub>: h(T<sub>k</sub>) = 1 + max(h(T<sub>k1</sub>), h(T<sub>k2</sub>)) ≥ 1 + log<sub>2</sub> k<sub>1</sub> = log<sub>2</sub> 2k<sub>1</sub> ≥ log<sub>2</sub>(k<sub>1</sub> + k<sub>2</sub>) = log<sub>2</sub> k.

**Theorem.** Any comparison sort performs Ω(n log n) comparisons in the worst case: h ≥ log<sub>2</sub> n! = Θ(n log n). Hence MergeSort is asymptotically optimal among comparison sorts.

(A **binary tree** has nodes with at most two children; the depth of a node is the number of edges from the root; the height is the maximum depth.)

## 5.5 Non-comparison sorting

The lower bound applies only to comparison sorts. Using other operations (on the values themselves) we can sort in linear time, at the price of constraints on the keys (class note: *counting sort works only for integers*).

### 5.5.1 CountingSort (Seward, 1954)

Assumption: keys are integers in a range \[a, b\] (possibly negative). Build an array B of size k = b − a + 1 that counts how many times each value occurs, then rewrite A.

     1: function countingsort(int A[1, ⋯, n])
     2:     a = min(A), b = max(A), k = b − a + 1
     3:     let B[1, ⋯, k] be a new array
     4:     for i = 1, ⋯, k do
     5:         B[i] = 0
     6:     for i = 1, ⋯, n do
     7:         B[A[i] − a + 1] = B[A[i] − a + 1] + 1
     8:     j = 1
     9:     for i = 1, ⋯, k do
    10:         while B[i] > 0 do
    11:             A[j] = i + a − 1
    12:             B[i] = B[i] − 1
    13:             j = j + 1

Values in \[a, b\] are rescaled to \[1, k\] by x ↦ x − a + 1. **Cost Θ(n + k)** in all cases: min and max Θ(n); the initialization Θ(k); counting Θ(n); the final for/while pair Θ(n + k) (the for runs k times and the while runs n times in total, because the counts sum to n; middle values must be visited even if they have zero occurrences). The range may be much larger than n (A = \[1, 2<sup>100</sup>\] has n = 2, k = 2<sup>100</sup>); if k = O(n) the cost is Θ(n). Class note: *k dominates the cost; the total is Θ(n + k) because we do not know how much larger k is than n.*

**Keys with data, stable version.** To sort records by an integer key, recode B as cumulative counts and copy into an auxiliary array C scanning A from the end (which makes it **stable**):

     1: function countingsort(A[1, ⋯, n])
     2:     a = minkey(A), b = maxkey(A), k = b − a + 1
     3:     let B[1, ⋯, k] and C[1, ⋯, n] be new arrays
     5:     for i = 1, ⋯, k do B[i] = 0
     7:     for i = 1, ⋯, n do B[A[i].key − a + 1] = B[A[i].key − a + 1] + 1
     9:     for i = 2, ⋯, k do
    10:         B[i] = B[i] + B[i − 1]     ▷ B[i] = number of keys ≤ i + a − 1
    12:     for i = n, ⋯, 1 do
    13:         C[B[A[i].key − a + 1]] = A[i]
    14:         B[A[i].key − a + 1] = B[A[i].key − a + 1] − 1
    15:     for i = 1, ⋯, n do
    16:         A[i] = C[i]

Some extra memory and time, but the asymptotic cost is unchanged.

### 5.5.2 RadixSort (Seward, 1954)

Assumption: keys are made of digits or characters; the **radix** is the number of possible digits. Sort first by the least significant digit, then by the second last, and so on; **each digit sort must be stable** (with a non-stable sort the order obtained on the previous digits would be destroyed).

    1: function radixsort(int A[1, ⋯, n])
    2:     d = max key length
    3:     for i = 1, ⋯, d do
    4:         stable sort of A on the i-th digit (digits numbered right to left)

Using CountingSort for each digit: **Θ(d(n + k))** in all cases, where k is the number of possible digit values (10 for decimal integers, the alphabet size for strings). If k = O(n) and d is constant, the cost is Θ(n). Class note: *RadixSort is interesting in computational biology because it can sort biological sequences, and it is very fast; it depends not only on n and k but also on the number of digits.*

---
> [[AADS 07 - Sorting algorithms · Divide et impera algorithms|← Sorting algorithms · Divide et impera algorithms]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 09 - Sorting algorithms · Summary … Exam exercises on sorting|Sorting algorithms · Summary … Exam exercises on sorting →]]
