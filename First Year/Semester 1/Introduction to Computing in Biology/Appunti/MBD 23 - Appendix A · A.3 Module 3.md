---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 23
tags: [note, mbd]
---

> [[MBD 22 - Appendix A · A.2 Module 2|← Appendix A · A.2 Module 2]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 24 - Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6|Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6 →]]

# A.3 Module 3

### A.3.1 Eigenvalues and eigenvectors (slide 135) — corrected

> **All four answers differ from the earlier draft**, which transcribed the matrices incorrectly (reading $\begin{pmatrix}
> 1 & 0 \\
> 5 & 3
> \end{pmatrix}$ as $\begin{pmatrix}
> 0 & 1 \\
> 3 & 5
> \end{pmatrix}$, and so on). The matrices as printed on the slide are below.

$M_{1} = \begin{pmatrix}
1 & 0 \\
5 & 3
\end{pmatrix}$**.** Lower triangular, so the eigenvalues are read straight off the diagonal: $\lambda_{1} = 1$, $\lambda_{2} = 3$. (Check: sum $= 4 = Tr$, product $= 3 = det$.)

- $\lambda = 1$: $\left( M_{1} - I \right)x = \begin{pmatrix}
  0 & 0 \\
  5 & 2
  \end{pmatrix}x = 0 \Rightarrow 5x_{1} + 2x_{2} = 0 \Rightarrow v_{1} = (2, - 5)^{T}$.
- $\lambda = 3$: $\left( M_{1} - 3I \right)x = \begin{pmatrix}
   - 2 & 0 \\
  5 & 0
  \end{pmatrix}x = 0 \Rightarrow x_{1} = 0 \Rightarrow v_{2} = (0,1)^{T}$.

$M_{2} = \begin{pmatrix}
1 & 0 \\
0 & 3
\end{pmatrix}$**.** Diagonal: $\lambda_{1} = 1$ with $v_{1} = (1,0)^{T}$, $\lambda_{2} = 3$ with $v_{2} = (0,1)^{T}$. The standard basis vectors are the eigenvectors — a diagonal matrix is already in its own eigenbasis.

$M_{3} = \begin{pmatrix}
1 & 1 \\
 - 1 & 1
\end{pmatrix}$**.** $\det\left( M_{3} - \lambda I \right) = (1 - \lambda)^{2} + 1 = 0 \Rightarrow \lambda_{1,2} = 1 \pm i$. **Complex eigenvalues**, with $v_{1,2} = (1, \pm i)^{T}$. Geometrically (§3.3) this is a rotation by $45^{\circ}$ scaled by $\sqrt{2}$: no real direction is left fixed, hence no real eigenvector.

$M_{4} = \begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}$**.** Symmetric, so real eigenvalues and orthogonal eigenvectors are guaranteed. $\det\left( M_{4} - \lambda I \right) = (1 - \lambda)^{2} - 4 = 0 \Rightarrow \lambda_{1} = 3$, $\lambda_{2} = - 1$.

- $\lambda = 3$: $v_{1} = (1,1)^{T}$. — $\lambda = - 1$: $v_{2} = (1, - 1)^{T}$. Indeed $\langle v_{1},v_{2}\rangle = 0$, as the spectral theorem requires.

(Shortcut for any $\begin{pmatrix}
a & b \\
b & a
\end{pmatrix}$: eigenvalues $a \pm b$ with eigenvectors $(1,1)^{T}$ and $(1, - 1)^{T}$.)

### A.3.2 Diagonalisation (slide 153) — corrected

> The earlier draft again worked from mis-transcribed matrices. The six as printed on the slide:

$A_{1} = \begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}$ **— DIAGONALISABLE (orthogonally).** Symmetric, $\lambda_{1} = 3$, $\lambda_{2} = - 1$:

$$
U = \begin{pmatrix}
1/\sqrt{2} & 1/\sqrt{2} \\
1/\sqrt{2} & - 1/\sqrt{2}
\end{pmatrix},\quad\quad U^{T}A_{1}U = \begin{pmatrix}
3 & 0 \\
0 & - 1
\end{pmatrix}
$$

$A_{2} = \begin{pmatrix}
1 & 0 \\
2 & 1
\end{pmatrix}$ **— NOT diagonalisable (defective).** $\lambda = 1$ with algebraic multiplicity 2, but $A_{2} - I = \begin{pmatrix}
0 & 0 \\
2 & 0
\end{pmatrix}$ has \operatorname{rank} 1, so the geometric multiplicity is $2 - 1 = 1$: only one independent eigenvector, $(0,1)^{T}$. A classic shear matrix.

$A_{3} = \begin{pmatrix}
1 & 1 \\
 - 1 & 1
\end{pmatrix}$ **— not diagonalisable over** $\mathbb{R}$**, diagonalisable over** $\mathbb{C}$**.** Eigenvalues $1 \pm i$, distinct, so over $\mathbb{C}$: $\Lambda = diag(1 + i,1 - i)$ with $U = \begin{pmatrix}
1 & 1 \\
i & - i
\end{pmatrix}$.

$A_{4} = \begin{pmatrix}
4 & 1 & 0 \\
1 & - 1 & 0 \\
0 & 0 & 3
\end{pmatrix}$ **— DIAGONALISABLE (orthogonally).** Block-diagonal and **symmetric**. The $2 \times 2$ block gives $\lambda^{2} - 3\lambda - 5 = 0$, so

$$
\lambda_{1,2} = \frac{3 \pm \sqrt{29}}{2} \approx 4.1926,\  - 1.1926,\quad\quad\lambda_{3} = 3
$$

Three distinct real eigenvalues. (Check: sum $= 3 + 3 = 6 = Tr$ ✓.)

$A_{5} = \begin{pmatrix}
1 & 0 & 0 \\
1 & 2 & 0 \\
0 & 5 & 3
\end{pmatrix}$ **— DIAGONALISABLE.** Lower triangular with three **distinct** diagonal entries, so $\lambda = 1,2,3$ and distinct eigenvalues guarantee independent eigenvectors. $\Lambda = diag(1,2,3)$.

$A_{6} = \begin{pmatrix}
2 & 0 & 0 \\
1 & 2 & 0 \\
0 & 5 & 1
\end{pmatrix}$ **— NOT diagonalisable (defective).** Lower triangular with $\lambda = 2$ (algebraic multiplicity 2) and $\lambda = 1$. For $\lambda = 2$:

$$
A_{6} - 2I = \begin{pmatrix}
0 & 0 & 0 \\
1 & 0 & 0 \\
0 & 5 & - 1
\end{pmatrix}
$$

has rank 2, so the geometric multiplicity of $\lambda = 2$ is $3 - 2 = 1 < 2$. Only two independent eigenvectors in total, fewer than the order 3.

> **The pattern across the six.** Distinct eigenvalues ($A_{3}$, $A_{4}$, $A_{5}$) or symmetry ($A_{1}$, $A_{4}$) always suffice. Failure occurs only with a **repeated** eigenvalue whose eigenspace is too small ($A_{2}$, $A_{6}$) — and triangular matrices make this easy to spot, since the eigenvalues are the diagonal entries: look for a repeated one, then compute the rank of $A - \lambda I$.

---
> [[MBD 22 - Appendix A · A.2 Module 2|← Appendix A · A.2 Module 2]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 24 - Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6|Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6 →]]
