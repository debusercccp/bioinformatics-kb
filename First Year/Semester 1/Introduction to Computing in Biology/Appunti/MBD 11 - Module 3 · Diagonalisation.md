---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 11
tags: [note, mbd]
---

> [[MBD 10 - Module 3 · Eigenvalues and eigenvectors|← Module 3 · Eigenvalues and eigenvectors]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 12 - Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant|Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant →]]

# Diagonalisation

For $A = \begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}$: $\lambda_{1} = - 1$, ${\overrightarrow{v}}^{(1)} = c(4,1)^{T}$; $\lambda_{2} = - 2$, ${\overrightarrow{v}}^{(2)} = c(3,1)^{T}$. The two eigenvectors fix two directions in the plane, along which $A$ acts as a simple stretching:

$$
A \rightarrow \Lambda = \begin{pmatrix}
\lambda_{1} & 0 \\
0 & \lambda_{2}
\end{pmatrix}
$$

**Diagonalisation** $\Rightarrow$ change the basis to ${\overrightarrow{v}}^{(1)},{\overrightarrow{v}}^{(2)}$.

**Change of basis.** Vectors are written as $n$-uples with respect to a particular basis (e.g. $\overrightarrow{i} = (1,0,0)^{T}$, $\overrightarrow{j} = (0,1,0)^{T}$, $\overrightarrow{k} = (0,0,1)^{T}$, $\overrightarrow{a} = a_{x}\overrightarrow{i} + a_{y}\overrightarrow{j} + a_{z}\overrightarrow{k}$). The same vector can be represented with respect to another basis: the vector does not change, its coordinates do. If the new basis vectors are $\overrightarrow{i}' = a\overrightarrow{i} + b\overrightarrow{j}$ and $\overrightarrow{j}' = c\overrightarrow{i} + d\overrightarrow{j}$, the matrix

$$
U = \begin{pmatrix}
a & c \\
b & d
\end{pmatrix},\quad\quad{\overrightarrow{v}}_{\{ i,j\}} = U\,{\overrightarrow{v}}_{\{ i',j'\}}
$$

(new basis vectors written in columns) transforms the coordinates from $\{ i',j'\}$ to $\{ i,j\}$. $U$ must be invertible ($|U| \neq 0$): otherwise $\overrightarrow{i}'$ and $\overrightarrow{j}'$ would be collinear and would not span the space.

**Diagonalisation.** If $A$ (order $n$) has $n$ linearly independent eigenvectors, they can serve as a new basis. With the eigenvectors written in columns in $U$, $AU = U\Lambda$ (because $A{\overrightarrow{u}}_{i} = \lambda_{i}{\overrightarrow{u}}_{i}$), hence

$$
U^{- 1}AU = \Lambda = \begin{pmatrix}
\lambda_{1} & & 0 \\
 & \ddots & \\
0 & & \lambda_{n}
\end{pmatrix}
$$

the transformation is diagonal in the new coordinate system. *Example:*

$$
U = \begin{pmatrix}
4 & 3 \\
1 & 1
\end{pmatrix},\ |U| = 1,\ U^{- 1} = \begin{pmatrix}
1 & - 3 \\
 - 1 & 4
\end{pmatrix},\quad U^{- 1}AU = \begin{pmatrix}
1 & - 3 \\
 - 1 & 4
\end{pmatrix}\begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}\begin{pmatrix}
4 & 3 \\
1 & 1
\end{pmatrix} = \begin{pmatrix}
 - 1 & 3 \\
2 & - 8
\end{pmatrix}\begin{pmatrix}
4 & 3 \\
1 & 1
\end{pmatrix} = \begin{pmatrix}
 - 1 & 0 \\
0 & - 2
\end{pmatrix}
$$

If $A$ is **symmetric** ($A = A^{T}$): its eigenvalues are real, its eigenvectors are orthogonal, and with normalised eigenvectors $U^{- 1} = U^{T}$, so $U^{T}AU$ is diagonal. A $U$ of the form of the rotation matrix (§3.2) is a counterclockwise rotation of the coordinates by $\theta$.

---
> [[MBD 10 - Module 3 · Eigenvalues and eigenvectors|← Module 3 · Eigenvalues and eigenvectors]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 12 - Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant|Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant →]]
