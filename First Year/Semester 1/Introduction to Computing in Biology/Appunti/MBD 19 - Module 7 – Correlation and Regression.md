---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 19
tags: [note, mbd]
---

> [[MBD 18 - Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions|← Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 20 - Module 8 – Principal Component Analysis|Module 8 – Principal Component Analysis →]]

# Module 7 — Correlation and Regression

## 7.1 Correlation coefficients and hypothesis testing

### 7.1.1 From covariance to correlation

Given $m$ paired observations of two variables, with means $M_{1},M_{2}$:

$$
cov\left( x_{1},x_{2} \right) = \frac{1}{n - 1}\sum_{i = 1}^{m}\left( x_{1i} - M_{1} \right)\left( x_{2i} - M_{2} \right),\quad\quad r = \frac{cov\left( x_{1},x_{2} \right)}{\sigma_{1}\sigma_{2}} \in \lbrack - 1,1\rbrack
$$

**Why normalise at all.** Covariance has the units of the product of the two variables, so its magnitude says nothing on its own: the covariance between two gene expressions in raw counts and the same pair in CPM differ by a factor of $10^{12}$. Dividing by both standard deviations removes the units and the scale, leaving a pure number in $\lbrack - 1,1\rbrack$. That the result is bounded is Cauchy–Schwarz applied to the centred vectors (§1.3.4, §1.3.7) — correlation **is** the cosine of the angle between the mean-centred data vectors.

| Measure | Formula and range | Assumptions and use |
|----|----|----|
| **Pearson** $r$ | $\frac{cov\left( x_{1},x_{2} \right)}{\sigma_{1}\sigma_{2}} \in \lbrack - 1,1\rbrack$ | parametric; measures **linear** dependence between continuous variables |
| **Spearman** $\rho$ | Pearson’s $r$ computed on the **ranks** $\left( R_{x_{i}},R_{y_{i}} \right)$ | non-parametric; captures any **monotonic** relationship, robust to outliers |
| **Matthews (MCC)** | $\frac{ad - bc}{\sqrt{(a + b)(a + c)(d + b)(d + c)}}$ | binary **categorical** data in a $2 \times 2$ contingency table |

**MCC in context.** For the classification of signal peptides:

|                        | Secreted  | Non-secreted | Total     |
|------------------------|-----------|--------------|-----------|
| With signal peptide    | $a$     | $b$        | $a + b$ |
| Without signal peptide | $c$     | $d$        | $c + d$ |
| **Total**              | $a + c$ | $b + d$    | $n$     |

> **MCC is Pearson’s** $r$ **applied to two binary variables** — the same formula, specialised. This is why it ranges over $\lbrack - 1,1\rbrack$ and why it is preferred to accuracy for **imbalanced** data: a classifier predicting “non-secreted” for everything scores high accuracy but $MCC = 0$, correctly reporting no better-than-chance association.
>
> **Choosing between Pearson and Spearman.** Pearson detects *linear* association only. A perfect but curved relationship can give a modest $r$ — the slides show an example with $R = 0.816$ for data that are visibly non-linear. Spearman ranks first, so any monotonic relationship (exponential, logarithmic, sigmoid) gives $\rho = \pm 1$, and single extreme outliers lose their leverage because a rank is bounded. Use Spearman when the relationship is monotone but not straight, when outliers are present, or when the data are ordinal. Note that *neither* detects a non-monotonic dependence such as $Y = X^{2}$ — the §6.2.4 counterexample again.

### 7.1.2 Statistical significance of a correlation

**Parametric** $t$**-test.** Under the null hypothesis $H_{0}:r = 0$, assuming normality,

$$
t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^{2}}}
$$

follows **Student’s** $t$**-distribution with** $\nu = n - 2$ **degrees of freedom**. The same statistic applies to Spearman’s $\rho$ in place of $r$.

> **Why** $n - 2$**.** Two parameters, the slope and the intercept, have been estimated from the data; each estimate costs one degree of freedom (§6.3.3).
>
> **What significance does and does not mean.** The test asks whether $r$ differs from zero, not whether it is *large*. With $n = 10,000$ samples, $r = 0.03$ is highly significant and biologically meaningless. Report the **effect size** $r$ (or $r^{2}$, the fraction of variance explained) alongside the $p$-value, and read the slides’ graph of the minimum $r$ significant at the 0.05 level against sample size as a reminder of how fast that threshold collapses.

### 7.1.3 Permutation test: significance without distributional assumptions

**The case.** Two experimentalists were asked to run 24 independent ELISA assays each on a $6 \times 4$ plate, from the same solution. The submitted readings $S_{1},S_{2}$ gave $R = 0.978$, $n = 24$, $t = 22.05$ — far too high for independent replicates, suggesting that two reads of the *same* plate had been submitted.

