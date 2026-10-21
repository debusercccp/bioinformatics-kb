---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 25
tags: [note, mbd]
---

> [[MBD 24 - Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6|← Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]]

# Appendix B — Master list of corrections

Two kinds of entry: **\[S\]** marks an error or ambiguity in the slide deck itself, **\[D\]** an error introduced in the earlier draft of these notes. All corrections have been verified by computation where computation applies.

## B.1 Mathematical errors

| \# | Where | As written | Correct statement |
|----|----|----|----|
| 1 | **\[S\]** §5.2, local optima | “a maximum if all eigenvalues are positive, a minimum if all the eigenvalues are negative” | **Inverted.** All $\lambda_{i} > 0$ (positive definite $H$) $\Rightarrow$ **minimum**; all $\lambda_{i} < 0$ $\Rightarrow$ **maximum**. The slide’s own worked Example 2 confirms this: $\lambda = - 2, - 4$ is labelled MAXIMUM and $\lambda = + 2, + 4$ MINIMUM. |
| 2 | **\[S\]** §6.3, chi-square | $Q = \sum_{i = 1}^{N}\left( X_{i} - \mu \right)^{2} \sim \chi_{n - 1}^{2}$ | Wrong twice. Must divide by $\sigma^{2}$; and the degrees of freedom depend on the centre: $\frac{1}{\sigma^{2}}\sum\left( X_{i} - \mu \right)^{2} \sim \chi_{n}^{2}$ (true mean), while $\frac{1}{\sigma^{2}}\sum\left( X_{i} - M \right)^{2} \sim \chi_{n - 1}^{2}$ (sample mean). Verified by simulation ($n = 8$: means $7.996$ and $7.000$). |
| 3 | **\[S\]** §1.3, inner product | “if $\langle A,B\rangle = 0$ the two gene programmes are statistically independent” | Wrong twice. Orthogonality $=$ *uncorrelatedness* only after mean-centring, and uncorrelated $\nRightarrow$ independent (§6.2.4 says so correctly). Rewrite: orthogonal centred signature vectors are **uncorrelated across samples**. |
| 4 | **\[S\]** §1.3, norm axiom | $\parallel \lambda X \parallel = \lambda \parallel X \parallel$ | $\parallel \lambda X \parallel = |\lambda|\, \parallel X \parallel$. Without the absolute value the norm of $- X$ would be negative. |
| 5 | **\[S\]** §1.3, norm axiom | “$\parallel X \parallel > 0$ if $X \neq 0$” | Incomplete; state the full axiom: $\parallel X \parallel \geq 0$ **and** $\parallel X \parallel = 0 \Leftrightarrow X = 0$. |
| 6 | **\[S\]** §1.3, inner product | positive-definiteness as $\langle X,X\rangle \geq 0$ | Incomplete: equality must hold **iff** $X = 0$. Otherwise the induced object is only a semi-norm. |
| 7 | **\[S\]** §8.1, diagonalisation | $U^{T} \cdot COV \cdot U = COV = diag\left( \lambda_{1},\ldots \right)$ | The middle term is $\Lambda$, not COV: $U^{T}\, COV\, U = \Lambda = diag\left( \lambda_{1},\ldots,\lambda_{n} \right)$. As written it asserts the hypothesis is the conclusion. |
| 8 | **\[S\]** §3.4, spectral theorem | “eigenvectors are orthogonal” | True as stated only for **distinct** eigenvalues. With a repeated eigenvalue, orthogonality within the eigenspace is not automatic, but an orthonormal basis of it can always be **chosen** (Gram–Schmidt), so $U$ is still orthogonal. Without this the theorem would not cover a covariance matrix with tied eigenvalues. |
| 9 | **\[S\]** §1.1, contact map | $n = L^{2}$ | $L^{2}$ counts *ordered* pairs. The map is symmetric with a trivial diagonal, so the number of distinct residue pairs is $\binom{L}{2} = L(L - 1)/2$. |
| 10 | **\[S\]** §1.4, hyperplane | $p = \langle X,W\rangle/ \parallel W \parallel$ described as “scalar distance” | It is the **signed** scalar projection; the distance is $|p|$. |
| 11 | **\[S\]** §4.1, graph transformations | “$b$ scales horizontally” and “$B$ is the period” | Two incompatible conventions. In $y = af\left( b(x + c) \right) + d$, $b$ is a *frequency* factor and the period is divided by $b$; in $f(x) = A\sin\left( \frac{2\pi}{B}(x - C) \right) + D$, $B$ **is** the period. Fix the convention before using either. |
| 12 | **\[S\]** §6.3, Gumbel | mean and variance left blank | $E\lbrack X\rbrack = \mu + \gamma\beta$ with $\gamma \approx 0.5772$ (Euler–Mascheroni); $Var(X) = \pi^{2}\beta^{2}/6 \approx 1.6449\beta^{2}$. |
| 13 | **\[S\]** §5.2, second-order test | only three cases listed | A fourth case is missing: if some $\lambda_{i} = 0$ the test is **inconclusive**, not a saddle; higher-order terms decide. |
| 14 | **\[D\]** §1.3 | norm and distance formulas lost their $\sqrt{\ }$ and $\sum$ | $\parallel A \parallel = \sqrt{\sum_{i}^{}A_{i}^{2}}$, $d(A,B) = \sqrt{\sum_{i}^{}\left( B_{i} - A_{i} \right)^{2}}$. |
| 15 | **\[D\]** §7.1 | “2\$\$2 contingency table” | Typo for $2 \times 2$. |

