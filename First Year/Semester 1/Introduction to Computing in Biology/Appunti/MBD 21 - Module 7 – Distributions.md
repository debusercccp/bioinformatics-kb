---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 21
tags: [note, mbd]
---

> [[MBD 20 - Module 6 – Probability|← Module 6 – Probability]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 22 - Module 8 – Exam Exercises – How to Solve Them|Module 8 – Exam Exercises – How to Solve Them →]]

# Module 7 — Distributions

## 7.1 Discrete distributions

Sample space $= \{ x_{1},x_{2},\ldots,x_{n},\ldots\}$, with $p\left( x_{i} \right) = p_{i}$. The probabilities of all the outcomes of an experiment (e.g. tossing a die) can be represented in a **histogram**, with one bar for each value $x_{1},x_{2},x_{3},\ldots,x_{n}$. Probabilities are described with **distributions**; for discrete variables the data take values on a discrete set $\left\{ x_{i},\ i \in I \right\}$:

- **probability distribution:** $f\left( x_{i} \right)$ = probability of the value $x_{i}$;
- **cumulative distribution:** $F\left( x_{i} \right)$ = probability of a value $\leq x_{i}$;
- **normalization:** $\sum_{i \in I}^{}f\left( x_{i} \right) = 1$, $F\left( x_{highest} \right) = 1$.

Experimental data are represented with **normalized histograms**: if the value $x_{i}$ is observed $n\left( x_{i} \right)$ times in $N$ trials, its relative frequency tends to its probability,

$$
\frac{n\left( x_{i} \right)}{N} = F\left( x_{i} \right) \rightarrow p_{i}
$$

## 7.2 Mean and variance

**Mean** (expected value):

$$
\mu = \text{mean} = E\lbrack x\rbrack = \sum_{x_{i} \in SS}^{}x_{i}\, p_{i} = \sum_{x_{i}}^{}\frac{n\left( x_{i} \right)}{N}\, x_{i}
$$

(the second form is the mean of an empirical distribution). More generally, the **expected value of a function** $f(x)$ is

$$
E\left\lbrack f(x) \right\rbrack = \sum_{x_{i} \in SS}^{}f\left( x_{i} \right)\, p_{i}
$$

**Variance** and **standard deviation:**

$$
VAR(x) = E\left\lbrack (x - \mu)^{2} \right\rbrack = E\left\lbrack x^{2} \right\rbrack - \mu^{2} = \sum_{x_{i}}^{}x_{i}^{2}\, p_{i} - \mu^{2},\quad\quad\text{s.d.} = \sigma = \sqrt{VAR}
$$

The second form follows by expanding the square (from the slides):

$$
VAR(x) = E\left\lbrack x^{2} - 2\mu x + \mu^{2} \right\rbrack = E\left\lbrack x^{2} \right\rbrack - 2\mu E\lbrack x\rbrack + \mu^{2} = E\left\lbrack x^{2} \right\rbrack - \mu^{2}
$$

The variance measures how spread the distribution is around $\mu$: **small variance** = the probability is concentrated in a few values close to $\mu$; **high variance** = the probability is spread over many values far from $\mu$.

## 7.3 Binomial distribution

*Fair coin, flipped 5 times.* Each sequence of 5 flips has probability $\left( \frac{1}{2} \right)^{5} = \frac{1}{32}$.

$$
P\left( 0\text{ heads} \right) = P(TTTTT) = \left( \frac{1}{2} \right)^{5}
$$

$P\left( 1\text{ head} \right)$: there are 5 configurations ($HTTTT$, $THTTT$, $TTHTT$, $TTTHT$, $TTTTH$), each with probability $\frac{1}{32}$, so $P\left( 1\text{ head} \right) = 5\left( \frac{1}{2} \right)^{5}$.

$P\left( 2\text{ heads} \right)$: the number of configurations is $\frac{5 \cdot 4}{2} = 10$, so $P\left( 2\text{ heads} \right) = 10\left( \frac{1}{2} \right)^{5}$, where

$$
\frac{5 \cdot 4}{2} = \binom{5}{2} = \frac{5!}{2!\,(5 - 2)!}
$$

$$
P\left( 3\text{ heads} \right) = \binom{5}{3}\left( \frac{1}{2} \right)^{5},\quad\quad\binom{5}{3} = \frac{5!}{3!\, 2!} = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{3 \cdot 2 \cdot 1 \cdot 2 \cdot 1} = 10
$$

$\binom{N}{k}$ is the **binomial coefficient**. *How to count without enumerating (from the slides):* with 5 flips and two possibilities each there are $2^{5} = 32$ configurations in total. To get $k$ heads, choose $k$ of the 5 positions: $5 \times 4 \times \ldots \times (5 - k + 1)$ ordered choices; the order of the choice is irrelevant and $k$ objects have $k!$ permutations, so the number of configurations is $\frac{5!}{k!\,(5 - k)!}$ (e.g. $\frac{5 \times 4 \times 3}{3!} = 10$ for $k = 3$).

