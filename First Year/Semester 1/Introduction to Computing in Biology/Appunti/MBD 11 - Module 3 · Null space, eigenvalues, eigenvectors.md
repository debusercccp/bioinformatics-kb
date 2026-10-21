---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 11
tags: [note, mbd]
---

> [[MBD 10 - Module 3 · Matrices as linear operators|← Module 3 · Matrices as linear operators]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 12 - Module 3 · Complex numbers … What is missing – the singular value decomposition|Module 3 · Complex numbers … What is missing – the singular value decomposition →]]

# Null space, eigenvalues, eigenvectors

### 3.2.1 Null space (kernel)

For an $m \times n$ matrix $A$, the null space is the set of vectors $b \in \mathbb{R}^{n}$ with $Ab = 0$. The zero vector always qualifies; the question is whether anything else does.

For a square $A$: if $A$ is invertible, $Ab = 0 \Rightarrow A^{- 1}Ab = 0 \Rightarrow b = 0$, so the null space is trivial. **A non-trivial null space exists iff** $A$ **is singular**, $\det(A) = 0$.

*Example.* $A = \begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}$, $|A| = 0$. The system $b_{1} + 2b_{2} = 0$, $2b_{1} + 4b_{2} = 0$ is degenerate — one equation, really — and every vector $b = \alpha(2, - 1)^{T}$ belongs to the null space.

> **Dimensional accounting (missing from the slides).** By rank–nullity (§2.5.1), $\dim\ker(A) = n - \operatorname{rank}(A)$. In the example $\operatorname{rank} = 1$ and $n = 2$, so the null space is a **line** — exactly the one-parameter family found. This tells you in advance how many free parameters to expect, instead of discovering it while solving.

### 3.2.2 Eigenvectors and eigenvalues

In general a matrix changes both the magnitude and the direction of a vector. For certain vectors it changes only the magnitude, leaving the direction unchanged (or exactly reversed). These are the **eigenvectors**.

A non-zero vector $x \neq 0$ is an eigenvector of a square $A$ if

$$
Ax = \lambda x \Leftrightarrow (A - \lambda I)x = 0
$$

The scalar $\lambda$ is the **eigenvalue**. The zero vector is never an eigenvector, but $\lambda = 0$ *can* be an eigenvalue.

**How to compute, step by step.**

1.  Write the **characteristic equation** $\det(A - \lambda I) = 0$ — the condition for $(A - \lambda I)$ to have a non-trivial null space.
2.  Solve it for $\lambda$. It is a degree-$n$ polynomial, so there are $n$ roots counted with multiplicity (over $\mathbb{C}$).
3.  For each $\lambda_{i}$, solve the homogeneous system $\left( A - \lambda_{i}I \right)x_{i} = 0$. The solutions form the **eigenspace** of $\lambda_{i}$; any non-zero element is an eigenvector.
4.  Eigenvectors are defined **up to a scalar** — if $x$ is one, so is $5x$. Normalise if you need uniqueness.

*Worked example.* $A = \begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}$.

$$
\det(\lambda I - A) = (\lambda - 2)(\lambda + 5) + 12 = \lambda^{2} + 3\lambda + 2 = (\lambda + 1)(\lambda + 2) = 0 \Longrightarrow \lambda = - 1,\, - 2
$$

For $\lambda = - 1$: $\begin{pmatrix}
3 & - 12 \\
1 & - 4
\end{pmatrix}x = 0 \Rightarrow x_{1} = 4x_{2} \Rightarrow x^{(1)} = t(4,1)^{T}$. For $\lambda = - 2$: $\begin{pmatrix}
4 & - 12 \\
1 & - 3
\end{pmatrix}x = 0 \Rightarrow x_{1} = 3x_{2} \Rightarrow x^{(2)} = s(3,1)^{T}$.

*Example with multiplicity.* $A = diag\text{-}like\begin{pmatrix}
2 & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix}$ gives $(\lambda - 2)^{3} = 0$, so $\lambda = 2$ with **algebraic multiplicity** 3. Solving $(A - 2I)x = 0$ gives $x = s(1,0,0)^{T} + t(0,0,1)^{T}$: only **two** independent eigenvectors. The **geometric multiplicity** (2) is smaller than the algebraic one (3).

