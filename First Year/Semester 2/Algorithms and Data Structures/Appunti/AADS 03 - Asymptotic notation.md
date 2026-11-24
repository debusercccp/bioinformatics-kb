---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 3
tags: [note, aads]
---

> [[AADS 02 - Introduction to algorithms – the Fibonacci example|← Introduction to algorithms – the Fibonacci example]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 04 - Computational complexity and amortized analysis|Computational complexity and amortized analysis →]]

# Asymptotic notation

*Reference: CLRS Ch. 3.*

## 2.1 Why asymptotic notation

We want to analyze running time and memory as functions of the input size. Seconds and megabytes depend on the machine and on the language, so we use a measure of the **asymptotic behavior**: it ignores multiplicative and additive constants and lower-order terms, describes how fast time and memory grow with the input size, and lets us compare algorithms independently of the hardware.

A **cost function** f(n) ≥ 0 is the amount of resources (time or memory) used by an algorithm on inputs of size n ≥ 0. Typically n is an integer and f(n) is real-valued. We are interested in the growth rate of f(n), ignoring constant factors and low-order terms.

*Example.* Algorithm A costs f<sub>A</sub>(n) = 10<sup>2</sup> n, algorithm B costs f<sub>B</sub>(n) = 10<sup>−2</sup> n<sup>2</sup>. For small n (up to 10<sup>4</sup>) B is faster, but beyond that A wins, and the gap grows without bound: for large inputs the linear algorithm is always better, whatever the constants. In class: *A has linear running time, B quadratic; asymptotically A is better.*

## 2.2 The five notations

**Big-O (asymptotic upper bound).** O(g(n)) = { f(n) \| ∃ c \> 0, n<sub>0</sub> ≥ 0 such that ∀ n ≥ n<sub>0</sub>, f(n) ≤ c·g(n) }. O(g(n)) is the set of functions with the same or smaller order of growth than g(n). With abuse of notation we write f(n) = O(g(n)) instead of f(n) ∈ O(g(n)).

*Example.* f(n) = 3n<sup>2</sup> + 10n = O(n<sup>2</sup>): we need 3n<sup>2</sup> + 10n ≤ cn<sup>2</sup>, i.e. c ≥ 3 + 10/n. For n<sub>0</sub> = 1 any c ≥ 13 works; we could also choose n<sub>0</sub> = 10 and c = 4.

**Big-Omega (asymptotic lower bound).** Ω(g(n)) = { f(n) \| ∃ c \> 0, n<sub>0</sub> ≥ 0 such that ∀ n ≥ n<sub>0</sub>, f(n) ≥ c·g(n) }: functions with the same or higher order of growth.

*Example.* n<sup>3</sup> + 2n<sup>2</sup> = Ω(n<sup>2</sup>): we need n + 2 ≥ c, true for every 0 \< c ≤ 2 and n ≥ 0.

**Theta (asymptotic equivalence).** Θ(g(n)) = { f(n) \| ∃ c<sub>1</sub>, c<sub>2</sub> \> 0, n<sub>0</sub> ≥ 0 such that ∀ n ≥ n<sub>0</sub>, c<sub>1</sub>g(n) ≤ f(n) ≤ c<sub>2</sub>g(n) }. **Theorem.** f(n) = Θ(g(n)) if and only if f(n) = O(g(n)) and f(n) = Ω(g(n)).

*Example.* n<sup>3</sup> + 2n<sup>2</sup> = Θ(n<sup>3</sup>): we need c<sub>1</sub> ≤ 1 + 2/n ≤ c<sub>2</sub>; with n<sub>0</sub> = 1, c<sub>1</sub> = 1, c<sub>2</sub> = 3.

**Little-o (strict upper bound).** o(g(n)) = { f(n) \| ∀ c \> 0, ∃ n<sub>0</sub> ≥ 0 such that ∀ n ≥ n<sub>0</sub>, f(n) \< c·g(n) }. The difference with O: f = O(g) means f ≤ cg for *some* constant c; f = o(g) means f \< cg for *all* constants c. For every g, g ≠ o(g) (e.g. n<sup>2</sup> ≠ o(n<sup>2</sup>) but n<sup>2</sup> = O(n<sup>2</sup>)). If f = o(g) then f = O(g); the converse is false in general.

**Little-omega (strict lower bound).** ω(g(n)) = { f(n) \| ∀ c \> 0, ∃ n<sub>0</sub> ≥ 0 such that ∀ n ≥ n<sub>0</sub>, f(n) \> c·g(n) }. g ≠ ω(g); f = ω(g) implies f = Ω(g), not conversely.

**Intuitive comparison between O and o (personal notes).** Think of O(n) as a big set of functions: n, 5n, log n, √n, constants. All of them are eventually bounded by some constant times n. Inside it there is a smaller set o(n) with the functions *strictly* smaller than n (log n, √n, 1) but not n itself. So o(n) ⊂ O(n).

