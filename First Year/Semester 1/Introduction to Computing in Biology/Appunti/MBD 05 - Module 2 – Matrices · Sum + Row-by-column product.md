---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 5
tags: [note, mbd]
---

> [[MBD 04 - Module 2 – Matrices · Definitions + Product by a scalar|← Module 2 – Matrices · Definitions + Product by a scalar]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 06 - Module 2 – Matrices · Transpose matrix … Orthogonal matrices|Module 2 – Matrices · Transpose matrix … Orthogonal matrices →]]

# Sum

For $A,B \in \mathbb{R}^{m \times n}$, $C = A + B \in \mathbb{R}^{m \times n}$ with $c_{ij} = a_{ij} + b_{ij}$:

$$
\begin{pmatrix}
1 & 2 \\
2 & 1 \\
0 & 3
\end{pmatrix} + \begin{pmatrix}
0 & 3 \\
1 & 1 \\
 - 1 & 0
\end{pmatrix} = \begin{pmatrix}
1 & 5 \\
3 & 2 \\
 - 1 & 3
\end{pmatrix}
$$

$A + (B + C) = (A + B) + C$; $\quad A + B = B + A$; $\quad\lambda(A + B) = \lambda A + \lambda B$.

The sum (and the difference) is possible **only if the matrices have the same size**: they are then *conformable for addition*. Matrices of different size cannot be added or subtracted.

The three properties are the commutative, associative and distributive laws. *Proof of* $\lambda(A + B) = \lambda A + \lambda B$: let $C = \lambda(A + B)$; then $c_{ij} = \lambda\left( a_{ij} + b_{ij} \right) = \lambda a_{ij} + \lambda b_{ij}$, so $C = \lambda A + \lambda B$.

## 2.4 Row-by-column product

$A \in \mathbb{R}^{m \times p}$ and $B \in \mathbb{R}^{p \times n}$ are **conformable for the product** (columns of $A$ = rows of $B$), and

$$
A \cdot B = C \in \mathbb{R}^{m \times n},\quad\quad c_{ij} = \sum_{k}^{}a_{ik}\, b_{kj}
$$

where $a_{ik}$ runs along the $i$-th row of $A$ and $b_{kj}$ along the $j$-th column of $B$.

$$
c_{ij} = \sum_{k = 1}^{p}a_{ik}\, b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \ldots + a_{ip}b_{pj},\quad\quad(m \times p)(p \times n) \rightarrow (m \times n)
$$

i.e. $c_{ij}$ is the scalar product of the $i$-th row of $A$ with the $j$-th column of $B$.

*Example.*

$$
\begin{pmatrix}
2 & 1 & 3 \\
1 & 2 & 3
\end{pmatrix}\begin{pmatrix}
1 & 2 & 1 \\
3 & 1 & 0 \\
 - 1 & 0 & 1
\end{pmatrix} = \begin{pmatrix}
2 \cdot 1 + 1 \cdot 3 + 3 \cdot ( - 1) & 2 \cdot 2 + 1 \cdot 1 + 3 \cdot 0 & 2 \cdot 1 + 1 \cdot 0 + 3 \cdot 1 \\
4 & 4 & 4
\end{pmatrix} = \begin{pmatrix}
2 & 5 & 5 \\
4 & 4 & 4
\end{pmatrix}
$$

### 2.4.1 The product is not commutative

With $A \in \mathbb{R}^{m \times p}$ and $B \in \mathbb{R}^{p \times n}$, $AB \in \mathbb{R}^{m \times n}$, while $BA$ is defined only if $m = n$, and then $BA \in \mathbb{R}^{p \times p}$. For square matrices $A,B \in \mathbb{R}^{n \times n}$ both $AB$ and $BA$ are in $\mathbb{R}^{n \times n}$, but **in general** $AB \neq BA$; if $AB = BA$, $A$ and $B$ **commute**.

$$
A = \begin{pmatrix}
2 & 1 \\
0 & 3
\end{pmatrix},\mspace{6mu} B = \begin{pmatrix}
1 & - 1 \\
2 & 0
\end{pmatrix}:\quad\quad AB = \begin{pmatrix}
4 & - 2 \\
6 & 0
\end{pmatrix},\quad\quad BA = \begin{pmatrix}
2 & - 2 \\
4 & 2
\end{pmatrix}
$$

