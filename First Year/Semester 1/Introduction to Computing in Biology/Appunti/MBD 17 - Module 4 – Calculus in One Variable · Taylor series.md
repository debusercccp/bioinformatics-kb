---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 17
tags: [note, mbd]
---

> [[MBD 16 - Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent)|← Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent)]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 18 - Module 4 – Calculus in One Variable · Integrals|Module 4 – Calculus in One Variable · Integrals →]]

# Taylor series

The idea: if $P(0) = f(0)$ and the first, second, third, … derivatives of $P$ and $f$ are the same at 0, $P$ is a good approximation of $f$ near 0.

Approximate $f(x)$ with a polynomial $P(x)$ around a point $x_{0}$. Consider $x_{0} = 0$:

$$
P(x) = f(0) + \left. \ \frac{df}{dx} \right|_{0}x + \frac{1}{2}\left. \ \frac{d^{2}f}{dx^{2}} \right|_{0}x^{2} + \frac{1}{6}\left. \ \frac{d^{3}f}{dx^{3}} \right|_{0}x^{3} + \ldots + \frac{1}{n!}\left. \ \frac{d^{n}f}{dx^{n}} \right|_{0}x^{n} + \ldots,\quad\quad n! = 1 \cdot 2 \cdot 3 \cdot 4\cdots n
$$

*Where the coefficients come from.* Write $P(x) = a_{0} + a_{1}x + a_{2}x^{2} + a_{3}x^{3} + \ldots + a_{n}x^{n} + \ldots$ and require that $P$ and its derivatives match $f$ and its derivatives at 0:

$$
P(0) = a_{0}\quad \Rightarrow \quad a_{0} = f(0)
$$

$$
\frac{dP}{dx} = a_{1} + 2a_{2}x + 3a_{3}x^{2} + 4a_{4}x^{3} + \ldots,\quad\left. \ \frac{dP}{dx} \right|_{0} = a_{1}\quad \Rightarrow \quad a_{1} = \left. \ \frac{df}{dx} \right|_{0}
$$

$$
\frac{d^{2}P}{dx^{2}} = 2a_{2} + 6a_{3}x + 4 \cdot 3a_{4}x^{2} + \ldots,\quad\left. \ \frac{d^{2}P}{dx^{2}} \right|_{0} = 2a_{2}\quad \Rightarrow \quad a_{2} = \frac{1}{2}\left. \ \frac{d^{2}f}{dx^{2}} \right|_{0}
$$

$$
f(x) \simeq f(0) + x\left. \ \frac{df}{dx} \right|_{0} + x^{2}\frac{1}{2}\left. \ \frac{d^{2}f}{dx^{2}} \right|_{0} + \ldots + x^{n}\frac{1}{n!}\left. \ \frac{d^{n}f}{dx^{n}} \right|_{0}\quad\text{(around 0)}
$$

*Example from the slides:* $f(x) = \ln(x + 1)$ at $x = 0$ with a fourth-degree polynomial. $f(0) = 0$, $f'(x) = \frac{1}{1 + x}$, $f'(0) = 1$; $f''(x) = - \frac{1}{(1 + x)^{2}}$, $f''(0) = - 1$; $f^{(3)}(0) = 2$; $f^{(4)}(0) = - 6$. Hence $a_{0} = 0$, $a_{1} = 1$, $a_{2} = - \frac{1}{2}$, $a_{3} = \frac{2}{6} = \frac{1}{3}$, $a_{4} = - \frac{6}{24} = - \frac{1}{4}$:

$$
P(x) = x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4}
$$

and near zero the two functions match very well. The series around 0 is the **Maclaurin series**; centred at another point it is the **Taylor series**.

Around a point $x_{0}$:

$$
f(x) \simeq f\left( x_{0} \right) + \left. \ \frac{df}{dx} \right|_{x_{0}}\left( x - x_{0} \right) + \frac{1}{2}\left. \ \frac{d^{2}f}{dx^{2}} \right|_{x_{0}}\left( x - x_{0} \right)^{2} + \ldots + \frac{1}{n!}\left. \ \frac{d^{n}f}{dx^{n}} \right|_{x_{0}}\left( x - x_{0} \right)^{n} + \ldots
$$

---
> [[MBD 16 - Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent)|← Module 4 – Calculus in One Variable · Numerical approximation of minima (gradient descent)]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 18 - Module 4 – Calculus in One Variable · Integrals|Module 4 – Calculus in One Variable · Integrals →]]
