---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 14
tags: [note, mbd]
---

> [[MBD 13 - Module 4 – Single-Variable Calculus|← Module 4 – Single-Variable Calculus]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 15 - Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem|Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem →]]

# Module 5 — Multivariable Calculus and Optimisation

## 5.1 Partial derivatives, gradient, Hessian

For $z = f(x,y)$, **level curves (contour lines)** are the curves in the $(x,y)$-plane along which $f(x,y) = c$ — contour lines on a topographic map.

### 5.1.1 First partial derivatives — how they are computed

Differentiate with respect to one variable while **holding all the others constant**:

$$
\frac{\partial f}{\partial x} = f_{x} = \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x,y) - f(x,y)}{\Delta x},\quad\quad\frac{\partial f}{\partial y} = f_{y} = \lim_{\Delta y \rightarrow 0}\frac{f(x,y + \Delta y) - f(x,y)}{\Delta y}
$$

Every single-variable rule of §4.2.1 applies unchanged; the only new instruction is *treat the other variables as numbers*.

*Worked example.* $f(x,y) = 5x^{4} - x^{2}y^{2} + 2x^{3}y$:

$$
f_{x} = 20x^{3} - 2xy^{2} + 6x^{2}y,\quad\quad f_{y} = - 2x^{2}y + 2x^{3}
$$

*With the quotient rule.* $f(x,y) = \frac{xy}{x - y}$ at $(2, - 2)$:

$$
f_{x} = \frac{(x - y)y - xy}{(x - y)^{2}} = \frac{- y^{2}}{(x - y)^{2}} \Longrightarrow f_{x}(2, - 2) = \frac{- 4}{16} = - \frac{1}{4}
$$

$$
f_{y} = \frac{(x - y)x + xy}{(x - y)^{2}} = \frac{x^{2}}{(x - y)^{2}} \Longrightarrow f_{y}(2, - 2) = \frac{4}{16} = \frac{1}{4}
$$

**Geometric meaning.** For fixed $x = x_{0}$, the curve $z = f\left( x_{0},y \right)$ is the intersection of the surface with the plane $x = x_{0}$; $f_{x}\left( x_{0},y_{0} \right)$ is the slope of that curve at $\left( x_{0},y_{0},f\left( x_{0},y_{0} \right) \right)$.

**More than two variables.** For $w = f\left( x_{1},\ldots,x_{n} \right)$ there are $n$ partial derivatives, each holding the other $n - 1$ fixed.

### 5.1.2 Second-order partials and Schwarz’s theorem

$$
f_{xx} = \frac{\partial^{2}f}{\partial x^{2}},\quad f_{yy} = \frac{\partial^{2}f}{\partial y^{2}},\quad f_{xy} = \frac{\partial^{2}f}{\partial y\,\partial x},\quad f_{yx} = \frac{\partial^{2}f}{\partial x\,\partial y}
$$

**Schwarz’s theorem.** If the mixed partials are continuous on an open disk, they are equal regardless of the order of differentiation:

$$
f_{xy}(x,y) = f_{yx}(x,y)
$$

*Worked example.* $f(x,y) = 3xy^{2} - 2y + 5x^{2}y$ gives $f_{x} = 3y^{2} + 10xy$, $f_{y} = 6xy - 2 + 5x^{2}$, $f_{xx} = 10y$, $f_{yy} = 6x$, and $f_{xy} = f_{yx} = 6y + 10x$.

*Three variables.* $f(x,y,z) = ye^{x} + x\ln z$ gives $f_{xz} = f_{zx} = \frac{1}{z}$, and all of $f_{xzz}$, $f_{zxz}$, $f_{zzx}$ equal $- \frac{1}{z^{2}}$: any permutation of the same derivatives gives the same result.

> **The consequence that is used later and never stated.** Schwarz’s theorem is precisely **why the Hessian is symmetric**, and symmetry is what the spectral theorem (§3.4.3) needs in order to guarantee real eigenvalues. Without Schwarz, the classification of §5.2 by the sign of the eigenvalues would not even be well posed, because the eigenvalues could be complex.

### 5.1.3 Gradient

For $f:\mathbb{R}^{n}\mathbb{\rightarrow R}$ of class $C^{2}$, the **gradient** is the vector of first partial derivatives:

$$
\nabla f(x) = \left( \frac{\partial f}{\partial x_{1}},\frac{\partial f}{\partial x_{2}},\ldots,\frac{\partial f}{\partial x_{n}} \right)
$$