$$
C = \begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}:\quad\quad AC = \begin{pmatrix}
4 & 1 \\
0 & 3
\end{pmatrix},\quad\quad CA = \begin{pmatrix}
4 & 2 \\
0 & 3
\end{pmatrix}
$$

$$
I = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}:\quad\quad AI = IA = \begin{pmatrix}
2 & 1 \\
0 & 3
\end{pmatrix} = A
$$

$I$ is the **identity** matrix.

*Example from the slides.* $A = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 4
\end{pmatrix}$, $B = \begin{pmatrix}
 - 1 & 2 \\
2 & 3 \\
5 & 0
\end{pmatrix}$: $c_{11} = 1( - 1) + 2(2) + 3(5) = 18$, $c_{12} = 1(2) + 2(3) + 3(0) = 8$, $c_{21} = 0( - 1) + 1(2) + 4(5) = 22$, $c_{22} = 0(2) + 1(3) + 4(0) = 3$:

$$
AB = \begin{pmatrix}
18 & 8 \\
22 & 3
\end{pmatrix},\quad\quad BA = \begin{pmatrix}
 - 1 & 0 & 5 \\
2 & 7 & 18 \\
5 & 10 & 15
\end{pmatrix}\quad\quad\left( AB \neq BA,\text{ not even the same size} \right)
$$

Every square matrix commutes with itself and with the identity, $AI = IA = A$.

### 2.4.2 Vectors as matrices

Writing $\overrightarrow{v}$ as an $n \times 1$ matrix $A$, its transpose is the row $A^{t} = \left( v_{1},\ldots,v_{n} \right)$ and

In general, if $A$ is a $1 \times m$ row and $B$ an $m \times 1$ column, $AB = \sum_{k}^{}a_{1k}b_{k1}$ is a **scalar**, but $BA$ is an $m \times m$ matrix with entries $b_{i1}a_{1j}$: again $AB \neq BA$.

$$
A^{t}A = \left( v_{1},\ldots,v_{n} \right)\begin{pmatrix}
v_{1} \\
 \vdots \\
v_{n}
\end{pmatrix} = \parallel \overrightarrow{v} \parallel^{2}
$$

$$
{\overrightarrow{v}}^{\, t}\overrightarrow{w} = \left( v_{1},\ldots,v_{n} \right)\begin{pmatrix}
w_{1} \\
 \vdots \\
w_{n}
\end{pmatrix} = \langle\overrightarrow{v},\overrightarrow{w}\rangle,\quad\quad\overrightarrow{v}\,{\overrightarrow{w}}^{\, t} = \begin{pmatrix}
v_{1} \\
 \vdots \\
v_{n}
\end{pmatrix}\left( w_{1},\ldots,w_{n} \right) = n \times n\text{ matrix}
$$

### 2.4.3 No cancellation rules

$$
AB = AC\quad \nRightarrow \quad B = C,\quad\quad\quad AB = 0\quad \nRightarrow \quad B = 0\text{ or }A = 0
$$

Other properties of the product (for conformable matrices): $A(B + C) = AB + AC$; $(A + B)C = AC + BC$; $A(BC) = (AB)C$. *Proof of* $A(B + C) = AB + AC$: with $X = B + C$, $y_{ij} = \sum_{k}^{}a_{ik}\left( b_{kj} + c_{kj} \right) = \sum_{k}^{}a_{ik}b_{kj} + \sum_{k}^{}a_{ik}c_{kj}$.

*Counter-examples.* With $A = \begin{pmatrix}
1 & 0 \\
1 & 0 \\
1 & 0
\end{pmatrix}$:

$$
B = \begin{pmatrix}
0 & 0 & 0 \\
1 & 1 & 1
\end{pmatrix} \Rightarrow AB = 0\text{ although }A,B \neq 0;\quad\quad B = \begin{pmatrix}
1 & 1 & 1 \\
1 & 1 & 1
\end{pmatrix},\ C = \begin{pmatrix}
1 & 1 & 1 \\
0 & 0 & 0
\end{pmatrix} \Rightarrow AB = AC\text{ although }B \neq C
$$

---
> [[MBD 04 - Module 2 – Matrices · Definitions + Product by a scalar|← Module 2 – Matrices · Definitions + Product by a scalar]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 06 - Module 2 – Matrices · Transpose matrix … Orthogonal matrices|Module 2 – Matrices · Transpose matrix … Orthogonal matrices →]]
