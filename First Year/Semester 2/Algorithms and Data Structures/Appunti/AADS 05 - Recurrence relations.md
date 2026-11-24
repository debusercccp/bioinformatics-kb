---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 5
tags: [note, aads]
---

> [[AADS 04 - Computational complexity and amortized analysis|← Computational complexity and amortized analysis]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 06 - Sorting algorithms · The sorting problem + Incremental algorithms|Sorting algorithms · The sorting problem + Incremental algorithms →]]

# Recurrence relations

*Reference: CLRS Ch. 4.*

## 4.1 Preliminaries

A **recurrence relation** describes each element of a sequence in terms of the preceding ones (the Fibonacci recurrence T(n) = T(n−1) + T(n−2) + 1 is an example). The running time of a recursive algorithm is naturally described by a recurrence, and we want its asymptotic growth. Methods: iteration (with substitution), recursion tree, and the master theorem.

The same idea appears in dynamic programming and in bioinformatics: in Hidden Markov Models the Forward algorithm computes the probability of the observations up to time t, the Backward algorithm the probability of the remaining observations from t onward; both compute the values at time t from those at time t − 1, i.e. through a recurrence.

Recurrences of recursive algorithms often look like T(n) = Θ(1) for n = 1, T(n) = 2T(⌊n/3⌋) + O(n) for n \> 1. We simplify them:

1.  replace the asymptotic terms with positive expressions: 2T(⌊n/3⌋) + cn;
2.  use 1 instead of symbolic constants: 2T(⌊n/3⌋) + n;
3.  drop floors and ceilings, which do not affect the asymptotic behavior: T(n) = 2T(n/3) + n.

Note from class: *we normally do not keep asymptotic notation inside the recurrence; floors and ceilings do not change the result.*

## 4.2 Iteration method

Brute-force approach: substitute the recursive part of the equation again and again until a pattern related to the iteration step i appears, then find when the recursion stops.

**Example 1.** T(n) = 1 for n = 1, T(n) = T(n/2) + c for n \> 1. T(n) = T(n/2) + c = T(n/4) + 2c = T(n/8) + 3c = ⋯ = T(n/2<sup>i</sup>) + c·i. Recursion ends when n/2<sup>i</sup> = 1, i.e. i = log<sub>2</sub> n: T(n) = 1 + c log<sub>2</sub> n = Θ(log n). (Same result with c = 1.)

**Example 2.** T(n) = T(n/2) + n. T(n) = T(n/4) + n/2 + n = T(n/8) + n/4 + n/2 + n = ⋯ = T(n/2<sup>i</sup>) + n Σ<sub>k=0..i−1</sub> 1/2<sup>k</sup> = T(n/2<sup>i</sup>) + 2n(1 − 1/2<sup>i</sup>). With i = log<sub>2</sub> n: T(n) = 1 + 2n(1 − 1/n) = 2n − 1 = Θ(n).

Personal notes on the procedure: *substitute T(n) with T(n/2), so the next step gives T(n/4); the third row is an example and the fourth is the general formula at step i. Then find the maximum number of steps in terms of n: the recursion ends when the argument equals 1. Substitute that i into the general formula; finally replace every constant c with 1.*

<figure>
![[AADS-rId57.jpg|168]]
<figcaption aria-hidden="true"><p>Iteration method, steps 1–3 (personal notes)</p></figcaption>
</figure>

<figure>
![[AADS-rId60.jpg|223]]
<figcaption aria-hidden="true"><p>General expansion at step i (personal notes)</p></figcaption>
</figure>

<figure>
![[AADS-rId63.jpg|307]]
<figcaption aria-hidden="true"><p>Stopping condition (personal notes)</p></figcaption>
</figure>

<figure>
![[AADS-rId66.jpg|139]]
<figcaption aria-hidden="true"><p>Substitution of i and final result (personal notes)</p></figcaption>
</figure>

<figure>
![[AADS-rId69.jpg|307]]
<figcaption aria-hidden="true"><p>Final step: constants replaced by 1 (personal notes)</p></figcaption>
</figure>

## 4.3 Master theorem

The master method solves recurrences of the form T(n) = aT(n/b) + f(n), with a ≥ 1, b \> 1 constants and f(n) asymptotically positive: algorithms that divide a problem of size n into a subproblems of size n/b, with cost f(n) for dividing and combining. It does not apply to every recurrence (e.g. not to Fibonacci, nor to T(n) = T(n − 1) + …).

