---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 4
tags: [note, mbd]
---

> [[MBD 03 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|← Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 05 - Module 2 – Matrices · Sum + Row-by-column product|Module 2 – Matrices · Sum + Row-by-column product →]]

# Definitions

A **matrix** is a table of numbers with rows and columns. Example:

$$
\begin{pmatrix}
3 & 1 & 2 \\
2 & 3 & 1
\end{pmatrix} \in \mathbb{R}^{2 \times 3}\quad\left( 2\text{ rows},\ 3\text{ columns} \right)
$$

A matrix is a rectangular array of numbers (symbols, expressions) arranged in rows and columns and enclosed by brackets. A matrix with $m$ rows and $n$ columns has size $m \times n$ and contains $mn$ elements $a_{ij}$: the first subscript is the row, the second the column. It is called “the $m \times n$ matrix $A = \left\lbrack a_{ij} \right\rbrack$”, or simply “the matrix $A$”.

$\mathbb{R}^{n \times n}$: **square matrices of order** $n$. In general

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} \in \mathbb{R}^{m \times n}
$$

In a square matrix of order $n$ the elements $a_{11},a_{22},\ldots,a_{nn}$ are the **diagonal** elements, and their sum is the **trace**, $Tr(A) = \sum_{i = 1}^{n}a_{ii} = a_{11} + a_{22} + \ldots + a_{nn}$ (§3.8). A square matrix with $a_{ij} = 0$ for $i \neq j$ is **diagonal**, $D = diag\left\lbrack a_{11},\ldots,a_{nn} \right\rbrack$; the diagonal matrix with $a_{11} = \ldots = a_{nn} = 1$ is the **identity** $I$ (§2.4.1).

A vector $\overrightarrow{v} \in \mathbb{R}^{n}$ is a **column matrix**, $\overrightarrow{v} \in \mathbb{R}^{n \times 1}$.

## 2.2 Product by a scalar

For $A \in \mathbb{R}^{m \times n}$ and $\lambda\mathbb{\in R}$, $B = \lambda A \in \mathbb{R}^{m \times n}$ with $\lbrack B\rbrack_{ij} = \lambda\lbrack A\rbrack_{ij}$, i.e. $b_{ij} = \lambda a_{ij}$:

$$
3\begin{pmatrix}
1 & 3 & 2 \\
4 & 5 & 6
\end{pmatrix} = \begin{pmatrix}
3 & 9 & 6 \\
12 & 15 & 18
\end{pmatrix}
$$

Each element of $A$ is multiplied by $\lambda$.

$(\lambda + \mu)A = \lambda A + \mu A$; $\quad\lambda(\mu A) = (\lambda\mu)A$.

---
> [[MBD 03 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|← Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 05 - Module 2 – Matrices · Sum + Row-by-column product|Module 2 – Matrices · Sum + Row-by-column product →]]
