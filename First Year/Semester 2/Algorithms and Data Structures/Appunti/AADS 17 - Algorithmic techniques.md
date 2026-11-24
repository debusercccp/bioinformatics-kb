---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 17
tags: [note, aads]
---

> [[AADS 16 - Hash tables|← Hash tables]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 18 - Disjoint-set data structure (Union–Find)|Disjoint-set data structure (Union–Find) →]]

# Algorithmic techniques

*Reference: CLRS Ch. 4 (divide and conquer), 15 (dynamic programming), 16 (greedy).*

An algorithmic technique is a general, proven approach to design algorithms. We study four of them, **brute force, divide et impera, dynamic programming, greedy**, applied to two problems.

**Maximum Sum Subarray (MSS).** Given an array of integers A\[1..n\], find the contiguous subarray A\[i..j\] with the largest sum Σ<sub>k=i..j</sub> A\[k\] (we compute only the sum, not the indices). There are n(n + 1)/2 = Θ(n<sup>2</sup>) candidate subarrays (1 of size n, 2 of size n − 1, …, n of size 1).

**Change Making (CM).** Given n distinct positive coin values \[c<sub>1</sub>, …, c<sub>n</sub>\] and an amount W ≥ 0, find non-negative integers w<sub>1</sub>, …, w<sub>n</sub> with W = Σ w<sub>i</sub>c<sub>i</sub> minimizing the number of coins F(W) = Σ w<sub>i</sub> (we compute only F(W)). Examples: coins \[1, 3, 4\], W = 6 = 3 + 3 ⇒ F(W) = 2; coins \[1, 5, 10, 20\], W = 8 = 5 + 1 + 1 + 1 ⇒ F(W) = 4. We may assume the coins sorted in non-decreasing order and c<sub>1</sub> = 1 (so change is always possible).

## 10.1 Brute force search

Enumerate all candidate solutions and check each one. Example: brute-force sorting tries all n! permutations (each checked in O(n)): O(n·n!) = O((n + 1)!), not a good idea. *Pros:* simple, always finds a solution if one exists. *Cons:* the cost is bounded by the number of candidates, which usually grows very fast (often exponentially).

    1: function bf-mss(int A[1, ⋯, n]) → int
    2:     mss = A[1]
    3:     for i = 1, ⋯, n do
    4:         tmp = 0
    5:         for j = i, ⋯, n do          ▷ all subarrays starting at i
    6:             tmp = tmp + A[j]
    7:             mss = max(mss, tmp)
    8:     return mss

Cost in all cases Σ<sub>i=1..n</sub> (n − i + 1) = n(n + 1)/2 = **Θ(n<sup>2</sup>)**.

     1: function BF-CM(int C[1, ⋯, n], int W) → int
     2:     if W < 0 then return ∞             ▷ not a solution
     4:     else if W == 0 then return 0       ▷ no more coins needed
     6:     else
     7:         res = ∞
     8:         for i = 1, ⋯, n do
     9:             res = min(res, BF-CM(C, W − C[i]) + 1)
    10:         return res

It tries every coin, recursing on W − C\[i\], and takes the minimum + 1 (the current coin); it returns ∞ if no change is possible (impossible if 1 is a coin). The recursion tree has height at most W (with coin 1) and every internal node has n children, so T(n, W) ≤ 1 + n + n<sup>2</sup> + ⋯ + n<sup>W</sup> = (n<sup>W+1</sup> − 1)/(n − 1) = **O(n<sup>W</sup>)**: exponential.

## 10.2 Divide et impera

Break the problem into two or more sub-problems until they are simple enough to be solved directly, then combine the solutions: divide, conquer (recursively), combine. *Pros:* powerful for difficult problems. *Cons:* inefficient when sub-problems overlap.

