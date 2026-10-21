---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 16
tags: [note, mbd]
---

> [[MBD 15 - Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem|← Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 17 - Module 6 – Probability Theory · Standard probability distributions|Module 6 – Probability Theory · Standard probability distributions →]]

# Descriptive statistics, moments, covariance

### 6.2.1 Discrete and continuous distributions

|  | Discrete | Continuous |
|----|----|----|
| Described by | PMF $f\left( x_{i} \right) = P\left( X = x_{i} \right)$ | PDF $f(x) = \frac{dF(x)}{dx}$ |
| Normalisation | $\sum_{i \in I}^{}f\left( x_{i} \right) = 1$ | $\int_{I}^{}f(x)\, dx = 1$ |
| Cumulative | $F\left( x_{i} \right) = P\left( X \leq x_{i} \right)$ | $F(x) = P(X \leq x)$, $F\left( x_{\text{highest}} \right) = 1$ |
| Interval probability | sum over the interval | $P(A < x \leq B) = F(B) - F(A) = \int_{A}^{B}f(x)\, dx$ |
| Point probability | $f\left( x_{i} \right)$, can be $> 0$ | $P\left( x = x_{1} \right) = \mathbf{0}$ |

> **The single most-misunderstood point.** A **PDF is not a probability**: $f(x)$ can exceed 1, and the probability of any exact value is zero. Only the *area* under the PDF is a probability. A PMF, by contrast, *is* a probability, bounded by 1. Empirical distributions are normalised histograms, $f\left( x_{i} \right) = N\left( x = x_{i} \right)/N_{\text{tot}}$.

### 6.2.2 Location and spread

- **Mode:** the most frequent value, the peak of the distribution. There can be more than one (multimodal).
- **Median (**$Q_{2}$**):** the value separating the ordered data into two equal halves. With an even number of observations, the mean of the two middle values.
- **Quartiles and IQR:** $Q_{1}$ (25th percentile), $Q_{3}$ (75th), $IQR = Q_{3} - Q_{1}$.

*Worked example.* Data $12,6,4,9,8,4,9,8,5,9,8,10$. Ordered: $4,4,5,6,8,8,8,9,9,9,10,12$. $Q_{1} = 5.5$, $Q_{2} = 8$, $Q_{3} = 9$, $IQR = 3.5$.

> **Mean vs median, in one line:** the mean is the balance point and uses every value, so a single outlier moves it; the median is the rank-based midpoint and is robust. Gene expression and sequencing-depth data are strongly right-skewed, which is why library-size normalisation uses medians (DESeq2’s median-of-ratios, TMM) and not means.

### 6.2.3 Expected value and moments

$$
E\left\lbrack g(X) \right\rbrack = \sum_{i \in I}^{}g\left( x_{i} \right)p\left( x_{i} \right)\quad\text{(discrete)},\quad\quad E\left\lbrack g(X) \right\rbrack = \int x\, f(x)\, dx\quad\text{(continuous)}
$$

$$
\mu = E\lbrack X\rbrack = \sum_{i}^{}x_{i}p\left( x_{i} \right),\quad\quad k\text{-th moment} = E\left\lbrack X^{k} \right\rbrack
$$

For an empirical distribution, $\mu = \sum_{i}^{}x_{i}\frac{N\left( x_{i} \right)}{N_{\text{tot}}} = \frac{\sum_{j \in \text{data}}^{}x_{j}}{N_{\text{tot}}}$ — the ordinary average.

**Linearity of expectation.**

$$
E\lbrack X + Y\rbrack = E\lbrack X\rbrack + E\lbrack Y\rbrack,\quad\quad E\lbrack X + c\rbrack = E\lbrack X\rbrack + c,\quad\quad E\lbrack aX + bY\rbrack = aE\lbrack X\rbrack + bE\lbrack Y\rbrack
$$

*Proof of the first.* $E\lbrack X + Y\rbrack = \sum_{i,j}^{}\left( x_{i} + y_{j} \right)p\left( x_{i},y_{j} \right) = \sum_{i}^{}x_{i}\sum_{j}^{}p\left( x_{i},y_{j} \right) + \sum_{j}^{}y_{j}\sum_{i}^{}p\left( x_{i},y_{j} \right) = E\lbrack X\rbrack + E\lbrack Y\rbrack$, using marginalisation.

> **This holds *always*, with no independence assumption** — the proof above never used one. It is the most useful fact in elementary probability, and the contrast with variance below is the point.

**Product of independent variables.** If $X,Y$ are independent, $E\lbrack XY\rbrack = E\lbrack X\rbrack E\lbrack Y\rbrack$. *Proof:* $\sum_{i,j}^{}x_{i}y_{j}p\left( x_{i},y_{j} \right) = \sum_{i,j}^{}x_{i}y_{j}p\left( x_{i} \right)p\left( y_{j} \right) = E\lbrack X\rbrack E\lbrack Y\rbrack$ — and here the independence is essential, at the factorisation step.

### 6.2.4 Variance and covariance

$$
Var(X) = \sigma^{2} = E\left\lbrack (X - \mu)^{2} \right\rbrack = E\left\lbrack X^{2} \right\rbrack - \left( E\lbrack X\rbrack \right)^{2}
$$

$$
Cov(X,Y) = E\left\lbrack \left( X - E\lbrack X\rbrack \right)\left( Y - E\lbrack Y\rbrack \right) \right\rbrack = E\lbrack XY\rbrack - E\lbrack X\rbrack E\lbrack Y\rbrack
$$

*Derivation of the computational form:* $E\left\lbrack (X - \mu)^{2} \right\rbrack = E\left\lbrack X^{2} - 2\mu X + \mu^{2} \right\rbrack = E\left\lbrack X^{2} \right\rbrack - 2\mu E\lbrack X\rbrack + \mu^{2} = E\left\lbrack X^{2} \right\rbrack - \mu^{2}$. The standard deviation is $\sigma\lbrack X\rbrack = \sqrt{Var\lbrack X\rbrack}$.

**Variance properties.**

$$
Var(X + c) = Var(X),\quad\quad Var(aX) = a^{2}Var(X)
$$

$$
Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)
$$

If $X,Y$ are independent then $Cov(X,Y) = 0$, so $Var(aX + bY) = a^{2}Var(X) + b^{2}Var(Y)$.

> **Independence** $\Rightarrow$ **Cov** $= 0$**, but Cov** $= 0$ $\nRightarrow$ **independence.** The standard counterexample: $X$ uniform on $\{ - 1,0,1\}$ and $Y = X^{2}$. Then $E\lbrack XY\rbrack = E\left\lbrack X^{3} \right\rbrack = 0 = E\lbrack X\rbrack E\lbrack Y\rbrack$, so the covariance vanishes — yet $Y$ is a deterministic function of $X$, about as dependent as two variables can be. Covariance only detects the **linear** part of a dependence. This is exactly the limitation that makes Spearman’s correlation (§7.1) and the non-linearity pitfall of PCA (§8.2) necessary, and it is why the Module 1 claim that orthogonality implies statistical independence is wrong.
>
> **Note also the contrast with expectation:** $E$ is linear unconditionally, while $Var$ adds only when the covariance vanishes. Variance is a *quadratic* functional — hence the $a^{2}$ — which is also why $Var(X + c) = Var(X)$: shifting moves the mean, not the spread.

---
> [[MBD 15 - Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem|← Module 6 – Probability Theory · Foundations, conditioning, Bayes’ theorem]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 17 - Module 6 – Probability Theory · Standard probability distributions|Module 6 – Probability Theory · Standard probability distributions →]]
