---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 15
tags: [note, mbd]
---

> [[MBD 14 - Module 5 – Multivariable Calculus and Optimisation|← Module 5 – Multivariable Calculus and Optimisation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 16 - Module 6 – Probability Theory · Descriptive statistics, moments, covariance|Module 6 – Probability Theory · Descriptive statistics, moments, covariance →]]

# Foundations, conditioning, Bayes’ theorem

### 6.1.1 Why probability

Probability is the language in which hypotheses are judged against data. In biology and bioinformatics this is everywhere: GWAS tests millions of SNPs and every $p$-value is a probability; diagnostic sensitivity, specificity and PPV are conditional probabilities; BLAST E-values, HMM emission probabilities and BLOSUM log-odds scores are all probabilistic; and even genetically identical cells show random variation in mRNA and protein counts.

### 6.1.2 Core concepts

- **Experiment:** a procedure that can be repeated (in principle infinitely) and has a well-defined set of possible outcomes.
- **Sample space** ($C$, $U$ or $S$): the set of all possible outcomes.
- **Event** ($E$): any subset of the sample space.

*Examples.* One coin flip: $C = \{ T,H\}$. Three flips: $C = \{ TTT,HTT,\ldots,HHH\}$, and “majority heads” is the event $\{ HHT,HTH,THH,HHH\}$. Flipping until the first tail: $C = \{ T,HT,HHT,\ldots\}$ — a countably infinite sample space.

*Biological probabilistic phenomena.* Which allele is passed to the offspring (sample space $\{ A,a\}$); whether a given base mutates in one replication (rate $\approx 10^{- 9}$ per site per generation); the number of mRNA molecules transcribed per minute (Poisson-distributed counts).

**Empirical (relative frequency) probability.** $P(E) \approx m/n$ over $n$ repetitions. If allele $A$ appears 340 times among 1,000 chromosomes, $P(A) \approx 0.34$. Over many loci and large populations these frequencies stabilise — Hardy–Weinberg equilibrium.

### 6.1.3 Axioms and set operations

1.  $0 \leq P\left( E_{i} \right) \leq 1$
2.  $P\left( \bigcup E_{i} \right) = 1$ over the entire sample space
3.  **General additivity (union, OR):**

$$
P\left( E_{1} \cup E_{2} \right) = P\left( E_{1} \right) + P\left( E_{2} \right) - P\left( E_{1} \cap E_{2} \right)
$$

- If $E_{1},E_{2}$ are **mutually exclusive** ($E_{1} \cap E_{2} = \varnothing$), then $P\left( E_{1} \cup E_{2} \right) = P\left( E_{1} \right) + P\left( E_{2} \right)$.

> **Why the subtraction is there.** Adding the two probabilities counts the overlap twice; subtracting it once restores the correct total. For three events the pattern continues (inclusion–exclusion): $P(A \cup B \cup C) = \sum P - \sum P\left( \text{pairs} \right) + P(A \cap B \cap C)$.

*Worked example.* Tossing two dice, $P\left( \text{sum even or} \geq 7 \right) = \frac{18}{36} + \frac{21}{36} - \frac{9}{36} = \frac{30}{36}$, the subtracted term being the sums 8, 10, 12 that are both.

### 6.1.4 Joint, marginal and conditional probability

This block is in the slides but absent from the earlier draft; it is the practical core of the module.

A **joint distribution** over two variables is read off a contingency table. Taking parents’ and children’s level of education:

| Child \\ Parent | primary  | high school | degree   | **total** |
|-----------------|----------|-------------|----------|-----------|
| **primary**     | 0.04     | 0.01        | 0.00     | **0.05**  |
| **high school** | 0.06     | 0.24        | 0.05     | **0.35**  |
| **degree**      | 0.05     | 0.30        | 0.25     | **0.60**  |
| **total**       | **0.15** | **0.55**    | **0.30** | **1.00**  |