**MSS.** Split A around the central element A\[q\]. The maximum subarray is either in the left part A\[p..q−1\], or in the right part A\[q+1..r\], or it crosses A\[q\]. The first two are computed recursively, the middle one iteratively (extend A\[q\] as much as useful to the left and to the right).

     1: function dei-mss(int A[1, ⋯, n], int p, int r)
     2:     if p > r then return −∞
     4:     else if p == r then return A[p]
     6:     else
     7:         q = ⌊(p + r)/2⌋
     8:         lmss = dei-mss(A, p, q − 1)         ▷ max sum in the left part
     9:         rmss = dei-mss(A, q + 1, r)         ▷ max sum in the right part
    10:         tmp = 0, lmss2 = 0, rmss2 = 0
    11:         for i = q − 1, ⋯, p do              ▷ extend A[q] to the left
    12:             tmp = tmp + A[i]
    13:             lmss2 = max(lmss2, tmp)
    14:         tmp = 0
    15:         for i = q + 1, ⋯, r do              ▷ extend A[q] to the right
    16:             tmp = tmp + A[i]
    17:             rmss2 = max(rmss2, tmp)
    18:         return max(lmss, rmss, A[q] + lmss2 + rmss2)

T(n) = 2T(n/2) + n ⇒ α = β = 1 ⇒ **Θ(n log n)**, better than brute force.

**CM.** F(W) = 0 if W = 0, otherwise F(W) = min{F(W − C\[i\]) + 1 : W − C\[i\] ≥ 0}. The sub-problems are solved recursively and combined by taking the minimum:

    1: function dei-cm(int C[1, ⋯, n], int W) → int
    2:     if W == 0 then return 0
    4:     else
    5:         res = ∞
    6:         for i = 1, ⋯, n do
    7:             if C[i] ≤ W then
    8:                 res = min(res, dei-cm(C, W − C[i]) + 1)
    9:         return res

It is equivalent to brute force (it simply does not recurse when W − C\[i\] \< 0): still O(n<sup>W</sup>). The problem is that **many sub-problems recur** (the recursion tree for \[1, 3, 4\], W = 6 contains F(2), F(1), F(0) many times).

## 10.3 Dynamic programming

Like divide et impera it derives the solution of P from its sub-problems, but it **saves the sub-problem solutions** to avoid solving them again. Conditions:

- **Optimal substructure:** the optimal solution of P can be built from optimal solutions of its sub-problems (and quickly).
- **Overlapping sub-problems:** the same sub-problems appear many times (if they do not overlap, use divide et impera); the space of distinct sub-problems must be small.

*Pros:* faster than divide et impera when sub-problems overlap. *Cons:* extra memory to store the solutions.

**Steps.** (1) Characterize the structure of an optimal solution (does P have optimal substructure?). (2) Define recursively the value of an optimal solution. (3) Compute the optimal values bottom-up, from the smallest sub-problems to P, storing them (usually in a table).

**Example: Fibonacci.** F(n) depends on F(n − 1) and F(n − 2) (optimal substructure, derived with a sum); F(n − 1) and F(n − 2) share F(n − 3) (overlapping); there are only n distinct sub-problems. dei-fib is exponential, dp-fib (an array F\[1..n\] filled left to right) is linear.

**MSS.** Let B\[i\] be the maximum sum of a subarray *starting at* i; the answer is max(B\[1\], …, B\[n\]). B\[n\] = A\[n\] and B\[i\] = max(A\[i\], A\[i\] + B\[i + 1\]) for i \< n: either the subarray is A\[i\] alone or it extends the best subarray starting at i + 1. There are exactly n overlapping sub-problems.

    1: function dp-mss(int A[1, ⋯, n]) → int
    2:     let B[1, ⋯, n] be a new array
    3:     B[n] = A[n]
    4:     for i = n − 1, ⋯, 1 do
    5:         B[i] = max(A[i], A[i] + B[i + 1])
    6:     return max(B[1], ⋯, B[n])

Cost **Θ(n)**, memory Θ(n). A second version keeps only the last local value and the running maximum (constant memory): it is in fact a greedy algorithm (known as Kadane’s algorithm).

    1: function dp-mss2(int A[1, ⋯, n]) → int
    2:     tmp = A[n], mss = A[n]
    3:     for i = n − 1, ⋯, 1 do
    4:         tmp = max(A[i], A[i] + tmp)
    5:         mss = max(mss, tmp)
    6:     return mss

**CM.** The sub-problem space is F(0), …, F(W) (W − C\[i\] \< W), with many overlaps. Fill F bottom-up:

     1: function dp-cm(int C[1, ⋯, n], int W) → int
     2:     let F[0, ⋯, W] be a new array
     3:     F[0] = 0
     4:     for i = 1, ⋯, W do
     5:         res = ∞
     6:         for j = 1, ⋯, n do
     7:             if C[j] ≤ i then
     8:                 res = min(res, F[i − C[j]] + 1)
     9:             (else break, if the coins are sorted increasingly)
    10:         F[i] = res
    11:     return F[W]

