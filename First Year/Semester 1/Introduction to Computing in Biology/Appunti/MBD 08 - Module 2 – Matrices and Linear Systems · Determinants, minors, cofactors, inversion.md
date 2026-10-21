---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 8
tags: [note, mbd]
---

> [[MBD 07 - Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication|← Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 09 - Module 2 – Matrices and Linear Systems · Linear systems Ax=b|Module 2 – Matrices and Linear Systems · Linear systems Ax=b →]]

# Determinants, minors, cofactors, inversion

### 2.4.1 Order 2

$$
|A| = \begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix} = a_{11}a_{22} - a_{12}a_{21},\quad\quad A^{- 1} = \frac{1}{|A|}\begin{pmatrix}
a_{22} & - a_{12} \\
 - a_{21} & a_{11}
\end{pmatrix}
$$

defined iff $|A| \neq 0$. The $2 \times 2$ inverse recipe in words: **swap the diagonal, negate the off-diagonal, divide by the determinant.**

### 2.4.2 Arbitrary order $\mathbf{n}$ — how to compute by hand

- **Minor** $M_{ij}$**:** the determinant of the $(n - 1) \times (n - 1)$ submatrix obtained by deleting row $i$ and column $j$.
- **Cofactor** $C_{ij}$**:** $C_{ij} = ( - 1)^{i + j}M_{ij}$. The sign pattern alternates like a chessboard, starting with $+$ at position $(1,1)$.
- **Laplace cofactor expansion**, along any row $i$ or any column $j$:

$$
\det(A) = \sum_{j = 1}^{n}a_{ij}C_{ij} = \sum_{i = 1}^{n}a_{ij}C_{ij}
$$

**Practical advice:** expand along the row or column containing the most zeros — each zero kills a whole minor computation.

### 2.4.3 Properties of determinants

| \# | Property |
|----|----|
| 1 | A zero row or column $\Rightarrow |A| = 0$. |
| 2 | Swapping two rows changes the **sign** of $|A|$. |
| 3 | Two identical rows $\Rightarrow |A| = 0$. |
| 4 | Multiplying **one** row by $\lambda$ scales the determinant by $\lambda$. |
| 5 | For an $n \times n$ matrix, $\det(\lambda A) = \lambda^{n}\det(A)$. |
| 6 | Adding a scalar multiple of one row to another leaves $|A|$ **unchanged**. |
| 7 | $\left| A^{T} \right| = |A|$. |
| 8 | For a triangular matrix, $|A| = \prod_{i = 1}^{n}a_{ii}$ (product of the diagonal). |
| 9 | Binet’s theorem: $|AB| = |A||B|$. |

> **Properties 4 and 5 are the one that trips people up.** Property 4 scales *a single row*; property 5 scales *all* $n$ *rows at once*, hence the $\lambda^{n}$. They are consistent, not contradictory.
>
> **Property 6 is the engine of Gaussian elimination**, and the practical way to get a determinant for $n \geq 4$: row-reduce to triangular form (tracking sign flips from property 2) and multiply the diagonal, by property 8. Cofactor expansion costs $O(n!)$ operations; elimination costs $O\left( n^{3} \right)$. No software ever uses cofactors.

### 2.4.4 General inversion via the adjugate

- **Cofactor matrix** $A^{c}$**:** replace each $a_{ij}$ by its cofactor $C_{ij}$.
- **Adjugate** $A^{a} = adj(A)$**:** the **transpose** of the cofactor matrix, $A^{a} = \left( A^{c} \right)^{T}$. Forgetting the transpose is the most common error.
- **Theorem.** A square matrix is invertible **iff** $|A| \neq 0$, and then

$$
A^{- 1} = \frac{1}{|A|}\, adj(A) = \frac{1}{|A|}\,\left( A^{c} \right)^{T}
$$

*Worked example.* For $A = \begin{pmatrix}
1 & 2 & 3 \\
0 & 4 & 5 \\
1 & 0 & 6
\end{pmatrix}$, $|A| = 22$ and

$$
A^{c} = \begin{pmatrix}
24 & 5 & - 4 \\
 - 12 & 3 & 2 \\
 - 2 & - 5 & 4
\end{pmatrix} \Longrightarrow A^{- 1} = \frac{1}{22}\begin{pmatrix}
24 & - 12 & - 2 \\
5 & 3 & - 5 \\
 - 4 & 2 & 4
\end{pmatrix} = \begin{pmatrix}
12/11 & - 6/11 & - 1/11 \\
5/22 & 3/22 & - 5/22 \\
 - 2/11 & 1/11 & 2/11
\end{pmatrix}
$$

**Always verify by computing** $AA^{- 1}$ **and checking you get** $I$**.**

---
> [[MBD 07 - Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication|← Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 09 - Module 2 – Matrices and Linear Systems · Linear systems Ax=b|Module 2 – Matrices and Linear Systems · Linear systems Ax=b →]]
