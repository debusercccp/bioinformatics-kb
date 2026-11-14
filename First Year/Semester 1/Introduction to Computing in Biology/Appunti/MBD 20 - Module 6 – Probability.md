---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 20
tags: [note, mbd]
---

> [[MBD 19 - Module 5 – Calculus in More Variables and Optimisation|← Module 5 – Calculus in More Variables and Optimisation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 21 - Module 7 – Distributions|Module 7 – Distributions →]]

# Module 6 — Probability

## 6.1 Experiment, sample space, events

Probability theory is a mathematical model for random phenomena: a phenomenon is probabilistic if the individual outcomes of an experiment are uncertain, but there is a regular distribution of outcomes in a large number of repetitions.

- **Experiment:** any procedure that (1) can be repeated, theoretically, an infinite number of times and (2) has a well-defined set of possible outcomes.
- **Sample space:** the set of all possible outcomes of an experiment.
- **Event:** any subset of the sample space.

*Example (die).* Rolling a die:

$$
\text{sample space} = \{ 1,2,3,4,5,6\},\quad\quad P(x) = \frac{1}{6}\quad\forall x\text{ in the sample space}
$$

*Examples from the slides (coin).* Flip a coin once: the coin can be tossed repeatedly under the same conditions and there are only two possible outcomes, so it is an experiment, with sample space $C = \{ T,H\}$ and events $C_{1} = \{ T\}$, $C_{2} = \{ H\}$. Flip a coin three times: $C = \{ TTT,HTT,THT,TTH,HHT,HTH,THH,HHH\}$; the event “the majority of coins show heads” is $C_{1} = \{ HHT,HTH,THH,HHH\}$.

**What is probability?** As a relative frequency: if an experiment is repeated a large number of times $n$ and the event $E$ occurs $m$ times, the relative frequency $m/n$ is approximately the probability of $E$, $P(E) \approx m/n$.

## 6.2 Probability of an event

The probability of an event is the sum of the probabilities of its outcomes. With the die:

$$
E_{1} = \{ 1,3,5\}\ \left( x\text{ odd} \right):\quad P\left( E_{1} \right) = P(1) + P(3) + P(5) = \frac{1}{2}
$$

$$
E_{2} = \{ 4,5,6\}\ (x \geq 4):\quad P\left( E_{2} \right) = P(4) + P(5) + P(6) = \frac{1}{2}
$$

**Properties of probability:**

1.  $0 \leq P\left( E_{i} \right) \leq 1$: the probability of $E_{i}$ is always a number between 0 and 1;
2.  $P\left( \cup E_{i} \right) = 1$: the sum over all the outcomes $E_{i}$ of the sample space is 1;
3.  additivity (§6.3).

Probabilities can be pictured as areas: $P(A) = \frac{\text{area of }A}{\text{area of }U}$, where $U$ is the sample space; the rest of $U$ is “not $A$”.

## 6.3 Union of two events (OR)

The union of two events, $E_{1}\text{ OR }E_{2} = E_{1} \cup E_{2}$, contains the outcomes that belong to at least one of them. With the die:

$$
P\left( E_{1}\text{ OR }E_{2} \right) = P\left( x\text{ odd OR }x \geq 4 \right) = P\{ 1,3,4,5,6\} = \frac{5}{6}\quad \neq \quad P\left( E_{1} \right) + P\left( E_{2} \right) = 1
$$

The outcome 5 belongs to both events (in the Venn diagram it lies where $E_{1}$ and $E_{2}$ overlap), so summing $P\left( E_{1} \right)$ and $P\left( E_{2} \right)$ counts it twice. It must be subtracted once:

$$
\boxed{P\left( E_{1}\text{ OR }E_{2} \right) = P\left( E_{1} \right) + P\left( E_{2} \right) - P\left( E_{1}\text{ AND }E_{2} \right)}
$$

$$
P\left( E_{1} \cup E_{2} \right) = P\left( E_{1} \right) + P\left( E_{2} \right) - P\left( E_{1} \cap E_{2} \right) = \frac{1}{2} + \frac{1}{2} - P(5) = \frac{5}{6}
$$

The **intersection** $E_{1}\text{ AND }E_{2} = E_{1} \cap E_{2}$ contains the outcomes that belong to both events (here $\{ 5\}$).

If $E_{1}$ and $E_{2}$ are **mutually exclusive** ($E_{1} \cap E_{2} = \varnothing$), the intersection term vanishes and $P\left( E_{1} \cup E_{2} \right) = P\left( E_{1} \right) + P\left( E_{2} \right)$. *Slide example:* rolling two dice, $P\left( \text{sum} = 2 \cup \text{sum} = 3 \right) = \frac{1}{36} + \frac{2}{36} = \frac{3}{36}$.

