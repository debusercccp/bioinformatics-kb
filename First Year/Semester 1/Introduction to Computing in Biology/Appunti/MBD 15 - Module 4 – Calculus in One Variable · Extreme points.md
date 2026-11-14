---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 15
tags: [note, mbd]
---

> [[MBD 14 - Module 4 – Calculus in One Variable · Derivatives|← Module 4 – Calculus in One Variable · Derivatives]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 16 - Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent)|Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent) →]]

# Extreme points

**Absolute (global) extrema** are the maximum or minimum values of the function on its whole domain; a **local maximum (minimum)** is the maximum (minimum) value within some open interval. If $f$ has a local max or min at an interior point $c$ and $f'(c)$ exists, then $f'(c) = 0$.

- Function increasing $\rightarrow f' > 0$
- Function decreasing $\rightarrow f' < 0$
- $\left. \ \frac{df}{dx} \right|_{x_{0}} = f'\left( x_{0} \right) = 0$ (horizontal tangent) $\rightarrow$ local minima or maxima, or a **flexus** (horizontal inflection point)

To find the minima and maxima of a function:

- check the points where $\left. \ \frac{df}{dx} \right|_{x_{0}} = 0$ (**critical points**);
- check the borders of the domain.

A **critical point** is a point of the domain where $f' = 0$ **or** $f'$ **does not exist**. Maxima and minima in the interior of a differentiable function always occur at critical points, but critical points are not always maxima or minima: $y = x^{3}$ has $f' = 0$ at 0 (flexus), and $y = x^{1/3}$ has $f'$ undefined at 0, without an extreme.

*Example from the slides (absolute extrema on a closed interval):* $f(x) = x^{2/3}$ on $\lbrack - 2,3\rbrack$. $f'(x) = \frac{2}{3}x^{- 1/3}$ is never 0 but is undefined at $x = 0$, so $(0,0)$ is a critical point; $f( - 1) = f(1) = 1 > 0$, so it is the absolute minimum. At the endpoints $f( - 2) \approx 1.587$ and $f(3) \approx 2.080$: the absolute maximum is $(3,\ 2.08)$.

**Meaning of the second derivative (curve sketching).** $y' > 0$: curve rising; $y' < 0$: falling; $y' = 0$: possible local max or min. $y'' > 0$: curve **concave up**; $y'' < 0$: **concave down**; $y'' = 0$: **possible** inflection point, where the concavity changes. So at a critical point $f'' < 0$ means concave down (maximum) and $f'' > 0$ concave up (minimum).

**Procedure.** $f(x) \rightarrow f'(x)$: find $x_{i}$ with $f'\left( x_{i} \right) = 0$ $\Rightarrow$ critical points. Then $\rightarrow f''(x) = \frac{d}{dx}\left( \frac{df}{dx} \right) = \frac{d^{2}f}{dx^{2}}$, and $\forall x_{i}$ compute $f''\left( x_{i} \right)$:

$$
f''\left( x_{i} \right)\left\{ \begin{matrix}
 > 0 \Rightarrow x_{i}\text{ local min} \\
 = 0 \Rightarrow x_{i}\text{ flexus} \\
 < 0 \Rightarrow x_{i}\text{ local maximum}
\end{matrix} \right.\ 
$$

*Example.* $f(x) = 2x^{4} - x^{2}$:

$$
\frac{df}{dx} = 8x^{3} - 2x = 0\quad \Rightarrow \quad 2x\left( 4x^{2} - 1 \right) = 0\quad \Rightarrow \quad x_{1} = 0,\quad x_{2} = \frac{1}{2},\quad x_{3} = - \frac{1}{2}
$$

$$
\frac{d^{2}f}{dx^{2}} = 24x^{2} - 2:\quad\quad f''(0) = - 2\ \text{(local max)},\quad\quad f''\left( \frac{1}{2} \right) = f''\left( - \frac{1}{2} \right) = 24 \cdot \frac{1}{4} - 2 = 4\ \text{(local min)}
$$

*Note:* $f''\left( x_{i} \right) = 0$ only says that $x_{i}$ is a **possible** flexus: it is one if the concavity actually changes there (the sign of $f''$ changes).

*Example from the slides:* $y = x^{3} - 3x^{2} + 4 = (x + 1)(x - 2)^{2}$, roots at $x = - 1$ and $x = 2$. $y' = 3x^{2} - 6x = 3x(x - 2) = 0$ at $x = 0,2$. First-derivative test: $y'( - 1) = 9 > 0$, $y'(1) = - 3 < 0$, $y'(3) = 9 > 0$ ⇒ maximum at 0, minimum at 2. Second-derivative test: $y'' = 6x - 6$, $y''(0) = - 6 < 0$ ⇒ $(0,4)$ local max; $y''(2) = 6 > 0$ ⇒ $(2,0)$ local min. $y'' = 0$ at $x = 1$ and $y''$ changes sign there ⇒ inflection point at $(1,2)$.

| $x$ | $y$ | $y'$ | $y''$ | behaviour                 |
|:------|:------|:-------|:--------|:--------------------------|
| −1    | 0     | 9      | −12     | rising, concave down      |
| 0     | 4     | 0      | −6      | local max                 |
| 1     | 2     | −3     | 0       | falling, inflection point |
| 2     | 0     | 0      | 6       | local min                 |
| 3     | 4     | 9      | 12      | rising, concave up        |

---
> [[MBD 14 - Module 4 – Calculus in One Variable · Derivatives|← Module 4 – Calculus in One Variable · Derivatives]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 16 - Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent)|Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent) →]]
