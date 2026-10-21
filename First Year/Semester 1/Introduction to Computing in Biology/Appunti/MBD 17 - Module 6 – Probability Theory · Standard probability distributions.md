---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 17
tags: [note, mbd]
---

> [[MBD 16 - Module 6 – Probability Theory · Descriptive statistics, moments, covariance|← Module 6 – Probability Theory · Descriptive statistics, moments, covariance]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 18 - Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions|Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions →]]

# Standard probability distributions

| Distribution | Type | PMF / PDF | $E\lbrack X\rbrack$ | $Var(X)$ | Context |
|----|----|----|----|----|----|
| **Binomial** | discrete, $k = 0,\ldots,n$ | $\binom{n}{k}p^{k}(1 - p)^{n - k}$ | $np$ | $np(1 - p)$ | $k$ successes in $n$ independent trials |
| **Poisson** | discrete, $k \geq 0$ | $\frac{\lambda^{k}e^{- \lambda}}{k!}$ | $\lambda$ | $\lambda$ | rare independent events in a fixed interval |
| **Uniform** | continuous, $a < x < b$ | $\frac{1}{b - a}$ | $\frac{a + b}{2}$ | $\frac{(b - a)^{2}}{12}$ | equal density on $\lbrack a,b\rbrack$ |
| **Normal** | continuous, $x\mathbb{\in R}$ | $\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{- (x - \mu)^{2}/2\sigma^{2}}$ | $\mu$ | $\sigma^{2}$ | CLT; experimental noise |
| **Chi-square** $\chi_{k}^{2}$ | continuous, $y > 0$ | sum of $k$ squared standard normals | $k$ | $2k$ | sample-variance deviations |
| **Student’s** $t_{\nu}$ | continuous, $t\mathbb{\in R}$ | bell-shaped, heavier tails than $N(0,1)$ | $0$ ($\nu > 1$) | $\frac{\nu}{\nu - 2}$ ($\nu > 2$) | testing with unknown variance |
| **Gumbel (EVD)** | continuous | $P(S \geq x) = 1 - exp\left( - Kmne^{- \lambda x} \right)$ | $\mu + \gamma\beta$ | $\frac{\pi^{2}\beta^{2}}{6}$ | maxima; BLAST $p$- and E-values |

> **Gumbel moments (left blank in the slides and in the earlier draft):** $E\lbrack X\rbrack = \mu + \gamma\beta$ with $\gamma \approx 0.5772$ the Euler–Mascheroni constant, and $Var(X) = \pi^{2}\beta^{2}/6 \approx 1.6449\,\beta^{2}$.

### 6.3.1 Binomial: counting without enumerating

*Motivating question:* the probability of exactly 3 tails in 5 fair coin tosses. Total configurations $2^{5} = 32$; configurations with 3 tails: choose 3 of the 5 positions, $5 \times 4 \times 3$ ordered ways, divided by the $3! = 6$ irrelevant orderings, giving $5!/(3!2!) = 10$, hence $f(3) = 10/32$. For a general success probability $p$:

$$
f(k \mid n,p) = \binom{n}{k}p^{k}(1 - p)^{n - k}
$$

*Mean, by direct summation.*

$$
\mu = \sum_{k = 0}^{n}k\binom{n}{k}p^{k}(1 - p)^{n - k} = \sum_{k = 1}^{n}\frac{n!}{(k - 1)!(n - k)!}p^{k}(1 - p)^{n - k} = np\sum_{j = 0}^{n - 1}\binom{n - 1}{j}p^{j}(1 - p)^{n - 1 - j} = np
$$

substituting $j = k - 1$ and recognising the total probability of a Binomial$(n - 1,p)$.

*Variance, via the second moment.* $E\left\lbrack X^{2} \right\rbrack = n(n - 1)p^{2} + np$, so $Var = n(n - 1)p^{2} + np - (np)^{2} = np(1 - p)$.

> **A far shorter route, worth knowing.** A binomial variable is a sum of $n$ independent Bernoulli variables, each with mean $p$ and variance $p(1 - p)$. By linearity of expectation and additivity of variance under independence (§6.2.4), $\mu = np$ and $Var = np(1 - p)$ immediately. Decomposing into independent pieces is almost always easier than summing the series.
>
> **When to use which discrete distribution.** Binomial: a *fixed* number $n$ of trials, counting successes. Poisson: no fixed $n$, counting events in an interval at rate $\lambda$ — it is the limit of the binomial as $n \rightarrow \infty$, $p \rightarrow 0$ with $np = \lambda$ fixed. For the Poisson, mean and variance are **equal**; RNA-seq counts routinely have variance larger than the mean (**overdispersion**), which is why DESeq2 and edgeR use the negative binomial instead.

### 6.3.2 Normal distribution and standardisation

Given $X \sim N\left( \mu,\sigma^{2} \right)$, define $z = \frac{x - \mu}{\sigma}$. Then

