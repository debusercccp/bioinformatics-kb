---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 6
tags: [note, mbd]
---

> [[MBD 05 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|← Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 07 - Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication|Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication →]]

# Definitions and special types

A **matrix** $A \in \mathbb{R}^{m \times n}$ is a rectangular array of $m \cdot n$ numbers $a_{ij}$ in $m$ rows ($i = 1,\ldots,m$) and $n$ columns ($j = 1,\ldots,n$). The first subscript is the row, the second the column.

> **Biological example.** A gene expression matrix has $m \approx 20,000$ rows (genes) and $k \approx 10$–$1000$ columns (samples); $a_{ij}$ is the expression of gene $i$ in sample $j$ (counts, CPM, TPM).

| Type | Definition and properties |
|----|----|
| **Square** | $m = n$ (order $n$). Elements $a_{ii}$ form the main diagonal. **Trace**: $Tr(A) = \sum_{i = 1}^{n}a_{ii}$. |
| **Column / row** | $n = 1$ (column vector, $m \times 1$) or $m = 1$ (row vector, $1 \times n$). An $n$-valued vector *is* an $n \times 1$ matrix. |
| **Equal** ($A = B$) | same size **and** $a_{ij} = b_{ij}$ for all $i,j$. |
| **Zero** ($0$) | every entry $a_{ij} = 0$. |
| **Upper / lower triangular** | square with $a_{ij} = 0$ for $i > j$ (upper) or $i < j$ (lower). |
| **Diagonal** ($D$) | square with $a_{ij} = 0$ for all $i \neq j$; written $diag\left\lbrack a_{11},\ldots,a_{nn} \right\rbrack$. |
| **Identity** ($I$) | diagonal with $a_{ii} = 1$. Satisfies $AI = IA = A$. |
| **Transpose** ($A^{T}$) | swap rows and columns, $\left( A^{T} \right)_{ij} = a_{ji}$. Properties: $\left( A^{T} \right)^{T} = A$, $(A + B)^{T} = A^{T} + B^{T}$, $(\lambda A)^{T} = \lambda A^{T}$, $(AB)^{T} = B^{T}A^{T}$. |
| **Symmetric** | $A^{T} = A$ ($a_{ji} = a_{ij}$). For any square $A$, $A + A^{T}$ is symmetric. |
| **Skew-symmetric** | $A^{T} = - A$. For any square $A$, $A - A^{T}$ is skew-symmetric. |
| **Inverse** ($A^{- 1}$) | square $B$ with $AB = BA = I$. Property: $(AB)^{- 1} = B^{- 1}A^{- 1}$. |
| **Orthogonal** | $AA^{T} = A^{T}A = I \Leftrightarrow A^{T} = A^{- 1}$. Represents rotations and reflections; $\det(A) = \pm 1$. |

> **Why the orthogonal case matters (missing from the slides).** An orthogonal matrix **preserves norms and inner products**:
>
> ``` math
> \parallel Ux \parallel = \parallel x \parallel ,\quad\quad\langle Ux,Uy\rangle = \langle x,y\rangle
> ```
>
> because $(Ux)^{T}(Uy) = x^{T}U^{T}Uy = x^{T}y$. This is *why* the change to an orthonormal basis in PCA (Module 8) does not distort distances or angles: it is a rigid rotation of the cloud of points, not a deformation of it.

**Proof that** $\det(A) = \pm 1$ **for orthogonal** $A$**.** From $AA^{T} = I$ and the properties below, $\left| AA^{T} \right| = |A|\left| A^{T} \right| = |A|^{2} = 1$, so $|A| = \pm 1$.

## 2.2 Operations — how they are performed

| Operation | Conformability | Recipe | Output size |
|----|----|----|----|
| $A \pm B$ | **same** $m \times n$ | $c_{ij} = a_{ij} \pm b_{ij}$ | $m \times n$ |
| $\lambda A$ | none | $c_{ij} = \lambda a_{ij}$ | $m \times n$ |
| $AB$ | cols of $A$ = rows of $B$ | $c_{ij} = \sum_{k = 1}^{p}a_{ik}b_{kj}$ | $m \times n$ |
| $A^{T}$ | none | $\left( A^{T} \right)_{ij} = a_{ji}$ | $n \times m$ |