- **Joint** $P\left( C_{d},P_{d} \right) = 0.25$ — read a single cell.
- **Marginal** $P\left( P_{d} \right) = 0.30$, $P\left( C_{d} \right) = 0.60$ — sum a row or a column. *Marginalising means summing out the variable you do not care about.*
- **Union** $P\left( P_{d} \cup C_{d} \right) = 0.30 + 0.60 - 0.25 = 0.65$; $P\left( P_{p} \cup C_{p} \right) = 0.15 + 0.05 - 0.04 = 0.16$; $P\left( P_{d} \cup C_{p} \right) = 0.30 + 0.05 - 0.00 = 0.35$.
- **Conditional** — divide a cell by the *margin of the conditioning variable*:

$$
P\left( C_{d} \mid P_{p} \right) = \frac{0.05}{0.15} = 0.33,\quad P\left( C_{d} \mid P_{hs} \right) = \frac{0.30}{0.55} = 0.54,\quad P\left( C_{d} \mid P_{d} \right) = \frac{0.25}{0.30} = 0.83
$$

**Conditional probability and independence.**

$$
P\left( E_{1} \mid E_{2} \right) = \frac{P\left( E_{1} \cap E_{2} \right)}{P\left( E_{2} \right)} \Leftrightarrow P\left( E_{1} \cap E_{2} \right) = P\left( E_{1} \mid E_{2} \right)P\left( E_{2} \right)
$$

Conditioning on an event means the total event space shrinks to that event — which is why one divides by its probability.

Two events are **statistically independent** iff $P\left( E_{1} \mid E_{2} \right) = P\left( E_{1} \right)$ **and** $P\left( E_{2} \mid E_{1} \right) = P\left( E_{2} \right)$, which is equivalent to $P\left( E_{1} \cap E_{2} \right) = P\left( E_{1} \right)P\left( E_{2} \right)$.

> **The three quantities, side by side — routinely confused.**

|  | Joint $P(A,B)$ | Marginal $P(A)$ | Conditional $P(A \mid B)$ |
|----|----|----|----|
| Question | how often do both happen? | how often does $A$ happen, regardless of $B$? | among the cases where $B$ happened, how often $A$? |
| From the table | one cell | sum a row/column | cell ÷ margin of $B$ |
| Sums to 1 over | all cells | all values of $A$ | all values of $A$, for fixed $B$ |

> And $P(A \mid B) \neq P(B \mid A)$: see §6.1.6.

*Numerical independence checks (two dice).*

| Statement | $P( \cdot \mid \cdot )$ | $P( \cdot )$ | Independent? |
|----|----|----|----|
| sum $= 10$ given dice equal | $1/6$ | $3/36$ | **No** |
| sum even given dice different | $12/30$ | $18/36$ | **No** |
| dice equal given first is even | $3/18$ | $6/36$ | **Yes** |
| first is even given dice equal | $3/6$ | $18/36$ | **Yes** |

Note that independence is symmetric: the last two rows are the same statement checked from both sides.

### 6.1.5 Odds ratio and log-odds score

$$
odd(A,B) = \frac{P(A,B)}{P(A)P(B)}
$$

If $A$ and $B$ are independent, $odd(A,B) = 1$ and $logodd(A,B) = 0$; values far from 0 in either direction indicate strong dependence. Used in **BLOSUM/PAM substitution matrices** (entries are $\log\left\lbrack P\left( aa_{i} \rightarrow aa_{j} \mid \text{homologs} \right)/P\left( aa_{j} \mid \text{random} \right) \right\rbrack$), in **GWAS logistic regression** (effects reported as log-odds ratios), and in **PWM motif scoring** over a background model.

> **Why the logarithm.** It makes the measure symmetric around zero (so “twice as likely” and “half as likely” are $\pm$ the same number), and it turns the product of independent position scores into a **sum** — which is what makes a PWM or a BLAST alignment score additive along the sequence.

### 6.1.6 Bayes’ theorem

Given a **partition** $\{ B_{i}\}$ of the sample space ($B_{i} \cap B_{j} = \varnothing$ and $\bigcup_{i}B_{i} = S$), the **law of total probability** is

