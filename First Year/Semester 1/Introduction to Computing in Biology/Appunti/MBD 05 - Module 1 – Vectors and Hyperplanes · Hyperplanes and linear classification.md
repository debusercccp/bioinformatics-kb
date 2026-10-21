---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 5
tags: [note, mbd]
---

> [[MBD 04 - Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different|← Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 06 - Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed|Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed →]]

# Hyperplanes and linear classification

**Hyperplane through the origin.** The set of vectors $X$ orthogonal to a normal weight vector $W$:

$$
\langle X,W\rangle = 0 \Longrightarrow \sum_{i = 1}^{n}W_{i}X_{i} = 0
$$

In $\mathbb{R}^{2}$ a line, in $\mathbb{R}^{3}$ a plane, in $\mathbb{R}^{n}$ an $(n - 1)$-dimensional subspace.

**General hyperplane with offset** $b$**.** Fix the **signed** projection of $X$ onto $W$ to the value $p = \parallel X \parallel cos\vartheta = \langle X,W\rangle/ \parallel W \parallel$ and set $p = - b/ \parallel W \parallel$:

$$
\langle X,W\rangle + b = W^{T}X + b = 0
$$

- $p > 0$ (i.e. $b < 0$): the hyperplane lies on the side $W$ points to.
- $p < 0$ (i.e. $b > 0$): it lies in the opposite half-space.

> **Correction.** The slides call $p$ a “scalar distance”. It is the **signed** scalar projection; the distance is its absolute value.

### 1.4.1 The missing computational piece: distance from a point to a hyperplane

$$
d\left( Y\mathcal{,H} \right) = \frac{\left| \langle Y,W\rangle + b \right|}{\parallel W \parallel}
$$

*Derivation.* The signed projection of $Y$ onto the unit normal $\widehat{W} = W/ \parallel W \parallel$ is $\langle Y,\widehat{W}\rangle$; the hyperplane sits at signed position $- b/ \parallel W \parallel$ along that same direction; subtract and take the absolute value.

### 1.4.2 Binary classification

Many classification problems seek an optimal separating hyperplane — **perceptrons**, **support vector machines** — dividing data into class $+ 1$ and class $- 1$. Given $W$ and $b$, a new point $Y$ is classified by the decision function

$$
f(Y) = \langle Y,W\rangle + b = \sum_{i = 1}^{n}w_{i}y_{i} + b,\quad\quad f(Y) > 0 \Rightarrow + 1,\quad\quad f(Y) < 0 \Rightarrow - 1
$$

**Training** is the algorithmic procedure that finds the $W$ and $b$ correctly classifying the examples of a training set.

Consequences of §1.4.1:

- $f(Y)$ is a **scaled signed distance**, not a probability. Its sign gives the class, its magnitude the confidence.
- Rescaling $(W,b) \rightarrow (\lambda W,\lambda b)$ leaves the hyperplane unchanged but multiplies $f$ by $\lambda$, so $f$ is comparable only across points of the *same* trained model.
- The SVM **margin** is $2/ \parallel W \parallel$, so maximising the margin means minimising $\parallel W \parallel$. The geometry of §1.3.5 reappears as the SVM objective, and the same $L^{2}$ norm reappears as ridge regularisation in Module 7.

## Collegamenti
- [[AML 12 - Logistic Regression · Decision Boundary]] — decision boundary nella regressione logistica

---
> [[MBD 04 - Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different|← Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 06 - Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed|Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed →]]