$$
E\lbrack z\rbrack = \frac{E\lbrack x\rbrack - \mu}{\sigma} = 0,\quad\quad E\left\lbrack z^{2} \right\rbrack = \frac{E\left\lbrack (x - \mu)^{2} \right\rbrack}{\sigma^{2}} = 1,\quad\quad z \sim N(0,1)
$$

*Worked example 1.* Female heights are $N\left( 63.6,{2.5}^{2} \right)$ inches. $P(X > 70)$: $z = (70 - 63.6)/2.5 = 2.56$; from tables $P(0 < z < 2.56) = 0.4948$, so $P(z > 2.56) = 0.5 - 0.4948 = 0.0052$.

*Worked example 2.* SAT scores are $N\left( 500,150^{2} \right)$. For the top 40%, the cut-off has $P\left( 0 < z < z^{*} \right) = 0.10$, giving $z^{*} = 0.26$ and $x^{*} = 150(0.26) + 500 = 539$.

The **central limit theorem** is why the normal appears everywhere: the sum of many independent random variables with finite means and variances tends to a normal distribution as their number grows, regardless of their individual shapes. Observational error is normally assumed normal for this reason.

### 6.3.3 Chi-square and degrees of freedom

The chi-square distribution with $k$ degrees of freedom is the distribution of a sum of $k$ squared independent standard normals, with mean $k$ and variance $2k$.

> **Correction — the slide conflates two different statements.** The slide writes $Q = \sum_{i = 1}^{N}\left( X_{i} - \mu \right)^{2} \sim \chi_{n - 1}^{2}$. This is wrong twice over: the sum must be divided by $\sigma^{2}$ to be dimensionless, and the degrees of freedom depend on *which centre* is subtracted:
>
> ``` math
> \frac{1}{\sigma^{2}}\sum_{i = 1}^{n}\left( X_{i} - \mu \right)^{2} \sim \chi_{\mathbf{n}}^{2}\quad\quad\text{(true mean }\mu\text{)}
> ```
>
> ``` math
> \frac{1}{\sigma^{2}}\sum_{i = 1}^{n}\left( X_{i} - M \right)^{2} \sim \chi_{\mathbf{n - 1}}^{2}\quad\quad\text{(sample mean }M\text{)}
> ```
>
> *Verified by simulation:* with $n = 8$, $\mu = 3$, $\sigma = 2$ and $2 \times 10^{5}$ replicates, the first quantity has mean $7.996 \approx 8 = n$, the second $7.000 = n - 1$.
>
> **Why one degree of freedom is lost.** The $n$ deviations from the *sample* mean satisfy the identity $\sum_{i}^{}\left( x_{i} - M \right) = 0$ by construction, so only $n - 1$ of them are free; fixing any $n - 1$ determines the last. No such constraint exists for deviations from the true mean $\mu$. This is also exactly why Bessel’s correction divides by $n - 1$ in §6.4, and why the $t$-test on a correlation uses $\nu = n - 2$ in §7.1 — two parameters, slope and intercept, have been estimated.

Consequently, for the unbiased sample variance $S^{2}$,

$$
\frac{(n - 1)S^{2}}{\sigma^{2}} \sim \chi_{n - 1}^{2} \Longrightarrow E\left\lbrack S^{2} \right\rbrack = \frac{\sigma^{2}}{n - 1}E\left\lbrack \chi_{n - 1}^{2} \right\rbrack = \frac{\sigma^{2}}{n - 1}(n - 1) = \sigma^{2}
$$

### 6.3.4 Uniform distribution: proof of mean and variance

For $f(x) = \frac{1}{b - a}$ on $\lbrack a,b\rbrack$:

$$
E\lbrack X\rbrack = \int_{a}^{b}\frac{x}{b - a}dx = \frac{b^{2} - a^{2}}{2(b - a)} = \frac{a + b}{2}
$$

$$
E\left\lbrack X^{2} \right\rbrack = \int_{a}^{b}\frac{x^{2}}{b - a}dx = \frac{b^{3} - a^{3}}{3(b - a)} = \frac{a^{2} + ab + b^{2}}{3}
$$

$$
Var(X) = \frac{a^{2} + ab + b^{2}}{3} - \frac{(a + b)^{2}}{4} = \frac{4a^{2} + 4ab + 4b^{2} - 3a^{2} - 6ab - 3b^{2}}{12} = \frac{(b - a)^{2}}{12}
$$

*Application (buffet example).* Salad weight uniform on $\lbrack 5,15\rbrack$ oz, so $f(x) = 1/10$. Then $P(12 < x < 15) = 3/10 = 0.3$; $P(8 < x < 12) = 4/10 = 0.4$; $P(0 < x < 12) = P(5 < x < 12) = 7/10 = 0.7$, since no mass lies below 5.

---
> [[MBD 16 - Module 6 – Probability Theory · Descriptive statistics, moments, covariance|← Module 6 – Probability Theory · Descriptive statistics, moments, covariance]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 18 - Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions|Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions →]]
