---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 13
tags: [note, mbd]
---

> [[MBD 12 - Module 3 · Complex numbers … What is missing – the singular value decomposition|← Module 3 · Complex numbers … What is missing – the singular value decomposition]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 14 - Module 5 – Multivariable Calculus and Optimisation|Module 5 – Multivariable Calculus and Optimisation →]]

# Module 4 — Single-Variable Calculus

## 4.1 Functions, logarithms, biological models

A relation $y = f(x)$ is a **function** if every $x$ maps to a unique $y$ (vertical line test). It is **one-to-one (injective)** if $f(a) \neq f(b)$ whenever $a \neq b$ (horizontal line test), which guarantees an **inverse function** $f^{- 1}(x)$, graphically a reflection across $y = x$.

### 4.1.1 Fundamental biological functions

| Model | Formula | What the parameters mean |
|----|----|----|
| Michaelis–Menten | $v\left( \lbrack A\rbrack \right) = \frac{v_{\max}\lbrack A\rbrack}{K_{M} + \lbrack A\rbrack}$ | $v_{\max}$ saturation rate; $K_{M}$ the $\lbrack A\rbrack$ at half-maximal velocity |
| Hill (cooperative) | $v\left( \lbrack A\rbrack \right) = \frac{v_{\max}\lbrack A\rbrack^{n}}{K_{M} + \lbrack A\rbrack^{n}}$ | $n$ the Hill coefficient: $n > 1$ positive cooperativity, sigmoid response |
| Gompertz (tumour growth) | $N(t) = Ke^{- ce^{- rt}}$ | $K$ plateau; growth rate decays exponentially |
| Logistic (population) | $N(t) = \frac{K}{1 + cKe^{- rt}}$ | $K$ carrying capacity; $r$ intrinsic growth rate |
| Sigmoid (activation) | $f(x) = \frac{1}{1 + e^{- x}}$ | $\frac{df}{dx} = f(x)\left( 1 - f(x) \right)$ |

> **Why the sigmoid derivative identity matters.** $f' = f(1 - f)$ means the gradient can be computed from the *output alone*, without re-evaluating the exponential. This is why the logistic function became the standard neural-network activation, and it is used directly in §4.3.
>
> **The shared shape worth noticing.** Michaelis–Menten, Hill with $n = 1$, and the logistic function are the same hyperbola/sigmoid family. Saturation — a finite resource, a finite number of binding sites, a finite carrying capacity — produces this shape everywhere in biology. Recognising it tells you which model to reach for.

### 4.1.2 Logarithms

$y = \log_{a}x \Leftrightarrow a^{y} = x$.

| Identity |  |
|----|----|
| $a^{\log_{a}x} = x$ | $\log_{a}\left( a^{x} \right) = x$ |
| $\log_{a}(xy) = \log_{a}x + \log_{a}y$ | $\log_{a}(x/y) = \log_{a}x - \log_{a}y$ |
| $\log_{a}\left( x^{y} \right) = y\log_{a}x$ | change of base: $\log_{a}x = \frac{\ln x}{\ln a}$ |

**Quantitative biology applications.**

- **PCR amplification.** $N(n) = N_{0} \cdot 2^{n} \Rightarrow C_{t} = \log_{2}\left( \text{threshold}/N_{0} \right)$. A difference of 1 $C_{t}$ is a **two-fold** difference in starting DNA.
- **pH scale.** $pH = - \log_{10}\left\lbrack H^{+} \right\rbrack$. A one-unit shift is a ten-fold change in $\left\lbrack H^{+} \right\rbrack$, strongly affecting enzyme conformation (pepsin optimal at pH 1.5, carbonic anhydrase at pH 7.0).
- **Lineweaver–Burk linearisation.** Taking reciprocals of Michaelis–Menten: $\frac{1}{v} = \frac{K_{M}}{V_{\max}}\frac{1}{\lbrack S\rbrack} + \frac{1}{V_{\max}}$, a straight line in $1/\lbrack S\rbrack$.
- **Radioactive decay.** $N(t) = N_{0}e^{- \lambda t} \Rightarrow t_{1/2} = \frac{\ln 2}{\lambda}$ — $^{14}$C dating, isotope clearance.

> **The general principle behind all four.** Logarithms turn multiplication into addition and exponentials into straight lines. Any process that is multiplicative — doubling, decay, fold-change, concentration over orders of magnitude — becomes additive and linear on a log scale. This is also why RNA-seq counts are log-transformed before PCA: it makes the variance roughly comparable across genes and turns fold-changes into differences, which are what a linear method can see.
>
> *Caveat the slides omit:* $\log(0)$ is undefined, which is why pipelines use $\log\left( \text{count} + 1 \right)$.

