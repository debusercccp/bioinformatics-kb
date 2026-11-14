---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 19
tags: [note, mbd]
---

> [[MBD 18 - Module 4 – Calculus in One Variable · Integrals|← Module 4 – Calculus in One Variable · Integrals]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 20 - Module 6 – Probability|Module 6 – Probability →]]

# Module 5 — Calculus in More Variables and Optimisation

## 5.1 Functions of more variables, partial derivatives, gradient

$f\left( x_{1},x_{2} \right):\mathbb{R}^{2}\mathbb{\rightarrow R}$; in general

$$
f:\mathbb{R}^{n}\mathbb{\rightarrow R,}\quad\quad\begin{pmatrix}
x_{1} \\
 \vdots \\
x_{n}
\end{pmatrix} \rightarrow y = f\left( \overrightarrow{x} \right)
$$

A function of two variables $z = f(x,y)$ is a surface; its **level curves** are drawn by holding $z$ constant (like the contour lines of a topographic map).

**Partial derivatives** are derivatives of a function of several variables in which all the variables except the one of interest are held fixed:

$$
f_{x}(x,y) = \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x,y) - f(x,y)}{\Delta x},\quad\quad f_{y}(x,y) = \lim_{\Delta y \rightarrow 0}\frac{f(x,y + \Delta y) - f(x,y)}{\Delta y}
$$

To find them, hold one variable constant and differentiate with respect to the other. *Example:* $f(x,y) = 5x^{4} - x^{2}y^{2} + 2x^{3}y$: $f_{x} = 20x^{3} - 2xy^{2} + 6x^{2}y$, $f_{y} = - 2x^{2}y + 2x^{3}$. Notation: $\frac{\partial f}{\partial x} = f_{x} = z_{x}$. Geometrically, $f_{x}\left( x_{0},y_{0} \right)$ is the slope of the curve obtained by cutting the surface with the plane $y = y_{0}$. With $n$ variables there are $n$ partial derivatives, each computed holding the other $n - 1$ variables constant.

$\frac{\partial f}{\partial x_{i}}$ is the **partial derivative** of $f$ with respect to $x_{i}$ (e.g. $\frac{\partial f}{\partial x_{1}}$, $\frac{\partial f}{\partial x_{2}}$). Collected in a vector they form the **gradient**:

$$
\overrightarrow{\nabla}f = \begin{pmatrix}
\frac{\partial f}{\partial x_{1}} \\
 \vdots \\
\frac{\partial f}{\partial x_{n}}
\end{pmatrix},\quad\quad\overrightarrow{\nabla}f = \overrightarrow{0} \rightarrow \text{critical points}
$$

The gradient is the vector of all the first-order partial derivatives. It is **locally perpendicular to the level curves**: for two nearby points $(x,y)$ and $\left( x + \varepsilon_{x},y + \varepsilon_{y} \right)$ of the level curve $f(x,y) = c$, $f\left( x + \varepsilon_{x},y + \varepsilon_{y} \right) \approx f(x,y) + {\overrightarrow{\varepsilon}}^{T}\overrightarrow{\nabla}f$, and since both equal $c$, ${\overrightarrow{\varepsilon}}^{T}\overrightarrow{\nabla}f = 0$: the gradient is perpendicular to $\overrightarrow{\varepsilon}$, which is parallel to the curve. The gradient points in the direction of **maximum increase** of $f$.

## 5.2 Hessian and nature of the critical points

$$
H = \begin{pmatrix}
\frac{\partial^{2}f}{\partial x_{1}^{2}} & \frac{\partial^{2}f}{\partial x_{2}\partial x_{1}} & \cdots & \frac{\partial^{2}f}{\partial x_{n}\partial x_{1}} \\
\frac{\partial^{2}f}{\partial x_{1}\partial x_{2}} & \frac{\partial^{2}f}{\partial x_{2}^{2}} & \cdots & \frac{\partial^{2}f}{\partial x_{n}\partial x_{2}} \\
 \vdots & & & \vdots \\
\frac{\partial^{2}f}{\partial x_{1}\partial x_{n}} & \frac{\partial^{2}f}{\partial x_{2}\partial x_{n}} & \cdots & \frac{\partial^{2}f}{\partial x_{n}^{2}}
\end{pmatrix}
$$