*Biased coin,* $p(H) = \frac{1}{4}$, $p(T) = \frac{3}{4}$, flipped 5 times:

$$
P(0\, H) = P(TTTTT) = \left( \frac{3}{4} \right)^{5}
$$

$P(1\, H)$: 5 configurations, $\binom{5}{1} = \frac{5!}{1!\, 4!} = \frac{5 \cdot 4!}{4!} = 5$, each with probability

$$
\underset{p(1\, H)}{\underbrace{\frac{1}{4}}} \cdot \underset{p(4\, T)}{\underbrace{\left( \frac{3}{4} \right)^{4}}}\quad \Rightarrow \quad P(1\, H) = 5 \cdot \frac{1}{4}\left( \frac{3}{4} \right)^{4}
$$

$$
P\left( k\text{ heads} \right) = \binom{N}{k}p_{H}^{k}\left( 1 - p_{H} \right)^{N - k}
$$

**In general:** $N$ independent experiments, $p$ = probability of the single (positive) event:

$$
\boxed{P\left( k\text{ events} \right) = \binom{N}{k}p^{k}(1 - p)^{N - k}}
$$

*Example (genetics).* Two parents $Aa \times Aa$: each child is $aa$ with $p(aa) = \frac{1}{4}$. With 5 children:

$$
P(k\ aa) = \binom{5}{k}\left( \frac{1}{4} \right)^{k}\left( \frac{3}{4} \right)^{5 - k}
$$

### 7.3.1 Mean and variance of the binomial

$$
E\lbrack k\rbrack = np,\quad\quad VAR\lbrack k\rbrack = np(1 - p)
$$

*Example:* $n = 5$, $p = \frac{1}{4}$: $E\lbrack k\rbrack = \frac{5}{4}$, $VAR = 5 \cdot \frac{1}{4} \cdot \frac{3}{4} = \frac{15}{16}$, $\sigma = \sqrt{VAR} = \frac{\sqrt{15}}{4}$.

*Proof of the mean (from the slides).* The $k = 0$ term vanishes; writing $k\binom{n}{k} = n\binom{n - 1}{k - 1}$ and $j = k - 1$:

$$
E\lbrack k\rbrack = \sum_{k = 0}^{n}k\binom{n}{k}p^{k}(1 - p)^{n - k} = np\sum_{j = 0}^{n - 1}\binom{n - 1}{j}p^{j}(1 - p)^{n - 1 - j} = np
$$

since the last sum is the total probability of a binomial with $n - 1$ experiments, i.e. 1. For the variance, computing directly $E\left\lbrack k^{2} \right\rbrack = n(n - 1)p^{2} + np$ gives $VAR\lbrack k\rbrack = E\left\lbrack k^{2} \right\rbrack - \left( E\lbrack k\rbrack \right)^{2} = n(n - 1)p^{2} + np - (np)^{2} = np(1 - p)$.

## 7.4 Poisson distribution

The Poisson distribution is the limit of the binomial for

- $p \rightarrow 0$: **rare events**;
- $n \rightarrow \infty$: **high number of experiments**;

with $pn = \lambda$ (**expected number of events**) fixed:

$$
P(k) = \frac{\lambda^{k}}{k!}e^{- \lambda},\quad\quad\sum_{k = 0}^{\infty}P(k) = 1
$$

where $e^{- \lambda}$ is the **normalization factor**.

$$
E\lbrack k\rbrack = \lambda,\quad\quad VAR\lbrack k\rbrack = \lambda,\quad\quad\sigma = \sqrt{\lambda}
$$

From the slides: the Poisson distribution expresses the probability of a number of events occurring in a fixed period of time, if these events occur with a known average rate $\lambda$ and independently of the time since the last event (it can also be used for the number of events in other intervals, such as distance, area or volume).

*Example:* $\lambda = 30$, $P(k) = \frac{30^{k}}{k!}e^{- 30}$:

$$
P(0) = \frac{30^{0}}{0!}e^{- 30} = e^{- 30}
$$

The distribution has its maximum around $k = 30$ and a longer tail on the right.

## 7.5 Continuous distributions

For a continuous variable, $x \in D\mathbb{\subset R}$, the probability is described by a **probability density function** (p.d.f.) $p(x)$. The probability that $x$ falls in an interval is the area under $p(x)$:

$$
P(a \leq x < b) = \int_{a}^{b}p(x)\, dx
$$

(the probability of a single exact value is 0). The **cumulative probability function** is

$$
F(X) = P(x \leq X),\quad\quad P(a \leq x < b) = P(x < b) - P(x < a) = F(b) - F(a),\quad\quad p(x) = \frac{dF(x)}{dx}
$$

