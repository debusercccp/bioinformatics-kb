---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 3
tags: [note, mbd]
---

> [[MBD 02 - Module 1 – Vectors and Hyperplanes · Scalar (dot) product|← Module 1 – Vectors and Hyperplanes · Scalar (dot) product]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 04 - Module 2 – Matrices · Definitions + Product by a scalar|Module 2 – Matrices · Definitions + Product by a scalar →]]

# Hyperplanes and linear classification

Linear classification separates two clouds of points with a flat object: in 2D with **lines**, in 3D with **planes**, in $n$D with **hyperplanes**.

### 1.5.1 Line / hyperplane through the origin

In 2D, a line through the origin is the set of points $\overrightarrow{x}$ perpendicular to a vector $\overrightarrow{w}$:

$$
\overrightarrow{x} \in \text{line}\quad \Leftrightarrow \quad\overrightarrow{w} \cdot \overrightarrow{x} = \langle\overrightarrow{w},\overrightarrow{x}\rangle = 0\quad \Leftrightarrow \quad w_{1}x_{1} + w_{2}x_{2} = 0\quad \Rightarrow \quad x_{2} = - \frac{w_{1}}{w_{2}}x_{1}\quad\text{if }w_{2} \neq 0
$$

($- w_{1}/w_{2}$ is the slope). In $n$ dimensions, the hyperplane through the origin is

$$
\langle\overrightarrow{w},\overrightarrow{x}\rangle = \overrightarrow{w} \cdot \overrightarrow{x} = w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} + \ldots + w_{n}x_{n} = 0
$$

In $\mathbb{R}^{2}$ a hyperplane is a line, in $\mathbb{R}^{3}$ it is a plane: the plane through the origin is the set of vectors perpendicular to $\overrightarrow{w}$, $w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} = 0$.

### 1.5.2 Line / hyperplane not through the origin

A line not through the origin is the set of points with **equal projection on** $\overrightarrow{w}$. With the signed projection $p = \parallel \overrightarrow{x} \parallel cos\theta$:

A vector $\overrightarrow{w}$ defines an infinity of lines perpendicular to it; a particular line is fixed when the projection of its points on $\overrightarrow{w}$ is fixed to a value $p$. $p > 0$ if the line lies on the side $\overrightarrow{w}$ points to, $p < 0$ if it lies on the opposite side: the line separates the plane into two half-spaces.

$$
p = \frac{\overrightarrow{x} \cdot \overrightarrow{w}}{\parallel \overrightarrow{w} \parallel} = \text{constant}\quad \Rightarrow \quad\overrightarrow{x} \cdot \overrightarrow{w} = p\, \parallel \overrightarrow{w} \parallel \text{ constant}\quad \Rightarrow \quad\overrightarrow{x} \cdot \overrightarrow{w} + b = 0,\quad b = - p\, \parallel \overrightarrow{w} \parallel
$$

$$
\boxed{\langle\overrightarrow{x},\overrightarrow{w}\rangle + b = 0}
$$

In $n$D the **hyperplane** is

$$
\langle\overrightarrow{w},\overrightarrow{x}\rangle + b = w_{1}x_{1} + w_{2}x_{2} + \ldots + w_{n}x_{n} + b = 0
$$

whose parameters are $w_{1},\ldots,w_{n}$ and $b$. Summary: $\overrightarrow{w} \in \mathbb{R}^{n}$ is perpendicular ($\bot$) to the hyperplane, the projection (signed distance of the hyperplane from the origin) is $- b/ \parallel \overrightarrow{w} \parallel$, and $b = 0$ gives a hyperplane through the origin. For every point of the hyperplane $p = \parallel \overrightarrow{x} \parallel cos\theta$, and therefore $\parallel \overrightarrow{w} \parallel \parallel \overrightarrow{x} \parallel cos\theta$, are constant.

With $- b/ \parallel \overrightarrow{w} \parallel$ as the distance from the origin, $b < 0$ puts the hyperplane on the side $\overrightarrow{w}$ points to and $b > 0$ on the opposite side.

### 1.5.3 Why it is useful: classification

Many problems amount to finding a (hyper)plane that separates the points of two classes (Class 1 / Class −1). Machine-learning methods find the optimal separating hyperplane with different optimality criteria, e.g. **perceptrons** (simple neural networks) and **Support Vector Machines**. Once $\overrightarrow{w}$ and $b$ are known, a new point $\overrightarrow{y}$ is classified by

$$
f\left( \overrightarrow{y} \right) = \overrightarrow{y} \cdot \overrightarrow{w} + b = w_{1}y_{1} + w_{2}y_{2} + \ldots + w_{n}y_{n} + b
$$

- $f\left( \overrightarrow{y} \right) > 0 \Rightarrow \overrightarrow{y}$ in the positive class;
- $f\left( \overrightarrow{y} \right) < 0 \Rightarrow \overrightarrow{y}$ in the negative class.

This is what a **perceptron** (the simplest neural network) computes: inputs $y_{1},\ldots,y_{n}$, weights $w_{1},\ldots,w_{n}$, threshold $- b$. The **training** is the procedure that finds $\overrightarrow{w}$ and $b$ assigning the correct class to all the points of a set of known examples (see §4.6.1 for a training by gradient descent).

## Collegamenti
- [[AML 12 - Logistic Regression · Decision Boundary]] — decision boundary nella regressione logistica

---
> [[MBD 02 - Module 1 – Vectors and Hyperplanes · Scalar (dot) product|← Module 1 – Vectors and Hyperplanes · Scalar (dot) product]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 04 - Module 2 – Matrices · Definitions + Product by a scalar|Module 2 – Matrices · Definitions + Product by a scalar →]]
