---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 18
tags: [note, mbd]
---

> [[MBD 17 - Module 4 – Calculus in One Variable · Taylor series|← Module 4 – Calculus in One Variable · Taylor series]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 19 - Module 5 – Calculus in More Variables and Optimisation|Module 5 – Calculus in More Variables and Optimisation →]]

# Integrals

The **definite integral** is the area under the curve between $a$ and $b$:

$$
A = \int_{a}^{b}f(x)\, dx
$$

It is negative where $f$ is below the axis: $A_{2} = \int_{c}^{d}f(x)\, dx < 0$. The integral is a sum ($\int \leftarrow \sum$) of thin rectangles of width $dx$ between $a$ and $b$.

**Riemann sum.** The area under a curve found by adding rectangles is a Riemann sum. The width of a rectangle is a **subinterval**, the entire interval $\lbrack a,b\rbrack$ is the **partition** $P$, and the length of the longest subinterval is the norm $\parallel P \parallel$ (subintervals do not all have to be the same size). As $\parallel P \parallel$ gets smaller the approximation gets better:

$$
\text{Area} = \lim_{\parallel P \parallel \rightarrow 0}\sum_{k = 1}^{n}f\left( c_{k} \right)\Delta x_{k} = \int_{a}^{b}f(x)\, dx
$$

With equal subintervals $\Delta x = \frac{b - a}{n}$ and the limit is $n \rightarrow \infty$. In $\int_{a}^{b}f(x)\, dx$, $a$ and $b$ are the lower and upper limits of integration, $f(x)$ is the integrand and $x$ the variable of integration (a “dummy” variable: the answer does not depend on its name).

$$
\int_{a}^{b}f(x)\, dx = F(b) - F(a),\quad\quad F(x):\text{ general integral},\quad\frac{dF(x)}{dx} = f(x)
$$

$F$ is the **indefinite integral** (primitive) of $f$, defined up to a constant $c$. **Fundamental theorem of calculus:** if $f$ is continuous on $\lbrack a,b\rbrack$, the function $F(x) = \int_{a}^{x}f(t)\, dt$ has a derivative at every point and $\frac{dF}{dx} = \frac{d}{dx}\int_{a}^{x}f(t)\, dt = f(x)$.

*Example from the slides:* area under $y = x^{2}$ from 1 to 2: $F = \frac{x^{3}}{3} + c$ (proof: $\frac{dF}{dx} = 3\frac{x^{2}}{3} + 0 = x^{2}$), $A = F(2) - F(1) = \frac{8}{3} - \frac{1}{3} = \frac{7}{3}$.

*Example.*

$$
\int_{0}^{1}x\, dx = F(1) - F(0),\quad\quad\frac{dF(x)}{dx} = f(x) = x\quad \Rightarrow \quad F(x) = \frac{x^{2}}{2} + C
$$

(check: $\frac{d}{dx}\left( \frac{x^{2}}{2} + C \right) = 2 \cdot \frac{1}{2}x + 0 = x$)

$$
\int_{0}^{1}x\, dx = F(1) - F(0) = \left( \frac{1}{2} + C \right) - (0 + C) = \frac{1}{2}
$$

### 4.8.1 Elementary integrals

$$
\int x^{n}dx = \frac{x^{n + 1}}{n + 1} + C\quad\quad\left( \text{check: }\frac{d}{dx}\left( \frac{x^{n + 1}}{n + 1} \right) = \frac{n + 1}{n + 1}x^{n} \right)
$$

$$
\int sin(x)\, dx = - cos(x) + C,\quad\quad\int cos(x)\, dx = sin(x) + C,\quad\quad\int e^{x}dx = e^{x} + C
$$

*Example.*

$$
\int_{0}^{\pi}cos\, x\, dx = F(\pi) - F(0),\quad F(x) = sin\, x + C\quad \Rightarrow \quad\int_{0}^{\pi}cos\, x\, dx = sin(\pi) - sin(0) = 0 - 0 = 0
$$

The positive area of $cos\, x$ between $0$ and $\pi/2$ cancels the negative area between $\pi/2$ and $\pi$.

To get the **geometric area** between the curve and the axis, the negative parts must be taken with a minus sign. *Slide example:* area between the $x$ axis and $y = cos\, x$ from 0 to $3\pi/2$:

$$
\int_{0}^{\pi/2}cos\, x\, dx - \int_{\pi/2}^{3\pi/2}cos\, x\, dx = \left( sin\frac{\pi}{2} - sin\, 0 \right) - \left( sin\frac{3\pi}{2} - sin\frac{\pi}{2} \right) = 1 - ( - 2) = 3
$$

**Rules for integrals:** $\int_{a}^{b}f\, dx = - \int_{b}^{a}f\, dx$ (reversing the limits changes the sign); $\int_{a}^{a}f\, dx = 0$; $\int_{a}^{b}kf\, dx = k\int_{a}^{b}f\, dx$; $\int_{a}^{b}(f + g)\, dx = \int_{a}^{b}f\, dx + \int_{a}^{b}g\, dx$; $\int_{a}^{b}f\, dx + \int_{b}^{c}f\, dx = \int_{a}^{c}f\, dx$.

---
> [[MBD 17 - Module 4 – Calculus in One Variable · Taylor series|← Module 4 – Calculus in One Variable · Taylor series]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 19 - Module 5 – Calculus in More Variables and Optimisation|Module 5 – Calculus in More Variables and Optimisation →]]
