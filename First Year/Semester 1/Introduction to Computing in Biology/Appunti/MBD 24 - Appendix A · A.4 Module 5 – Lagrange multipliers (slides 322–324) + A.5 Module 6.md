---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 24
tags: [note, mbd]
---

> [[MBD 23 - Appendix A · A.3 Module 3|← Appendix A · A.3 Module 3]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 25 - Appendix B – Master list of corrections|Appendix B – Master list of corrections →]]

# A.4 Module 5 — Lagrange multipliers (slides 322–324)

> *The equations on slides 326–327 are blank placeholders in the deck; the worked box problem is the canonical template.*

**Maximum-volume box with surface area 64 cm².** Maximise $f = xyz$ subject to $g = xy + xz + yz - 32 = 0$.

$$
L = xyz - \lambda(xy + xz + yz - 32)
$$

$$
yz = \lambda(y + z),\quad\quad xz = \lambda(x + z),\quad\quad xy = \lambda(x + y)
$$

Multiplying the first by $x$, the second by $y$ and subtracting gives $z(y - x) = 0$; similarly $y(z - x) = 0$ and $x(z - y) = 0$. No edge can be zero, so $x = y = z$. The constraint then gives $3x^{2} = 32$:

$$
x = y = z = \sqrt{\frac{32}{3}} = \frac{4\sqrt{6}}{3} = 4\sqrt{\frac{2}{3}} \approx 3.266\ \text{cm}
$$

with maximum volume $V = x^{3} \approx 34.84$ cm³ and surface area $6x^{2} = 64$ cm² ✓.

> **Correction.** The earlier draft rendered this answer as “$4\sqrt{3}$” ($\approx 6.93$ cm), which would give a surface area of $6(6.93)^{2} \approx 288$ cm², violating the constraint. The correct value is $\sqrt{32/3} \approx 3.266$ cm.

## A.5 Module 6

### A.5.1 Basic probability, set 1 (slide 347)

**Fair die, one roll** ($S = \{ 1,\ldots,6\}$):

| Event | Outcomes | $P$ |
|----|----|----|
| odd | $\{ 1,3,5\}$ | $3/6 = 1/2$ |
| greater than 4 | $\{ 5,6\}$ | $2/6 = 1/3$ |
| odd **or** prime | $\{ 1,3,5\} \cup \{ 2,3,5\} = \{ 1,2,3,5\}$ | $4/6 = 2/3$ |

(For the third, note $P\left( \text{odd} \right) + P\left( \text{prime} \right) - P\left( \text{both} \right) = \frac{3}{6} + \frac{3}{6} - \frac{2}{6} = \frac{4}{6}$ — the union rule, since 3 and 5 are both.)

**Bag of 6 red, 3 white, 1 blue (total 10):** not white $= 7/10$; blue $= 1/10$; white or blue $= 4/10 = 2/5$; “not red or blue” = white, $3/10$, reading it as *not (red or blue)* — if instead read as *(not red) or blue*, the event is $\{ W,B\}$ and $P = 4/10$. The phrasing is ambiguous; state your reading.

**Class of 23 pupils** (A: 4, B: 8, C: 5, D: 2, hence E $= 23 - 19 = 4$): from B $= 8/23$; from D or E $= 6/23$; from A or C $= 9/23$.

**Bag of 12 balls**, $x$ red, $2x$ white, $3x$ blue, so $6x = 12$ and $x = 2$ (2 red, 4 white, 6 blue): red $= 2/12 = 1/6$; not white $= 8/12 = 2/3$; white or blue $= 10/12 = 5/6$.

### A.5.2 Basic probability, set 2 (slide 348)

**Urn with red and blue only**, $P\left( \text{blue} \right) = 0.30$: $P\left( \text{red} \right) = 1 - 0.30 = 0.70$.

**Mutually exclusive** $A,B,C$ with $P(A) = P(B) = 1/4$, $P(C) = 1/2$: both $A \cup C$ and $B \cup C$ have probability $\frac{1}{4} + \frac{1}{2} = \frac{3}{4}$. (Addition without subtraction is legitimate precisely because the events are mutually exclusive.)

**Sample space** $\{ a,b,c,d\}$ with $P\left( \{ a\} \right) = 1/10$, $P\left( \{ a,b\} \right) = 5/10$, $P\left( \{ a,b,c\} \right) = 7/10$. Then $P(b) = 4/10$, $P(c) = 2/10$, $P(d) = 1 - 7/10 = 3/10$. Since $H = \{ c,d\}$ is the complement of $F = \{ a,b\}$:

$$
P(H) = 1 - P(F) = 1 - \frac{5}{10} = \frac{5}{10} = \frac{1}{2}
$$

### A.5.3 Independence of complements; mutual exclusivity (slides 369, 373)