### 4.1.3 Graph transformations and trigonometry

For $y = af\left( b(x + c) \right) + d$: $a$ scales vertically ($|a| > 1$ stretch, $|a| < 1$ shrink, $a < 0$ flips across the $x$-axis); $b$ scales horizontally ($b > 1$ shrink, $b < 1$ stretch); $+ c$ shifts left; $+ d$ shifts up.

For $f(x) = A\sin\left( \frac{2\pi}{B}(x - C) \right) + D$: $|A|$ is the amplitude, $B$ **is** the period, $C$ the horizontal phase shift, $D$ the vertical shift.

> **Correction.** The two conventions above conflict in the slides, where $B$ is described both as a horizontal scaling factor and as the period. They are different parametrisations: in $f(b \cdot x)$ the factor $b$ is a *frequency* and the period is divided by $b$; in $\sin\left( \frac{2\pi}{B}x \right)$ the quantity $B$ *is* the period. Fix the convention before using either.

**Symmetry.** $\cos( - \theta) = cos\theta$ and $\sec( - \theta) = sec\theta$ are **even** ($y$-axis symmetry); $sin,csc,tan,cot$ are **odd** ($f( - \theta) = - f(\theta)$, origin symmetry).

## 4.2 Continuity and derivatives

$f$ is **continuous** at $x = a$ if $\lim_{x \rightarrow a}f(x) = f(a)$ — no jumps, holes or vertical asymptotes. Biological growth curves (bacterial OD, tumour volume) are continuous functions of time.

**Definition of the derivative.** The instantaneous rate of change, i.e. the slope of the tangent line:

$$
f'(x) = \frac{dy}{dx} = \lim_{h \rightarrow 0}\frac{f(x + h) - f(x)}{h}
$$

**Tangent line** at $\left( x_{1},y_{1} \right)$: $y - y_{1} = m\left( x - x_{1} \right)$ with $m = f'\left( x_{1} \right)$. The **normal line** has slope $m_{\bot} = - 1/m$.

**Differentiability** requires continuity *and* smoothness. It fails at **corners** ($|x|$), **cusps** ($x^{2/3}$), **vertical tangents** ($\sqrt[3]{x}$) and **discontinuities** (step functions).

> **The implication goes one way only:** differentiable $\Rightarrow$ continuous, but continuous $\nRightarrow$ differentiable. $|x|$ at the origin is the standard counterexample. This matters in §4.3: the $L^{1}$ penalty of LASSO is continuous but not differentiable at zero, which is both why it produces exact zeros and why it needs a different optimiser from ridge.

### 4.2.1 Differentiation rules

| Rule | Formula |
|----|----|
| Constant | $\frac{d}{dx}(c) = 0$ |
| Power | $\frac{d}{dx}\left( x^{n} \right) = nx^{n - 1}$ |
| Linearity | $\frac{d}{dx}\lbrack cu \pm dv\rbrack = c\frac{du}{dx} \pm d\frac{dv}{dx}$ |
| Product | $\frac{d}{dx}(uv) = u\frac{dv}{dx} + v\frac{du}{dx}$ |
| Quotient | $\frac{d}{dx}\left( \frac{u}{v} \right) = \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^{2}}$ |
| Chain | $y = f(u),\ u = g(x) \Rightarrow \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = f'\left( g(x) \right)g'(x)$ |

**Trigonometric.** $\frac{d}{dx}\sin x = cosx$; $\frac{d}{dx}\cos x = - sinx$; $\frac{d}{dx}\tan x = \sec^{2}x$; $\frac{d}{dx}\cot x = - \csc^{2}x$; $\frac{d}{dx}\sec x = secx\tan x$; $\frac{d}{dx}\csc x = - cscx\cot x$.

**Exponential and logarithmic.** $\frac{d}{dx}e^{x} = e^{x}$; $\frac{d}{dx}a^{x} = a^{x}\ln a$; $\frac{d}{dx}\ln x = \frac{1}{x}$; $\frac{d}{dx}\log_{a}x = \frac{1}{x\ln a}$.

> **The chain rule is the single most important one in this course.** It is what makes gradient descent possible through a multi-layer model (§4.3), what multiplies sensitivities along a signalling cascade, and — in its multivariable form — what backpropagation is.

### 4.2.2 Biological applications