Properties of a p.d.f., $p(x):D\mathbb{\rightarrow R}$:

$$
p(x) \geq 0\quad\forall x \in D,\quad\quad\int_{D}^{}p(x)\, dx = 1\quad\text{(normalization)}
$$

**Mean, expected value, variance:** the sums of the discrete case become integrals,

$$
\mu = E\lbrack x\rbrack = \sum_{x_{i}}^{}x_{i}\, p_{i}\quad \rightarrow \quad\mu = E\lbrack x\rbrack = \int_{D}^{}x\, p(x)\, dx
$$

$$
E\left\lbrack f(x) \right\rbrack = \int_{D}^{}f(x)\, p(x)\, dx
$$

$$
VAR\lbrack x\rbrack = E\left\lbrack (x - \mu)^{2} \right\rbrack = \int_{D}^{}(x - \mu)^{2}p(x)\, dx = \int_{D}^{}x^{2}p(x)\, dx - \mu^{2}
$$

## 7.6 Uniform distribution

On $\lbrack a,b\rbrack$, $p(x) = c$ (and 0 elsewhere). **Normalization:**

$$
\int_{a}^{b}c\, dx = 1\quad \Rightarrow \quad\left. \ c\, x \right|_{a}^{b} = 1\quad \Rightarrow \quad c(b - a) = 1\quad \Rightarrow \quad c = \frac{1}{b - a}
$$

$$
p(x) = \frac{1}{b - a}
$$

($a$ = smallest and $b$ = largest value the variable can assume.)

**Mean:**

$$
\mu = \int_{a}^{b}x\, p(x)\, dx = \int_{a}^{b}\frac{x}{b - a}dx = \frac{1}{b - a}\left. \ \frac{x^{2}}{2} \right|_{a}^{b} = \frac{1}{b - a}\frac{b^{2} - a^{2}}{2} = \frac{b + a}{2}
$$

**Variance:**

$$
VAR\lbrack x\rbrack = E\left\lbrack x^{2} \right\rbrack - \mu^{2} = \int_{a}^{b}x^{2}\frac{1}{b - a}dx - \mu^{2} = \left. \ \frac{x^{3}}{3} \cdot \frac{1}{b - a} \right|_{a}^{b} - \left( \frac{b + a}{2} \right)^{2}
$$

The whiteboard stops here; the slides give the result, $VAR\lbrack x\rbrack = \frac{(b - a)^{2}}{12}$: indeed $\frac{b^{3} - a^{3}}{3(b - a)} = \frac{a^{2} + ab + b^{2}}{3}$ and $\frac{a^{2} + ab + b^{2}}{3} - \frac{(a + b)^{2}}{4} = \frac{a^{2} - 2ab + b^{2}}{12}$.

**Probability of an interval** $\lbrack c,d\rbrack \subset \lbrack a,b\rbrack$ (shaded area of the rectangle of height $\frac{1}{b - a}$):

$$
P(c < x \leq d) = \int_{c}^{d}\underset{p(x)}{\underbrace{\frac{1}{b - a}}}\, dx = \frac{d - c}{b - a}
$$

*Example from the slides (buffet).* The amount of salad taken is uniformly distributed between 5 and 15 ounces: $p(x) = \frac{1}{10}$ for $5 < x < 15$. Then $P(12 < x < 15) = \frac{1}{10} \cdot 3 = 0.3$; $P(8 < x < 12) = \frac{1}{10} \cdot 4 = 0.4$; $P(0 < x < 12) = P(5 < x < 12) = \frac{1}{10} \cdot 7 = 0.7$.

## 7.7 Gaussian (normal) distribution

$$
p(x) = \frac{1}{\sqrt{2\pi\sigma^{2}}}\exp\left\lbrack - \frac{(x - \mu)^{2}}{2\sigma^{2}} \right\rbrack
$$

where $\frac{1}{\sqrt{2\pi\sigma^{2}}}$ is the **normalization** factor:

$$
\int_{- \infty}^{+ \infty}p(x)\, dx = 1
$$

$$
E\lbrack x\rbrack = \int_{- \infty}^{+ \infty}\frac{x}{\sqrt{2\pi\sigma^{2}}}\exp\left\lbrack - \frac{(x - \mu)^{2}}{2\sigma^{2}} \right\rbrack dx = \mu,\quad\quad VAR\lbrack x\rbrack = \int_{- \infty}^{+ \infty}\frac{(x - \mu)^{2}}{\sqrt{2\pi\sigma^{2}}}\exp\left\lbrack - \frac{(x - \mu)^{2}}{2\sigma^{2}} \right\rbrack dx = \sigma^{2}
$$

($\mu$ is the mean and $\sigma^{2}$ the variance; equivalently $E\left\lbrack x^{2} \right\rbrack = \mu^{2} + \sigma^{2}$.)