**Theorem (general form).** T(n) = 1 for n = 1, T(n) = aT(n/b) + f(n) for n \> 1. Then:

1.  if f(n) = O(n<sup>logb a − ε</sup>) for some ε \> 0, then T(n) = Θ(n<sup>logb a</sup>);
2.  if f(n) = Θ(n<sup>logb a</sup>), then T(n) = Θ(n<sup>logb a</sup> log n);
3.  if f(n) = Ω(n<sup>logb a + ε</sup>) for some ε \> 0, and a·f(n/b) ≤ c·f(n) for some c \< 1 and all large n, then T(n) = Θ(f(n)).

In all cases we compare f(n) with n<sup>logb a</sup>: if f is dominated the recursion wins; if they grow equally we multiply by log n; if f dominates, f wins. The regularity condition of case 3 is hard to remember, so in practice we use the simplified version.

**Theorem (simplified version, the one used at the exam).** T(n) = 1 for n ≤ 1, T(n) = aT(n/b) + c·n<sup>β</sup> for n \> 1, with a ≥ 1, b \> 1. Let **α = log<sub>b</sub> a**. Then:

1.  if α \> β: T(n) = Θ(n<sup>α</sup>);
2.  if α = β: T(n) = Θ(n<sup>α</sup> log n);
3.  if α \< β: T(n) = Θ(n<sup>β</sup>).

We do not need the exact value of α, only whether it is greater than, equal to or smaller than β. β is the exponent of n in the non-recursive cost: constant cost means β = 0, linear means β = 1, quadratic β = 2. (Notes: *compare α and β, the higher one wins and determines the solution.*)

**Examples.**

- T(n) = T(n/2) + c: a = 1, b = 2, α = log<sub>2</sub> 1 = 0 = β ⇒ Θ(log n).
- T(n) = T(n/2) + n: α = 0 \< 1 = β ⇒ Θ(n).
- T(n) = 3T(n/4) + cn<sup>2</sup>: α = log<sub>4</sub> 3 ≈ 0.79 \< 2 = β ⇒ Θ(n<sup>2</sup>).

**Recursive binary search.**

     1: function binsearch(int A[1 ⋯ n], int x, int i, int j) → int
     2:     if i > j then
     3:         return −1
     4:     else
     5:         m = (i + j)/2                 ▷ integer division
     6:         if A[m] == x then
     7:             return m
     8:         else if A[m] > x then
     9:             return binsearch(A, x, i, m − 1)
    10:         else
    11:             return binsearch(A, x, m + 1, j)

Called as binsearch(A, x, 1, n). Best case O(1). Worst case (x missing): T(n) = 1 for n = 0, T(n) = T(n/2) + 1 for n \> 0; α = 0 = β ⇒ Θ(log n).

**Tighter bound for the Fibonacci recurrence.** We proved 2<sup>n/2</sup> ≈ 1.41<sup>n</sup> ≤ T(n) ≤ 2<sup>n</sup>. In fact T(n) = 2F<sub>n</sub> − 1 (by induction), so T(n) = Θ(F<sub>n</sub>) = Θ(φ<sup>n</sup>) ≈ Θ(1.62<sup>n</sup>).

## 4.4 Exercises (from the slides)

| Recurrence | Master theorem | Iteration method |
|:---|:---|:---|
| T(n/4) + c | α = 0 = β ⇒ Θ(log n) | T(n/4<sup>i</sup>) + ci, i = log<sub>4</sub> n ⇒ Θ(log n) |
| 2T(n/4) + c | α = 1/2 \> 0 ⇒ Θ(√n) | 2<sup>i</sup>T(n/4<sup>i</sup>) + c Σ 2<sup>k</sup> = 2<sup>log4 n</sup> d + c(√n − 1) = Θ(√n) |
| 4T(n/4) + c | α = 1 \> 0 ⇒ Θ(n) | 4<sup>log4 n</sup> d + c(n − 1)/3 = Θ(n) |
| 8T(n/4) + c | α = 3/2 \> 0 ⇒ Θ(n<sup>3/2</sup>) = Θ(√(n<sup>3</sup>)) | n<sup>3/2</sup> d + c(n<sup>3/2</sup> − 1)/7 = Θ(√(n<sup>3</sup>)) |