**Geometric properties.** From $f\left( x + \varepsilon_{x},y + \varepsilon_{y} \right) \approx f(x,y) + \nabla f^{T}\varepsilon$, two points on the same level curve both equal $c$, so $\nabla f^{T}\varepsilon = 0$. For small $\varepsilon$, $\varepsilon$ is parallel to the curve, hence:

- **the gradient is locally perpendicular (normal) to the level curves**, and
- **it points in the direction of maximum increase** of $f$.

> **A dimensional remark worth making explicit.** The gradient of a scalar function is a *vector*, one component per input variable. It is **not** a derivative “with respect to a direction” — that is the directional derivative $D_{u}f = \langle\nabla f,u\rangle$ for a unit $u$. Cauchy–Schwarz (§1.3.4) says $\left| D_{u}f \right| \leq \parallel \nabla f \parallel$ with equality when $u \parallel \nabla f$: *this inequality is the proof* that the gradient is the direction of steepest ascent. The two facts above are one application of §1.3 each — orthogonality and Cauchy–Schwarz.

### 5.1.4 Hessian

The symmetric $n \times n$ matrix of second-order partials:

$$
H_{ij} = \frac{\partial^{2}f}{\partial x_{i}\,\partial x_{j}}
$$

### 5.1.5 Multivariable Taylor expansion

Around a point $x^{*}$:

$$
f(x) = f\left( x^{*} \right) + \nabla f\left( x^{*} \right)^{T}\left( x - x^{*} \right) + \frac{1}{2}\left( x - x^{*} \right)^{T}H\left( x^{*} \right)\left( x - x^{*} \right) + \ldots
$$

This is §4.3.3 with $\nabla f$ in place of $f'$ and $H$ in place of $f''$. The quadratic term is a quadratic form (§3.4.4): near a critical point, where the linear term vanishes, the surface *is* a quadratic form, and its shape is read off the eigenvalues of $H$. That is the whole content of the next section.

## 5.2 Unconstrained optimisation

**Necessary condition for a local optimum.** $\nabla f\left( x^{*} \right) = 0$: all first partial derivatives vanish, and $x^{*}$ is a stationary (critical) point.

**Second-order classification via the eigenvalues of** $H\left( x^{*} \right)$**.** Since $H$ is real and symmetric, all $n$ eigenvalues $\lambda_{1},\ldots,\lambda_{n}$ are real (spectral theorem, §3.4.3):

| All $\lambda_{i} > 0$ ($H$ positive definite) | **local minimum** |
|----|----|
| All $\lambda_{i} < 0$ ($H$ negative definite) | **local maximum** |
| Eigenvalues of **different signs** | **saddle point** |
| Some $\lambda_{i} = 0$ | inconclusive — higher-order terms decide |

> **Correction — important, because the slide states this backwards.** The slide reads *“a maximum if all eigenvalues are positive, a minimum if all the eigenvalues are negative.”* This is inverted. The worked Example 2 on the following slides confirms the correct version: at $(1/2,1/2)$, $\lambda = - 2, - 4$ (both negative) is labelled MAXIMUM, and at $( - 1/2, - 1/2)$, $\lambda = + 2, + 4$ (both positive) is labelled MINIMUM.
>
> **Positive eigenvalues = minimum.** The one-dimensional mnemonic of §4.3.2 carries over exactly: $f'' > 0$ is concave up, which holds a minimum, and the eigenvalues of $H$ are the second derivatives along the principal axes.
>
> The last row of the table is also absent from the slides: a zero eigenvalue makes the second-order test **inconclusive**, not a saddle.

**Why the eigenvalues and not the entries of** $H$**.** The eigenvalues are the curvatures along the principal axes of the quadratic form (§3.4.4). Reading the diagonal entries of $H$ instead would be reading the curvature along the *coordinate* axes, which is only the same thing when $H$ happens to be diagonal. Sylvester’s criterion (§3.4.3) gives the same classification from leading principal minors without computing eigenvalues, and is faster by hand for $2 \times 2$ and $3 \times 3$.

### 5.2.1 Worked examples

**Example 1 — a saddle.** $f(x,y) = x^{2} - 4y^{2}$. Then $\nabla f = (2x, - 8y)$, vanishing only at $(0,0)$, and

$$
H = \begin{pmatrix}
2 & 0 \\
0 & - 8
\end{pmatrix}\quad\text{(constant)}
$$

Eigenvalues $+ 2$ and $- 8$: **different signs, so a saddle point**. Along $x$ the surface curves up, along $y$ it curves down.