From the slides: the normal distribution is the most “basic” continuous distribution. By the **central limit theorem**, under certain conditions the sum of a number of random variables with finite means and variances approaches a normal distribution as the number of variables increases. For this reason it is used throughout the natural sciences as a simple model for complex phenomena; e.g. the observational error in an experiment is usually assumed to be normally distributed.

### 7.7.1 Standard normal distribution

The **standard normal distribution** has $\mu = 0$, $\sigma^{2} = 1$. Any normal distribution with $\mu,\sigma^{2}$, $\mathcal{N}\left( x \mid \mu,\sigma^{2} \right)$, is brought to the standard one with the **z-value**

$$
z = \frac{x - \mu}{\sigma},\quad\quad\mathcal{N}(z \mid 0,1)\ \text{(standard)}
$$

Indeed (slides) $E\lbrack z\rbrack = \frac{E\lbrack x\rbrack - \mu}{\sigma} = 0$ and $VAR\lbrack z\rbrack = \frac{VAR\lbrack x\rbrack}{\sigma^{2}} = 1$.

*Example from the slides.* Heights of females are normally distributed with mean 63.6 inches and standard deviation 2.5 inches. Probability that a female selected at random is taller than 70 inches: $z = \frac{70 - 63.6}{2.5} = 2.56$; from the standard normal table $P(0 < z < 2.56) = 0.4948$, so $P(z > 2.56) = 0.5 - 0.4948 = 0.0052$.

## 7.8 Estimating mean and standard deviation from data

Given a sample $x^{1},x^{2},\ldots,x^{N}$ (a histogram of the values), with $x\mathcal{\sim N}\left( x \mid \mu,\sigma^{2} \right)$: how to evaluate $\mu$ and $\sigma^{2}$?

$$
\widetilde{\mu} = \frac{\sum_{i}^{}x^{i}}{N},\quad\quad\widetilde{\sigma} = \sqrt{\frac{\sum_{i}^{}\left( x^{i} - \widetilde{\mu} \right)^{2}}{N - 1}}\quad\text{(unbiased evaluation of the s.d.)}
$$

*Why* $N - 1$ *(from the slides).* The maximum-likelihood estimates (the parameters that maximize the probability of the sampled values) are $\mu_{ML} = \frac{1}{N}\sum_{i}^{}x^{i}$ and $\sigma_{ML}^{2} = \frac{1}{N}\sum_{i}^{}\left( x^{i} - \mu_{ML} \right)^{2}$. $\mu_{ML}$ is unbiased ($E\left\lbrack \mu_{ML} \right\rbrack = \mu$), but $\sigma_{ML}^{2}$ is biased, $E\left\lbrack \sigma_{ML}^{2} \right\rbrack = \frac{N - 1}{N}\sigma^{2}$: it underestimates $\sigma^{2}$, because the deviations are measured from the sample mean instead of the true mean. Dividing by $N - 1$ instead of $N$ corrects the bias.

### 7.8.1 Distribution of the sample mean: error on the mean

Repeat the sampling $M$ times: each sample $x_{j}^{1},x_{j}^{2},\ldots,x_{j}^{N}$ gives a mean $\mu_{j}$ ($\mu_{1},\mu_{2},\ldots,\mu_{M}$). The sample means are distributed around $\mu$, in a peak narrower than the distribution of the data:

$$
x\mathcal{\sim N}\left( x \mid \mu,\sigma^{2} \right)\quad \Rightarrow \quad\widetilde{\mu}\mathcal{\sim N}\left( \widetilde{\mu} \mid \mu,\frac{\sigma^{2}}{N} \right)
$$

**Error on the mean:** $\frac{\sigma}{\sqrt{N}}$, and the result is written $\mu \pm \frac{\sigma}{\sqrt{N}}$.

From the slides: the sample mean is a linear combination of independent, identically distributed normal variables, so it is normally distributed, with $E\lbrack M\rbrack = \mu$ and, using $E\left\lbrack x_{i}x_{j} \right\rbrack = \mu^{2} + \delta_{ij}\sigma^{2}$,

$$
E\left\lbrack M^{2} \right\rbrack = \frac{1}{N^{2}}\sum_{i = 1}^{N}{\sum_{j = 1}^{N}E}\left\lbrack x_{i}x_{j} \right\rbrack = \mu^{2} + \frac{1}{N}\sigma^{2}\quad \Rightarrow \quad var\lbrack M\rbrack = E\left\lbrack M^{2} \right\rbrack - \mu^{2} = \frac{\sigma^{2}}{N}
$$

---
> [[MBD 20 - Module 6 – Probability|← Module 6 – Probability]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 22 - Module 8 – Exam Exercises – How to Solve Them|Module 8 – Exam Exercises – How to Solve Them →]]