(Useful identity: 2<sup>log4 n</sup> = √n and 8<sup>log4 n</sup> = n<sup>3/2</sup>, from a<sup>logb n</sup> = n<sup>logb a</sup>.)

**Ex. 5. FibMatPow (exponentiation by squaring).** One recursive call on n/2 plus constant work: T(n) = T(n/2) + 1, α = 0 = β ⇒ Θ(log n).

<figure>
![[AADS-rId74.jpg|212]]
<figcaption aria-hidden="true"><p>Exercise 5 solved in class (whiteboard)</p></figcaption>
</figure>

**Ex. 6. Exponentiation by cubing.** FibMatPow(n/3) and then M∗M∗M (times A or A<sup>2</sup> depending on n mod 3): T(n) = T(n/3) + 1 ⇒ Θ(log n). Not asymptotically faster than squaring, and more complex. (Notes: *the result means that the asymptotic rate is logarithmic.*)

**Ex. 7.**

     1: function mystery1(int n) → int
     2:     if n ≤ 1 then return 123
     3:     else
     4:         k = mystery2(n/2) + mystery1(n/3)
     5:         return k + mystery1(n/3)
     6: function mystery2(int n) → int
     7:     if n == 0 then return 321
     8:     else return 2 ∗ mystery2(n/4) − mystery2(n/4)

mystery2: two recursive calls on n/4 (the “2 ∗” is just a multiplication of the returned value, not two more calls): T’(n) = 2T’(n/4) + 1, α = 1/2 \> 0 ⇒ Θ(√n). mystery1: two recursive calls on n/3 plus a call to mystery2(n/2) of cost Θ(√n): T(n) = 2T(n/3) + n<sup>1/2</sup>, α = log<sub>3</sub> 2 ≈ 0.63 \> 0.5 = β ⇒ **Θ(n<sup>log3 2</sup>)**.

**Ex. 8.** mystery1(n) returns mystery2(n/2) + mystery1(n/2), and mystery2(n) returns 2 ∗ mystery2(n − 1). mystery2: T’(n) = T’(n − 1) + 1 (not solvable with the master theorem); by iteration T’(n) = T’(n − i) + i, ending at i = n − 1, so Θ(n). mystery1: T(n) = T(n/2) + n, α = 0 \< 1 ⇒ **Θ(n)**.

**Ex. 9.** mystery1 has a while loop with i = 1, 2, 4, … (i doubled while i ≤ n) that calls mystery2(n/2) twice; mystery2(n) runs a while loop of n iterations and calls itself twice on n/3. mystery2: T’(n) = 2T’(n/3) + n, α ≈ 0.63 \< 1 ⇒ Θ(n). The while loop in mystery1 stops at the iteration k with 2<sup>k</sup> \> n, i.e. k \> log<sub>2</sub> n: Θ(log n) iterations, each costing Θ(n/2) + Θ(n/2). Total **Θ(n log n)**.

**Ex. 10.** mystery1(n): a while loop with i = 1, 3, 5, … ≤ n (n/2 iterations), each calling mystery2(n/2), then three recursive calls mystery1(n/4). mystery2 costs Θ(n) as above, so the loop costs (n/2)·Θ(n/2) = Θ(n<sup>2</sup>). T(n) = 3T(n/4) + n<sup>2</sup>, α = log<sub>4</sub> 3 ≈ 0.79 \< 2 ⇒ **Θ(n<sup>2</sup>)**.

## 4.5 How to solve Exercise 1 at the exam (“mystery” functions)

These exercises are typically “useless” functions doing mysterious things inefficiently; some code is there only to confuse. Do not try to understand what they compute: detect the parts that contribute to the complexity.