> **The distinction the slides never name, and which decides everything in §3.4.** - **Algebraic multiplicity** of $\lambda$ = its multiplicity as a root of the characteristic polynomial. - **Geometric multiplicity** of $\lambda$ = $\dim\ker(A - \lambda I)$ = number of independent eigenvectors for it.
>
> Always $1 \leq$ geometric $\leq$ algebraic. When geometric $<$ algebraic for some $\lambda$, the matrix is called **defective** and is **not diagonalisable**. This is the single criterion behind every answer in the diagonalisation exercise.

### 3.2.3 Properties of eigenvalues

| Property |
|----|
| $\sum_{i = 1}^{n}\lambda_{i} = Tr(A)$ (sum equals the trace) |
| $\prod_{i = 1}^{n}\lambda_{i} = det(A)$ (product, with multiplicity, equals the determinant) |
| $A$ is singular $\Leftrightarrow$ at least one $\lambda = 0$ |
| the eigenvalues of a triangular or diagonal matrix are its diagonal entries |
| if $\lambda$ is an eigenvalue of $A$, then $1/\lambda$ is one of $A^{- 1}$ (when invertible) |
| if $\lambda$ is an eigenvalue of $A$, then $k\lambda$ is one of $kA$ |
| if $\lambda$ is an eigenvalue of $A$, then $\lambda^{k}$ is one of $A^{k}$ |
| if $\lambda$ is an eigenvalue of $A$, then $\lambda$ is one of $A^{T}$ |

> **Use the first two as a free check.** Having computed eigenvalues, verify that they sum to the trace and multiply to the determinant. Two cheap arithmetic checks catch almost every algebra slip.

### 3.2.4 Eigen-decomposition of the Leslie matrix

For $L = \begin{pmatrix}
0 & 4 \\
0.5 & 0
\end{pmatrix}$: $\det(L - \lambda I) = \lambda^{2} - 2 = 0 \Rightarrow \lambda_{1,2} = \pm \sqrt{2}$.

- $\lambda_{1} = + \sqrt{2} \Rightarrow b^{(1)} = \left( 2\sqrt{2},\, 1 \right)^{T}$: the biologically meaningful solution ($J > 0$, $A > 0$), a constantly growing population with a **stable juvenile/adult ratio** of $2\sqrt{2} \approx 2.83$.
- $\lambda_{2} = - \sqrt{2} \Rightarrow b^{(2)} = \left( - 2\sqrt{2},\, 1 \right)^{T}$: non-physical ($J < 0$), producing oscillations.

Any initial vector decomposes as $v_{0} = \alpha b^{(1)} + \beta b^{(2)}$ and evolves as

$$
v_{t} = \alpha\lambda_{1}^{t}b^{(1)} + \beta\lambda_{2}^{t}b^{(2)}
$$

> **Why this is the central idea of the whole module.** Computing $L^{100}v_{0}$ directly is 100 matrix multiplications; in the eigenbasis it is two scalar exponentials. More importantly, the **dominant eigenvalue** (largest $|\lambda|$) governs the long-run behaviour: $|\lambda| > 1$ means exponential growth, $|\lambda| < 1$ extinction, $|\lambda| = 1$ a stable population. Its eigenvector is the **stable age distribution** the population converges to regardless of where it started. Here $\left| \lambda_{1} \right| = \left| \lambda_{2} \right| = \sqrt{2}$ exactly — a degenerate case caused by the strictly alternating life cycle, which is why the trajectory oscillates instead of settling.
>
> This is the **Perron–Frobenius** setting, and the same mathematics gives the stationary distribution of a Markov chain, the equilibrium of the signal cascade in §2.3.1, and PageRank.

---
> [[MBD 10 - Module 3 · Matrices as linear operators|← Module 3 · Matrices as linear operators]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 12 - Module 3 · Complex numbers … What is missing – the singular value decomposition|Module 3 · Complex numbers … What is missing – the singular value decomposition →]]