$$
P(A) = \sum_{i}^{}P\left( A,B_{i} \right) = \sum_{i}^{}P\left( A \mid B_{i} \right)P\left( B_{i} \right)
$$

and Bayes’ rule inverts the conditioning:

$$
P\left( B_{i} \mid A \right) = \frac{P\left( A \mid B_{i} \right)P\left( B_{i} \right)}{\sum_{j}^{}P\left( A \mid B_{j} \right)P\left( B_{j} \right)}
$$

In modelling language, relating the **prior** $P(M)$ and the **likelihood** $P(s \mid M)$ to the **posterior** $P(M \mid s)$:

$$
P(M \mid s) = \frac{P(s \mid M)P(M)}{P(s)}
$$

> **The four names, since they are used loosely everywhere.** For data $s$ and model $M$: the **prior** $P(M)$ is what you believed before seeing data; the **likelihood** $P(s \mid M)$ is how well the model explains the data (a function of $M$, *not* a probability distribution over $M$); the **evidence** $P(s)$ is the normalising denominator; the **posterior** $P(M \mid s)$ is the updated belief. Module 6.4 maximises the likelihood alone, which is the same as maximising the posterior under a flat prior.

**Clinical diagnostic example (base-rate fallacy).** Prevalence $P\left( \text{ill} \right) = 10^{- 5}$, sensitivity $P\left( + \mid \text{ill} \right) = 0.99$, false-positive rate $P\left( + \mid \text{healthy} \right) = 0.01$:

$$
P\left( \text{ill} \mid + \right) = \frac{0.99 \times 10^{- 5}}{0.99 \times 10^{- 5} + 0.01 \times \left( 1 - 10^{- 5} \right)} \approx 9.89 \times 10^{- 4}
$$

Less than 0.1%: despite a 99%-sensitive test, a positive result is far more likely to be a false positive, because healthy people vastly outnumber ill ones. **The prior dominates when the base rate is extreme.**

**Prosecutor’s fallacy (“is the Pope an alien?”).** $P\left( \text{Pope} \mid \text{Human} \right) \approx 1/\left( 6 \times 10^{9} \right) \approx 1.7 \times 10^{- 10}$ is tiny, yet $P\left( \text{Human} \mid \text{Pope} \right) \approx 1.0$, because $P\left( \text{Alien} \right) \approx 0$ in the denominator. Confusing the two conditionals is the same error as above.

*Other fallacious inferences of the same type:* “soccer is the most dangerous sport” (most sport accidents occur in soccer — which is also the most played); “private homes as danger spots” (a third of fatal accidents happen at home — where people spend most of their time); and conclusions about groups of drivers drawn without equalising sample sizes.

### 6.1.7 Hardy–Weinberg equilibrium

For a biallelic locus with alleles $A$ (frequency $p$) and $a$ (frequency $q = 1 - p$), random mating is **independent sampling of two alleles from the gene pool**:

$$
P(AA) = p^{2},\quad\quad P(Aa) = 2pq,\quad\quad P(aa) = q^{2},\quad\quad p^{2} + 2pq + q^{2} = 1
$$

The factor 2 in the heterozygote term is because the two parental orders $A \cdot a$ and $a \cdot A$ are distinct and equally likely. These frequencies are constant across generations — a fixed point of the mating map.

Deviations from HWE detect natural selection (sickle-cell trait HbAS, $2pq \approx 0.04$ in malaria-endemic Africa), inbreeding, population stratification, or genotyping error in GWAS quality control. Hardy–Weinberg is the **probabilistic null model** of population genetics: what is informative is the deviation from it.

## Collegamenti
- [[SATAUMV 03 - Hardy-Weinberg equilibrium (HWE)]] — Hardy-Weinberg: probabilità applicata alle popolazioni

---
> [[MBD 14 - Module 5 – Multivariable Calculus and Optimisation|← Module 5 – Multivariable Calculus and Optimisation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 16 - Module 6 – Probability Theory · Descriptive statistics, moments, covariance|Module 6 – Probability Theory · Descriptive statistics, moments, covariance →]]