**The product, step by step.** $A \in \mathbb{R}^{m \times p}$, $B \in \mathbb{R}^{p \times n}$, $C = AB \in \mathbb{R}^{m \times n}$. To get the entry $c_{ij}$: take **row** $i$ **of** $A$, take **column** $j$ **of** $B$, multiply them element by element and sum. In other words, $c_{ij}$ is the inner product of the $i$-th row of $A$ with the $j$-th column of $B$. The dimension check $(m \times p)(p \times n) \rightarrow (m \times n)$ is the first thing to verify, every time.

*Worked example.*

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 4
\end{pmatrix},\quad B = \begin{pmatrix}
 - 1 & 2 \\
2 & 3 \\
5 & 0
\end{pmatrix},\quad C = AB = \begin{pmatrix}
18 & 8 \\
22 & 3
\end{pmatrix}
$$

since $c_{11} = 1( - 1) + 2(2) + 3(5) = 18$, $c_{12} = 1(2) + 2(3) + 3(0) = 8$, $c_{21} = 0( - 1) + 1(2) + 4(5) = 22$, $c_{22} = 0(2) + 1(3) + 4(0) = 3$. The reverse product has a different shape entirely:

$$
BA = \begin{pmatrix}
 - 1 & 0 & 5 \\
2 & 7 & 18 \\
5 & 10 & 15
\end{pmatrix} \in \mathbb{R}^{3 \times 3}
$$

**Two special shapes.**

- **Row** $\times$ **column** ($1 \times m$ by $m \times 1$): a $1 \times 1$ **scalar** — this is exactly the dot product, $A \cdot B = A^{T}B = B^{T}A$.
- **Column** $\times$ **row** ($m \times 1$ by $1 \times m$): an $m \times m$ **outer product** matrix. Note $A \cdot B^{T}$ and $B \cdot A^{T}$ are two *different* $m \times m$ matrices.

**Properties.** $A(B + C) = AB + AC$, $(A + B)C = AC + BC$, $A(BC) = (AB)C$, $\lambda(A + B) = \lambda A + \lambda B$, $A + B = B + A$, $A + (B + C) = (A + B) + C$.

**Three caveats that break ordinary algebra.**

1.  **Non-commutative:** $AB \neq BA$ in general. If $AB = BA$ they *commute* ($I$ and $0$ commute with any square $A$, as does $A$ with itself and with its own powers and inverse); if $AB = - BA$ they *anti-commute*.
2.  **Zero divisors exist:** $AB = 0$ does **not** imply $A = 0$ or $B = 0$.
3.  **No cancellation:** $AB = AC$ does **not** imply $B = C$.

*Counterexample for 2 and 3.* With $A = \begin{pmatrix}
1 & 0 \\
1 & 0 \\
1 & 0
\end{pmatrix}$, $B = \begin{pmatrix}
0 & 0 & 0 \\
1 & 1 & 1
\end{pmatrix}$, $C = \begin{pmatrix}
1 & 1 & 1 \\
1 & 1 & 1
\end{pmatrix}$, $D = \begin{pmatrix}
1 & 1 & 1 \\
0 & 0 & 0
\end{pmatrix}$: $AB = 0$ with $A,B \neq 0$; and $AC = AD$ with $C \neq D$.

> **Why this happens — the conceptual reason.** $A$ above collapses $\mathbb{R}^{2}$ onto a line (it is singular, §2.4). Once information is destroyed, two different inputs can produce the same output, so you cannot “divide” to recover the input. Cancellation **is** valid when $A$ is invertible: $AB = AC \Rightarrow A^{- 1}AB = A^{- 1}AC \Rightarrow B = C$.

**Biological reading.** Summing gene × sample count matrices merges sequencing lanes or batches. Scaling sample columns by $\lambda = 10^{6}/\text{total reads}$ gives CPM normalisation.

---
> [[MBD 05 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|← Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 07 - Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication|Module 2 – Matrices and Linear Systems · Biological applications of matrix multiplication →]]
