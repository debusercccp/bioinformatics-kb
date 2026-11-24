---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 2
tags: [note, aads]
---

> [[AADS 01 - How these notes are organized|← How these notes are organized]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 03 - Asymptotic notation|Asymptotic notation →]]

# Introduction to algorithms: the Fibonacci example

*Reference: Demetrescu, Finocchi, Italiano, “Algoritmi e Strutture Dati”, Ch. 1.*

## 1.1 What is an algorithm

An **algorithm** is a procedure with a finite number of steps that solves a problem. The word comes from the Persian mathematician Muhammad ibn Musa al-Khwarizmi (c. 780–850), Latinized as *Algoritmi*, whose book on calculation with Hindu numerals spread the Hindu-Arabic numeral system in the Middle East and Europe.

An algorithm is different from a program. The algorithm is a high-level description of a computing procedure: it exists independently of computers, it cannot be executed on a physical machine and it may assume unbounded memory. A program is the implementation of an algorithm in a programming language: it runs on a real machine and has to deal with memory constraints.

An algorithm takes some value(s) as input (possibly none), follows a finite sequence of instructions and eventually produces some value(s) as output. The problem statement fixes the relation between input and output; there are infinitely many sets of instructions that solve the same problem (same output for the same input), and we want the most efficient one.

**Example: Euclid’s algorithm.** The GCD of x ≥ y: divide x by y and call r the remainder; if r = 0 then y is the GCD, otherwise assign y to x and r to y and repeat.

    1: function GCD(int x, int y) → int
    2:     if y == 0 then
    3:         return x
    4:     else
    5:         r = x mod y
    6:         return GCD(y, r)

To design algorithms we need to understand the problem (possible inputs and outputs, how they are related, mathematical properties), to estimate efficiency in **time** (how fast?) and **memory** (how much space?), and to know the basic techniques and data structures: different problems often share the same structure, and most new problems are solved by adapting known algorithms.

## 1.2 The Fibonacci numbers

The Fibonacci sequence F<sub>1</sub>, F<sub>2</sub>, … is defined by the recurrence

F<sub>n</sub> = 1 if n = 1 or n = 2; F<sub>n</sub> = F<sub>n−1</sub> + F<sub>n−2</sub> otherwise (by convention F<sub>0</sub> = 0).

It models the idealized growth of a rabbit population (each pair breeds from the second month, gives birth to a new pair every month, and rabbits never die). We look at six algorithms computing F<sub>n</sub>.

### 1.2.1 Algorithm 1: closed formula

F<sub>n</sub> = (1/√5)(φ<sup>n</sup> − φ̂<sup>n</sup>), with φ = (1+√5)/2 ≈ 1.618 and φ̂ = (1−√5)/2 ≈ −0.618.

    1: function Fib1(int n) → int
    2:     return (1/√5)(φ^n − φ̂^n)    ▷ rounded to int

Problem: φ and φ̂ are irrational, so the machine works with approximations. Fib1(3) = 1.999863 ≈ 2 is fine, but Fib1(18) = 2583.023 ≈ 2583 ≠ F<sub>18</sub> = 2584. Increasing the precision does not solve the problem: we need another solution.

### 1.2.2 Algorithm 2: naive recursion

    1: function Fib2(int n) → int
    2:     if n ≤ 2 then
    3:         return 1
    4:     else
    5:         return Fib2(n − 1) + Fib2(n − 2)

*Memory.* Apparently Fib2 only stores n, but every recursive call allocates an **activation record** on the call stack (parameters, local variables, return address, return value). The memory used at time t depends on all the calls active at time t; the maximum number of active calls is the length of the longest root–leaf path of the **recursion tree**, so the memory is proportional to n in the worst case.

*Time.* Measuring seconds or machine instructions depends on the machine and on the language; the machine-independent approach is to **count elementary operations in the pseudocode**. Each call performs a constant number of operations, so the running time is proportional to T(n) = number of nodes in the recursion tree of Fib2(n). From the pseudocode we extract the recurrence

T(n) = 1 if n ≤ 2; T(n) = T(n−1) + T(n−2) + 1 if n \> 2

(one node plus the nodes of the two sub-trees). In the personal notes: *the T(n) formula counts how many recursive calls are made with input n, i.e. the number of nodes of the recursion tree.*

*Lower bound* (using T(n−1) ≥ T(n−2)): T(n) ≥ 2T(n−2) + 1 ≥ 4T(n−4) + 2 + 1 ≥ 8T(n−6) + 4 + 2 + 1 ≥ … ≥ 2<sup>k</sup> T(n−2k) + Σ<sub>i=0..k−1</sub> 2<sup>i</sup>. We stop when n − 2k ≤ 2, i.e. k ≈ ⌈n/2⌉ − 1, and get T(n) ≥ 2<sup>⌈n/2⌉</sup> − 1: the number of nodes is at least exponential, about 2<sup>n/2</sup>.

*Upper bound* (using T(n−2) ≤ T(n−1)): T(n) ≤ 2T(n−1) + 1 ≤ 4T(n−2) + 2 + 1 ≤ … ≤ 2<sup>k</sup> T(n−k) + Σ<sub>i=0..k−1</sub> 2<sup>i</sup>; stopping at k = n − 2 we get T(n) ≤ 2·2<sup>n−2</sup> − 1 \< 2<sup>n</sup>.