1.  **Start from the innermost function** (mystery2), which is called by mystery1. Write its recurrence: count the recursive calls and their input (n/2, n/3, n − 1, …); everything else with constant cost gives β = 0, a loop of n iterations gives β = 1, and so on. Solve with the master theorem (or iteration if the input decreases by subtraction).
2.  **Then analyze mystery1**, where the cost of the line that calls mystery2 is not constant: it is the cost of mystery2 *on the argument passed at that iteration*.
3.  **Count loop iterations carefully**: a loop i = 1, 2, …, n runs n times; i = i·2 runs Θ(log n) times; i = i + 2 runs n/2 times; a loop up to a constant runs a constant number of times. If the argument changes at each iteration, the total is a summation.
4.  **Constants are distractors**: 2<sup>100</sup>·n is still Θ(n); a loop of 2<sup>100</sup> iterations is constant. Notes: *n·2<sup>100</sup> · n·2<sup>100</sup> = n<sup>2</sup>·2<sup>200</sup> grows as n<sup>2</sup> even if the constant is huge; don’t be fooled at the exam.*
5.  Use **Θ** when best, average and worst case collapse into one (the number of iterations is exactly known); use O when you only have an upper bound.

Useful summations:

- Σ<sub>i=1..n</sub> i = n(n+1)/2 = Θ(n<sup>2</sup>); Σ<sub>i=1..n</sub> (n − i) = Θ(n<sup>2</sup>).
- Σ<sub>i=0..k</sub> 2<sup>i</sup> = 2<sup>k+1</sup> − 1; Σ<sub>i≥0</sub> (1/2)<sup>i</sup> = 2 (geometric series).
- Σ<sub>i=1..n</sub> log i = log(n!) = Θ(n log n).
- Σ<sub>i=1..n</sub> 1/i ≤ 1 + ln n = Θ(log n) (harmonic sum).
- Σ<sub>i=1..n</sub> √i = Θ(n√n): upper bound n·√n; lower bound: the last n/2 terms are each ≥ √(n/2).
- If the loop index halves the argument (n/2, n/4, …) and the cost is linear in the argument: n + n/2 + n/4 + ⋯ ≤ 2n = Θ(n).

### 4.5.1 Solved exam exercises

**Exam 1 July 2026, Ex. 1.**

    1: function mystery1(int n) → int
    2:     x = 0
    3:     for i = 1, ⋯, n do
    4:         x = x + mystery2(log₂ i^100)
    5:     return x
    7: function mystery2(int n) → int
    8:     if n ≤ 0 then return 1
    9:     else return mystery2(n/2) + mystery2(n/2) + n² + n + 1

mystery2 makes two recursive calls on n/2, the rest is constant (n<sup>2</sup> + n + 1 is a computed *value*, not a cost!): T’(n) = 2T’(n/2) + 1, α = log<sub>2</sub> 2 = 1 \> 0 = β ⇒ T’(n) = Θ(n). In mystery1 the loop runs n times and iteration i costs T’(log<sub>2</sub> i<sup>100</sup>) = Θ(100 log i) = Θ(log i). Total: Σ<sub>i=1..n</sub> Θ(log i) = Θ(log Π i) = Θ(log n!) = **Θ(n log n)**.

**Exam 13 February 2026, Ex. 1.** mystery1 loops i = 1..n and calls mystery2(2<sup>100</sup> n/i); mystery2 makes three recursive calls on n/3 and returns … + n<sup>3</sup> + n<sup>2</sup> + n. mystery2: T’(n) = 3T’(n/3) + 1, α = 1 \> 0 ⇒ Θ(n). mystery1: Σ<sub>i=1..n</sub> Θ(2<sup>100</sup> n/i) = Θ(n Σ 1/i). Since the harmonic sum is ≤ 1 + ln n, the worst case is **O(n log n)** (in fact Θ(n log n)).

**Exam 14 November 2025, Ex. 1.** mystery1(n) returns mystery1(n − 1) + mystery2(n); mystery2(n) runs a loop of ∛n iterations and calls itself twice on n/4. mystery2: T’(n) = 2T’(n/4) + n<sup>1/3</sup>, α = 1/2 \> 1/3 = β ⇒ Θ(√n). mystery1: T(n) = T(n − 1) + √n (iteration method): T(n) = T(n − i) + Σ<sub>k=0..i−1</sub> √(n − k); with i = n, T(n) = 1 + Σ<sub>i=1..n</sub> √i = **Θ(n√n)** (upper bound Σ√i ≤ n√n; lower bound Σ<sub>i=n/2..n</sub> √i ≥ (n/2)√(n/2)).

