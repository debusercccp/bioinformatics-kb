---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 4
tags: [note, aads]
---

> [[AADS 03 - Asymptotic notation|← Asymptotic notation]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 05 - Recurrence relations|Recurrence relations →]]

# Computational complexity and amortized analysis

*Reference: CLRS Ch. 3 and 17.*

## 3.1 Complexity of an algorithm and of a problem

The running time of an algorithm depends on the number of operations executed relative to the size of the input (the same for memory). For inputs of the same size n the algorithm may be fast on some instances and slow on others, so complexity is analyzed under different conditions and expressed with asymptotic notation.

**Definition (complexity of an algorithm).** An algorithm A has computational complexity O(f(n)) with respect to a resource if the amount of that resource needed to execute A on inputs of size n is O(f(n)).

**Definition (complexity of a problem).** A problem P has computational complexity O(f(n)) if the best performing algorithm solving P has cost O(f(n)).

The main resources are time and memory; the definitions hold for all the asymptotic notations.

## 3.2 Best, worst and average case

- **Best case:** behavior under optimal conditions (linear search where the element is the first one).
- **Worst case:** behavior under unfavourable conditions (linear search where the element is last or missing).
- **Average case:** behavior averaged over all possible inputs, under a probabilistic assumption.

When designing algorithms we are mostly interested in improving the worst and/or the average case. There can be several best cases: in linear search, finding x in position 1 costs f(n) = 3 = O(1), in position 2 costs f(n) = 5 = O(1); both are best cases because the cost does not depend on n. If x is in the last position we perform 2n + 1 operations: Θ(n), linear.

### 3.2.1 Linear search

    1: function linsearch(int A[1 ⋯ n], int x) → int
    2:     for i = 1, ⋯, n do
    3:         if A[i] == x then
    4:             return i
    5:     return −1

Best case O(1); worst case Θ(n). **Average case**: assume uniform probability, including the “not found” case, which we pretend is position n + 1 (to discover that x is missing we must scan the whole array). Position i has probability P<sub>i</sub> = 1/(n+1) and inspection time T<sub>i</sub> = i, so

Average cost = Σ<sub>i=1..n+1</sub> P<sub>i</sub>T<sub>i</sub> = (1/(n+1)) Σ<sub>i=1..n+1</sub> i = (1/(n+1))·(n+1)(n+2)/2 = (n+2)/2 = Θ(n).

The uniform assumption is not always true, but without more information we cannot do better.

### 3.2.2 Binary search (sorted array)

     1: function binsearch(int A[1 ⋯ n], int x) → int
     2:     i = 1, j = n
     3:     while i ≤ j do
     4:         m = (i + j)/2
     5:         if A[m] == x then
     6:             return m
     7:         else if A[m] < x then
     8:             i = m + 1
     9:         else
    10:             j = m − 1
    11:     return −1

Best case: x in the middle, O(1). Worst case: x missing. After each iteration the search space is halved: n, n/2, n/4, …, n/2<sup>i−1</sup>. The loop ends when the space is \< 1: n/2<sup>i−1</sup> \< 1 ⇔ i \> log<sub>2</sub> n + 1, so the loop runs Θ(log n) times and the worst case is Θ(log n). (Class example: looking for 13, we find 11 \< 13 in the middle and continue on the right half.)

Average case (excluding the missing element, P<sub>i</sub> = 1/n): 1 slot is reached in 1 step, 2 slots in 2 steps, 4 slots in 3 steps, … 2<sup>i−1</sup> slots in i steps, for at most log n steps:

(1/n) Σ<sub>i=1..log n</sub> i·2<sup>i−1</sup> ≤ (log n / n) Σ<sub>i=1..log n</sub> 2<sup>i−1</sup> ≤ (log n / n)·(2<sup>log n+1</sup> − 2)/(2 − 1) = O(log n).

### 3.2.3 Minimum value

    1: function min(int A[1 ⋯ n]) → int
    2:     m = 1
    3:     for i = 2, ⋯, n do
    4:         if A[i] < A[m] then
    5:             m = i
    6:     return m

