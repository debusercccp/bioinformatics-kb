---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 14
tags: [note, mbd]
---

> [[MBD 13 - Module 4 – Calculus in One Variable · Functions … Elementary functions|← Module 4 – Calculus in One Variable · Functions … Elementary functions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 15 - Module 4 – Calculus in One Variable · Extreme points|Module 4 – Calculus in One Variable · Extreme points →]]

# Derivatives

The tangent to $f$ at $x_{0}$ is the line

$$
f(x) - f\left( x_{0} \right) = m\left( x - x_{0} \right)
$$

whose slope $m$ is the **derivative**. Between two points $x$ and $x + \Delta x$ the secant has slope

$$
f(x + \Delta x) - f(x) = m'(x + \Delta x - x)\quad \Rightarrow \quad m' = \frac{f(x + \Delta x) - f(x)}{\Delta x}
$$

*Example from the slides:* the slope of $f(x) = x^{2}$ at $(1,1)$ can be approximated by secants through $(4,16)$, $(3,9)$, $(2,4)$, $(1.1,1.21)$: $\frac{15}{3} = 5$, $\frac{8}{2} = 4$, $\frac{3}{1} = 3$, $\frac{0.21}{0.1} = 2.1$. In the limit, $m = \lim_{h \rightarrow 0}\frac{(1 + h)^{2} - 1}{h} = \lim_{h \rightarrow 0}(2 + h) = 2$.

and for $\Delta x \rightarrow 0$ the secant becomes the tangent:

$$
\dot{f} = f' = \left. \ \frac{df}{dx} \right|_{x} = \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x) - f(x)}{\Delta x}
$$

The slope of a curve at a point is the slope of its tangent line there, and the derivative is the slope of the original function. Notations: $f'(x)$ (“f prime x”), $y'$, $\frac{dy}{dx}$, $\frac{df}{dx}$, $\frac{d}{dx}f(x)$. *Example:* $y = x^{2} - 3$, $y' = \lim_{h \rightarrow 0}\frac{(x + h)^{2} - 3 - \left( x^{2} - 3 \right)}{h} = \lim_{h \rightarrow 0}(2x + h) = 2x$.

A function can be **continuous but not derivable** at $x_{0}$: at a corner or cusp the tangent is not defined.

A function is **differentiable** if it has a derivative everywhere in its domain: it must be continuous **and** smooth. Derivatives fail to exist at a corner ($f(x) = |x|$), a cusp ($f(x) = x^{2/3}$), a vertical tangent ($f(x) = \sqrt[3]{x}$) and a discontinuity.

### 4.4.1 Derivatives of elementary functions

$$
f(x) = ax \rightarrow \frac{df}{dx} = a,\quad\quad f(x) = ax^{n} \rightarrow \frac{df}{dx} = n\, ax^{n - 1},\quad\quad\frac{d}{dx}\left( 3x^{3} \right) = 9x^{2}
$$

The derivative of a constant is zero, $\frac{d}{dx}c = 0$ (a constant function has slope 0). The **power rule** $\frac{d}{dx}x^{n} = nx^{n - 1}$ follows the pattern of Pascal’s triangle in the expansion of $(x + h)^{n}$ ($2x$, $3x^{2}$, $4x^{3}$, …), e.g. $\frac{d}{dx}x^{8} = 8x^{7}$. **Constant multiple rule:** $\frac{d}{dx}(cu) = c\frac{du}{dx}$, e.g. $\frac{d}{dx}7x^{5} = 35x^{4}$: the limit has no effect on a constant coefficient.

*Proof for* $f(x) = ax$:

$$
\lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x) - f(x)}{\Delta x} = \lim_{\Delta x \rightarrow 0}\frac{a(x + \Delta x) - ax}{\Delta x} = \frac{a\Delta x}{\Delta x} = a
$$

$$
\frac{d}{dx}e^{x} = e^{x},\quad\quad\frac{d}{dx}ln\, x = \frac{d}{dx}\log_{e}x = \frac{1}{x},\quad\quad\frac{d}{dx}sin\, x = cos\, x,\quad\quad\frac{d}{dx}cos\, x = - sin\, x
$$

More generally $\frac{d}{dx}a^{x} = a^{x}ln\, a$ and $\frac{d}{dx}\log_{a}x = \frac{1}{x\, ln\, a}$.

### 4.4.2 Rules

**Sum.** $g(x) = f_{1}(x) \pm f_{2}(x)$:

$$
\frac{dg}{dx} = \frac{df_{1}}{dx} \pm \frac{df_{2}}{dx};\quad\quad g(x) = 3x^{4} + 2x \rightarrow \frac{dg}{dx} = 12x^{3} + 2
$$

Each term is treated separately.

**Product.** $g(x) = f_{1}(x) \cdot f_{2}(x)$:

$$
\frac{dg}{dx} = f_{1}(x)\frac{df_{2}}{dx} + \frac{df_{1}}{dx}f_{2}(x);\quad\quad g(x) = sin\, x \cdot cos\, x \rightarrow \frac{dg}{dx} = sin\, x( - sin\, x) + cos\, x \cdot cos\, x
$$

Notice that it is **not** just the product of the two derivatives. Slide example: $\frac{d}{dx}\left\lbrack \left( x^{2} + 3 \right)\left( 2x^{3} + 5x \right) \right\rbrack = \left( x^{2} + 3 \right)\left( 6x^{2} + 5 \right) + \left( 2x^{3} + 5x \right)(2x) = 10x^{4} + 33x^{2} + 15$.