## 2.3 Asymptotic notation and limits

The order of growth can be compared through the limit of the ratio, when the limit exists:

- lim<sub>n→∞</sub> f(n)/g(n) = 0 ⇒ f(n) = o(g(n)) ⇒ f(n) = O(g(n));
- lim<sub>n→∞</sub> f(n)/g(n) = ∞ ⇒ f(n) = ω(g(n)) ⇒ f(n) = Ω(g(n));
- lim<sub>n→∞</sub> f(n)/g(n) = k \> 0 ⇒ f(n) = Θ(g(n)).

In class: *if the limit goes to 0 the growth of g is higher than that of f.* Usually limits are the fastest way to compare two functions; when the limit does not exist we go back to the definitions.

**Intuitive interpretation** (analogy with real numbers): f = O(g) ~ f ≤ g; f = o(g) ~ f \< g; f = Ω(g) ~ f ≥ g; f = ω(g) ~ f \> g; f = Θ(g) ~ f = g.

Unlike real numbers, **not all growth rates are comparable**. f(n) = n and g(n) = n<sup>sin(n)+1</sup>: f ≠ O(g) because when sin(n) = −1, g(n) = 1; f ≠ Ω(g) because when sin(n) = 1, g(n) = n<sup>2</sup>. Plotted, n<sup>sin(n)+1</sup> oscillates forever above and below n (in the notes: *the curve never stays above or below the other function*).

## 2.4 Properties and rules

- **Transitivity:** f = O(g) and g = O(h) ⇒ f = O(h); same for Ω, Θ, o, ω.
- **Reflexivity:** f = O(f); same for Ω and Θ, but not for o and ω.
- **Symmetry:** f = Θ(g) ⇔ g = Θ(f).
- **Transpose symmetry:** f = O(g) ⇔ g = Ω(f); f = o(g) ⇔ g = ω(f).
- **Sum:** f<sub>1</sub> = O(g<sub>1</sub>), f<sub>2</sub> = O(g<sub>2</sub>) ⇒ f<sub>1</sub> + f<sub>2</sub> = O(g<sub>1</sub> + g<sub>2</sub>) (the largest term dominates).
- **Product:** f<sub>1</sub>·f<sub>2</sub> = O(g<sub>1</sub>·g<sub>2</sub>).
- **Constants:** f = O(g), a \> 0 ⇒ a·f = O(g). Multiplication by a positive constant does not change the growth rate.

**Asymptotic notation in equations.** 2n<sup>2</sup> + Θ(n) means 2n<sup>2</sup> + f(n) for some f(n) ∈ Θ(n) (e.g. 3n + 1). 2n<sup>2</sup> + Θ(n) = Θ(n<sup>2</sup>) means: for every f(n) ∈ Θ(n), 2n<sup>2</sup> + f(n) ∈ Θ(n<sup>2</sup>).

## 2.5 Order of growth (most common)

From slowest to fastest growth:

| Order | Name |
|:---|:---|
| O(1) | constant |
| O(log n) | logarithmic |
| O(log<sup>k</sup> n), k ≥ 1 | polylogarithmic |
| O(n<sup>k</sup>), 0 \< k \< 1 | sublinear (e.g. √n) |
| O(n) | linear |
| O(n log n) | pseudolinear (linearithmic) |
| O(n<sup>2</sup>), O(n<sup>3</sup>), O(n<sup>k</sup>) | quadratic, cubic, polynomial |
| O(c<sup>n</sup>), c \> 1 | exponential |
| O(n!) | factorial |
| O(n<sup>n</sup>) | exponential with base n |

Notation: log n = log<sub>2</sub> n and log<sup>k</sup> n = (log n)<sup>k</sup>. Remember (class note): *if the algorithm is fast its cost function grows slowly, and vice versa.*

## 2.6 Exercises (from the slides)

**Ex. 1. Is 6n<sup>2</sup> = Ω(n<sup>3</sup>)?** We would need 6n<sup>2</sup> ≥ cn<sup>3</sup>, i.e. c ≤ 6/n; for any fixed c \> 0 there is n with 6/n \< c. False. With limits: lim 6n<sup>2</sup>/n<sup>3</sup> = lim 6/n = 0, so 6n<sup>2</sup> = o(n<sup>3</sup>) and 6n<sup>2</sup> ≠ Ω(n<sup>3</sup>).

**Ex. 2. Is 10n<sup>3</sup> + 2n<sup>2</sup> + 7 = O(n<sup>3</sup>)?** For n ≥ 1, 10n<sup>3</sup> + 2n<sup>2</sup> + 7 ≤ 10n<sup>3</sup> + 2n<sup>3</sup> + 7n<sup>3</sup> = 19n<sup>3</sup>: true with c = 19, n<sub>0</sub> = 1. With limits: the ratio tends to 10 \> 0, so it is Θ(n<sup>3</sup>) ⊆ O(n<sup>3</sup>).

