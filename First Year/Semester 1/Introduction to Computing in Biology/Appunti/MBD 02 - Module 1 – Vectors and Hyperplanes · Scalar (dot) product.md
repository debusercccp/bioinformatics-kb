---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 2
tags: [note, mbd]
---

> [[MBD 01 - Module 1 – Vectors and Hyperplanes · Vectors … Vector operations|← Module 1 – Vectors and Hyperplanes · Vectors … Vector operations]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 03 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification →]]

# Scalar (dot) product

For $\overrightarrow{v},\overrightarrow{u} \in \mathbb{R}^{n}$ the scalar product is a number:

$$
\overrightarrow{v} \cdot \overrightarrow{u} = \langle\overrightarrow{v},\overrightarrow{u}\rangle = {\overrightarrow{v}}^{\, T}\overrightarrow{u} \in \mathbb{R}
$$

The scalar (or “dot”, or “inner”) product is a map that takes two vectors of the same dimension and returns a real number, $c:\mathbb{R}^{n} \times \mathbb{R}^{n} \rightarrow \mathbb{R}$.

### 1.4.1 Physical example: work

A force $\overrightarrow{F}$ moving a body along a displacement $\overrightarrow{s}$ does work

$$
W = \overrightarrow{F} \cdot \overrightarrow{s} = \parallel \overrightarrow{F} \parallel \, \parallel \overrightarrow{s} \parallel cos\theta = \parallel \overrightarrow{s} \parallel \cdot \left( \parallel \overrightarrow{F} \parallel cos\theta \right)
$$

where $\parallel \overrightarrow{F} \parallel cos\theta$ is the **projection of** $\overrightarrow{F}$ **on** $\overrightarrow{s}$.

### 1.4.2 From the geometry to the components

Choose the axes so that $\overrightarrow{v}$ lies on the $x_{1}$ axis and $\overrightarrow{w}$ forms an angle $\theta$ with it:

$$
\overrightarrow{v} = \begin{pmatrix}
v_{1} \\
0
\end{pmatrix} = \begin{pmatrix}
 \parallel \overrightarrow{v} \parallel \\
0
\end{pmatrix},\quad\quad\overrightarrow{w} = \begin{pmatrix}
 \parallel \overrightarrow{w} \parallel cos\theta \\
 \parallel \overrightarrow{w} \parallel sin\theta
\end{pmatrix}
$$

$$
\overrightarrow{v} \cdot \overrightarrow{w} = \langle\overrightarrow{v},\overrightarrow{w}\rangle = \parallel \overrightarrow{v} \parallel \, \parallel \overrightarrow{w} \parallel cos\theta = v_{1}w_{1} + v_{2}w_{2}
$$

In $\mathbb{R}^{n}$:

$$
\langle\overrightarrow{v},\overrightarrow{w}\rangle = \overrightarrow{v} \cdot \overrightarrow{w} = v_{1}w_{1} + v_{2}w_{2} + \ldots + v_{n}w_{n} = \sum_{i = 1}^{n}v_{i}w_{i} = \parallel \overrightarrow{v} \parallel \cdot \parallel \overrightarrow{w} \parallel \cdot cos\theta
$$

A reference frame in which one of the two vectors lies on the $x_{1}$ axis can **always** be found, so the result holds in general: the scalar product is the norm of one vector times the (signed) projection of the other onto it.

### 1.4.3 Angle and orthogonality

$$
cos\theta = \frac{\overrightarrow{v} \cdot \overrightarrow{w}}{\parallel \overrightarrow{v} \parallel \, \parallel \overrightarrow{w} \parallel}
$$

When are $\overrightarrow{v}$ and $\overrightarrow{w}$ **orthogonal**? When the angle is $90^{\circ}$:

$$
cos\theta = 0\quad \Leftrightarrow \quad\overrightarrow{v} \cdot \overrightarrow{w} = 0
$$

The sign of the scalar product tells the angle:

| Angle                   | Scalar product             |
|:------------------------|:---------------------------|
| $\theta < 90^{\circ}$ | $\langle A,B\rangle > 0$ |
| $\theta = 90^{\circ}$ | $\langle A,B\rangle = 0$ |
| $\theta > 90^{\circ}$ | $\langle A,B\rangle < 0$ |

### 1.4.4 No cancellation rule

For real numbers, $a \cdot b = a \cdot c \Leftrightarrow b = c$ (with $a \neq 0$). For the scalar product this does **not** hold:

