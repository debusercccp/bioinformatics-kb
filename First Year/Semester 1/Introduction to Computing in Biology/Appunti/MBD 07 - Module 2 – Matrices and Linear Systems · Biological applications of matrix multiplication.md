---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 7
tags: [note, mbd]
---

> [[MBD 06 - Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed|← Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 08 - Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion|Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion →]]

# Biological applications of matrix multiplication

### 2.3.1 Signal transduction cascade

A two-step phosphorylation cascade, ligand $(L) \rightarrow$ kinase A $\rightarrow$ kinase B. Each protein is in state 0 (inactive) or 1 (active), described by a **probability state vector** $s = \left\lbrack P\left( \text{inactive} \right),P\left( \text{active} \right) \right\rbrack^{T}$ summing to 1. Transition matrices, with $T_{A}(i,j) = P\left( A\text{ in state }i \mid L\text{ in state }j \right)$:

$$
T_{A} = \begin{pmatrix}
0.9 & 0.2 \\
0.1 & 0.8
\end{pmatrix},\quad\quad T_{B} = \begin{pmatrix}
0.8 & 0.05 \\
0.2 & 0.95
\end{pmatrix}
$$

Without signal A is 90% inactive; with signal, 80% active. If A is inactive B is only 20% active (basal noise); if A is active B is 95% active (strong amplification).

**End-to-end transmission** is the matrix product — and the order matters, $T_{B}$ acts *after* $T_{A}$:

$$
T_{B}T_{A} = \begin{pmatrix}
0.8 & 0.05 \\
0.2 & 0.95
\end{pmatrix}\begin{pmatrix}
0.9 & 0.2 \\
0.1 & 0.8
\end{pmatrix} = \begin{pmatrix}
0.725 & 0.20 \\
0.275 & 0.80
\end{pmatrix}
$$

> **Reading the result.** Columns are ligand states, rows are B states. Ligand OFF leaves B 27.5% active, ligand ON makes it 80% active: the cascade has a signal-to-background ratio of about 2.9. Note that each column sums to 1 — the product of two column-stochastic matrices is column-stochastic, which is why the composite is still a legitimate transition matrix. This is the entry point to Markov chains.

### 2.3.2 Age-structured populations: the Leslie matrix

A population split into juveniles $J(t)$ and adults $A(t)$, state vector $v(t) = \left\lbrack J(t),A(t) \right\rbrack^{T}$. Each adult produces $f$ juveniles per year (**fecundity**); a fraction $s$ of juveniles survive to adulthood (**survival**).

$$
v(t + 1) = Lv(t) = \begin{pmatrix}
0 & f \\
s & 0
\end{pmatrix}\begin{pmatrix}
J(t) \\
A(t)
\end{pmatrix}
$$

Fecundity sits in entry $(1,2)$ (adults make juveniles), survival in the sub-diagonal entry $(2,1)$.

**Forward projection.** With $v(0) = \lbrack 10,5\rbrack^{T}$, $f = 4$, $s = 0.5$:

$$
L = \begin{pmatrix}
0 & 4 \\
0.5 & 0
\end{pmatrix},\quad L^{2} = \begin{pmatrix}
2 & 0 \\
0 & 2
\end{pmatrix},\quad L^{3} = \begin{pmatrix}
0 & 8 \\
1 & 0
\end{pmatrix} \Longrightarrow v(3) = L^{3}v(0) = \begin{pmatrix}
40 \\
10
\end{pmatrix}
$$

**Backward projection.** Since $\det(L) = - fs \neq 0$, $L$ is invertible:

$$
L^{- 1} = \begin{pmatrix}
0 & 1/s \\
1/f & 0
\end{pmatrix} = \begin{pmatrix}
0 & 2 \\
0.25 & 0
\end{pmatrix},\quad\quad v(t - k) = \left( L^{- 1} \right)^{k}v(t) = \left( L^{k} \right)^{- 1}v(t)
$$

The identity $\left( L^{- 1} \right)^{k} = \left( L^{k} \right)^{- 1}$ is worth checking explicitly: $\left( L^{3} \right)^{- 1} = \begin{pmatrix}
0 & 1 \\
0.125 & 0
\end{pmatrix} = \left( L^{- 1} \right)^{3}$.

> **What the matrix powers are telling you.** $L^{2} = 2I$ means the population exactly doubles every *two* years while swapping nothing, which is why the trajectory looks like a staircase. The clean explanation only arrives with eigenvalues (§3.2): $\lambda = \pm \sqrt{2}$, and $\left( \sqrt{2} \right)^{2} = 2$.

---
> [[MBD 06 - Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed|← Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 08 - Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion|Module 2 – Matrices and Linear Systems · Determinants, minors, cofactors, inversion →]]
