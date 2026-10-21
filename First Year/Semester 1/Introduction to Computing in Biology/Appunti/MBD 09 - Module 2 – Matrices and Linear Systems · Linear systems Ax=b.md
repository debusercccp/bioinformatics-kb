---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 9
tags: [note, mbd]
---

> [[MBD 08 - Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion|← Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 10 - Module 3 · Matrices as linear operators|Module 3 · Matrices as linear operators →]]

# Linear systems $\mathbf{Ax}\mathbf{=}\mathbf{b}$

A system of $m$ linear equations in $n$ variables is written $Ax = b$, where the coefficient matrix has as many rows as equations and as many columns as variables. For $m = n$ and $|A| \neq 0$ the unique solution is

$$
x = A^{- 1}b
$$

### 2.5.1 What the slides do not cover: when $\mathbf{\det}\left( \mathbf{A} \right)\mathbf{=}\mathbf{0}$

The slides treat only the invertible case. But in omics the normal situation is $p \gg n$ — far more variables than equations — so the singular case is the rule, not the exception. Two of the three $3 \times 3$ exercise systems on the slides are in fact singular, and the question “solvable or not?” cannot be answered without the following.

**Rank.** The **rank** of a matrix is the number of linearly independent rows, equivalently of linearly independent columns, equivalently the size of the largest non-vanishing minor. *How to compute:* row-reduce and count the non-zero rows.

**Rank–nullity theorem.** For $A \in \mathbb{R}^{m \times n}$,

$$
\operatorname{rank}(A) + \dim\ker(A) = n
$$

where $\ker(A)$ is the null space of §3.2. A square $A$ is invertible iff $\operatorname{rank}(A) = n$ iff $\dim\ker(A) = 0$ iff $\det(A) \neq 0$ — these are four ways of saying the same thing.

**Rouché–Capelli theorem.** Let $\left\lbrack A|b \right\rbrack$ be the augmented matrix. Then:

| Condition | Conclusion |
|----|----|
| $\operatorname{rank}(A) < rank\left( \lbrack A \mid b\rbrack \right)$ | **no solution** (inconsistent) |
| $\operatorname{rank}(A) = rank\left( \lbrack A \mid b\rbrack \right) = n$ | **exactly one** solution |
| $\operatorname{rank}(A) = rank\left( \lbrack A \mid b\rbrack \right) = r < n$ | **infinitely many**, with $n - r$ free parameters |

The general solution in the third case is *one particular solution plus any element of the null space*:

$$
x = x_{\text{part}} + \sum_{k = 1}^{n - r}t_{k}\, v_{k},\quad\quad v_{k} \in ker(A)
$$

> **This is the right mental model for the singular case.** “$\det A = 0$” alone tells you only that the unique-solution route is closed; it does not say whether there are none or infinitely many. Only comparing the two ranks does.

### 2.5.2 Least squares: what to do when there is no exact solution

When $m > n$ (more measurements than parameters, the usual experimental situation) the system is **overdetermined** and generally has *no* exact solution. One then minimises $\parallel Ax - b \parallel^{2}$, whose solution satisfies the **normal equations**

$$
A^{T}Ax = A^{T}b \Longrightarrow \widehat{x} = \left( A^{T}A \right)^{- 1}A^{T}b
$$

valid whenever $A$ has full column rank. The matrix $A^{+} = \left( A^{T}A \right)^{- 1}A^{T}$ is the **Moore–Penrose pseudo-inverse**. This single formula is the matrix form of the linear regression derived coordinate-by-coordinate in Module 7, and it generalises immediately to many predictors — which the scalar derivation does not.

> **Connection worth holding on to.** $\widehat{x}$ makes $A\widehat{x}$ the **orthogonal projection** of $b$ onto the column space of $A$ (§1.2.5), and the residual $b - A\widehat{x}$ is orthogonal to that space. Least squares *is* projection. When $A^{T}A$ is singular or near-singular — collinear predictors — one adds $\lambda I$ to it, which is exactly ridge regression, $\widehat{x} = \left( A^{T}A + \lambda I \right)^{- 1}A^{T}b$.

---
> [[MBD 08 - Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion|← Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 10 - Module 3 · Matrices as linear operators|Module 3 · Matrices as linear operators →]]
