---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 25
tags: [note, mbd]
---

> [[MBD 24 - Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem|← Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]]

# Exercise 5 — Distributions or correlation

### 8.5.1 Binomial or Poisson

Typical questions: a) which distribution, $E\lbrack X\rbrack$ and $Var\lbrack X\rbrack$; b) $P(X = k)$; c) $P(X \geq k)$ or $P(X \leq k)$.

**Recognise the distribution:**

- **Binomial** $X \sim Bin(n,p)$: a fixed number $n$ of independent trials, each “success” with probability $p$ (e.g. $n$ offspring of a cross $Aa \times Aa$, $p = 1/4$ for $aa$). $P(X = k) = \binom{n}{k}p^{k}(1 - p)^{n - k}$, $E\lbrack X\rbrack = np$, $Var\lbrack X\rbrack = np(1 - p)$ (§7.3).
- **Poisson** $X \sim Poisson(\lambda)$: number of rare events with a given **average** $\lambda$ (mutations per exon, SNVs per exon). $P(X = k) = \frac{\lambda^{k}}{k!}e^{- \lambda}$, $E\lbrack X\rbrack = Var\lbrack X\rbrack = \lambda$ (§7.4).

**Recipe for the probabilities:**

- $P(X \leq k) = P(0) + P(1) + \ldots + P(k)$: sum the terms.
- $P(X \geq k) = 1 - P(X \leq k - 1)$: use the **complement** (much shorter).
- Remember $0! = 1$, $\lambda^{0} = 1$, $\binom{n}{0} = 1$; leave $e^{- \lambda}$ and fractions exact.

**Worked example (Practice 1).** $Aa \times Aa$, $p = 1/4$, $n = 6$ offspring, $X$ = number of $aa$.

1)  $X \sim Bin(6,1/4)$; $E\lbrack X\rbrack = 6 \cdot \frac{1}{4} = \frac{3}{2}$; $Var\lbrack X\rbrack = 6 \cdot \frac{1}{4} \cdot \frac{3}{4} = \frac{9}{8}$.

2)  $P(X = 0) = \left( \frac{3}{4} \right)^{6} = \frac{729}{4096}$.

3)  $P(X = 1) = \binom{6}{1}\frac{1}{4}\left( \frac{3}{4} \right)^{5} = 6 \cdot \frac{243}{4096} = \frac{1458}{4096}$; $P(X \geq 2) = 1 - P(0) - P(1) = 1 - \frac{729}{4096} - \frac{1458}{4096} = \frac{1909}{4096}$.

**Poisson (Practice 3,** $\lambda = 2$**):** $E\lbrack X\rbrack = Var\lbrack X\rbrack = 2$; $P(X = 0) = e^{- 2}$; $P(X = 1) = 2e^{- 2}$; $P(X \leq 1) = 3e^{- 2}$. **(Practice 5,** $\lambda = 1$**):** $P(0) = e^{- 1}$, $P(1) = e^{- 1}$, $P(2) = \frac{e^{- 1}}{2}$, $P(X \leq 2) = \frac{5}{2}e^{- 1}$.

### 8.5.2 Covariance and Pearson correlation of two genes

*Covariance and correlation have not been written on the whiteboard yet; the formulas are from the slides (7 – Distributions, 8 – Correlation and Regression), with the* $n - 1$ *denominator used in the slides and in the solution keys.*

Typical questions: a) sample means; b) sample covariance; c) Pearson $r$ and its interpretation.

**Recipe** — build a table with one row per sample:

1.  **Means:** $M_{A} = \frac{1}{n}\sum_{i}^{}A_{i}$, $M_{B} = \frac{1}{n}\sum_{i}^{}B_{i}$.

2.  **Deviations:** $A_{i} - M_{A}$ and $B_{i} - M_{B}$ (check: each column of deviations sums to 0).

3.  **Covariance:** sum of the products of the deviations, divided by $n - 1$:

$$
cov(A,B) = \frac{\sum_{i}^{}\left( A_{i} - M_{A} \right)\left( B_{i} - M_{B} \right)}{n - 1}
$$

4.  **Standard deviations:** $\sigma_{A}^{2} = \frac{\sum_{i}^{}\left( A_{i} - M_{A} \right)^{2}}{n - 1}$ (the squares of the deviations, same denominator), same for $B$.

5.  **Pearson correlation:**

$$
r = \frac{cov(A,B)}{\sigma_{A}\,\sigma_{B}} \in \lbrack - 1,1\rbrack
$$

6.  **Interpretation:** $r \approx 1$ strong positive linear co-expression (the genes go up and down together); $r \approx - 1$ strong negative (one up, the other down); $r \approx 0$ no **linear** relation (not necessarily independence: independent $\Rightarrow cov = 0$, but not vice versa).

**Worked example (Practice 2).** Gene A: 1, 3, 2, 5, 4; Gene B: 2, 4, 3, 6, 5 ($n = 5$).

| Sample | $A$ | $B$ | $A - M_{A}$ | $B - M_{B}$ | product | $\left( A - M_{A} \right)^{2}$ | $\left( B - M_{B} \right)^{2}$ |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | 2 | −2 | −2 | 4 | 4 | 4 |
| 2 | 3 | 4 | 0 | 0 | 0 | 0 | 0 |
| 3 | 2 | 3 | −1 | −1 | 1 | 1 | 1 |
| 4 | 5 | 6 | 2 | 2 | 4 | 4 | 4 |
| 5 | 4 | 5 | 1 | 1 | 1 | 1 | 1 |
| sum | 15 | 20 | 0 | 0 | 10 | 10 | 10 |

1)  $M_{A} = 15/5 = 3$, $M_{B} = 20/5 = 4$. b) $cov(A,B) = 10/4 = 5/2$. c) $\sigma_{A}^{2} = \sigma_{B}^{2} = 10/4 = 5/2$, $r = \frac{5/2}{\sqrt{5/2 \cdot 5/2}} = 1$: perfect positive linear co-expression ($B = A + 1$ in every sample).

**Practice 4:** $J$ = 4, 8, 6, 2, 10 ($M_{J} = 6$), $K$ = 3, 7, 5, 6, 4 ($M_{K} = 5$); deviations $- 2,2,0, - 4,4$ and $- 2,2,0,1, - 1$; products $4 + 4 + 0 - 4 - 4 = 0 \Rightarrow cov = 0$, $r = 0$: no linear correlation between the two genes.

## 8.6 Checklist for the exam

- Write **every** step: formula first, then numbers, then the conclusion in words (“→ invertible”, “→ local maximum”, “negative concentration, discarded”).
- Leave results exact ($1/e$, $\sqrt{2}$, $98/593$, $3e^{- 2}$) unless a percentage is asked.
- **Matrices:** check eigenvalues with trace and determinant, eigenvectors with $A\overrightarrow{v} = \lambda\overrightarrow{v}$.
- **Derivatives:** respect the domain ($x > 0$ with $\ln$); evaluate the value in $f$, not in $f'$.
- **Lagrange:** always write $g(x,y) = 0$ explicitly; justify the choice of the sign of $\lambda$.
- **Bayes:** $P( + )$ has **two** terms; $P\left( \overline{D} \right) = 1 - P(D)$; with counts, use the table.
- **Distributions:** “at least” → complement; Poisson has $E = Var = \lambda$.
- **Correlation:** divide by $n - 1$; the deviations must sum to 0; $r$ must be in $\lbrack - 1,1\rbrack$.

---
> [[MBD 24 - Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem|← Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]]
