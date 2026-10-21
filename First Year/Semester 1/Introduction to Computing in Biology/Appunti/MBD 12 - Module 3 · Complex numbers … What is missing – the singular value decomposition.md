---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 12
tags: [note, mbd]
---

> [[MBD 11 - Module 3 · Null space, eigenvalues, eigenvectors|← Module 3 · Null space, eigenvalues, eigenvectors]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 13 - Module 4 – Single-Variable Calculus|Module 4 – Single-Variable Calculus →]]

# Complex numbers

Eigenvalues of real matrices need not exist in $\mathbb{R}$. For $A = \begin{pmatrix}
1 & 1 \\
 - 1 & 1
\end{pmatrix}$, $(1 - \lambda)^{2} + 1 = 0$ has no real solution, but in $\mathbb{C}$, $\lambda = 1 \pm i$. By the fundamental theorem of algebra, eigenvalues **always** exist in the complex field.

A complex number is $z = a + ib$ with $i = \sqrt{- 1}$ ($i^{2} = - 1$), $a = Re(z)$, $b = Im(z)$.

| Operation | Rule | Example |
|----|----|----|
| Addition | $(a + bi) + (c + di) = (a + c) + (b + d)i$ | $(2 + 3i) + (4 + 2i) = 6 + 5i$ |
| Subtraction | $(a + bi) - (c + di) = (a - c) + (b - d)i$ | $(2 + 3i) - (4 + 2i) = - 2 + i$ |
| Multiplication | $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$ | $(2 + 3i)(4 + 2i) = 2 + 14i$ |
| Division | multiply above and below by the conjugate $c - di$ | $\frac{2 + 3i}{4 + 2i} = \frac{7 + 4i}{10}$ |

$$
\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^{2} + d^{2}} = \frac{ac + bd}{c^{2} + d^{2}} + \frac{bc - ad}{c^{2} + d^{2}}i
$$

> **What complex eigenvalues mean geometrically** — omitted from the slides, and the only reason to care here. A real matrix with complex eigenvalues $\lambda = \rho e^{\pm i\theta}$ acts as a **rotation by** $\theta$ **combined with a scaling by** $\rho = |\lambda|$. Such a matrix has *no* real eigenvector, because a rotation leaves no real direction fixed. In a dynamical system, complex eigenvalues mean **oscillation**: $|\lambda| > 1$ gives growing oscillations, $|\lambda| < 1$ damped ones, $|\lambda| = 1$ a sustained cycle — predator–prey dynamics, circadian oscillators, cell-cycle models. Complex eigenvalues of a real matrix always come in conjugate pairs.

## 3.4 Change of basis, diagonalisation, spectral theorem

### 3.4.1 Change of basis

A vector has coordinates only *relative to a basis*. Changing basis changes the coordinates, not the vector.

If a new basis $\{ i',j'\}$ is expressed in the old one as $i' = a\, i + b\, j$ and $j' = c\, i + d\, j$, collect those as the **columns** of the transition matrix

$$
U = \begin{pmatrix}
a & c \\
b & d
\end{pmatrix},\quad\quad|U| \neq 0
$$

Then

$$
v_{\{ i,j\}} = U\, v'_{\{ i',j'\}},\quad\quad v'_{\{ i',j'\}} = U^{- 1}v_{\{ i,j\}}
$$

$U$ must be invertible, otherwise the new “basis” vectors would be collinear and would not span the space — the geometric reading of the determinant again.

> **The direction of the arrow is the classic trap.** $U$ holds the new basis vectors *written in old coordinates*, so $U$ converts **new coordinates into old ones**, and $U^{- 1}$ does the reverse. Checking it on a single basis vector takes five seconds and is worth doing every time.

### 3.4.2 Diagonalisation

If an $n \times n$ matrix $A$ has $n$ **linearly independent** eigenvectors $u_{1},\ldots,u_{n}$, place them as the columns of $U$. Then $AU = U\Lambda$ by the definition of eigenvector, so

$$
U^{- 1}AU = \Lambda = diag\left( \lambda_{1},\ldots,\lambda_{n} \right)
$$

In the eigenvector basis, the transformation is **diagonal**: it simply stretches each new axis by its eigenvalue.

*Worked example.* $A = \begin{pmatrix}
2 & - 12 \\
1 & - 5
\end{pmatrix}$ with $\lambda_{1} = - 1$, $x_{1} = (4,1)^{T}$ and $\lambda_{2} = - 2$, $x_{2} = (3,1)^{T}$:

$$
U = \begin{pmatrix}
4 & 3 \\
1 & 1
\end{pmatrix},\quad|U| = 1,\quad U^{- 1} = \begin{pmatrix}
1 & - 3 \\
 - 1 & 4
\end{pmatrix},\quad U^{- 1}AU = \begin{pmatrix}
 - 1 & 0 \\
0 & - 2
\end{pmatrix}
$$

**When is a matrix diagonalisable?** Exactly when geometric multiplicity equals algebraic multiplicity for every eigenvalue (§3.2.2). Two sufficient conditions are worth memorising:

- $n$ **distinct** eigenvalues $\Rightarrow$ always diagonalisable (distinct eigenvalues force independent eigenvectors).
- $A$ real **symmetric** $\Rightarrow$ always diagonalisable, and orthogonally so (§3.4.3).

A repeated eigenvalue does *not* by itself prevent diagonalisation — $I$ has one eigenvalue repeated $n$ times and is already diagonal. It only *permits* failure, which must then be checked.

