---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 7
tags: [note, mbd]
---

> [[MBD 06 - Module 2 – Matrices · Transpose matrix … Orthogonal matrices|← Module 2 – Matrices · Transpose matrix … Orthogonal matrices]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 08 - Module 3 · The determinant as an area|Module 3 · The determinant as an area →]]

# Matrices as linear maps

For $\overrightarrow{v} \in \mathbb{R}^{m}$ and $A \in \mathbb{R}^{n \times m}$:

$$
A \cdot \overrightarrow{v} = A^{(n \times m)}\, v^{(m \times 1)} \in \mathbb{R}^{n},\quad\quad A^{(n \times m)}:\mathbb{R}^{m} \rightarrow \mathbb{R}^{n}
$$

If $A$ is a square matrix, $A \in \mathbb{R}^{n \times n}$, then $A:\mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$.

The transformation is **linear**:

$$
A\left( \overrightarrow{v} + \overrightarrow{u} \right) = A\overrightarrow{v} + A\overrightarrow{u},\quad\quad A\left( \lambda\overrightarrow{v} \right) = \lambda A\overrightarrow{v}
$$

*Examples.* A $3 \times 2$ matrix sends $\mathbb{R}^{2}$ into $\mathbb{R}^{3}$: $\begin{pmatrix}
1 & 2 \\
4 & - 3 \\
2 & - 1
\end{pmatrix}\begin{pmatrix}
1 \\
1
\end{pmatrix} = \begin{pmatrix}
3 \\
1 \\
1
\end{pmatrix}$. A square matrix transforms vectors within the same space, e.g. $\begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}\begin{pmatrix}
1 \\
0
\end{pmatrix} = \begin{pmatrix}
1 \\
2
\end{pmatrix}$.

## 3.2 Rotation matrix

$$
A = \begin{pmatrix}
cos\theta & - sin\theta \\
sin\theta & cos\theta
\end{pmatrix},\quad\quad A\, A^{t} = \begin{pmatrix}
cos\theta & - sin\theta \\
sin\theta & cos\theta
\end{pmatrix}\begin{pmatrix}
cos\theta & sin\theta \\
 - sin\theta & cos\theta
\end{pmatrix} = \begin{pmatrix}
cos^{2}\theta + sin^{2}\theta & cos\theta\, sin\theta - sin\theta\, cos\theta \\
sin\theta\, cos\theta - sin\theta\, cos\theta & sin^{2}\theta + cos^{2}\theta
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

so $A^{t} = A^{- 1}$: the rotation matrix is orthogonal.

To see that it is a rotation by $\theta$, look at what it does to the axes: $A\begin{pmatrix}
1 \\
0
\end{pmatrix} = \begin{pmatrix}
cos\theta \\
sin\theta
\end{pmatrix}$ and $A\begin{pmatrix}
0 \\
1
\end{pmatrix} = \begin{pmatrix}
 - sin\theta \\
cos\theta
\end{pmatrix}$: both unit vectors are turned counterclockwise by $\theta$.

---
> [[MBD 06 - Module 2 – Matrices · Transpose matrix … Orthogonal matrices|← Module 2 – Matrices · Transpose matrix … Orthogonal matrices]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 08 - Module 3 · The determinant as an area|Module 3 · The determinant as an area →]]
