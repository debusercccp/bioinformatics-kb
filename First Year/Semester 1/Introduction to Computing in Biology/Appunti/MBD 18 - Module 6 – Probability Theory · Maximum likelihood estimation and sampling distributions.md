---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 18
tags: [note, mbd]
---

> [[MBD 17 - Module 6 – Probability Theory · Standard probability distributions|← Module 6 – Probability Theory · Standard probability distributions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 19 - Module 7 – Correlation and Regression|Module 7 – Correlation and Regression →]]

# Maximum likelihood estimation and sampling distributions

Given data $D$ and a parametric model $M$ with parameters $T$, **maximum likelihood** selects

$$
T^{*} = arg\max_{T}P(D \mid T,M) = arg\max_{T}\ln P(D \mid T,M)
$$

the logarithm being legitimate because it is monotonic — and essential in practice, since it turns a product of many small probabilities into a sum, avoiding numerical underflow and making differentiation tractable.

> **Likelihood is not probability.** $P(D \mid T)$ read as a function of $D$ with $T$ fixed is a probability distribution and integrates to 1; read as a function of $T$ with $D$ fixed it is the **likelihood**, and it does *not* integrate to 1 over $T$. ML asks which parameter makes the observed data least surprising — not which parameter is most probable, which would require a prior (§6.1.6).

### 6.4.1 Binomial parameter

Maximising $f(k \mid n,p) = \binom{n}{k}p^{k}(1 - p)^{n - k}$ with respect to $p$:

$$
\frac{df}{dp} = 0 \Longrightarrow kp^{k - 1}(1 - p)^{n - k} - p^{k}(n - k)(1 - p)^{n - k - 1} = 0 \Longrightarrow k(1 - p) - p(n - k) = 0 \Longrightarrow p_{ML} = \frac{k}{n}
$$

The observed frequency — reassuringly, the obvious estimator is the maximum-likelihood one.

### 6.4.2 Normal distribution parameters

The likelihood of $n$ i.i.d. observations is $f\left( X \mid \mu,\sigma^{2} \right) = \prod_{i = 1}^{n}\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{- \left( x_{i} - \mu \right)^{2}/2\sigma^{2}}$, with log-likelihood

$$
\ln f = - \frac{n}{2}\ln(2\pi) - \frac{n}{2}\ln\left( \sigma^{2} \right) - \frac{1}{2\sigma^{2}}\sum_{i = 1}^{n}\left( x_{i} - \mu \right)^{2}
$$

Setting $\partial/\partial\mu = 0$ gives $\sum_{i}^{}\left( x_{i} - \mu_{ML} \right) = 0$, and $\partial/\partial\sigma^{2} = 0$ gives the second:

$$
\mu_{ML} = M = \frac{1}{n}\sum_{i = 1}^{n}x_{i},\quad\quad\sigma_{ML}^{2} = \frac{1}{n}\sum_{i = 1}^{n}\left( x_{i} - M \right)^{2}
$$

### 6.4.3 Bias

$\mu_{ML}$ **is unbiased:** $E\left\lbrack \mu_{ML} \right\rbrack = \frac{1}{n}\sum_{i}^{}E\left\lbrack x_{i} \right\rbrack = \mu$.

$\sigma_{ML}^{2}$ **is biased**, and underestimates $\sigma^{2}$, because the deviations are measured around the *sample* mean $M$ rather than the true $\mu$ — and $M$ sits, by construction, as close to the data as possible:

$$
E\left\lbrack \sigma_{ML}^{2} \right\rbrack = \frac{n - 1}{n}\sigma^{2}
$$

*Sketch of the proof.* Expanding $E\left\lbrack \frac{1}{n}\sum_{i}^{}\left( x_{i} - \frac{1}{n}\sum_{j}^{}x_{j} \right)^{2} \right\rbrack$ and using $E\left\lbrack x_{i}x_{j} \right\rbrack = \mu^{2} + \delta_{ij}\sigma^{2}$ gives $\sigma^{2} + \mu^{2} - \frac{\sigma^{2}}{n} - \mu^{2} = \frac{n - 1}{n}\sigma^{2}$.

**Unbiased sample variance (Bessel’s correction):**

$$
S^{2} = \frac{n}{n - 1}\sigma_{ML}^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\left( x_{i} - M \right)^{2} \Longrightarrow E\left\lbrack S^{2} \right\rbrack = \sigma^{2}
$$

> **The general lesson.** Maximum likelihood is **consistent** (it converges to the truth as $n \rightarrow \infty$) but **not always unbiased** at finite $n$. The two are different guarantees. Here the bias factor $\frac{n - 1}{n}$ is negligible for large $n$ and matters for small samples — precisely the regime of most biological experiments. It is the same lost degree of freedom as in §6.3.3.

### 6.4.4 Distribution of the sample mean

For $n$ i.i.d. $X_{i} \sim N\left( \mu,\sigma^{2} \right)$, the sample mean $M = \frac{1}{n}\sum_{i}^{}x_{i}$ is a linear combination of independent normals, hence itself normal, with

$$
E\lbrack M\rbrack = \mu,\quad\quad Var(M) = \frac{\sigma^{2}}{n}
$$

*Proof of the variance.* $E\left\lbrack M^{2} \right\rbrack = \frac{1}{n^{2}}\sum_{i,j}^{}E\left\lbrack x_{i}x_{j} \right\rbrack = \frac{1}{n^{2}}\sum_{i,j}^{}\left( \mu^{2} + \delta_{ij}\sigma^{2} \right) = \mu^{2} + \frac{\sigma^{2}}{n}$, so $Var(M) = \sigma^{2}/n$.

> **This is the formula behind every error bar.** The **standard error of the mean** is $\sigma/\sqrt{n}$, *not* $\sigma$: the spread of the *estimate* shrinks as $\sqrt{n}$, while the spread of the *data* does not shrink at all. Quadrupling the sample size halves the error bar. Confusing the standard deviation with the standard error is the most common error in figure legends in the biological literature; state which one a bar shows.

## Collegamenti
- [[AML 13 - Logistic Regression · Cost Function]] — cost function logistica = log-verosimiglianza

---
> [[MBD 17 - Module 6 – Probability Theory · Standard probability distributions|← Module 6 – Probability Theory · Standard probability distributions]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 19 - Module 7 – Correlation and Regression|Module 7 – Correlation and Regression →]]