So Fib2 runs in exponential time. The problem: most Fibonacci numbers are computed many times, because the recursion does not remember the values already computed.

### 1.2.3 Algorithm 3: iterative solution with an array

    1: function Fib3(int n) → int
    2:     let F[1, …, n] be a new array of int    ▷ 1 time
    3:     F[1] = 1                                ▷ 1 time
    4:     F[2] = 1                                ▷ 1 time
    5:     for i = 3, …, n do                      ▷ n − 2 times
    6:         F[i] = F[i − 1] + F[i − 2]          ▷ n − 2 times
    7:     return F[n]                             ▷ 1 time

Total 4 + 3(n − 2) = 3n − 2 elementary operations: time proportional to n. Memory proportional to n (the array F). But we do not need to store the whole array.

### 1.2.4 Algorithm 4: constant memory

    1: function Fib4(int n) → int
    2:     a = 1
    3:     b = 1
    4:     for i = 3, …, n do
    5:         c = a + b
    6:         a = b
    7:         b = c
    8:     return b

3 + 5(n − 2) = 5n − 7 operations (more than Fib3, but the same order), and **constant memory**: five variables (n, i, a, b, c) whatever n is.

### 1.2.5 Algorithm 5: matrix power

Let A = \[\[1, 1\], \[1, 0\]\]. For every n ≥ 2, A<sup>n−1</sup> = \[\[F<sub>n</sub>, F<sub>n−1</sub>\], \[F<sub>n−1</sub>, F<sub>n−2</sub>\]\].

*Proof by induction.* Base case n = 2: A<sup>1</sup> = \[\[1, 1\], \[1, 0\]\] = \[\[F<sub>2</sub>, F<sub>1</sub>\], \[F<sub>1</sub>, F<sub>0</sub>\]\]. Inductive case: if A<sup>k−1</sup> = \[\[F<sub>k</sub>, F<sub>k−1</sub>\], \[F<sub>k−1</sub>, F<sub>k−2</sub>\]\] then A<sup>k</sup> = A<sup>k−1</sup>·A = \[\[F<sub>k</sub>+F<sub>k−1</sub>, F<sub>k</sub>\], \[F<sub>k−1</sub>+F<sub>k−2</sub>, F<sub>k−1</sub>\]\] = \[\[F<sub>k+1</sub>, F<sub>k</sub>\], \[F<sub>k</sub>, F<sub>k−1</sub>\]\].

**Mathematical induction** proves a property P for all natural numbers by proving a base case and the inductive case (if P holds for values ≤ n then it holds for n + 1). We may start from any initial value, and we may assume more than one previous case (e.g. P(n) and P(n+1) imply P(n+2)); then we need as many base cases.

    1: function Fib5(int n) → int
    2:     A = [[1,1],[1,0]]
    3:     for i = 3, …, n do
    4:         A = A ∗ [[1,1],[1,0]]      ▷ ∗ is the matrix product
    5:     return A[1][1]

Time proportional to n (n − 2 matrix products), constant memory: no improvement over Fib4 so far. Personal note: *we did not prove the running time or the memory of Algorithm 5; it is a new version of 3 and 4 and it is not faster than them.* The improvement comes from computing the power faster.

### 1.2.6 Algorithm 6: fast matrix power (exponentiation by squaring)

A<sup>n</sup> = (A<sup>n/2</sup>)<sup>2</sup> if n is even; A<sup>n</sup> = A·(A<sup>(n−1)/2</sup>)<sup>2</sup> if n is odd.

    1: function FibMatPow(int n) → FibMat
    2:     A = [[1,1],[1,0]]
    3:     if n > 1 then
    4:         M = FibMatPow(n/2)          ▷ integer division
    5:         A = M ∗ M
    6:         if n mod 2 ≠ 0 then
    7:             A = A ∗ [[1,1],[1,0]]
    8:     return A

    1: function Fib6(int n) → int
    2:     M = FibMatPow(n − 1)
    3:     return M[1][1]

About log<sub>2</sub> n recursive calls, each with constant work: time proportional to log n, memory proportional to log n (constant memory for each of the log n active calls).

### 1.2.7 Summary

|        | Fib1 | Fib2               | Fib3 | Fib4 | Fib5 | Fib6     |
|:-------|:-----|:-------------------|:-----|:-----|:-----|:---------|
| Time   | O(1) | Ω(2<sup>n/2</sup>) | O(n) | O(n) | O(n) | O(log n) |
| Memory | O(1) | O(n)               | O(n) | O(1) | O(1) | O(log n) |

We went from an exponential algorithm (unusable in practice) to a logarithmic one. All six compute the same function; what makes them usable or not is their efficiency.

### 1.2.8 Input value vs input size

We measured costs as functions of the input *value* n. Computer scientists prefer the input *size*: the number of bits needed to represent n, \|n\| = ⌈log<sub>2</sub> n⌉, so n ≈ 2<sup>\|n\|</sup>. In terms of input size, Fib3, Fib4, Fib5 take time O(2<sup>\|n\|</sup>) (exponential!), Fib2 becomes doubly exponential (Ω(2<sup>n/2</sup>) with n ≈ 2<sup>\|n\|</sup>), and Fib6 takes O(\|n\|). The actual running time does not change; only the way we express it.

---
> [[AADS 01 - How these notes are organized|← How these notes are organized]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 03 - Asymptotic notation|Asymptotic notation →]]