**The objection.** The $t$-test is valid only if the data are normally distributed, which cannot be demonstrated here.

**The non-parametric answer.** Use the data themselves to generate the null distribution:

1.  Randomly **shuffle** (permute) the entries of $S_{2}$, breaking the true pairings while keeping both marginal distributions exactly as observed.
2.  Compute $r$ for the shuffled pairing. One such shuffle gives $R = 0.25$.
3.  Repeat many times (say 1,000) and build the cumulative histogram of the resampled correlations.
4.  The fraction of resamplings reaching $r \geq r_{\text{obs}}$ is a **distribution-free empirical** $p$**-value**.

> **Why this works, and the one thing to watch.** Under the null hypothesis the pairing carries no information, so every permutation is equally likely; the observed statistic is then just one draw from the set of all permuted values. No normality, no formula, no degrees of freedom — only the exchangeability of the labels under $H_{0}$. The resolution is limited by the number of permutations: with 1,000 shuffles the smallest reportable $p$-value is $1/1000$, so for genome-scale thresholds ($p < 5 \times 10^{- 8}$) you need either far more permutations or a parametric tail approximation.
>
> *Terminology:* strictly, shuffling labels is a **permutation test**; **bootstrapping** resamples *with replacement* to estimate the sampling distribution of a statistic (for confidence intervals). The slides use the two names together; they answer different questions.

## 7.2 Linear and polynomial regression, overfitting, regularisation

### 7.2.1 Simple linear regression by least squares

Model $y_{i} = ax_{i} + b + \varepsilon_{i}$, where $\varepsilon_{i}$ are the **residuals**. Minimise the sum of squared residuals

$$
E(a,b) = \sum_{i = 1}^{m}\varepsilon_{i}^{2} = \sum_{i = 1}^{m}(y_{i} - \left( ax_{i} + b \right))^{2}
$$

Setting the two partial derivatives to zero:

$$
\frac{\partial E}{\partial b} = 0 \Longrightarrow - 2\sum_{i}^{}\left( y_{i} - \left( ax_{i} + b \right) \right) = 0 \Longrightarrow b = \bar{y} - a\bar{x}
$$

$$
\frac{\partial E}{\partial a} = 0 \Longrightarrow \sum_{i}^{}x_{i}y_{i} - a\sum_{i}^{}x_{i}^{2} - \bar{y}\sum_{i}^{}x_{i} + a\bar{x}\sum_{i}^{}x_{i} = 0
$$

$$
\Longrightarrow a = \frac{\frac{1}{m}\sum_{i}^{}x_{i}y_{i} - \bar{x}\bar{y}}{\frac{1}{m}\sum_{i}^{}x_{i}^{2} - {\bar{x}}^{2}} = \frac{cov(x,y)}{\sigma_{x}^{2}}
$$

> **Two readings of the result worth keeping.**

1.  $b = \bar{y} - a\bar{x}$ says the fitted line **always passes through the centroid** $\left( \bar{x},\bar{y} \right)$. Useful as a sanity check on any fit.
2.  $a = cov(x,y)/\sigma_{x}^{2} = r\,\sigma_{y}/\sigma_{x}$. So the slope is the correlation rescaled by the ratio of the spreads — and regressing $y$ on $x$ gives a *different* line from regressing $x$ on $y$ (slope $r\,\sigma_{x}/\sigma_{y}$). The two coincide only when $|r| = 1$. Regression is **not** symmetric, whereas correlation is. Which variable you call “dependent” matters.

> **Why squared residuals and not absolute ones?** Squares make the objective differentiable everywhere (§4.2), giving the closed form above; and under Gaussian noise, minimising the squared error *is* maximum likelihood (§6.4) — the exponent of the normal density is exactly $- \frac{1}{2\sigma^{2}}\sum\left( y_{i} - {\widehat{y}}_{i} \right)^{2}$. Minimising absolute deviations instead gives median regression, which is more robust to outliers but has no closed form. Least squares is sensitive to outliers precisely because the square gives a distant point disproportionate weight.

**Matrix form, for more than one predictor.** The scalar derivation above does not generalise comfortably. With $X$ the design matrix (one row per observation, one column per predictor plus a column of ones), the same minimisation gives the normal equations of §2.5.2:

$$
\widehat{\beta} = \left( X^{T}X \right)^{- 1}X^{T}y
$$

This single expression covers simple regression, multiple regression and polynomial regression — the last by putting $1,x,x^{2},\ldots,x^{p}$ in the columns of $X$.

### 7.2.2 Polynomial regression and overfitting

Fitting a degree-$p$ polynomial $y = P(x) = \sum_{k = 1}^{p}a_{k}x^{k} + b$. A dataset of $m$ points can be **perfectly interpolated** ($E = 0$) by a polynomial of degree $p = m - 1$: two points define a unique line, three a unique parabola, and so on. Increasing the degree always decreases the training error.