- **Enzyme initial velocity.** $v_{0} = \left. \ \frac{d\lbrack P\rbrack}{dt} \right|_{t = 0}$, measured by stopped-flow spectrophotometry.
- **Logistic growth dynamics.** $\frac{dN}{dt} = rN\left( 1 - \frac{N}{K} \right)$. Equilibria at $N = 0$ (unstable) and $N = K$ (carrying capacity, stable); maximum growth rate at the inflection point $N = K/2$.
- **Cascade sensitivity (chain rule).** If transcription-factor activity is $a = g(p)$ and phosphorylation $p = f\left( \lbrack L\rbrack \right)$, then $\frac{da}{d\lbrack L\rbrack} = \frac{da}{dp} \cdot \frac{dp}{d\lbrack L\rbrack}$. Multiplying sensitivities across steps creates the switch-like ultrasensitivity of MAP-kinase pathways.
- **First-order drug elimination.** $\frac{dC}{dt} = - kC \Rightarrow C(t) = C_{0}e^{- kt}$, with $t_{1/2} = \frac{\ln 2}{k}$. Since $\frac{d^{2}C}{dt^{2}} = k^{2}C > 0$, the concentration curve is strictly concave up.

> **How to find the maximum-growth point of the logistic model**, since it is a standard exam step. Set $\frac{d^{2}N}{dt^{2}} = 0$: differentiating $rN(1 - N/K)$ with respect to $N$ gives $r(1 - 2N/K)$, which vanishes at $N = K/2$. The population grows fastest when it is at half its carrying capacity — not at the start.

## 4.3 Extrema, curve sketching, Taylor series, numerical optimisation

### 4.3.1 Critical points and extrema

**Critical points** are interior points $c$ where $f'(c) = 0$ or $f'(c)$ is undefined. Every local extremum occurs at a critical point, **but not every critical point is an extremum**: $y = x^{3}$ has $f'(0) = 0$ and $y = x^{1/3}$ has $f'(0)$ undefined, yet neither is an extremum.

To find **global (absolute) extrema** on a closed interval $\lbrack a,b\rbrack$, evaluate $f$ at all critical points **and at the endpoints** $a$ and $b$. Forgetting the endpoints is the standard mistake.

### 4.3.2 First and second derivative tests

| Sign        | Meaning                                                   |
|-------------|-----------------------------------------------------------|
| $y' > 0$  | rising                                                    |
| $y' < 0$  | falling                                                   |
| $y' = 0$  | stationary point                                          |
| $y'' > 0$ | **concave up**; if also $y' = 0$, a local **minimum**   |
| $y'' < 0$ | **concave down**; if also $y' = 0$, a local **maximum** |

**Inflection point:** where concavity changes sign ($y'' = 0$ **and** changes sign — $y'' = 0$ alone is not enough, as $y = x^{4}$ at the origin shows).

> **Mnemonic that survives into Module 5.** Concave up is a cup, so it holds a minimum. In $n$ dimensions “$y'' > 0$” becomes “all eigenvalues of the Hessian are positive” (§5.2) — the same statement, one dimension at a time along the principal axes.

### 4.3.3 Taylor and Maclaurin series

Approximating a smooth $f$ near $x = a$ with an $n$-th degree polynomial that matches derivatives, $P^{(k)}(a) = f^{(k)}(a)$:

$$
P(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^{2} + \frac{f'''(a)}{3!}(x - a)^{3} + \ldots
$$

The **Maclaurin series** is the case $a = 0$:

$$
P(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^{2} + \frac{f'''(0)}{3!}x^{3} + \ldots
$$

*Example.* $f(x) = ln(1 + x)$ at $x = 0$: $P(x) = x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4} + \ldots$

> **What Taylor expansion is really for in this course.** Truncating at order 1 gives the *linear* approximation — the basis of every “locally linear” argument, of error propagation, and of the delta method. Truncating at order 2 gives the *quadratic* approximation, which is exactly what Newton’s method minimises below and what the Hessian analysis of §5.2 reads. The multivariable version in §5.1 is the same formula with $\nabla f$ in place of $f'$ and $H$ in place of $f''$.

### 4.3.4 Numerical optimisation in 1D

**Gradient descent.** Update the parameter against the derivative:

$$
x^{(t + 1)} = x^{(t)} - a\, f'\left( x^{(t)} \right)
$$

where $a$ is the **learning rate**. Too small and convergence is slow; too large and the updates overshoot and diverge.

*Simple neuron training.* For $z = \frac{1}{1 + e^{- wx}}$, target $d$, squared error $E(w) = \frac{1}{2}(z - d)^{2}$, the chain rule gives

$$
\frac{dE}{dw} = \frac{dE}{dz}\frac{dz}{da}\frac{da}{dw} = (z - d) \cdot z(1 - z) \cdot x
$$

using the sigmoid identity of §4.1.1. The three factors are, in order: the error, the local slope of the activation, and the input.