> **Why diagonalise at all.** Once $A = U\Lambda U^{- 1}$:
>
> ``` math
> A^{k} = U\Lambda^{k}U^{- 1},\quad\quad A^{- 1} = U\Lambda^{- 1}U^{- 1},\quad\quad e^{A} = Ue^{\Lambda}U^{- 1}
> ```
>
> and $\Lambda^{k}$ is just each diagonal entry raised to $k$. Matrix powers, inverses, exponentials and the solution of linear ODE systems all become scalar operations. In Module 8 this is what turns a correlated covariance matrix into uncorrelated principal components.

### 3.4.3 Symmetric matrices and the spectral theorem

If $A$ is real and **symmetric** ($A = A^{T}$):

1.  all eigenvalues $\lambda_{i}$ are **real**;
2.  eigenvectors of **distinct** eigenvalues are **orthogonal**, $\langle u_{i},u_{j}\rangle = 0$;
3.  normalising them to unit norm makes $U$ an **orthogonal** matrix ($U^{- 1} = U^{T}$), giving

$$
U^{T}AU = \Lambda
$$

> **Correction / completion.** Point 2 as stated covers only distinct eigenvalues. With a repeated eigenvalue, eigenvectors within one eigenspace are not *automatically* orthogonal — but an orthonormal basis of that eigenspace can **always be chosen** (Gram–Schmidt). So the conclusion survives in full: *every* real symmetric matrix admits an orthonormal eigenbasis and is orthogonally diagonalisable, repeated eigenvalues or not. Without this, the spectral theorem would not apply to a covariance matrix with tied eigenvalues, and PCA would have a hole in its justification.

**Why this theorem carries the rest of the course.** Three of the central objects are real and symmetric:

| Object | Where | What the theorem gives |
|----|----|----|
| Hessian $H$ | §5.2 | real eigenvalues, so max/min/saddle classification by sign is meaningful |
| Covariance matrix $\Sigma$ | §8.1 | orthogonal PCs, real non-negative variances |
| Correlation matrix | §8.1 | same, standardised |

**Positive definiteness** (used in §5.2 but never defined there). A symmetric $A$ is

- **positive definite** if $x^{T}Ax > 0$ for all $x \neq 0$ $\Leftrightarrow$ all $\lambda_{i} > 0$ $\Leftrightarrow$ all leading principal minors $> 0$ (Sylvester’s criterion);
- **positive semi-definite** if $x^{T}Ax \geq 0$ $\Leftrightarrow$ all $\lambda_{i} \geq 0$;
- **negative definite** if all $\lambda_{i} < 0$ $\Leftrightarrow$ the leading principal minors alternate in sign starting with $< 0$;
- **indefinite** if eigenvalues of both signs.

A covariance matrix is always positive semi-definite, because $x^{T}\Sigma x = var\left( x^{T}X \right) \geq 0$ — a variance cannot be negative.

### 3.4.4 Quadratic forms

In the orthonormal eigenvector basis ($x = Ux'$), a quadratic form $x^{T}Ax = 1$ becomes

$$
(x')^{T}U^{T}AUx' = (x')^{T}\Lambda x' = \sum_{i}^{}\lambda_{i}\left( x_{i}' \right)^{2} = 1
$$

the **canonical form**, with all mixed cross-terms eliminated. Geometrically: the level set of a quadratic form is a conic (ellipse, hyperbola, parabola) whose principal axes *are* the eigenvectors and whose semi-axis lengths are $1/\sqrt{\lambda_{i}}$. All eigenvalues positive gives an ellipse (ellipsoid); mixed signs give a hyperbola. This is literally the picture of a PCA biplot: the confidence ellipse of a Gaussian cloud is a level set of $x^{T}\Sigma^{- 1}x$, with axes along the principal components.

### 3.4.5 Rotation matrices are orthogonal

$$
U = \begin{pmatrix}
\cos\theta & - sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix},\quad\quad U^{T}U = \begin{pmatrix}
\cos^{2}\theta + \sin^{2}\theta & 0 \\
0 & \cos^{2}\theta + \sin^{2}\theta
\end{pmatrix} = I
$$

so $U^{T} = U^{- 1}$. Since the columns of $U$ are the new basis vectors in terms of the old, $U$ represents a counterclockwise rotation of coordinates by $\theta$ — and, being orthogonal, it preserves all norms and angles (§2.1).

## 3.5 What is missing: the singular value decomposition

Diagonalisation applies only to square matrices, and not even to all of those. Every matrix — rectangular, singular, defective, anything — admits the **singular value decomposition**

$$
X = U\Sigma V^{T}
$$

with $U$ ($m \times m$) and $V$ ($n \times n$) orthogonal and $\Sigma$ diagonal with non-negative entries $\sigma_{1} \geq \sigma_{2} \geq \ldots \geq 0$, the **singular values**.

Relation to what precedes: the columns of $V$ are the eigenvectors of $X^{T}X$, the columns of $U$ the eigenvectors of $XX^{T}$, and $\sigma_{i}^{2}$ are their shared eigenvalues. For a symmetric positive semi-definite matrix, SVD and eigendecomposition coincide.

**Why it belongs in these notes.** Every software package computes PCA by taking the SVD of the centred data matrix, never by forming the covariance matrix and diagonalising it. With $p \approx 10^{6}$ SNPs, $\Sigma$ would be a $10^{6} \times 10^{6}$ matrix — $8$ terabytes — while the SVD route never builds it. SVD is also the basis of the pseudo-inverse for rank-deficient systems, of low-rank denoising, and of latent-factor methods.

---
> [[MBD 11 - Module 3 · Null space, eigenvalues, eigenvectors|← Module 3 · Null space, eigenvalues, eigenvectors]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 13 - Module 4 – Single-Variable Calculus|Module 4 – Single-Variable Calculus →]]
