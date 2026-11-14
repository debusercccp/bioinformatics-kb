---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 6
tags: [note, mbd]
---

> [[MBD 05 - Module 2 – Matrices · Sum + Row-by-column product|← Module 2 – Matrices · Sum + Row-by-column product]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 07 - Module 3 · Matrices as linear maps + Rotation matrix|Module 3 · Matrices as linear maps + Rotation matrix →]]

# Transpose matrix

For $A \in \mathbb{R}^{n \times m}$, the transpose $A^{t} \in \mathbb{R}^{m \times n}$ swaps rows and columns:

$$
A = \begin{pmatrix}
1 & 2 \\
3 & 1 \\
0 & 2
\end{pmatrix},\quad\quad A^{t} = \begin{pmatrix}
1 & 3 & 0 \\
2 & 1 & 2
\end{pmatrix},\quad\quad\left( A^{t} \right)^{t} = A
$$

For $A = \left\lbrack a_{ij} \right\rbrack$, $A^{t} = \left\lbrack b_{ij} \right\rbrack$ with $b_{ij} = a_{ji}$; $A^{t}$ and $A$ are conformable for the product in both directions. Symmetric means $a_{ji} = a_{ij}$ for all $i,j$; $A + A^{t}$ is always symmetric, since $\left( A + A^{t} \right)^{t} = A^{t} + A$.

Properties: $\left( A^{t} \right)^{t} = A$; $(\lambda A)^{t} = \lambda A^{t}$; $(A + B)^{t} = A^{t} + B^{t}$; $(AB)^{t} = B^{t}A^{t}$.

If $A \in \mathbb{R}^{n \times n}$ and $A^{t} = A$, $A$ is **symmetric**, e.g. $A = \begin{pmatrix}
1 & 2 \\
2 & 3
\end{pmatrix} = A^{t}$.

## 2.6 Inverse matrix

$I \in \mathbb{R}^{n \times n}$ satisfies $IA = AI = A$ for all $A \in \mathbb{R}^{n \times n}$. With numbers, $1 \cdot a = a \cdot 1 = a$, and the inverse $a^{- 1}$ satisfies $a^{- 1} \cdot a = a \cdot a^{- 1} = 1$ if $a \neq 0$. For $A \in \mathbb{R}^{n \times n}$: can we find $A^{- 1} \in \mathbb{R}^{n \times n}$ so that

$$
A^{- 1}A = AA^{- 1} = I\ ?
$$

If possible, $A^{- 1}$ is the **inverse matrix**.

If two square matrices satisfy $AB = BA = I$, $B$ is the inverse of $A$ ($B = A^{- 1}$) and $A$ is the inverse of $B$ ($A = B^{- 1}$). Not every square matrix has an inverse. Property: $(AB)^{- 1} = B^{- 1}A^{- 1}$, since $(AB)\left( B^{- 1}A^{- 1} \right) = A\left( BB^{- 1} \right)A^{- 1} = I$ and $\left( B^{- 1}A^{- 1} \right)(AB) = B^{- 1}\left( A^{- 1}A \right)B = I$.

*Example.*

$$
A = \begin{pmatrix}
2 & 1 \\
1 & 0
\end{pmatrix},\quad A^{- 1} = \begin{pmatrix}
0 & 1 \\
1 & - 2
\end{pmatrix}:\quad\quad AA^{- 1} = \begin{pmatrix}
2 & 1 \\
1 & 0
\end{pmatrix}\begin{pmatrix}
0 & 1 \\
1 & - 2
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} = I,\quad\quad A^{- 1}A = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} = I
$$

### 2.6.1 Determinant of a $\mathbf{2}\mathbf{\times}\mathbf{2}$ matrix

For $A \in \mathbb{R}^{n \times n}$ with $n = 2$, the determinant (written $\det(A)$ or $|A|$) is the product of the main diagonal minus the product of the other diagonal:

$$
A = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix},\quad\quad\det(A) = a_{11}a_{22} - a_{12}a_{21}
$$

*Note:* on the whiteboard it appears as $\det(A) = \parallel A \parallel$; the usual notation is $|A|$ (it is not a norm).

The determinant is a **number**. Example: $\begin{vmatrix}
1 & 2 \\
3 & 4
\end{vmatrix} = 1 \cdot 4 - 2 \cdot 3 = - 2$.

Properties (true for square matrices of any order): if every element of a row (column) is zero, $|A| = 0$; $\left| A^{t} \right| = |A|$; $|AB| = |A||B|$.

### 2.6.2 Inverse of a $\mathbf{2}\mathbf{\times}\mathbf{2}$ matrix

$$
A^{- 1} = \frac{1}{\det(A)}\begin{pmatrix}
a_{22} & - a_{12} \\
 - a_{21} & a_{11}
\end{pmatrix}
$$

(swap the diagonal elements, change sign to the off-diagonal ones, divide by the determinant). *Proof:*

$$
A\, A^{- 1} = \frac{1}{\det(A)}\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}\begin{pmatrix}
a_{22} & - a_{12} \\
 - a_{21} & a_{11}
\end{pmatrix} = \frac{1}{\det(A)}\begin{pmatrix}
a_{11}a_{22} + a_{12}\left( - a_{21} \right) & - a_{11}a_{12} + a_{12}a_{11} \\
a_{21}a_{22} - a_{22}a_{21} & - a_{21}a_{12} + a_{22}a_{11}
\end{pmatrix} = \frac{1}{\det(A)}\begin{pmatrix}
\det(A) & 0 \\
0 & \det(A)
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

$$
A^{- 1}\text{ exists}\quad \Leftrightarrow \quad\det(A) \neq 0
$$

If $A$ has null determinant its inverse cannot be defined. *Example from the slides:* $A = \begin{pmatrix}
 - 1 & 0 \\
1 & 2
\end{pmatrix}$, $\det(A) = - 2$, $A^{- 1} = \frac{1}{- 2}\begin{pmatrix}
2 & 0 \\
 - 1 & - 1
\end{pmatrix} = \begin{pmatrix}
 - 1 & 0 \\
1/2 & 1/2
\end{pmatrix}$.

## 2.7 Orthogonal matrices

If $A^{- 1}$ exists and $A^{- 1} = A^{t}$, $A$ is **orthogonal**.

Equivalently, $AA^{t} = A^{t}A = I$. Orthogonal matrices represent **rotations** (§3.2). The determinant of an orthogonal matrix is $\pm 1$: from $AA^{t} = I$, $|A|\left| A^{t} \right| = |A|^{2} = 1$.

---
> [[MBD 05 - Module 2 – Matrices · Sum + Row-by-column product|← Module 2 – Matrices · Sum + Row-by-column product]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 07 - Module 3 · Matrices as linear maps + Rotation matrix|Module 3 · Matrices as linear maps + Rotation matrix →]]