The Hessian is the square matrix of order $n$ of all the second-order partial derivatives. Notation: $f_{xx} = \frac{\partial^{2}f}{\partial x^{2}}$, $f_{yy}$, and the mixed $f_{xy} = \frac{\partial}{\partial y}\left( \frac{\partial f}{\partial x} \right)$, $f_{yx}$. **Theorem:** if $f_{xy}$ and $f_{yx}$ are continuous, $f_{xy} = f_{yx}$, so $H$ is **symmetric** and has $n$ real eigenvalues. *Example:* $f = 3xy^{2} - 2y + 5x^{2}y$: $f_{x} = 3y^{2} + 10xy$, $f_{y} = 6xy - 2 + 5x^{2}$, $f_{xx} = 10y$, $f_{yy} = 6x$, $f_{xy} = f_{yx} = 6y + 10x$.

At a critical point, compute the eigenvalues of $H$, $\det(H - \lambda I) = 0$:

- all $\lambda > 0$ $\Rightarrow$ min
- some $\lambda > 0$, some $\lambda < 0$ $\Rightarrow$ **saddle**
- all $\lambda < 0$ $\Rightarrow$ max

*Note:* the slide (Local optima without constraints) swaps the two cases (“maximum if all eigenvalues are positive”); the whiteboard is correct: all positive ⇒ minimum, all negative ⇒ maximum, as the examples below show.

*Example 1.* $f(x,y) = x^{2} - 4y^{2}$: $\overrightarrow{\nabla}f = (2x, - 8y)$, critical point $(0,0)$, $H = \begin{pmatrix}
2 & 0 \\
0 & - 8
\end{pmatrix}$ for every point: eigenvalues of different sign ⇒ **saddle point**.

*Example 2.* $f(x,y) = (x + y)\, exp\left( - x^{2} - y^{2} \right)$: $\overrightarrow{\nabla}f = \exp\left( - x^{2} - y^{2} \right)\left( 1 - 2x^{2} - 2xy,\ 1 - 2y^{2} - 2xy \right) = \overrightarrow{0}$ gives $x = \pm y$; $x = y$ ⇒ $1 - 4x^{2} = 0$ ⇒ critical points $(1/2,1/2)$ and $( - 1/2, - 1/2)$ ($x = - y$ gives no solution).

$$
H(1/2,1/2) = e^{- 1/2}\begin{pmatrix}
 - 3 & - 1 \\
 - 1 & - 3
\end{pmatrix}\ (\lambda \propto - 2, - 4) \Rightarrow \text{MAXIMUM};\quad H( - 1/2, - 1/2) = e^{- 1/2}\begin{pmatrix}
3 & 1 \\
1 & 3
\end{pmatrix}\ (\lambda \propto 2,4) \Rightarrow \text{MINIMUM}
$$

## 5.3 Gradient descent in more dimensions

On a contour plot of $f\left( x_{1},x_{2} \right)$ with several minima, gradient descent moves from ${\overrightarrow{x}}_{0}$ to ${\overrightarrow{x}}_{1}$, ${\overrightarrow{x}}_{2}$, … always against the gradient, and ends in the nearest local minimum.

Steepest descent finds the **local** minimum of a function by always moving in the direction that leads downhill, $- \overrightarrow{\nabla}f$: $\overrightarrow{x}(t + 1) = \overrightarrow{x}(t) - \eta\overrightarrow{\nabla}f\left( \overrightarrow{x}(t) \right)$.

## 5.4 Constrained optimisation: Lagrange multipliers

We want to maximise (or minimise) $z = f(x,y)$ subject to a constraint $g(x,y) = c$, a curve in the $(x,y)$ plane. A simple solution would be to solve the constraint, e.g. $y = h(x)$, substitute it and maximise $f\left( x,h(x) \right)$ in $x$; but solving the constraint analytically can be very difficult.

**Idea.** Walk along the constraint line $g(x,y) = c$: in general it crosses different contour lines of $f$, so $f$ increases or decreases. Only where the constraint touches a contour line of $f$ **tangentially** does $f$ stop changing: there $f$ is at its local max or min along the constraint. At that point the gradient of $f$ is perpendicular to the curve $g = c$ (otherwise we could increase or decrease $f$ by moving along the curve), and so is the gradient of $g$: the two gradients are parallel.