$$
\overrightarrow{v} \cdot \overrightarrow{u} = \overrightarrow{w} \cdot \overrightarrow{u}\quad \nRightarrow \quad\overrightarrow{v} = \overrightarrow{w}
$$

The equation only says that $\overrightarrow{u} \cdot \left( \overrightarrow{v} - \overrightarrow{w} \right) = 0$, i.e. $\overrightarrow{u}\bot\left( \overrightarrow{v} - \overrightarrow{w} \right)$ (orthogonal). Geometrically: $\overrightarrow{u} \cdot \overrightarrow{v} = \parallel \overrightarrow{u} \parallel \parallel \overrightarrow{v} \parallel cos\theta = \parallel \overrightarrow{u} \parallel \cdot$ (projection of $\overrightarrow{v}$) and $\overrightarrow{u} \cdot \overrightarrow{w} = \parallel \overrightarrow{u} \parallel \cdot$ (projection of $\overrightarrow{w}$): two different vectors can have the same projection on $\overrightarrow{u}$.

### 1.4.5 Properties

- Commutative: $\overrightarrow{v} \cdot \overrightarrow{u} = \overrightarrow{u} \cdot \overrightarrow{v}$
- Linearity: $\overrightarrow{v} \cdot \left( \overrightarrow{u} + \overrightarrow{w} \right) = \overrightarrow{v} \cdot \overrightarrow{u} + \overrightarrow{v} \cdot \overrightarrow{w}$ and $\left( \lambda\overrightarrow{v} \right) \cdot \overrightarrow{u} = \lambda\left( \overrightarrow{v} \cdot \overrightarrow{u} \right) = \overrightarrow{v} \cdot \left( \lambda\overrightarrow{u} \right)$
- $\langle X,X\rangle \geq 0$

### 1.4.6 Norm and scalar product

$$
\overrightarrow{v} \cdot \overrightarrow{v} = \sum_{i = 1}^{n}v_{i}v_{i} = \sum_{i = 1}^{n}\left( v_{i} \right)^{2} = \parallel \overrightarrow{v} \parallel^{2}
$$

The square norm is the scalar product of a vector with itself, so $\parallel \overrightarrow{v} \parallel = \sqrt{\langle\overrightarrow{v},\overrightarrow{v}\rangle}$.

### 1.4.7 Worked example

$$
A = \begin{pmatrix}
2 \\
2 \\
3
\end{pmatrix},\mspace{6mu} B = \begin{pmatrix}
 - 1 \\
3
\end{pmatrix},\mspace{6mu} C = \begin{pmatrix}
 - 1 \\
3 \\
4
\end{pmatrix},\mspace{6mu} D = \begin{pmatrix}
 - 1 \\
3 \\
4 \\
0
\end{pmatrix},\mspace{6mu} E = \begin{pmatrix}
1 \\
 - 3 \\
 - 4 \\
0
\end{pmatrix}
$$

$$
\parallel A \parallel = \sqrt{17},\quad \parallel B \parallel = \sqrt{10},\quad \parallel C \parallel = \sqrt{26},\quad \parallel D \parallel = \sqrt{26},\quad \parallel E \parallel = \sqrt{26}
$$

$$
A + C = \begin{pmatrix}
1 \\
5 \\
7
\end{pmatrix},\quad\quad A - C = \begin{pmatrix}
3 \\
 - 1 \\
 - 1
\end{pmatrix},\quad\quad d(A,C) = \parallel A - C \parallel = \sqrt{11}
$$

$$
A \cdot C = - 2 + 6 + 12 = 16,\quad\quad cos\theta = \frac{A \cdot C}{\parallel A \parallel \, \parallel C \parallel} = \frac{16}{\sqrt{17} \cdot \sqrt{26}}\quad\left( \theta = \widehat{AC} \right)
$$

$$
D \cdot E = - 1 - 9 - 16 = - 26,\quad\quad cos\alpha = \frac{D \cdot E}{\parallel D \parallel \, \parallel E \parallel} = \frac{- 26}{\sqrt{26} \cdot \sqrt{26}} = - 1\quad\left( \alpha = \widehat{DE} \right)
$$

---
> [[MBD 01 - Module 1 – Vectors and Hyperplanes · Vectors … Vector operations|← Module 1 – Vectors and Hyperplanes · Vectors … Vector operations]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 03 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification →]]