The loop is executed n − 1 times at O(1) cost: best, worst and average are all O(n), and in fact Θ(n), because every element must be inspected whatever the input.

## 3.3 Amortized analysis

Amortized analysis evaluates the **average cost of a sequence of operations**. The average cost is the average of a single operation (over random inputs); the amortized cost is the average over a sequence of (different) operations, in the worst case, with no probability involved. It is useful when an operation is very expensive in some situations and very cheap in others: worst-case analysis would be too pessimistic, and average-case analysis needs probabilistic assumptions that may be hard to formulate.

**Aggregate method.** Find an upper bound T(n) on the total cost of a sequence of n operations and divide by n. Better when the total cost is easy to define. (Notes: *sometimes it is very hard to know the cost of each single operation, but we can find the total cost.*)

**Accounting method.** Assign an amortized cost to each operation. Every executed operation is charged its amortized cost; the difference between amortized and actual cost is saved as credit; when the actual cost is higher than the amortized one, it is paid with the credit. The amortized cost is correct if the credit never becomes negative. Better when there are different kinds of operations. (Notes: *imagine someone gives you money for every operation; cheap operations leave credit, which pays for the expensive ones.*)

Neither method is better than the other; in class the professor said that the computation of amortized costs will not be asked directly.

**Example: monthly expenses.** Worst-case cost of a month is 2000 €, i.e. 24000 € per year in the worst case. Aggregate method: the actual costs of the year sum to 9300 €, so the amortized cost is 9300/12 = 775 € per month. Accounting method: we budget 800 € per month, pay the costs and save the rest as credit, used for the months that exceed the budget; the credit must never go negative. With a budget of 775 € we would be broke in April, so the amortized cost found by accounting is 800 €. The two numbers need not coincide; what matters is that the cost is roughly constant per month.

### 3.3.1 Binary counter

A k-bit binary number is stored in A\[1..k\], most significant bit in A\[1\]. INCREMENT flips the trailing 1s to 0 and the first 0 to 1. A single increment can cost k (e.g. 0111 → 1000), so a naive bound for n increments is O(nk).

Looking at the table of successive values one sees a regularity: the last bit changes at every increment, the one before every two increments, and so on.

<figure>
![[AADS-rId44.jpg|252]]
<figcaption aria-hidden="true"><p>Binary counter table (personal notes)</p></figcaption>
</figure>

**Aggregate method.** The last bit flips n times, the previous n/2 times, the one before n/4 times, …:

n + n/2 + ⋯ + n/2<sup>k−1</sup> ≤ n Σ<sub>i≥0</sub> (1/2)<sup>i</sup> = n·1/(1 − 1/2) = 2n

(only k bits exist even when n \> 2<sup>k</sup>, overflow). The total cost of n increments is O(n), so the amortized cost per increment is O(n)/n = **O(1)**.

<figure>
![[AADS-rId47.jpg|391]]
<figcaption aria-hidden="true"><p>Summation of the amortized cost, and bound with the geometric series (personal notes)</p></figcaption>
</figure>

<figure>
![[AADS-rId50.jpg|391]]
<figcaption aria-hidden="true"><p>Upper bound solution (personal notes)</p></figcaption>
</figure>

**Accounting method.** Charge 2 € to every flip 0 → 1: 1 € pays the flip, 1 € stays on the bit as credit and will pay for flipping it back to 0. Flips 1 → 0 are not charged. *Theorem:* at any time each 1 in the array carries 1 € of credit, so the credit equals the number of 1s and is never negative. *Theorem:* n increments cost 2n €, because each increment sets exactly one bit from 0 to 1. Amortized cost 2n/n = O(1).

A second classical application, the dynamic array that doubles when full (amortized O(1) push), is studied with stacks in the chapter on elementary data structures.

---
> [[AADS 03 - Asymptotic notation|← Asymptotic notation]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 05 - Recurrence relations|Recurrence relations →]]