**Example 2 — a maximum and a minimum.** $f(x,y) = (x + y)e^{- x^{2} - y^{2}}$.

$$
\nabla f = e^{- x^{2} - y^{2}}\begin{pmatrix}
1 - 2x^{2} - 2xy \\
1 - 2y^{2} - 2xy
\end{pmatrix}
$$

Setting both to zero: subtracting gives $x^{2} = y^{2}$. The branch $x = - y$ gives $1 - 2x^{2} + 2x^{2} = 1 = 0$, impossible; the branch $x = y$ gives $1 - 4x^{2} = 0$, so $x = \pm 1/2$. Critical points $(1/2,1/2)$ and $( - 1/2, - 1/2)$.

$$
H(1/2,1/2) = e^{- 1/2}\begin{pmatrix}
 - 3 & - 1 \\
 - 1 & - 3
\end{pmatrix} \Longrightarrow \lambda_{1} = - 2,\ \lambda_{2} = - 4 \Longrightarrow \text{MAXIMUM}
$$

$$
H( - 1/2, - 1/2) = e^{- 1/2}\begin{pmatrix}
3 & 1 \\
1 & 3
\end{pmatrix} \Longrightarrow \lambda_{1} = + 2,\ \lambda_{2} = + 4 \Longrightarrow \text{MINIMUM}
$$

(For the eigenvalues of $\begin{pmatrix}
a & b \\
b & a
\end{pmatrix}$ there is a shortcut: they are $a \pm b$, with eigenvectors $(1,1)^{T}$ and $(1, - 1)^{T}$.)

### 5.2.2 Steepest descent

Steepest descent finds a **local** minimum by always stepping in the downhill direction:

$$
x^{(t + 1)} = x^{(t)} - \eta\,\nabla f\left( x^{(t)} \right)
$$

The minus sign is because $\nabla f$ points *uphill* (§5.1.3). This is §4.3.4 in $n$ dimensions, and $\eta$ is the learning rate, with the same trade-off.

### 5.2.3 Biological application: protein folding on an energy landscape

- A protein conformation is a vector of bond and dihedral angles $x = \left( x_{1},\ldots,x_{n} \right) \in \mathbb{R}^{n}$ on a potential energy surface $E(x)$.
- **Native state (correctly folded):** a minimum, where $\nabla E\left( x^{*} \right) = 0$ and $H = \nabla^{2}E\left( x^{*} \right)$ is **positive definite**.
- **Physical folding as steepest descent:** $x^{(t + 1)} = x^{(t)} - \eta\nabla E\left( x^{(t)} \right)$.
- **Saddle points** are **transition states** — activation energy barriers along the folding pathway.
- **Local minima traps** explain **misfolding diseases** (Alzheimer’s, Parkinson’s), where a protein becomes kinetically trapped in a wrong local minimum instead of reaching the global one.

> **The point of the example.** It makes concrete why the distinction between the three classes of critical point is not bookkeeping: minima are stable structures, saddles are the barriers between them and set the folding *rate*, and the gradient flow is the physics. It also shows the central limitation of all first-order methods — gradient descent cannot escape a local minimum, which is exactly the biological failure mode.

## 5.3 Constrained optimisation: Lagrange multipliers

To maximise or minimise $f(x,y)$ subject to a constraint $g(x,y) = c$.

**The naive route.** Solve the constraint for one variable, $y = h(x)$, substitute, and maximise $f\left( x,h(x) \right)$ in one variable. This works when the constraint can be solved explicitly — which in practice it usually cannot.

**Geometric principle.** Walking along the constraint curve, the value of $f$ changes as long as you keep crossing contour lines of $f$. Only where the constraint curve is **tangent** to a contour line does $f$ stop changing to first order: that is the constrained optimum. Tangency means the two normals are parallel, and the normal to a level curve is its gradient (§5.1.3):

$$
\nabla_{x,y}f = \lambda\,\nabla_{x,y}g
$$

**The Lagrangian.** Introduce the multiplier $\lambda$ and define

$$
F(x,y,\lambda) = f(x,y) - \lambda\,\left( g(x,y) - c \right)
$$

then solve $\nabla_{x,y,\lambda}F = 0$. Differentiating with respect to $\lambda$ returns the constraint itself, so the single system encodes both conditions. For $m$ constraints $g_{i}(x) = 0$, introduce $m$ multipliers:

$$
\frac{\partial}{\partial x}\left\lbrack f(x) + \sum_{i = 1}^{m}\alpha_{i}g_{i}(x) \right\rbrack = 0
$$

> **What** $\lambda$ **actually is**, beyond an algebraic device: $\lambda = \frac{\partial f^{*}}{\partial c}$, the rate of change of the optimal value as the constraint is relaxed. In economics it is the **shadow price**; in the bacterial example below it is the growth gained per unit of extra protein budget. A large $\lambda$ says the constraint is expensive, $\lambda = 0$ says it is not binding.

### 5.3.1 Worked example: maximum-volume box

Maximise $f(x,y,z) = xyz$ subject to total surface area $2(xy + xz + yz) = 64$, i.e. $g = xy + xz + yz - 32 = 0$.

$$
L = xyz - \lambda(xy + xz + yz - 32)
$$

$$
\frac{\partial L}{\partial x} = yz - \lambda(y + z) = 0,\quad\frac{\partial L}{\partial y} = xz - \lambda(x + z) = 0,\quad\frac{\partial L}{\partial z} = xy - \lambda(x + y) = 0
$$

Multiplying the first by $x$ and the second by $y$ and subtracting gives $z(y - x) = 0$; similarly $y(z - x) = 0$ and $x(z - y) = 0$. Since no edge is zero, $x = y = z$. Substituting into the constraint, $3x^{2} = 32$, so

$$
x = y = z = \sqrt{32/3} = 4\sqrt{2/3} \approx 3.266\ cm
$$

The maximum-volume box of fixed surface area is a cube — as symmetry would suggest, and as the symmetry of the three stationarity equations formalises.

### 5.3.2 Optimal resource allocation in a growing bacterium

A bacterium divides its total protein budget $C$ between ribosomes ($c_{1}$) and metabolic enzymes ($c_{2}$), subject to $c_{1} + c_{2} = C$. Growth rate follows a Cobb–Douglas form:

$$
\mu\left( c_{1},c_{2} \right) = r\, c_{1}^{\alpha}c_{2}^{1 - \alpha}
$$

which is concave with no free maximum — it grows in both arguments, so the optimum exists only because of the budget constraint. Solving $\nabla\mu = \lambda\nabla g$:

$$
\frac{\alpha\mu}{c_{1}} = \lambda = \frac{(1 - \alpha)\mu}{c_{2}} \Longrightarrow \frac{c_{1}}{c_{2}} = \frac{\alpha}{1 - \alpha} \Longrightarrow c_{1}^{*} = \alpha C,\quad c_{2}^{*} = (1 - \alpha)C
$$

In *E. coli*, proteomics data give $\alpha \approx 0.6$. The multiplier $\lambda$ is the **shadow price** of the resource: the marginal growth per unit of extra protein budget.

### 5.3.3 Maximum-entropy distribution

Given discrete probabilities $p_{i}$ ($i = 1,\ldots,n$) constrained by $\sum_{i}^{}p_{i} = 1$, maximise the Shannon entropy $S = - \sum_{i}^{}p_{i}\ln p_{i}$:

$$
L = \sum_{i}^{}\left( - p_{i}\ln p_{i} \right) - \lambda\left( \sum_{i}^{}p_{i} - 1 \right)
$$

$$
\frac{\partial L}{\partial p_{k}} = - lnp_{k} - 1 - \lambda = 0 \Longrightarrow p_{k} = e^{- 1 - \lambda}
$$

The right-hand side does not depend on $k$, so all $p_{k}$ are equal; applying $\sum_{i}^{}p_{i} = 1$ gives

$$
p_{k} = \frac{1}{n},\quad\quad S_{\max} = - \sum_{i = 1}^{n}\frac{1}{n}\ln\frac{1}{n} = lnn
$$

> **Why this result matters later.** “Maximum entropy subject to the known constraints” is the principle that *derives* the standard distributions rather than postulating them: with only normalisation, the uniform; with a fixed mean, the exponential; with a fixed mean and variance, the **Gaussian**. That is a second, deeper reason why the normal distribution is ubiquitous in Module 6 — alongside the central limit theorem, it is the least-committal distribution consistent with knowing a mean and a variance. The same principle underlies maximum-entropy models of protein contacts (direct coupling analysis) and of sequence motifs.

## Collegamenti
- [[AML 05 - Univariate Model Regression · Gradient Descent Algorithm]] — gradient descent

---
> [[MBD 13 - Module 4 – Single-Variable Calculus|← Module 4 – Single-Variable Calculus]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 15 - Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem|Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem →]]
