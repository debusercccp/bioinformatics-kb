---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 1
tags: [note, mbd]
---

> [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 02 - Module 1 – Vectors and Hyperplanes · Scalar (dot) product|Module 1 – Vectors and Hyperplanes · Scalar (dot) product →]]

# Vectors

A vector can be seen as a displacement: going from Bologna to Milano is described by the two components of the displacement, $\overrightarrow{S} = \left( S_{x},S_{y} \right)$, along the two axes. In general a vector in $n$ dimensions is a column of $n$ real numbers:

$$
\overrightarrow{v} = \begin{pmatrix}
v_{1} \\
v_{2} \\
 \vdots \\
v_{n}
\end{pmatrix} \in \mathbb{R}^{n}
$$

$n$ can be very large: an expression profile is a vector with $\approx 20,000$ components, $\overrightarrow{a} = \left( a_{1},\ldots,a_{20000} \right)^{T}$, $\overrightarrow{b} = \left( b_{1},\ldots,b_{20000} \right)^{T}$, and all the operations below work the same way.

**Notation.** A vector can be written with an arrow ($\overrightarrow{a}$), in bold (**a**), or as a column array; its transpose is the corresponding row: ${\overrightarrow{v}}^{\, T} = \left( v_{1},v_{2},\ldots,v_{n} \right)$.

## 1.2 Norm

In $\mathbb{R}^{2}$ the length of $\overrightarrow{v} = \left( v_{1},v_{2} \right)^{T}$ is given by Pythagoras; this is the **norm** $L_{2}$:

$$
\parallel \overrightarrow{v} \parallel = \sqrt{v_{1}^{2} + v_{2}^{2}},\quad\quad\overrightarrow{v} \in \mathbb{R}^{n}:\quad \parallel \overrightarrow{v} \parallel = \sqrt{v_{1}^{2} + v_{2}^{2} + \ldots + v_{n}^{2}} = \sqrt{\sum_{i = 1}^{n}v_{i}^{2}}
$$

*Note:* on the whiteboard of 20 Oct the norm is written as $\sum_{i}^{}\left( v_{i} \right)^{2}$ without the square root: that is $\parallel \overrightarrow{v} \parallel^{2}$.

**Properties of a norm.**

1.  $\parallel X + Y \parallel \leq \parallel X \parallel + \parallel Y \parallel$ (triangle inequality)
2.  $\parallel \lambda X \parallel = |\lambda|\, \parallel X \parallel$
3.  $\parallel X \parallel > 0$ if $X \neq \overrightarrow{0}$

## 1.3 Vector operations

### 1.3.1 Product by a scalar

For $\lambda \in \mathbb{R}$ and $\overrightarrow{v} \in \mathbb{R}^{n}$:

$$
\overrightarrow{u} = \lambda\overrightarrow{v} = \begin{pmatrix}
\lambda v_{1} \\
\lambda v_{2} \\
 \vdots \\
\lambda v_{n}
\end{pmatrix},\quad\quad\left( \lambda\overrightarrow{v} \right)_{i} = \lambda v_{i},\quad\quad\lambda\overrightarrow{v} \in \mathbb{R}^{n}
$$

For $\lambda,\mu \in \mathbb{R}$: $(\lambda + \mu)\overrightarrow{v} = \lambda\overrightarrow{v} + \mu\overrightarrow{v}$; $\quad(\lambda\mu)\overrightarrow{v} = \lambda\left( \mu\overrightarrow{v} \right)$.

The components of the rescaled vector are the rescaled components: geometrically $\lambda\overrightarrow{v}$ has the same direction as $\overrightarrow{v}$ and a length multiplied by $|\lambda|$ (the verse is reversed if $\lambda < 0$).

### 1.3.2 Sum

For $\overrightarrow{v},\overrightarrow{w} \in \mathbb{R}^{n}$ the sum is computed component by component:

$$
\overrightarrow{u} = \overrightarrow{v} + \overrightarrow{w} = \begin{pmatrix}
v_{1} + w_{1} \\
v_{2} + w_{2} \\
 \vdots \\
v_{n} + w_{n}
\end{pmatrix},\quad\quad\left( \overrightarrow{v} + \overrightarrow{w} \right)_{i} = v_{i} + w_{i},\quad\quad\overrightarrow{v} + \overrightarrow{w} \in \mathbb{R}^{n}
$$

Example in the plane: $(1,0)^{T} + (0,1)^{T} = (1,1)^{T}$ (the diagonal of the square built on the two vectors).

The components of the sum vector are the sums of the components; geometrically the sum is the diagonal of the parallelogram built on the two vectors.

### 1.3.3 Difference

$$
\overrightarrow{u} = \overrightarrow{v} - \overrightarrow{w} = \overrightarrow{v} + ( - 1)\,\overrightarrow{w} = \begin{pmatrix}
v_{1} - w_{1} \\
v_{2} - w_{2} \\
 \vdots \\
v_{n} - w_{n}
\end{pmatrix}
$$

Geometrically, if $\overrightarrow{v}$ and $\overrightarrow{w}$ point to $A$ and $B$, the difference $\overrightarrow{u} = \overrightarrow{v} - \overrightarrow{w}$ is the arrow joining $B$ to $A$, and its norm is the **distance between A and B**:

$$
d(A,B) = \parallel \overrightarrow{u} \parallel = \parallel \overrightarrow{v} - \overrightarrow{w} \parallel
$$

The distance is symmetric, $d(A,B) = \parallel A - B \parallel = \parallel B - A \parallel$; in 2D

$$
d(A,B) = \sqrt{\left( B_{1} - A_{1} \right)^{2} + \left( B_{2} - A_{2} \right)^{2}}
$$

### 1.3.4 Properties

For $\lambda,\mu \in \mathbb{R}$ and $\overrightarrow{u},\overrightarrow{v},\overrightarrow{w} \in \mathbb{R}^{n}$:

$$
\lambda\left( \overrightarrow{u} + \overrightarrow{v} \right) = \lambda\overrightarrow{u} + \lambda\overrightarrow{v},\quad(\lambda + \mu)\overrightarrow{v} = \lambda\overrightarrow{v} + \mu\overrightarrow{v},\quad\left( \overrightarrow{u} + \overrightarrow{v} \right) + \overrightarrow{w} = \overrightarrow{u} + \left( \overrightarrow{v} + \overrightarrow{w} \right),\quad\overrightarrow{u} + \overrightarrow{v} = \overrightarrow{v} + \overrightarrow{u}
$$

---
> [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 02 - Module 1 – Vectors and Hyperplanes · Scalar (dot) product|Module 1 – Vectors and Hyperplanes · Scalar (dot) product →]]
