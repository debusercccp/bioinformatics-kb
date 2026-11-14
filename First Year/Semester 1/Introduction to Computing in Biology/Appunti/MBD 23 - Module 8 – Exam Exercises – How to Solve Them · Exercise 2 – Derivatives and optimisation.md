---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 23
tags: [note, mbd]
---

> [[MBD 22 - Module 8 – Exam Exercises – How to Solve Them|← Module 8 – Exam Exercises – How to Solve Them]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 24 - Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem|Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem →]]

# Exercise 2 — Derivatives and optimisation

Two variants: a function of **one** variable (P1, P3, P5) or of **two** variables (P2, P4).

### 8.2.1 One variable: $\mathbf{f}\left( \mathbf{x} \right)$

Typical questions: a) $f'(x)$; b) critical point(s) and their nature; c) extreme value.

**Recipe:**

1.  **Derivative** with the rules (§4.4.2). The exam functions are products with $e^{- x}$ or $\ln x$: use the product rule $(uv)' = u'v + uv'$ and the chain rule for $e^{- x}$ ($\frac{d}{dx}e^{- x} = - e^{- x}$). Factor the result (e.g. collect $e^{- t}$).
2.  **Critical points:** $f'(x) = 0$. Use that $e^{\ldots} > 0$ always (so only the other factor can be 0) and **respect the domain** ($x > 0$ for $\ln x$; discard negative solutions).
3.  **Nature:** compute $f''(x)$ and evaluate it at the critical point: $f'' > 0 \Rightarrow$ local minimum, $f'' < 0 \Rightarrow$ local maximum (§4.5).
4.  **Extreme value:** substitute the critical point in $f$ (not in $f'$!). Leave exact forms ($1/e$, $- 1/e$).

**Worked example (Practice 1).** $f(t) = t\, e^{- t}$, $t \geq 0$.

1)  $f'(t) = 1 \cdot e^{- t} + t \cdot \left( - e^{- t} \right) = e^{- t}(1 - t)$.

2)  $f'(t) = 0 \Rightarrow 1 - t = 0$ (since $e^{- t} > 0$) $\Rightarrow t^{*} = 1$. $f''(t) = - e^{- t}(1 - t) + e^{- t}( - 1) = e^{- t}(t - 2)$; $f''(1) = - e^{- 1} < 0 \Rightarrow$ **local maximum**.

3)  $f(1) = 1 \cdot e^{- 1} = \frac{1}{e}$.

**Other practice exams:**

| Function | $f'(x)$ | Critical point | $f''$ at the point | Result |
|:---|:---|:---|:---|:---|
| $x\ln x$, $x > 0$ (P3) | $\ln x + 1$ | $\ln x = - 1 \Rightarrow x^{*} = 1/e$ | $f'' = 1/x$, $f''(1/e) = e > 0$ | min, $f(1/e) = - 1/e$ |
| $x^{2} - 2\ln x$, $x > 0$ (P5) | $2x - 2/x$ | $x^{2} = 1 \Rightarrow x^{*} = 1$ ($x > 0$) | $f'' = 2 + 2/x^{2}$, $f''(1) = 4 > 0$ | min, $f(1) = 1$ |

### 8.2.2 Two variables: $\mathbf{g}\left( \mathbf{x}\mathbf{,}\mathbf{y} \right)$

Typical questions: a) $\partial g/\partial x$, $\partial g/\partial y$; b) critical point(s); c) classify them (and compute $g$ there).

**Recipe:**

1.  **Partial derivatives** (§5.1): differentiate with respect to $x$ treating $y$ as a constant, and vice versa.
2.  **Critical points:** solve $\partial g/\partial x = 0$, $\partial g/\partial y = 0$ (for the exam polynomials it is a linear system: solve one equation for one variable and substitute).
3.  **Hessian** (§5.2): $H = \begin{pmatrix}
    g_{xx} & g_{xy} \\
    g_{xy} & g_{yy}
    \end{pmatrix}$, compute its eigenvalues with $\det(H - \lambda I) = 0$ (same procedure as Exercise 1). All $\lambda > 0 \Rightarrow$ **minimum**; all $\lambda < 0 \Rightarrow$ **maximum**; opposite signs $\Rightarrow$ **saddle**. *Quick check* for $2 \times 2$: $\lambda_{1}\lambda_{2} = det(H)$ and $\lambda_{1} + \lambda_{2} = Tr(H)$, so $\det(H) > 0$ and $Tr(H) > 0 \Rightarrow$ both positive (minimum); $\det(H) > 0$, $Tr(H) < 0 \Rightarrow$ both negative (maximum); $\det(H) < 0 \Rightarrow$ saddle.
4.  **Value:** substitute the critical point in $g$.

**Worked example (Practice 2).** $g(x,y) = x^{2} + y^{2} - 2x - 4y$.

1)  $\frac{\partial g}{\partial x} = 2x - 2$, $\frac{\partial g}{\partial y} = 2y - 4$.

2)  $2x - 2 = 0$, $2y - 4 = 0 \Rightarrow (1,2)$.

3)  $H = \begin{pmatrix}
    2 & 0 \\
    0 & 2
    \end{pmatrix}$, eigenvalues $2,2 > 0 \Rightarrow$ **minimum**; $g(1,2) = 1 + 4 - 2 - 8 = - 5$.

**Practice 4:** $g = x^{2} + 2y^{2} + 2xy$: $g_{x} = 2x + 2y$, $g_{y} = 4y + 2x$; $x = - y \Rightarrow 2y = 0 \Rightarrow (0,0)$. $H = \begin{pmatrix}
2 & 2 \\
2 & 4
\end{pmatrix}$, $\lambda^{2} - 6\lambda + 4 = 0 \Rightarrow \lambda = 3 \pm \sqrt{5}$, both positive $\Rightarrow$ minimum, $g(0,0) = 0$. *Note:* the solution key writes the eigenvalues as $\left( 6 \pm \sqrt{10} \right)/2$; the correct value is $\left( 6 \pm \sqrt{20} \right)/2 = 3 \pm \sqrt{5}$ (the conclusion does not change).

---
> [[MBD 22 - Module 8 – Exam Exercises – How to Solve Them|← Module 8 – Exam Exercises – How to Solve Them]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 24 - Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem|Module 8 – Exam Exercises – How to Solve Them · Exercise 3 – Constrained optimisation (Lagrange) + Exercise 4 – Probability – diagnostic test and Bayes’ theorem →]]