**Ex. 3. Is (2 + (−1)<sup>n</sup>)n<sup>2</sup> = Θ(n<sup>2</sup>)?** We need c<sub>1</sub> ≤ 2 + (−1)<sup>n</sup> ≤ c<sub>2</sub>: true for c<sub>1</sub> = 1, c<sub>2</sub> = 3, n<sub>0</sub> = 0. True. Here the limit is *inconclusive*: the ratio oscillates between 1 and 3 and has no limit, so we must use the definition.

**Ex. 4. True or false?**

1.  1325n<sup>2</sup> + 12n + 1 = Θ(n<sup>3</sup>): ratio → 0, so it is o(n<sup>3</sup>). **False.**
2.  76n<sup>3</sup> = O(n<sup>3</sup>): ratio → 76 \> 0. **True.**
3.  n<sup>2</sup> log n = O(n<sup>2</sup>): ratio = log n → ∞, so ω(n<sup>2</sup>). **False.**
4.  3<sup>n</sup> = O(2<sup>n</sup>): ratio = 1.5<sup>n</sup> → ∞. **False.**
5.  2<sup>n+100</sup> = O(2<sup>n</sup>): ratio = 2<sup>100</sup> \> 0, so Θ(2<sup>n</sup>). **True.**
6.  log n = O(n): by de l’Hôpital, lim (1/(n ln 2))/1 = 0. **True.**
7.  n = O(n log n): ratio 1/log n → 0. **True.**
8.  n<sup>2</sup> = O(n log n): ratio n/log n → ∞. **False.**
9.  log n<sup>2</sup> = Θ(log n): log n<sup>2</sup> = 2 log n, ratio → 2. **True** (use the logarithm property log a<sup>b</sup> = b log a).
10. (n + 1)n/2 = Θ(n<sup>2</sup>): ratio → 1/2. **True.**

Class notes on this exercise: the first relation is false; in the second the two functions have the same growth rate; in the third one grows faster than the other (the limit contains a log n that tends to +∞); logarithmic growth is quite slow; for the ninth use the logarithm property.

**Ex. 5.** (1) For every a, b \> 1, log<sub>a</sub> n = Θ(log<sub>b</sub> n): log<sub>a</sub> n = log<sub>b</sub> n / log<sub>b</sub> a and log<sub>b</sub> a is a nonzero constant. **The base of a logarithm does not matter asymptotically.** (2) For any a, b \> 0, log<sup>a</sup> n = O(n<sup>b</sup>): first lim log n / n<sup>b</sup> = lim (1/(n ln 2)) / (b n<sup>b−1</sup>) = 0 by de l’Hôpital, so log n = o(n<sup>b</sup>); the general case follows because log<sup>a</sup> n = O(n<sup>b</sup>) is equivalent to log n = O(n<sup>b/a</sup>). **Any polylogarithm is smaller than any polynomial.**

**Ex. 6. log n! = Θ(n log n).** Upper bound: n! ≤ n<sup>n</sup> ⇒ log n! ≤ n log n. Lower bound: n! ≥ n(n−1)⋯(n/2) ≥ (n/2)<sup>n/2</sup> ⇒ log n! ≥ (n/2) log(n/2) = Ω(n log n).

**Ex. 7.** (1) For 1 \< a \< b, a<sup>n</sup> = O(b<sup>n</sup>): lim (a/b)<sup>n</sup> = 0 since a/b \< 1. (2) For a \> 0, n<sup>log a</sup> = Θ(a<sup>log n</sup>): in fact a<sup>log n</sup> = n<sup>log a</sup> (take log<sub>2</sub> of both sides: log n · log a in both cases).

**Ex. 8 (CLRS 3-2).** For k ≥ 1, c \> 1, ε \> 0, say whether A is O, o, Ω, ω, Θ of B:

| A                 | B                  | O   | o   | Ω   | ω   | Θ   |
|:------------------|:-------------------|:----|:----|:----|:----|:----|
| log<sup>k</sup> n | n<sup>ε</sup>      | yes | yes | no  | no  | no  |
| n<sup>k</sup>     | c<sup>n</sup>      | yes | yes | no  | no  | no  |
| √n                | n<sup>sin n</sup>  | no  | no  | no  | no  | no  |
| 2<sup>n</sup>     | 2<sup>n/2</sup>    | no  | no  | yes | yes | no  |
| n<sup>log c</sup> | c<sup>log n</sup>  | yes | no  | yes | no  | yes |
| log(n!)           | log(n<sup>n</sup>) | yes | no  | yes | no  | yes |

---
> [[AADS 02 - Introduction to algorithms – the Fibonacci example|← Introduction to algorithms – the Fibonacci example]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 04 - Computational complexity and amortized analysis|Computational complexity and amortized analysis →]]