Cost **O(nW)** (Θ(nW) if the coins are not sorted). It returns ∞ if W is smaller than every coin. Note that O(nW) is *pseudo-polynomial*: polynomial in the value W, exponential in its size (number of bits).

*Example*, coins \[1, 3, 4\], W = 6: F = \[0, 1, 2, 1, 1, 2, 2\] for amounts 0…6 (F(6) = F(3) + 1 = 2, i.e. 3 + 3).

## 10.4 Greedy approach

A greedy algorithm makes, at each step, the **locally optimal choice**; it does not always lead to an optimal solution. It works when the problem has:

1.  **optimal substructure** (so it is also solvable with dynamic programming);
2.  the **greedy-choice property**: a globally optimal solution can be reached by locally optimal choices only.

Dynamic programming considers all possible choices at each step; greedy considers only one. *Pros:* when applicable, faster and simpler than dynamic programming. *Cons:* it may be hard to prove the greedy-choice property.

**CM.** At each step take the largest coin not greater than the remaining amount.

    1: function greedy-cm(int C[1, ⋯, n], int W) → int
    2:     res = 0, i = n
    3:     while W > 0 and i > 0 do
    4:         if W ≥ C[i] then
    5:             W = W − C[i]
    6:             res = res + 1
    7:         else
    8:             i = i − 1
    9:     if W ≠ 0 then return ∞ else return res

C is assumed sorted (otherwise sort it in Θ(n log n)). Each iteration decreases W (by at least 1) or i (by exactly 1): O(n + W). Second version: take the coin C\[i\] W/C\[i\] times in one step:

    1: function greedy-cm(int C[1, ⋯, n], int W) → int
    2:     res = 0, i = n
    3:     while W > 0 and i > 0 do
    4:         if W ≥ C[i] then
    5:             res = res + W/C[i]          ▷ integer division
    6:             W = W mod C[i]
    7:         i = i − 1
    8:     if W ≠ 0 then return ∞ else return res

At most n iterations: **O(n)** with sorted coins, O(n log n) otherwise.

**Canonical coin systems.** The greedy choice is optimal only if the coin system is **canonical** (by definition: greedy gives the optimal solution for every W). Standard currencies (euro, dollar) are canonical; there is no simple characterization, but it can be checked computationally. Non-canonical example: \[1, 3, 4\], W = 6: greedy gives 4 + 1 + 1 (3 coins), optimum 3 + 3 (2 coins). Canonical example: \[1, 5, 10, 20\], W = 8: greedy 5 + 1 + 1 + 1 = 4 coins, optimal.

**Proof that greedy is optimal for \[1, 5, 10, 20\].** Let G = \[w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub>, w<sub>4</sub>\] be the greedy solution and S = \[w’<sub>1</sub>, …, w’<sub>4</sub>\] an optimal one for W. In S: w’<sub>1</sub> ≤ 4 (five 1s could be replaced by one 5), w’<sub>2</sub> ≤ 1 (two 5s by one 10), w’<sub>3</sub> ≤ 1 (two 10s by one 20), so w’<sub>1</sub> + 5w’<sub>2</sub> + 10w’<sub>3</sub> ≤ 4 + 5 + 10 = 19 \< 20. Hence w’<sub>4</sub> = ⌊W/20⌋ = w<sub>4</sub> (the number of 20s is the one chosen by greedy). Repeating the argument on the remaining amount with the smaller coins gives w’<sub>3</sub> = w<sub>3</sub>, w’<sub>2</sub> = w<sub>2</sub>, w’<sub>1</sub> = w<sub>1</sub>: G = S.

## 10.5 Summary

|  | MSS | CM |
|:---|:---|:---|
| Brute force | Θ(n<sup>2</sup>) | O(n<sup>W</sup>) |
| Divide et impera | Θ(n log n) | O(n<sup>W</sup>) |
| Dynamic programming | Θ(n) | O(nW) |
| Greedy | Θ(n) | O(n) (sorted coins; optimal only for canonical systems) |

Worst-case costs; for MSS n is the array length, for CM n is the number of coin values and W the amount.

