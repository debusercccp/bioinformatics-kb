---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 10
tags: [note, mbd]
---

> [[MBD 09 - Module 2 – Matrices and Linear Systems · Linear systems Ax=b|← Module 2 – Matrices and Linear Systems · Linear systems Ax=b]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 11 - Module 3 · Null space, eigenvalues, eigenvectors|Module 3 · Null space, eigenvalues, eigenvectors →]]

# Matrices as linear operators

An $n \times m$ matrix $A$ acts as a linear operator $\mathbb{R}^{m} \rightarrow \mathbb{R}^{n}$, $v \mapsto Av$, satisfying the **linearity conditions**

$$
A(v + u) = Av + Au,\quad\quad A(\lambda v) = \lambda(Av)
$$

A square matrix of order $m$ maps the space into itself. Computationally, $(Av)_{i} = \sum_{k}^{}a_{ik}v_{k}$: each output component is the inner product of a row of $A$ with $v$.

> **The one sentence that unifies Modules 2 and 3.** A matrix is not a table of numbers, it is *a function*. Matrix multiplication is **composition of functions**, which is why it is associative (composition always is) and why it is not commutative (doing A then B differs from doing B then A). The inverse matrix is the inverse function. The determinant is the volume scaling factor of that function. Everything else follows.

### 3.1.1 Standard 2D geometric transformations

| Transformation | Matrix | Effect |
|----|----|----|
| Reflection across $x_{1}$-axis | $\begin{pmatrix}
1 & 0 \\
0 & - 1
\end{pmatrix}$ | flips $x_{2}$ |
| Reflection across $x_{2}$-axis | $\begin{pmatrix}
 - 1 & 0 \\
0 & 1
\end{pmatrix}$ | flips $x_{1}$ |
| Isotropic rescaling | $\begin{pmatrix}
a & 0 \\
0 & a
\end{pmatrix}$ | expansion if $|a| > 1$, contraction if $|a| < 1$ |
| Counterclockwise rotation by $\theta$ | $\begin{pmatrix}
\cos\theta & - sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix}$ | rigid rotation |

*How to read a transformation matrix:* **the columns are the images of the basis vectors.** Apply the rotation matrix to $e_{1} = (1,0)^{T}$ and you get $\left( \cos\theta,sin\theta \right)^{T}$, its first column; apply it to $e_{2}$ and you get $( - sin\theta,cos\theta)^{T}$, its second. This is the fastest way both to read an unfamiliar matrix and to construct one you need.

### 3.1.2 Composition

Applying $A$ then $B$ gives $X' = B(AX) = (BA)X$ — note the **right-to-left** order. Order matters because matrices do not commute.

*Explicit example.* Rotation by $\theta$ then reflection across $x_{2}$:

$$
BA = \begin{pmatrix}
 - 1 & 0 \\
0 & 1
\end{pmatrix}\begin{pmatrix}
\cos\theta & - sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix} = \begin{pmatrix}
 - cos\theta & \sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix}
$$

Reflection first, then rotation:

$$
AB = \begin{pmatrix}
\cos\theta & - sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix}\begin{pmatrix}
 - 1 & 0 \\
0 & 1
\end{pmatrix} = \begin{pmatrix}
 - cos\theta & - sin\theta \\
 - sin\theta & \cos\theta
\end{pmatrix}
$$

Different matrices, so different transformations.

### 3.1.3 Adjoint relation with the scalar product

$$
(Av) \cdot w = v \cdot \left( A^{T}w \right)
$$

*Proof.* $\sum_{i}^{}\left( \sum_{k}^{}A_{ik}v_{k} \right)w_{i} = \sum_{k}^{}{\sum_{i}^{}A_{ik}}w_{i}v_{k} = \sum_{k}^{}\left( A^{T}w \right)_{k}v_{k}$.

This is the defining property of the transpose, and the reason $A^{T}$ appears everywhere a projection or a least-squares problem does.

### 3.1.4 Geometric meaning of the determinant

Under the transformation $A$, the area of the unit square in $\mathbb{R}^{2}$ — or the volume of the unit cube in $\mathbb{R}^{3}$ — spanned by the basis vectors is scaled by $|A|$.

*Proof in 2D.* $A = \begin{pmatrix}
a & c \\
b & d
\end{pmatrix}$ maps $e_{1} \mapsto (a,b)^{T}$ and $e_{2} \mapsto (c,d)^{T}$. The parallelogram they span has area

$$
(a + c)(b + d) - 2 \cdot \frac{(a + c + c)b}{2} - 2 \cdot \frac{cd}{2} = ad - bc = det(A)
$$

If $|A| = 0$ the transformation collapses space into a lower dimension — area or volume zero — and is non-invertible (**singular**).

*Example of collapse.* $A = \begin{pmatrix}
1 & - 2 \\
 - 1 & 2
\end{pmatrix}$ has $|A| = 0$, and maps both $(2,0)^{T}$ and $(0, - 1)^{T}$ to $(2, - 2)^{T}$. Two different inputs, one output: the inverse transformation cannot be defined.

> **The sign of the determinant** also carries information, which the slides omit: $|A| > 0$ means the transformation preserves orientation, $|A| < 0$ means it reverses it (a reflection). A rotation has $|A| = + 1$, a reflection $|A| = - 1$ — both orthogonal.

---
> [[MBD 09 - Module 2 – Matrices and Linear Systems · Linear systems Ax=b|← Module 2 – Matrices and Linear Systems · Linear systems Ax=b]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 11 - Module 3 · Null space, eigenvalues, eigenvectors|Module 3 · Null space, eigenvalues, eigenvectors →]]