## B.2 Mis-transcribed exercises in the earlier draft

In each case the draft’s arithmetic was internally consistent but applied to a matrix that is not the one on the slide. Corrected solutions are in Appendix A.

| \# | Exercise | Draft’s data | Slide’s actual data | Consequence |
|----|----|----|----|----|
| 16 | **\[D\]** Module 2, slide 103 | $b = (0,0,1)^{T}$ for all three systems; determinants $10$, $- 6$, $- 3$ | $b = (3,0,1)^{T}$, $(3,0,1)^{T}$, $(2,2,1)^{T}$ | **Two of the three systems are singular** ($det = 0$) and both are *inconsistent*. All three of the draft’s solution vectors are wrong. See §A.2.4. |
| 17 | **\[D\]** Module 2, slide 102 | matrices read column-wise | $\begin{pmatrix}
1 & 0 & 1 \\
1 & 2 & 1 \\
0 & 2 & 0
\end{pmatrix}$, $\begin{pmatrix}
1 & 0 & 0 \\
1 & 2 & 0 \\
0 & 2 & 1
\end{pmatrix}$, $\begin{pmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{pmatrix}$, $\begin{pmatrix}
1 & 0 & 1 \\
1 & 2 & 1 \\
0 & 1 & 1
\end{pmatrix}$ | Inverses differ; the singular/invertible verdicts happen to survive. See §A.2.3. |
| 18 | **\[D\]** Module 3, slide 135 | $M_{1}$ read as $\begin{pmatrix}
0 & 1 \\
3 & 5
\end{pmatrix}$, giving $\lambda = \frac{5 \pm \sqrt{37}}{2}$ | $M_{1} = \begin{pmatrix}
1 & 0 \\
5 & 3
\end{pmatrix}$ | Triangular, so $\lambda = 1,3$. Similarly $M_{2} = \begin{pmatrix}
1 & 0 \\
0 & 3
\end{pmatrix}$ gives $\lambda = 1,3$ (draft: $\pm \sqrt{3}$). See §A.3.1. |
| 19 | **\[D\]** Module 3, slide 153 | $A_{4}$ giving $\lambda_{2,3} = \frac{5 \pm \sqrt{13}}{2}$; $A_{5} = \begin{pmatrix}
1 & 0 & 0 \\
1 & 2 & 0 \\
0 & 5 & 3
\end{pmatrix}$ read with other entries | $A_{4} = \begin{pmatrix}
4 & 1 & 0 \\
1 & - 1 & 0 \\
0 & 0 & 3
\end{pmatrix}$ | $A_{4}$ is symmetric with $\lambda = \frac{3 \pm \sqrt{29}}{2}$ and $3$. The draft also omitted $A_{2} = \begin{pmatrix}
1 & 0 \\
2 & 1
\end{pmatrix}$ and $A_{6} = \begin{pmatrix}
2 & 0 & 0 \\
1 & 2 & 0 \\
0 & 5 & 1
\end{pmatrix}$, both **defective**. See §A.3.2. |
| 20 | **\[D\]** Module 5, box problem | $x = y = z = 4\sqrt{3} \approx 6.93$ cm | $x = y = z = \sqrt{32/3} = \frac{4\sqrt{6}}{3} \approx 3.266$ cm | The draft’s value gives a surface area of $\approx 288$ cm², violating the 64 cm² constraint. See §A.4. |

## B.3 Material omitted from both the slides and the earlier draft

Not errors, but gaps that make later modules harder than they need to be. Each is now covered in the section indicated.

| Topic | Now in | Why it is needed |
|----|----|----|
| Linear combination, span, independence, basis | §1.2.3 | prerequisite for change of basis, eigenvectors, PCA |
| Projection and orthogonal decomposition | §1.2.5 | PC scores *are* projections; also Gram–Schmidt, regressing out covariates |
| Cauchy–Schwarz inequality | §1.3.4 | the only reason $\cos\vartheta$ and Pearson’s $r$ lie in $\lbrack - 1,1\rbrack$ |
| $L^{p}$ norms, unit-ball geometry | §1.3.5 | explains LASSO vs ridge; non-Euclidean biological distances |
| Geometry $\leftrightarrow$ statistics dictionary | §1.3.7 | covariance *is* an inner product; makes Modules 6–8 nearly free |
| Distance from a point to a hyperplane | §1.4.1 | the SVM margin $2/ \parallel W \parallel$ |
| Norm preservation by orthogonal matrices | §2.1 | why the PCA rotation does not distort distances |
| Rank, rank–nullity theorem | §2.5.1 | dimensional accounting for null spaces |
| Rouché–Capelli | §2.5.1 | the only way to classify singular systems; needed for the slide-103 exercise |
| Pseudo-inverse, normal equations | §2.5.2, §7.2.1 | regression in matrix form, multiple predictors |
| Algebraic vs geometric multiplicity | §3.2.2 | the single criterion deciding diagonalisability |
| Geometric meaning of complex eigenvalues | §3.3 | rotation + scaling; oscillating biological dynamics |
| Positive-definiteness tests | §3.4.3 | used in §5.2 but never defined there |
| Singular value decomposition | §3.5, §8.1.3 | how PCA is actually computed; essential when $p \gg n$ |
| Gradient descent vs Newton comparison | §4.3.4 | why deep learning uses first-order methods |
| Joint / marginal / conditional table | §6.1.4 | the practical core of conditional probability |
| Prior / likelihood / evidence / posterior | §6.1.6 | the vocabulary of §6.4 and of Bayesian genomics |
| Uncorrelated $\nRightarrow$ independent, with counterexample | §6.2.4 | corrects the §1.3 claim; motivates Spearman and kernel PCA |
| Standard error vs standard deviation | §6.4.4 | the most common error in figure legends |
| Permutation vs bootstrap | §7.1.3 | they answer different questions |
| Regression is not symmetric | §7.2.1 | $y$ on $x$ differs from $x$ on $y$ unless $|r| = 1$ |
| Multiple testing (Bonferroni, Benjamini–Hochberg) | §7.2.4 | 20,000 genes at $\alpha = 0.05$ gives ~1,000 false positives |
| Scores vs loadings | §8.1.1 | the most common source of PCA confusion |
| PCA is not clustering | §8.1.3 | PCA is unsupervised and provides coordinates, not labels |

## B.4 Verification note

The following were checked numerically rather than taken on trust:

- all determinants, inverses, ranks and solutions in §A.2 and §A.3, by exact rational arithmetic;
- the consistency of the two singular systems of §A.2.4, by comparing $\operatorname{rank}(A)$ with $rank\left( \lbrack A \mid b\rbrack \right)$;
- diagonalisability of the six matrices of §A.3.2, by counting independent eigenvectors ($rank$ of the eigenvector matrix);
- the chi-square degrees-of-freedom claim of §6.3.3, by Monte Carlo with $2 \times 10^{5}$ replicates;
- the cosine-versus-correlation contrast of §1.3.8 and every numerical value in the Module 1 running example;
- the Lagrange box solution of §A.4, by substituting back into the constraint.

---
> [[MBD 24 - Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6|← Appendix A · A.4 Module 5 – Lagrange multipliers (slides 322–324) + A.5 Module 6]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]]