Find the MAX or MIN of $f\left( \overrightarrow{x} \right)$ on the curve $g\left( \overrightarrow{x} \right) = 0$. At the solution the constraint curve is tangent to a contour line of $f$, so the two gradients are parallel:

$$
\boxed{\overrightarrow{\nabla}f = \lambda\overrightarrow{\nabla}g}\quad\quad\lambda:\text{ Lagrange multiplier}
$$

$$
\mathcal{L}\left( \overrightarrow{x},\lambda \right) = f\left( \overrightarrow{x} \right) - \lambda g\left( \overrightarrow{x} \right),\quad\quad\left\{ \begin{matrix}
\frac{\partial\mathcal{L}}{\partial x_{i}} = 0\quad\forall i \Rightarrow \overrightarrow{\nabla}f = \lambda\overrightarrow{\nabla}g \\
\frac{\partial\mathcal{L}}{\partial\lambda} = 0 \Rightarrow g\left( \overrightarrow{x} \right) = 0
\end{matrix} \right.\ 
$$

The auxiliary function $\mathcal{L}$ (the **Lagrangian**, for a constraint $g = c$: $\mathcal{L =}f - \lambda(g - c)$) puts both conditions into one equation, ${\overrightarrow{\nabla}}_{x,\lambda}\mathcal{L =}\overrightarrow{0}$. With several constraints $g_{i}\left( \overrightarrow{x} \right) = 0$, $i = 1,\ldots,m$, there is one Lagrange multiplier $\lambda_{i}$ for each constraint.

*Example from the slides:* the box (rectangular parallelepiped) with the largest volume and total surface $64\ cm^{2}$. Maximise $f = xyz$ with $2xy + 2xz + 2yz = 64$: $\mathcal{L =}xyz - \lambda(xy + xz + yz - 32)$,

$$
\left\{ \begin{matrix}
yz - \lambda(y + z) = 0 \\
xz - \lambda(x + z) = 0 \\
xy - \lambda(x + y) = 0 \\
xy + xz + yz - 32 = 0
\end{matrix} \right.\ \quad \Rightarrow \quad\lambda z(y - x) = 0,\ \lambda y(z - x) = 0,\ \lambda x(z - y) = 0\quad \Rightarrow \quad x = y = z,\ 3x^{2} = 32,\ x = y = z = 4\sqrt{\frac{2}{3}}
$$

(the cube).

### 5.4.1 Example: rectangle with maximum area

Perimeter $P = 100$ cm: find the rectangle (sides $a$, $b$) with max area.

$$
2a + 2b = 100,\quad\quad A = a \cdot b \rightarrow \text{MAX},\quad\quad f(a,b) = a \cdot b,\quad\quad g:\ 2a + 2b - 100 = 0
$$

$$
\mathcal{L}(a,b,\lambda) = a \cdot b - \lambda(2a + 2b - 100)
$$

$$
\left\{ \begin{matrix}
\frac{\partial\mathcal{L}}{\partial a} = b - 2\lambda = 0 \\
\frac{\partial\mathcal{L}}{\partial b} = a - 2\lambda = 0 \\
\frac{\partial\mathcal{L}}{\partial\lambda} = 2a + 2b - 100 = 0
\end{matrix} \right.\ \quad \Rightarrow \quad a = b,\quad 4a = 100,\quad a = b = 25
$$

### 5.4.2 Example: growth of a bacterium

A bacterium divides its protein resources between ribosomes ($c_{1}$) and metabolic enzymes ($c_{2}$); the growth rate has the Cobb–Douglas form below (concave, no free maximum) and the total protein budget is fixed.

The growth rate depends on two resources, $\mu\left( c_{1},c_{2} \right) = r\, c_{1}^{a}c_{2}^{1 - a} \rightarrow \text{MAX}\ \mu$, with the constraint $c_{1} + c_{2} = C$.

$$
\mathcal{L}\left( c_{1},c_{2},\lambda \right) = r\, c_{1}^{a}c_{2}^{1 - a} - \lambda\left( c_{1} + c_{2} - C \right)
$$

$$
\left\{ \begin{matrix}
\frac{\partial\mathcal{L}}{\partial c_{1}} = r\, a\, c_{1}^{a - 1}c_{2}^{1 - a} - \lambda = 0 \\
\frac{\partial\mathcal{L}}{\partial c_{2}} = r\, c_{1}^{a}(1 - a)c_{2}^{- a} - \lambda = 0 \\
\frac{\partial\mathcal{L}}{\partial\lambda} = c_{1} + c_{2} - C = 0
\end{matrix} \right.\ 
$$

From the first two equations, $\lambda = r\, a\, c_{1}^{a - 1}c_{2}^{1 - a} = r\, c_{1}^{a}(1 - a)c_{2}^{- a}$; dividing by $r\, c_{1}^{a - 1}c_{2}^{- a}$:

$$
\left\{ \begin{matrix}
a\, c_{2} = c_{1} - a\, c_{1} \\
c_{1} + c_{2} = C
\end{matrix} \right.\ \quad \Rightarrow \quad a\left( c_{1} + c_{2} \right) = c_{1}\quad \Rightarrow \quad c_{1} = aC,\quad c_{2} = (1 - a)C
$$

In *E. coli* $a \approx 0.6$ (measured from proteomics data). The multiplier $\lambda$ has a biological meaning: it is the “shadow price” of the resource, i.e. how much growth is gained per unit of extra budget.

### 5.4.3 Example: closest and farthest point of a circle from the origin

Circle $(x - 1)^{2} + (y - 2)^{2} = 4$; distance from the origin $d(x,y) = \sqrt{x^{2} + y^{2}}$. Maximising/minimising $d$ is the same as maximising/minimising $f(x,y) = x^{2} + y^{2}$.

$$
\mathcal{L}(x,y,\lambda) = x^{2} + y^{2} - \lambda\left\lbrack (x - 1)^{2} + (y - 2)^{2} - 4 \right\rbrack
$$

$$
\left\{ \begin{matrix}
\frac{\partial\mathcal{L}}{\partial x} = 2x - 2\lambda(x - 1) = 0 \\
\frac{\partial\mathcal{L}}{\partial y} = 2y - 2\lambda(y - 2) = 0 \\
\frac{\partial\mathcal{L}}{\partial\lambda} = (x - 1)^{2} + (y - 2)^{2} - 4 = 0
\end{matrix} \right.\ \quad \Rightarrow \quad\left\{ \begin{matrix}
2x(1 - \lambda) = - 2\lambda \\
2y(1 - \lambda) = - 4\lambda
\end{matrix} \right.\ \quad \Rightarrow \quad\left\{ \begin{matrix}
x = - \frac{\lambda}{1 - \lambda} \\
y = - \frac{2\lambda}{1 - \lambda}
\end{matrix} \right.\ \quad \Rightarrow \quad y = 2x
$$

$$
(x - 1)^{2} + (2x - 2)^{2} = 4\quad \Rightarrow \quad(x - 1)^{2} + 4(x - 1)^{2} = 4\quad \Rightarrow \quad(x - 1)^{2} = \frac{4}{5}\quad \Rightarrow \quad x - 1 = \pm \sqrt{\frac{4}{5}} = \pm \frac{2}{\sqrt{5}}
$$

$$
x = 1 \pm \frac{2}{\sqrt{5}},\quad\quad y = 2 \pm \frac{4}{\sqrt{5}}
$$

The two candidate points are $\left( 1 + \frac{2}{\sqrt{5}},\ 2 + \frac{4}{\sqrt{5}} \right)$ and $\left( 1 - \frac{2}{\sqrt{5}},\ 2 - \frac{4}{\sqrt{5}} \right)$; evaluating $x^{2} + y^{2}$ at each of them tells which is the farthest (max) and which the closest (min) point.

## Collegamenti
- [[AML 05 - Univariate Model Regression · Gradient Descent Algorithm]] — gradient descent

---
> [[MBD 18 - Module 4 – Calculus in One Variable · Integrals|← Module 4 – Calculus in One Variable · Integrals]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 20 - Module 6 – Probability|Module 6 – Probability →]]