**Exam 15 January 2026, Ex. 1.** mystery1 loops i = 1..n: x = mystery2(i), then search(A, x). mystery2: T’(n) = T’(n/2) + 1 ⇒ Θ(log n), so the calls cost Σ Θ(log i) = Θ(n log n). (a) Sorted A and binary search: n searches of Θ(log n) ⇒ total Θ(n log n). (b) Unsorted A and linear search: n searches of Θ(n) ⇒ Θ(n<sup>2</sup>) dominates ⇒ Θ(n<sup>2</sup>).

**Exam 28 October 2022, Ex. 1 (solved in class).** Recurrences T(n) = 2T(n/2) + 1 ⇒ Θ(n) by master theorem, and T(n) = T(n − 1) + n solved by iteration: T(n) = T(n − i) + Σ<sub>k=0..i−1</sub> (n − k); the cost is quadratic. Personal note: *on top of the summation we write i − 1 instead of i: changing Θ(n) into Θ(n − 1) does not change the result; the goal is to simplify the computation as much as possible.*

<figure>
![[AADS-rId78.jpg|212]]
<figcaption aria-hidden="true"><p>Exercise 1, exam 28/10/2022, solved in class</p></figcaption>
</figure>

**Exam 26 July 2024, Ex. 1 (needs disjoint sets).** mystery2 makes three recursive calls on n/9 plus constant work: T’(n) = 3T’(n/9) + 1, α = log<sub>9</sub> 3 = 1/2 \> 0 ⇒ Θ(√n). mystery1 creates n singletons with MAKE-SET, then for i = 1..n computes x = mystery2(i<sup>2</sup>) and y = mystery2(i<sup>2</sup>/4) and, if FIND-SET(D, x) ≠ FIND-SET(D, y), calls UNION(D, x, y). In the worst case there are n + 2n + n = 4n disjoint-set operations, which with union by rank and path compression cost Θ(n) overall. The calls cost Σ Θ(√(i<sup>2</sup>)) = Σ Θ(i) = Θ(n<sup>2</sup>) and Σ Θ(√(i<sup>2</sup>/4)) = Σ Θ(i/2) = Θ(n<sup>2</sup>). Total T(n) = Θ(n) + Θ(n<sup>2</sup>) + Θ(n<sup>2</sup>) = **Θ(n<sup>2</sup>)**.

<figure>
![[AADS-rId81.jpg|212]]
<figcaption aria-hidden="true"><p>Exercise 1, exam 26/07/2024 (whiteboard)</p></figcaption>
</figure>

<figure>
![[AADS-rId84.jpg|212]]
<figcaption aria-hidden="true"><p>Exercise 1, exam 26/07/2024, continued</p></figcaption>
</figure>

**Exam 24 July 2025 and 15 December 2025, Ex. 1 (needs string matching).** mystery(P, S) calls ESM(P\[1..i\], S) for i = 1..m. With brute force ESM (O(i·n) each): Σ O(i·n) = O(nm<sup>2</sup>). With KMP (Θ(i + n) each): Θ(nm + m<sup>2</sup>) = Θ(nm) assuming n ≥ m. With a suffix trie: preprocessing O(n<sup>2</sup>) + Σ O(i) = O(n<sup>2</sup> + m<sup>2</sup>). With a suffix array: preprocessing O(n) + Σ O(i log n) = O(n + m<sup>2</sup> log n).

### 4.5.2 Past exam exercises on this topic (A = analysis)

Computational complexity analysis, Exercise 1 of: 2022/06/24 F, 2022/07/21 F, 2022/10/28 F, 2022/11/30 F, 2023/01/16 F, 2023/02/06, 2023/06/29, 2023/07/24 (requires sorting algorithms) F, 2023/10/27, 2023/12/01, 2024/01/15, 2024/02/12, 2024/04/24, 2024/06/28, 2024/07/26 (requires disjoint sets), 2024/11/15 (requires hash tables), 2024/12/16 (requires graphs), 2025/02/14; plus the later exams 2025/06/03, 2025/07/01, 2025/07/24, 2025/11/14, 2025/12/15, 2026/01/15, 2026/02/13, 2026/07/01.

---
> [[AADS 04 - Computational complexity and amortized analysis|← Computational complexity and amortized analysis]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 06 - Sorting algorithms · The sorting problem + Incremental algorithms|Sorting algorithms · The sorting problem + Incremental algorithms →]]