**Slide 369.** If $A$ and $B$ are independent, so are their complements. By De Morgan,

$$
P(\neg A,\neg B) = P\left( \neg(A \cup B) \right) = 1 - P(A \cup B) = 1 - \left\lbrack P(A) + P(B) - P(A)P(B) \right\rbrack
$$

$$
= \left( 1 - P(A) \right)\left( 1 - P(B) \right) = P(\neg A)P(\neg B)
$$

**Slide 373.** Two events with non-zero probabilities **cannot** be both mutually exclusive and independent: exclusivity requires $P(A \cap B) = 0$, independence requires $P(A \cap B) = P(A)P(B) > 0$. The only way to satisfy both is the trivial case where at least one event has probability 0.

> **These are opposite notions, not similar ones.** Mutually exclusive means *maximally dependent*: knowing $A$ occurred tells you $B$ certainly did not. Independent means knowing $A$ tells you nothing about $B$. They are routinely confused because both licence a simple formula — but one applies to $P(A \cup B)$ and the other to $P(A \cap B)$.

### A.5.4 Bayes’ theorem (slide 384)

**Two urns** ($U_{1}$: 50 red / 50 blue; $U_{2}$: 30 red / 70 blue; $P\left( U_{1} \right) = P\left( U_{2} \right) = 0.5$). A red ball is drawn:

$$
P\left( U_{1} \mid \text{Red} \right) = \frac{0.5 \times 0.5}{(0.5 \times 0.5) + (0.3 \times 0.5)} = \frac{0.25}{0.40} = \frac{5}{8} = 0.625\quad(62.5\%)
$$

**Recession model** ($P(R) = 0.20$, $P\left( \text{Pred} \mid R \right) = 0.80$, $P\left( \text{Pred} \mid \neg R \right) = 0.10$):

$$
P\left( R \mid \text{Pred} \right) = \frac{0.80 \times 0.20}{(0.80 \times 0.20) + (0.10 \times 0.80)} = \frac{0.16}{0.24} = \frac{2}{3} \approx 66.7\%
$$

**Alice’s coins** (fair coin with $P(H) = 0.5$; two-headed coin with $P(H) = 1.0$; priors $0.5$ each). Having obtained heads:

$$
P\left( C_{\text{fair}} \mid H \right) = \frac{0.5 \times 0.5}{(0.5 \times 0.5) + (1.0 \times 0.5)} = \frac{0.25}{0.75} = \frac{1}{3} \approx 33.3\%
$$

**Clinical diagnosis** ($P\left( \text{ill} \right) = 10^{- 5}$, $P\left( + \mid \text{ill} \right) = 0.99$, $P\left( + \mid \text{healthy} \right) = 0.01$):

$$
P\left( \text{ill} \mid + \right) = \frac{0.99 \times 10^{- 5}}{0.99 \times 10^{- 5} + 0.01 \times \left( 1 - 10^{- 5} \right)} \approx 9.890 \times 10^{- 4}\quad\left( \text{under }0.1\% \right)
$$

> **Read the three toy problems together.** In each, the posterior moves away from the prior by a factor given by the likelihood ratio, and the *prior* decides how far it can get. With a 50/50 prior, moderate evidence shifts belief substantially (62.5%, 66.7%, 33.3%). With a prior of $10^{- 5}$, even a 99-to-1 likelihood ratio leaves the posterior under 0.1%. This is the whole of the base-rate fallacy, and the reason rare-disease screening requires a confirmatory second test.

### A.5.5 Uniform distribution: mean and variance (slide 428)

For $f(x) = \frac{1}{b - a}$ on $\lbrack a,b\rbrack$:

$$
E\lbrack X\rbrack = \int_{a}^{b}\frac{x}{b - a}dx = \frac{b^{2} - a^{2}}{2(b - a)} = \frac{(b - a)(b + a)}{2(b - a)} = \frac{a + b}{2}
$$

$$
E\left\lbrack X^{2} \right\rbrack = \int_{a}^{b}\frac{x^{2}}{b - a}dx = \frac{b^{3} - a^{3}}{3(b - a)} = \frac{a^{2} + ab + b^{2}}{3}
$$

$$
Var(X) = E\left\lbrack X^{2} \right\rbrack - \left( E\lbrack X\rbrack \right)^{2} = \frac{a^{2} + ab + b^{2}}{3} - \frac{(a + b)^{2}}{4} = \frac{4a^{2} + 4ab + 4b^{2} - 3a^{2} - 6ab - 3b^{2}}{12} = \frac{(b - a)^{2}}{12}
$$

both factorisations using $b^{n} - a^{n} = (b - a)(\ldots)$.

---
> [[MBD 23 - Appendix A · A.3 Module 3|← Appendix A · A.3 Module 3]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 25 - Appendix B – Master list of corrections|Appendix B – Master list of corrections →]]