**Overfitting.** The coefficients explode as the degree rises. From the standard example ($M$ the polynomial degree):

|           | $M = 0$ | $M = 1$  | $M = 3$ | $M = 9$       |
|-----------|-----------|------------|-----------|-----------------|
| $b$     | 0.19      | 0.82       | 0.31      | 0.35            |
| $a_{1}$ |           | $- 1.27$ | 7.99      | 232.37          |
| $a_{3}$ |           |            | 17.37     | 48,568          |
| $a_{6}$ |           |            |           | $- 1,061,800$ |
| $a_{9}$ |           |            |           | 125,201         |

Coefficients of order $10^{6}$ with alternating signs produce a curve that passes exactly through every training point by oscillating wildly between them. The model fits the **noise**, and predicts new points catastrophically — especially when extrapolating, and especially when $m$ is small.

> **The distinction this illustrates.** Training error always decreases with model complexity; **generalisation** error does not. A model with as many free parameters as data points learns the sample, not the process. This is why performance must be assessed on data not used for fitting — held-out test set or cross-validation — and the lesson transfers directly to the “how many PCs to keep” question of §8.1 and to every classifier in the course.

### 7.2.3 Regularised regression (ridge, $\mathbf{L}^{\mathbf{2}}$ penalty)

Add a penalty discouraging large coefficients:

$$
E = \sum_{i = 1}^{m}(y_{i} - P\left( x_{i} \right))^{2} + \lambda\sum_{k = 1}^{p}a_{k}^{2}
$$

where $\lambda$ controls the regularisation strength. The effect on the degree-9 fit is dramatic:

|  | $\ln\lambda = 0$ | $\ln\lambda = - 18$ | $\ln\lambda = - \infty$ (none) |
|----|----|----|----|
| $a_{1}$ | $- 0.05$ | 4.74 | 232.37 |
| $a_{6}$ | $- 0.01$ | 41.32 | $- 1,061,800$ |
| $a_{9}$ | 0.01 | 72.68 | 125,201 |

With $\lambda$ too large the model is over-smoothed (all coefficients near zero, underfitting); with $\lambda = 0$ it overfits; an intermediate value generalises. $\lambda$ **is chosen by cross-validation, never on the training error** — which by construction always prefers $\lambda = 0$.

> **Connections across the course.**

- The penalty term is $\lambda \parallel a \parallel_{2}^{2}$, the squared $L^{2}$ norm of §1.3.5. Replacing it with the $L^{1}$ norm $\lambda\sum_{k}^{}\left| a_{k} \right|$ gives **LASSO**, which sets coefficients exactly to zero and so performs variable selection. The geometric reason is the shape of the unit balls (§1.3.5): the $L^{1}$ diamond has corners on the axes, the $L^{2}$ circle does not. With $p \approx 20,000$ genes and $n \approx 100$ samples, that sparsity is what makes the problem tractable at all.
- In matrix form, ridge is $\widehat{\beta} = \left( X^{T}X + \lambda I \right)^{- 1}X^{T}y$: adding $\lambda I$ makes a singular or near-singular $X^{T}X$ invertible. So regularisation is not only a statistical device against overfitting, it is also the numerical fix for collinear predictors — which is the normal state of gene expression data, where co-expressed genes are nearly duplicate columns.
- The same $\parallel W \parallel$ appears as the SVM margin in §1.4.2. Maximising the margin and penalising the norm are the same operation.

### 7.2.4 What is missing: multiple testing

The whole module tests **one** correlation at a time. In practice you test $20,000$ genes, or $10^{6}$ SNPs, simultaneously. At $\alpha = 0.05$, testing 20,000 genes with no real signal whatsoever still yields about **1,000 “significant” results** by chance alone. Two standard corrections:

- **Bonferroni:** use the threshold $\alpha/m$. Controls the family-wise error rate (the probability of *any* false positive); very conservative, which is where the genome-wide significance threshold $5 \times 10^{- 8} \approx 0.05/10^{6}$ comes from.
- **Benjamini–Hochberg (FDR):** sort the $p$-values ascending and find the largest $k$ with $p_{(k)} \leq \frac{k}{m}\alpha$; reject all hypotheses up to $k$. Controls the *expected proportion* of false positives among the rejections. Much more powerful, and the default for differential expression — a DESeq2 or edgeR “adjusted $p$-value” is a BH-corrected one.

Without a correction, no $p$-value quoted from a genome-scale screen means anything.

## Collegamenti
- [[AML 03 - Univariate Model Regression]] — regressione in ML
- [[AML 17 - Regularisation]] — regolarizzazione

---
> [[MBD 18 - Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions|← Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 20 - Module 8 – Principal Component Analysis|Module 8 – Principal Component Analysis →]]
