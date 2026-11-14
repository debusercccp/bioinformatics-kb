---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 10
tags: [note, mbd]
---

> [[MBD 09 - Module 3 · Null space|← Module 3 · Null space]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 11 - Module 3 · Diagonalisation|Module 3 · Diagonalisation →]]

# Eigenvalues and eigenvectors

For $A \in \mathbb{R}^{n \times n}$ and $\overrightarrow{v} \in \mathbb{R}^{n}$:

$$
A\overrightarrow{v} = \lambda\overrightarrow{v}\quad\quad\lambda:\text{ eigenvalue},\quad\overrightarrow{v}:\text{ eigenvector}
$$

($A$ only stretches $\overrightarrow{v}$, without changing its direction).

In general a matrix acts on a vector by changing both its magnitude and its direction. On some vectors, however, it changes only the magnitude, leaving the direction unchanged (or reversing it): these are the **eigenvectors** of the matrix. The factor that multiplies the magnitude is the **eigenvalue**: positive if the direction is unchanged, negative if it is reversed.

*Example.* With $A = \begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}$, $A(1,0)^{T} = (1,2)^{T}$ and $A(0,1)^{T} = (2,1)^{T}$ change direction, while $A(1,1)^{T} = (3,3)^{T}$ does not: $(1,1)^{T}$ is an eigenvector with eigenvalue 3.

The zero vector cannot be an eigenvector (even though $A\overrightarrow{0} = \lambda\overrightarrow{0}$), but $\lambda = 0$ can be an eigenvalue.

$$
A\overrightarrow{v} - \lambda I\overrightarrow{v} = \overrightarrow{0}\quad \Rightarrow \quad(A - \lambda I)\overrightarrow{v} = \overrightarrow{0}\quad \Rightarrow \quad\overrightarrow{v} \in \text{null space of }A - \lambda I\quad \Rightarrow \quad\det(A - \lambda I) = 0
$$

The eigenvectors are the non-trivial elements of the null space of $A - \lambda I$, and they exist only if $\det(A - \lambda I) = 0$: this is the **characteristic equation** of $A$, whose roots are the eigenvalues. To each distinct eigenvalue $\lambda_{i}$ corresponds at least one eigenvector, the solution of the homogeneous system $\left( A - \lambda_{i}I \right){\overrightarrow{x}}_{i} = \overrightarrow{0}$.

### 3.5.1 Worked example

$$
A = \begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}
$$

*Eigenvalues.*

$$
A - \lambda I = \begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix} - \lambda\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} = \begin{pmatrix}
2 - \lambda & - 12 \\
1 & - 5 - \lambda
\end{pmatrix}\quad \Rightarrow \quad\det(A - \lambda I) = 0
$$

$$
(2 - \lambda)( - 5 - \lambda) + 12 = 0\quad \Rightarrow \quad\lambda^{2} - 2\lambda + 5\lambda - 10 + 12 = 0\quad \Rightarrow \quad\lambda^{2} + 3\lambda + 2 = 0
$$

$$
\lambda = \frac{- b \pm \sqrt{b^{2} - 4ac}}{2a} = \frac{- 3 \pm \sqrt{9 - 8}}{2} = \frac{- 3 \pm 1}{2}\quad \Rightarrow \quad\lambda_{1} = - 1,\quad\lambda_{2} = - 2
$$

*First eigenvector,* $\lambda_{1} = - 1$: $A{\overrightarrow{v}}^{(1)} = - 1\,{\overrightarrow{v}}^{(1)}$

$$
\begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}\begin{pmatrix}
v_{1}^{(1)} \\
v_{2}^{(1)}
\end{pmatrix} = \begin{pmatrix}
 - v_{1}^{(1)} \\
 - v_{2}^{(1)}
\end{pmatrix}\quad \Rightarrow \quad\left\{ \begin{matrix}
2v_{1}^{(1)} - 12v_{2}^{(1)} = - v_{1}^{(1)} \\
v_{1}^{(1)} - 5v_{2}^{(1)} = - v_{2}^{(1)}
\end{matrix} \right.\ \quad \Rightarrow \quad\left\{ \begin{matrix}
3v_{1}^{(1)} - 12v_{2}^{(1)} = 0 \\
v_{1}^{(1)} - 4v_{2}^{(1)} = 0
\end{matrix} \right.\ \quad \Rightarrow \quad{\overrightarrow{v}}^{(1)} = c\begin{pmatrix}
4 \\
1
\end{pmatrix}
$$

*Proof:*

$$
A\overrightarrow{v} = \begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}\begin{pmatrix}
4c \\
c
\end{pmatrix} = \begin{pmatrix}
8c - 12c \\
4c - 5c
\end{pmatrix} = \begin{pmatrix}
 - 4c \\
 - c
\end{pmatrix} = - 1\,{\overrightarrow{v}}^{(1)}
$$

where $- 1$ is the eigenvalue and ${\overrightarrow{v}}^{(1)}$ the eigenvector.

*Normalisation.* $\parallel {\overrightarrow{v}}^{(1)} \parallel = \sqrt{16c^{2} + c^{2}} = |c|\sqrt{17}$, so the eigenvector has norm 1 for $c = 1/\sqrt{17}$.

*Second eigenvector,* $\lambda_{2} = - 2$:

$$
\begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}\begin{pmatrix}
v_{1}^{(2)} \\
v_{2}^{(2)}
\end{pmatrix} = - 2\begin{pmatrix}
v_{1}^{(2)} \\
v_{2}^{(2)}
\end{pmatrix}\quad \Rightarrow \quad\left\{ \begin{matrix}
2v_{1}^{(2)} - 12v_{2}^{(2)} = - 2v_{1}^{(2)} \\
v_{1}^{(2)} - 5v_{2}^{(2)} = - 2v_{2}^{(2)}
\end{matrix} \right.\ \quad \Rightarrow \quad\left\{ \begin{matrix}
4v_{1}^{(2)} - 12v_{2}^{(2)} = 0 \\
v_{1}^{(2)} - 3v_{2}^{(2)} = 0
\end{matrix} \right.\ \quad \Rightarrow \quad v_{1} = 3v_{2}
$$

$$
{\overrightarrow{v}}^{(2)} = c\begin{pmatrix}
3 \\
1
\end{pmatrix},\quad\text{normalised if }c = \frac{1}{\sqrt{10}}
$$

### 3.5.2 Properties of eigenvalues

- The sum of the eigenvalues equals the trace of the matrix (here $- 1 - 2 = - 3 = 2 - 5$).
- The product of the eigenvalues (counting multiplicity) equals the determinant (here $( - 1)( - 2) = 2 = - 10 + 12$).
- A matrix is singular (non-invertible) if and only if it has a zero eigenvalue.
- The eigenvalues of an upper (or lower) triangular matrix are the elements on the main diagonal.
- If $\lambda$ is an eigenvalue of an invertible $A$, $1/\lambda$ is an eigenvalue of $A^{- 1}$.
- If $\lambda$ is an eigenvalue of $A$: $k\lambda$ is an eigenvalue of $kA$; $\lambda^{k}$ is an eigenvalue of $A^{k}$ ($k$ positive integer); $\lambda$ is an eigenvalue of $A^{T}$.

## Collegamenti
- [[AML 43 - Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA]] — PCA nel corso di ML
- [[SATAUMV 13 - Population structure analyses – principal component analysis (PCA)]] — PCA in genetica di popolazione

---
> [[MBD 09 - Module 3 · Null space|← Module 3 · Null space]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 11 - Module 3 · Diagonalisation|Module 3 · Diagonalisation →]]