From the short notes: brute force is simple and correct but usually too slow (often exponential); divide et impera is powerful but inefficient when sub-problems overlap; dynamic programming is faster than divide et impera with overlapping sub-problems but may need extra memory; greedy, when applicable, is faster and simpler than dynamic programming, but the greedy-choice property can be hard to prove.

## 10.6 Exam exercises on algorithmic techniques

**Exam 1 July 2026, Ex. 2: increasing index.** A\[1..n\] with A\[1\] \< A\[n\]; find i ∈ \[1, n − 1\] with A\[i\] \< A\[i + 1\]. *Hint:* if A\[j\] \< A\[k\] for j \< k, there is an increasing index in \[j, k − 1\].

1)  Brute force: check all indices.

<!-- -->

    1: function bf-incrind(int A[1, ⋯, n]) → int
    2:     for i = 1, ⋯, n − 1 do
    3:         if A[i] < A[i + 1] then return i

2)  Divide et impera: check the middle index; if it is not increasing, recurse on the half that is guaranteed to contain one.

<!-- -->

    1: function dei-incrind(int A[1, ⋯, n], int p, int r) → int
    2:     q = (p + r)/2
    3:     if A[q] < A[q + 1] then return q
    5:     else if A[p] < A[q] then return dei-incrind(A, p, q)
    7:     else return dei-incrind(A, q, r)

Called with p = 1, r = n. If A\[q\] ≥ A\[q + 1\]: either A\[p\] \< A\[q\] (an increasing index exists in \[p, q − 1\]), or A\[p\] ≥ A\[q\], and since A\[p\] \< A\[r\] we get A\[q\] \< A\[r\] (an increasing index exists in \[q, r − 1\]).

3)  Brute force: Θ(n) in the worst case (the only increasing index is n − 1). Divide et impera: T(n) = T(n/2) + 1 (until the subarray has size 2), α = 0 = β ⇒ **Θ(log n)**.

**Exam 15 November 2024, Ex. 2: maximum number of objects in a container of capacity W** (simplified knapsack). Greedy: sort the weights in non-decreasing order and insert the lightest first.

    1: function greedy-pack(real w[1, ⋯, n], real W) → int
    2:     sort(w)                       ▷ non-decreasing order
    3:     i = 1
    4:     while i ≤ n and W − w[i] ≥ 0 do
    5:         W = W − w[i]
    6:         i = i + 1
    7:     return i − 1                  ▷ number of objects inserted

(The official solution returns i; since i starts from 1, the number of inserted objects is i − 1.) Cost Θ(n log n) (mergesort) + O(n) = Θ(n log n). Why greedy is exact: if the maximum number of storable objects is k, then the k lightest objects have the minimum total weight among all k-subsets, so they fit whenever any k objects fit, and they leave the largest remaining capacity.

**Exam 16 December 2024, Ex. 3: maximum partition product.** P(n) = max{(n − i)·P(i) : i \< n}, P(0) = 1 (e.g. P(3) = 3, P(4) = 4, P(5) = 6). Brute force: suitable but exponential (it enumerates all partitions of n, whose number grows exponentially). Divide et impera: suitable thanks to optimal substructure, but the sub-problems P(1), …, P(n − 1) overlap heavily ⇒ exponential. Dynamic programming: the best choice, filling P\[0..n\] bottom-up, each entry a max over at most n values ⇒ O(n<sup>2</sup>), polynomial. Greedy: hard to judge without further mathematical analysis (a greedy choice may not give the optimum); however the literature shows that the maximum partition products have the form 3<sup>k</sup>, 2·3<sup>k</sup> or 4·3<sup>k</sup> (use as many 3s as possible), so an efficient greedy algorithm exists, with at most linear cost in n.

### 10.6.1 Past exam exercises on this topic

3)  Ex. 6 2023/07/24 (requires sequence alignment) F; (C) Ex. 5 2024/07/26 (requires sequence alignment); (C) Ex. 2 2024/11/15; (A) Ex. 3 2024/12/16; (C) Ex. 2 2025/02/14; (C) Ex. 2 2026/07/01.

---
> [[AADS 16 - Hash tables|← Hash tables]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 18 - Disjoint-set data structure (Union–Find)|Disjoint-set data structure (Union–Find) →]]