*Example from the slides (two dice,* $x$ *= sum of the two dice):* the probabilities of the sums $2,3,\ldots,12$ are $\frac{1}{36},\frac{2}{36},\frac{3}{36},\frac{4}{36},\frac{5}{36},\frac{6}{36},\frac{5}{36},\frac{4}{36},\frac{3}{36},\frac{2}{36},\frac{1}{36}$.

$$
P\left( \text{sum even OR sum} \leq 7 \right) = P\left( \text{sum even} \right) + P\left( \text{sum} \leq 7 \right) - P\left( \text{sum} = 2,4,6 \right) = \frac{18}{36} + \frac{21}{36} - \frac{9}{36} = \frac{30}{36}
$$

## 6.4 Independent events

*Coin.* Flipping a coin twice, the probability of two heads is

$$
P(H,H) = \frac{1}{2} \cdot \frac{1}{2}\quad\quad\left( 1^{st}\text{ flip},\ 2^{nd}\text{ flip} \right)
$$

*Die.* With $E_{1} = \{ 1,3,5\}$ and $E_{2} = \{ 4,5,6\}$, the probability of getting $E_{1}$ at the first roll and $E_{2}$ at the second roll is

$$
P\left( E_{1},E_{2} \right) = \frac{1}{2} \cdot \frac{1}{2}\quad\quad\left( 1^{st}\text{ roll},\ 2^{nd}\text{ roll} \right)
$$

The two flips (rolls) do not influence each other: they are **independent events**, and for independent events the probability of the intersection is the product of the probabilities:

$$
P\left( E_{1} \cap E_{2} \right) = P\left( E_{1} \right) \cdot P\left( E_{2} \right)
$$

(in general $P\left( E_{1} \cap E_{2} \right) = P\left( E_{1} \right)P\left( E_{2} \right)$ does **not** hold: it holds only for independent events, see §6.5).

## 6.5 Conditional probability

$$
P\left( E_{2} \mid E_{1} \right)
$$

is the probability of $E_{2}$ **given** $E_{1}$, i.e. knowing that $E_{1}$ has happened. From the slides:

$$
P\left( E_{1} \mid E_{2} \right) = \frac{P\left( E_{1} \cap E_{2} \right)}{P\left( E_{2} \right)},\quad\quad P\left( E_{1} \cap E_{2} \right) = P\left( E_{1} \mid E_{2} \right) \cdot P\left( E_{2} \right)
$$

“Conditioning on an event” means that the new total event space is reduced to that event: this is why we divide by its probability. The second formula computes the joint probability (intersection): assume $E_{2}$ is certain and compute $P\left( E_{1} \mid E_{2} \right)$, then relax the assumption by multiplying by $P\left( E_{2} \right)$.

**Independence.** Two events $E_{1}$ and $E_{2}$ are independent when

$$
P\left( E_{1} \mid E_{2} \right) = P\left( E_{1} \right)\quad\text{and}\quad P\left( E_{2} \mid E_{1} \right) = P\left( E_{2} \right)
$$

both hold: knowing that one happened does not change the probability of the other. Then $P\left( E_{1} \cap E_{2} \right) = P\left( E_{1} \mid E_{2} \right)P\left( E_{2} \right) = P\left( E_{1} \right)P\left( E_{2} \right)$, the product rule of §6.4.

*Example from the slides (two dice):*

| Conditional probability | Unconditional probability | Independent? |
|:---|:---|:---|
| $P\left( \text{sum} = 10 \mid \text{dice equal} \right) = \frac{1}{6}$ | $P\left( \text{sum} = 10 \right) = \frac{3}{36}$ | no |
| $P\left( \text{sum even} \mid \text{dice different} \right) = \frac{12}{30}$ | $P\left( \text{sum even} \right) = \frac{18}{36}$ | no |
| $P\left( \text{dice equal} \mid \text{first even} \right) = \frac{3}{18}$ | $P\left( \text{dice equal} \right) = \frac{6}{36}$ | yes |
| $P\left( \text{first even} \mid \text{dice equal} \right) = \frac{3}{6}$ | $P\left( \text{first even} \right) = \frac{18}{36}$ | yes |

## Collegamenti
- [[SATAUMV 03 - Hardy-Weinberg equilibrium (HWE)]] — Hardy-Weinberg: probabilità applicata alle popolazioni

---
> [[MBD 19 - Module 5 – Calculus in More Variables and Optimisation|← Module 5 – Calculus in More Variables and Optimisation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 21 - Module 7 – Distributions|Module 7 – Distributions →]]
