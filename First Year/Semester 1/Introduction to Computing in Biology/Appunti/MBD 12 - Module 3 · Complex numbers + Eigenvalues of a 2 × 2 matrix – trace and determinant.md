---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 12
tags: [note, mbd]
---

> [[MBD 11 - Module 3 · Diagonalisation|← Module 3 · Diagonalisation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 13 - Module 4 – Calculus in One Variable · Functions … Elementary functions|Module 4 – Calculus in One Variable · Functions … Elementary functions →]]

# Complex numbers

*Why they are needed:* eigenvalues always exist in the complex field. For $A = \begin{pmatrix}
1 & 1 \\
 - 1 & 1
\end{pmatrix}$, $\det(A - \lambda I) = (1 - \lambda)^{2} + 1 = 0$ has no real solution, but $(1 - \lambda)^{2} = - 1 \Rightarrow 1 - \lambda = \pm i \Rightarrow \lambda = 1 \pm i$.

In $\mathbb{R}$, $\sqrt{- 1}$ is not defined $\rightarrow$ $i$, the **imaginary unit**, with $(i)^{2} = - 1$.

$$
z\mathbb{\in C,}\quad\quad z = a + ib,\quad a,b\mathbb{\in R,}\quad\quad a = Re(z),\quad b = Im(z)
$$

For $z_{1},z_{2}\mathbb{\in C}$, $z_{1} = a + bi$, $z_{2} = c + di$:

$$
z_{1} + z_{2} = (a + c) + (b + d)i
$$

$$
z_{1} \cdot z_{2} = (a + ib)(c + id) = ac + iad + ibc + (ib)(id) = ac - bd + i(ad + bc)\quad\quad\left( i^{2} = - 1 \right)
$$

Difference: $(a + bi) - (c + di) = (a - c) + (b - d)i$. Examples: $(2 + 3i) + (4 + 2i) = 6 + 5i$; $(2 + 3i) - (4 + 2i) = - 2 + i$; $(2 + 3i)(4 + 2i) = 8 + 4i + 12i + 6i^{2} = 2 + 16i$.

Division: multiply numerator and denominator by $c - di$,

$$
\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{ac + bd}{c^{2} + d^{2}} + \frac{bc - ad}{c^{2} + d^{2}}i,\quad\quad\frac{2 + 3i}{4 + 2i} = \frac{14 + 8i}{20} = \frac{7 + 4i}{10}
$$

*Note:* the slide computes $(2 + 3i)(4 + 2i)$ with $2i$ instead of $4i$ for the term $2 \cdot 2i$ and gets $2 + 14i$; the correct result is $2 + 16i$.

## 3.8 Eigenvalues of a 2 × 2 matrix: trace and determinant

$$
A^{(2 \times 2)} = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix},\quad\quad A - \lambda I = \begin{pmatrix}
a_{11} - \lambda & a_{12} \\
a_{21} & a_{22} - \lambda
\end{pmatrix}
$$

$$
\det(A - \lambda I) = \left( a_{11} - \lambda \right)\left( a_{22} - \lambda \right) - a_{12}a_{21} = \lambda^{2} - \lambda\underset{Tr(A)}{\underbrace{\left( a_{11} + a_{22} \right)}} + \underset{\det(A)}{\underbrace{a_{11}a_{22} - a_{12}a_{21}}}
$$

$Tr(A)$ is the **trace**. Hence

$$
\lambda = \frac{Tr(A) \pm \sqrt{\left( Tr(A) \right)^{2} - 4\det(A)}}{2}\quad\quad\Delta > 0 \Rightarrow 2\text{ real eigenvalues};\quad\Delta < 0 \Rightarrow 2\text{ complex eigenvalues}
$$

with $\Delta = \left( Tr(A) \right)^{2} - 4\det(A)$.

---
> [[MBD 11 - Module 3 · Diagonalisation|← Module 3 · Diagonalisation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 13 - Module 4 – Calculus in One Variable · Functions … Elementary functions|Module 4 – Calculus in One Variable · Functions … Elementary functions →]]