**Newton’s method.** Use a second-order Taylor expansion $f\left( x^{(i)} + s \right) \approx f\left( x^{(i)} \right) + f'\left( x^{(i)} \right)s + \frac{1}{2}f''\left( x^{(i)} \right)s^{2}$ and set $\frac{df}{ds} = 0$:

$$
f'\left( x^{(i)} \right) + f''\left( x^{(i)} \right)s = 0 \Longrightarrow s = - \frac{f'\left( x^{(i)} \right)}{f''\left( x^{(i)} \right)}
$$

> **The comparison the slides leave implicit.**

|  | Gradient descent | Newton’s method |
|----|----|----|
| Information used | first derivative | first **and** second |
| Step size | chosen by hand ($a$) | computed automatically |
| Convergence near optimum | linear | quadratic (much faster) |
| Cost per step | cheap | needs $f''$; in $n$ dimensions, an $n \times n$ Hessian and its inverse |
| Failure mode | too-large $a$ diverges | converges to a *saddle* or *maximum* just as happily, since $f' = 0$ is all it enforces |

> This is why deep learning uses gradient descent and its variants rather than Newton: with millions of parameters the Hessian is unusable, and quasi-Newton methods (BFGS, L-BFGS) approximate it instead.

## 4.4 Definite and indefinite integrals

**Riemann sum and definite integral.** Partitioning $\lbrack a,b\rbrack$ into subintervals of width $\Delta x_{k}$ (norm $\parallel P \parallel$ = largest width), the area under $f$ is

$$
\lim_{\parallel P \parallel \rightarrow 0}\sum_{k = 1}^{n}f\left( c_{k} \right)\Delta x_{k} = \int_{a}^{b}f(x)\, dx = F(b) - F(a)
$$

where $F$ is the **indefinite integral (antiderivative)** satisfying $\frac{dF}{dx} = f(x)$, defined up to an arbitrary constant $+ C$.

**Fundamental theorem of calculus.** If $f$ is continuous on $\lbrack a,b\rbrack$ and $F(x) = \int_{a}^{x}f(t)\, dt$, then

$$
\frac{dF}{dx} = \frac{d}{dx}\int_{a}^{x}f(t)\, dt = f(x)
$$

Differentiation and integration are inverse operations.

**Properties of definite integrals.**

$$
\int_{a}^{a}f = 0,\quad\quad\int_{b}^{a}f = - \int_{a}^{b}f,\quad\quad\int_{a}^{b}kf = k\int_{a}^{b}f
$$

$$
\int_{a}^{b}(f \pm g) = \int_{a}^{b}f \pm \int_{a}^{b}g,\quad\quad\int_{a}^{b}f + \int_{b}^{c}f = \int_{a}^{c}f
$$

### 4.4.1 Integration techniques

- **Substitution (**$u$**-substitution).** Reverses the chain rule: set $u = g(x)$, $du = g'(x)\, dx$. *Use it when* the integrand contains a function and (a multiple of) its own derivative.
- **Integration by parts.** From the product rule $d(uv) = u\, dv + v\, du$:

$$
\int u\, dv = uv - \int v\, du
$$

- *Use it when* the integrand is a product of two unrelated types of function. Example: $\int lnx\, dx = x\ln x - x + C$ with $u = lnx$, $dv = dx$.

> **How to choose, in one line:** substitution undoes the chain rule, parts undoes the product rule. Look at which rule would have *produced* your integrand.

### 4.4.2 Biological applications

- **Pharmacokinetics (AUC).** $AUC = \int_{0}^{\infty}C(t)\, dt$ measures total drug exposure; oral bioavailability is $F = {AUC}_{\text{oral}}/{AUC}_{\text{IV}}$.
- **Respiratory physiology.** Tidal volume $V = \int_{0}^{T_{\text{insp}}}v(t)\, dt$ integrates airflow rate over time (FVC, FEV1).
- **Population genetics.** Fixation and threshold probabilities in Wright–Fisher diffusion models, $P = \int_{x^{*}}^{1}\phi(x)\, dx$.
- **RNA-seq coverage.** Total reads over a gene of length $L$ is $\int_{0}^{L}c(x)\, dx$, used to compute RPK, RPKM and FPKM.

> **The pattern across all four.** An integral converts a *rate* into a *total*: concentration-over-time into exposure, flow into volume, coverage into read count, density into probability. Whenever a biological quantity is measured per unit of something and the question asks for the accumulated amount, the answer is an integral. The next module’s probability densities (§6.2) are the same idea once more.

---
> [[MBD 12 - Module 3 · Complex numbers … What is missing – the singular value decomposition|← Module 3 · Complex numbers … What is missing – the singular value decomposition]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 14 - Module 5 – Multivariable Calculus and Optimisation|Module 5 – Multivariable Calculus and Optimisation →]]
