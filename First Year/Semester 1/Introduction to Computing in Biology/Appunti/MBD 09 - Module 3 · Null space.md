---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 9
tags: [note, mbd]
---

> [[MBD 08 - Module 3 · The determinant as an area|← Module 3 · The determinant as an area]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 10 - Module 3 · Eigenvalues and eigenvectors|Module 3 · Eigenvalues and eigenvectors →]]

# Null space

In general, for an $m \times n$ matrix the null space is the set of $n$-valued vectors $\overrightarrow{b}$ with $A\overrightarrow{b} = \overrightarrow{0}$ ($m$ zeros); we consider only square matrices.

For $A \in \mathbb{R}^{n \times n}$, which vectors $\overrightarrow{v} \in \mathbb{R}^{n}$ satisfy $A\overrightarrow{v} = \overrightarrow{0}$? $\overrightarrow{v} = \overrightarrow{0}$ always does. Is there any $\overrightarrow{v} \neq \overrightarrow{0}$ that satisfies $A\overrightarrow{v} = \overrightarrow{0}$? If yes, $\overrightarrow{v} \in$ **null space**.

If $\det(A) \neq 0$, then $A^{- 1}$ exists ($\exists A^{- 1}$) and

$$
\underset{I}{\underbrace{A^{- 1}A}}\overrightarrow{v} = A^{- 1}\overrightarrow{0}\quad \Rightarrow \quad\overrightarrow{v} = \overrightarrow{0}
$$

**A non-trivial null space exists only if** $\det(A) = 0$.

*Example.* $A = \begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}$, $\det A = 0$ $\Rightarrow$ a non-trivial null space exists. We look for $\overrightarrow{v} = \left( v_{1},v_{2} \right)^{T}$ with $A\overrightarrow{v} = \overrightarrow{0}$:

$$
\begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}\begin{pmatrix}
v_{1} \\
v_{2}
\end{pmatrix} = \begin{pmatrix}
v_{1} + 2v_{2} \\
2v_{1} + 4v_{2}
\end{pmatrix} = \begin{pmatrix}
0 \\
0
\end{pmatrix}\quad \Rightarrow \quad\left\{ \begin{matrix}
v_{1} + 2v_{2} = 0 \\
2v_{1} + 4v_{2} = 0
\end{matrix} \right.\ \quad \Rightarrow \quad v_{1} = - 2v_{2}\quad \Rightarrow \quad\overrightarrow{v} = c\begin{pmatrix}
 - 2 \\
1
\end{pmatrix}\quad\forall c
$$

*Proof:* $\begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}\begin{pmatrix}
 - 2c \\
c
\end{pmatrix} = \begin{pmatrix}
 - 2c + 2c \\
 - 4c + 4c
\end{pmatrix} = \begin{pmatrix}
0 \\
0
\end{pmatrix}$. The null space is a line through the origin.

---
> [[MBD 08 - Module 3 · The determinant as an area|← Module 3 · The determinant as an area]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 10 - Module 3 · Eigenvalues and eigenvectors|Module 3 · Eigenvalues and eigenvectors →]]
