---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 22
tags: [note, mbd]
---

> [[MBD 21 - Module 7 – Distributions|← Module 7 – Distributions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 23 - Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimisation|Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimisation →]]

# Module 8 — Exam Exercises: How to Solve Them

The practice exams (Practice 1–5) all have the same structure: **90 minutes, 5 exercises × 6 points = 30 points, no aids**. Answers may be left in exact form (fractions, square roots, $e$, $\pi$), but **every step must be written**: answers without derivation receive no credit. The five exercises are always of the same five types, in the same order:

| Exercise | Topic | Notes sections |
|:---|:---|:---|
| 1 | $2 \times 2$ matrix: determinant, inverse, eigenvalues, eigenvectors | §2.6, §3.4–3.5, §3.8 |
| 2 | Derivatives and optimisation: $f(x)$ in one variable **or** $g(x,y)$ in two variables | §4.4–4.5, §5.1–5.2 |
| 3 | Constrained optimisation with Lagrange multipliers | §5.4 |
| 4 | Probability: diagnostic test, Bayes’ theorem | §6.5, §8.4 |
| 5 | Distributions (binomial, Poisson) **or** covariance and correlation of two genes | §7.3–7.4, §8.5 |

Below, for each type: what is asked, the recipe step by step, a fully worked example from the practice exams, and the results of the other practice exams to check yourself.

## 8.1 Exercise 1 — 2 × 2 matrix

Typical questions: a) $\det(A)$, is $A$ invertible? b) $A^{- 1}$; c) eigenvalues; d) one eigenvector for each eigenvalue (sometimes: verify that they are orthogonal).

**Recipe** for $A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}$:

1.  **Determinant:** $\det(A) = ad - bc$. Write the conclusion: $\det(A) \neq 0 \Rightarrow$ invertible; $\det(A) = 0 \Rightarrow$ **not invertible (singular)**, and then do not compute the inverse.
2.  **Inverse:** swap the diagonal, change sign to the off-diagonal, divide by the determinant: $A^{- 1} = \frac{1}{\det(A)}\begin{pmatrix}
    d & - b \\
     - c & a
    \end{pmatrix}$. Check (mentally) one entry of $AA^{- 1} = I$.
3.  **Eigenvalues:** characteristic equation $\det(A - \lambda I) = (a - \lambda)(d - \lambda) - bc = 0$, i.e. $\lambda^{2} - Tr(A)\,\lambda + det(A) = 0$. Solve the second-degree equation. **Checks:** $\lambda_{1} + \lambda_{2} = Tr(A) = a + d$ and $\lambda_{1}\lambda_{2} = det(A)$. If $\det(A) = 0$, one eigenvalue is 0 and the other equals the trace.
4.  **Eigenvectors:** for each $\lambda_{i}$ write $\left( A - \lambda_{i}I \right)\overrightarrow{v} = \overrightarrow{0}$. The two equations are proportional (that is why $\det\left( A - \lambda_{i}I \right) = 0$), so use only the first one, $\left( a - \lambda_{i} \right)v_{1} + b\, v_{2} = 0$, choose a convenient value for one component and get the other. Any multiple $c\overrightarrow{v}$ is also an eigenvector. **Check:** compute $A\overrightarrow{v}$ and verify that it equals $\lambda_{i}\overrightarrow{v}$.
5.  **Orthogonality** (if asked): ${\overrightarrow{v}}_{1} \cdot {\overrightarrow{v}}_{2} = 0$. For a **symmetric** matrix ($b = c$) the eigenvectors of distinct eigenvalues are always orthogonal — useful as a check.

**Worked example (Practice 5).** $E = \begin{pmatrix}
5 & 2 \\
2 & 2
\end{pmatrix}$.

1)  $\det(E) = 5 \cdot 2 - 2 \cdot 2 = 6 \neq 0 \Rightarrow E$ is invertible.

2)  $E^{- 1} = \frac{1}{6}\begin{pmatrix}
    2 & - 2 \\
     - 2 & 5
    \end{pmatrix} = \begin{pmatrix}
    1/3 & - 1/3 \\
     - 1/3 & 5/6
    \end{pmatrix}$.

3)  $(5 - \lambda)(2 - \lambda) - 4 = 0 \Rightarrow \lambda^{2} - 7\lambda + 6 = 0 \Rightarrow (\lambda - 1)(\lambda - 6) = 0 \Rightarrow \lambda_{1} = 1,\ \lambda_{2} = 6$. Check: $1 + 6 = 7 = Tr(E)$, $1 \cdot 6 = 6 = det(E)$ ✓.

4)  $\lambda_{1} = 1$: $(5 - 1)v_{1} + 2v_{2} = 0 \Rightarrow v_{2} = - 2v_{1} \Rightarrow {\overrightarrow{v}}_{1} = (1, - 2)^{T}$. $\lambda_{2} = 6$: $(5 - 6)v_{1} + 2v_{2} = 0 \Rightarrow v_{1} = 2v_{2} \Rightarrow {\overrightarrow{v}}_{2} = (2,1)^{T}$. Check: $E(2,1)^{T} = (12,6)^{T} = 6(2,1)^{T}$ ✓; ${\overrightarrow{v}}_{1} \cdot {\overrightarrow{v}}_{2} = 2 - 2 = 0$ ✓.

**Other practice exams:**

| Matrix | det | Inverse | Eigenvalues | Eigenvectors |
|:---|:---|:---|:---|:---|
| $\begin{pmatrix}
3 & 1 \\
1 & 3
\end{pmatrix}$ (P1) | 8 | $\frac{1}{8}\begin{pmatrix}
3 & - 1 \\
 - 1 & 3
\end{pmatrix}$ | 2, 4 | $(1, - 1)$, $(1,1)$ |
| $\begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}$ (P2) | 3 | $\frac{1}{3}\begin{pmatrix}
2 & - 1 \\
 - 1 & 2
\end{pmatrix}$ | 1, 3 | $(1, - 1)$, $(1,1)$; orthogonal |
| $\begin{pmatrix}
4 & 2 \\
2 & 1
\end{pmatrix}$ (P3) | 0, singular | — | 0, 5 | $(1, - 2)$, $(2,1)$ |
| $\begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}$ (P4) | 0, singular | — | 0, 5 | $(2, - 1)$, $(1,2)$ |

*Note:* for a singular matrix the eigenvector of $\lambda = 0$ is a non-trivial element of the **null space** (§3.4): e.g. for P4 it is the vector found on the whiteboard, $c( - 2,1)^{T}$.

---
> [[MBD 21 - Module 7 – Distributions|← Module 7 – Distributions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 23 - Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimisation|Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimisation →]]
