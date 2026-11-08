---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 13
tags: [note, mbd]
---

> [[MBD 12 - Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant|← Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 14 - Module 4 – Calculus in One Variable · Derivatives|Module 4 – Calculus in One Variable · Derivatives →]]

# Functions

A function associates to each element of the **domain** ($\subset \mathbb{R}$) one element of the **codomain** ($\subset \mathbb{R}$). 1-D functions: $D \subset \mathbb{R} \rightarrow C \subset \mathbb{R}$; $f(x):\mathbb{R} \rightarrow \mathbb{R}$, $x \rightarrow f(x)$.

A relation is a **function** if for each $x$ there is one and only one $y$ (vertical line test).

A curve that gives two values for the same $x$ (e.g. a “C”-shaped curve) is **not a function**.

**1-to-1 function**: 1 element in the domain $\Leftrightarrow$ 1 element in the codomain $\rightarrow$ the function is **invertible**, $f^{- 1}$. A parabola is not 1-to-1 (two values of $x$ give the same $f(x)$); a monotonic curve such as a cubic is 1-to-1.

Formally, $f$ is one-to-one on $D$ if $f(a) \neq f(b)$ whenever $a \neq b$; to be one-to-one a function must pass the horizontal line test as well as the vertical line test ($y = x^{2}$ is not one-to-one; $x = y^{2}$ is not even a function).

**Inverse function.** Solve $y = f(x)$ for $x$ and switch $x$ and $y$. E.g. $y = \frac{1}{2}x + 1 \Rightarrow 2y - 2 = x \Rightarrow f^{- 1}(x) = 2x - 2$. The graphs of a function and of its inverse are reflections about the line $y = x$.

## 4.2 Continuous functions

A function is continuous when its graph can be drawn without lifting the pen; it can still have corners (e.g. a “$\land$” shape). A function with a jump is not continuous.

Most techniques of calculus require continuous functions. Formally, a function is continuous at a point if the limit there is the same as the value of the function (the one-sided limits match the value). Continuous functions can be added, subtracted, multiplied, divided and multiplied by a constant, and the result remains continuous; composites of continuous functions are continuous (e.g. $y = sin\left( x^{2} \right)$, $y = |cos\, x|$).

## 4.3 Elementary functions

**Exponential**, $f(x) = e^{x}$:

$$
\lim_{x \rightarrow - \infty}f(x) = 0,\quad\quad f(0) = 1,\quad\quad\lim_{x \rightarrow + \infty}f(x) = + \infty
$$

**Trigonometric**, $f(x) = sin\, x$ and $f(x) = cos\, x$: periodic, between $- 1$ and $1$; $sin\, x$ is 0 at $0,\pi,2\pi$ and has its maximum at $\pi/2$; $cos\, x$ is 1 at $0$.

$cos$ is **even**, $cos( - x) = cos(x)$ (symmetric about the $y$ axis); $sin$ is **odd**, $sin( - x) = - sin(x)$ (symmetric about the origin). In $f(x) = A\, sin\left\lbrack \frac{2\pi}{B}(x - C) \right\rbrack + D$, $|A|$ is the amplitude, $|B|$ the period, $C$ the horizontal shift and $D$ the vertical shift. Trigonometric functions are not one-to-one, but they become invertible if the domain is restricted.

**Logarithm**, $ln\, x$: the inverse of the exponential, $ln\left( exp(x) \right) = x$. It is defined only for $x > 0$ and $ln\, 1 = 0$.

$$
\log_{a}x = y\quad \Leftrightarrow \quad a^{y} = x
$$

$a^{x}$ is one-to-one, so it has an inverse: the **logarithm** ($a > 0$, $a \neq 1$, $x > 0$). Example: $16 = 2^{4} \Leftrightarrow 4 = \log_{2}16$ (“two raised to what power is 16?”). The most common bases are 10, $\log_{10}x = \log x$ (common log), and $e$, $\log_{e}x = ln\, x$ (natural log). Since logs and exponentiation are inverse functions, they “undo” each other.

$$
\log_{a}(x \cdot y) = \log_{a}x + \log_{a}y,\quad\quad\log_{a}\frac{x}{y} = \log_{a}x - \log_{a}y,\quad\quad\log_{a}x^{y} = y\log_{a}x
$$

(product, quotient and power rules), and the change of base formula $\log_{a}x = \frac{ln\, x}{ln\, a}$.

---
> [[MBD 12 - Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant|← Module 3 · Complex numbers + Eigenvalues of a 2 × 2 matrix – trace and determinant]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 14 - Module 4 – Calculus in One Variable · Derivatives|Module 4 – Calculus in One Variable · Derivatives →]]