**Quotient.** $g(x) = \frac{n(x)}{d(x)}$, $d(x) \neq 0$:

$$
\frac{dg}{dx} = \frac{d(x) \cdot \frac{dn}{dx} - n(x) \cdot \frac{d(d)}{dx}}{\left\lbrack d(x) \right\rbrack^{2}}
$$

A quotient can always be written as a product, $\frac{n(x)}{d(x)} = n(x)\left( d(x) \right)^{- 1}$.

**Chain rule.** $g(x) = f_{2}\left( f_{1}(x) \right) = z$, i.e. $x\overset{f_{1}}{\rightarrow}y\overset{f_{2}}{\rightarrow}z$:

$$
\frac{dg}{dx} = \frac{df_{2}}{dy} \cdot \frac{df_{1}}{dx} = \frac{df_{2}}{dy} \cdot \frac{dy}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx}
$$

In words: differentiate the outside function (at the inside one), then multiply by the derivative of the inside function. E.g. $y = sin\left( x^{2} - 4 \right) \Rightarrow y' = cos\left( x^{2} - 4 \right) \cdot 2x$. The rule can be used more than once (that is what makes the “chain”): $\frac{d}{dx}cos^{2}(3x) = 2cos(3x) \cdot \left( - sin(3x) \right) \cdot 3 = - 6\, cos(3x)\, sin(3x)$.

### 4.4.3 Worked examples

*1.* $g(x) = cos\, 3x$: $x \rightarrow y = 3x \rightarrow z = cos\, y$

$$
\frac{dg}{dx} = \frac{d(cos\, y)}{dy} \cdot \frac{d(3x)}{dx} = - sin(3x) \cdot 3
$$

*2. Sigmoid function,* $f(x) = \frac{1}{1 + e^{- x}}$, with the quotient rule ($n(x) = 1$, $d(x) = 1 + e^{- x}$):

$$
\frac{df}{dx} = \frac{\left( 1 + e^{- x} \right) \cdot 0 - 1 \cdot \frac{d}{dx}\left( 1 + e^{- x} \right)}{\left( 1 + e^{- x} \right)^{2}} = \frac{- 1 \cdot \frac{d}{dx}\left( e^{- x} \right)}{\left( 1 + e^{- x} \right)^{2}} = \frac{e^{- x}}{\left( 1 + e^{- x} \right)^{2}}
$$

where, by the chain rule with $x \rightarrow y = - x \rightarrow z = e^{y}$:

$$
\frac{d}{dx}\left( e^{- x} \right) = \frac{de^{y}}{dy} \cdot \frac{d( - x)}{dx} = e^{y}( - 1) = - e^{- x}
$$

The result can be written in terms of $f$ itself: $\frac{e^{- x}}{\left( 1 + e^{- x} \right)^{2}} = \frac{1}{1 + e^{- x}} \cdot \frac{1 + e^{- x} - 1}{1 + e^{- x}} = f(x)\left( 1 - f(x) \right)$ (used in §4.6.1).

*3.* $f(x) = cos\left\lbrack ln\left( 3x^{3} + 2x \right) \right\rbrack$, with $3x^{3} + 2x > 0$: $x \rightarrow y = 3x^{3} + 2x \rightarrow z = ln\, y \rightarrow s = cos\, z$

$$
\frac{df}{dx} = \frac{d(cos\, z)}{dz} \cdot \frac{d(ln\, y)}{dy} \cdot \frac{d\left( 3x^{3} + 2x \right)}{dx} = - sin(z) \cdot \frac{1}{y} \cdot \left( 9x^{2} + 2 \right) = - sin\left( ln\left( 3x^{3} + 2x \right) \right) \cdot \frac{1}{3x^{3} + 2x} \cdot \left( 9x^{2} + 2 \right)
$$

*4.* $f(x) = exp\left( exp( - x) \right) = e^{e^{- x}}$: $x \rightarrow y = - x \rightarrow z = exp(y) \rightarrow s = exp\, z$

$$
\frac{df}{dx} = \frac{d\left( e^{z} \right)}{dz} \cdot \frac{d\left( e^{y} \right)}{dy} \cdot \frac{d( - x)}{dx} = e^{z} \cdot e^{y}( - 1) = - 1 \cdot e^{e^{- x}}e^{- x}
$$

### 4.4.4 Higher derivatives

$$
f(x) \rightarrow \left. \ \frac{df}{dx} \right|_{x_{0}} = f'(x) \rightarrow \frac{df'}{dx} = \frac{d^{2}f}{dx^{2}}
$$

*Kinematics:* position $s(t) \rightarrow \frac{ds(t)}{dt} = v(t)$ (velocity) $\rightarrow \frac{dv(t)}{dt} = a(t)$ (acceleration).

Notation: $y'$ first derivative, $y'' = \frac{d}{dx}\frac{dy}{dx} = \frac{d^{2}y}{dx^{2}}$ second derivative (“y double prime”), $y^{'''}$ third, $y^{(4)}$ fourth.

---
> [[MBD 13 - Module 4 – Calculus in One Variable · Functions … Elementary functions|← Module 4 – Calculus in One Variable · Functions … Elementary functions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 15 - Module 4 – Calculus in One Variable · Extreme points|Module 4 – Calculus in One Variable · Extreme points →]]
