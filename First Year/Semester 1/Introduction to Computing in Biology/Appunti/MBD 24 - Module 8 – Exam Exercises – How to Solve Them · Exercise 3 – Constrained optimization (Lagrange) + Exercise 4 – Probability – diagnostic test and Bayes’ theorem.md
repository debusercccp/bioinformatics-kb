---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 24
tags: [note, mbd]
---

> [[MBD 23 - Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimization|← Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimization]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 25 - Module 8 – Exam Exercises – How to Solve Them · Exercise 5 – Distributions or correlation + Checklist for the exam|Module 8 – Exam Exercises – How to Solve Them · Exercise 5 – Distributions or correlation + Checklist for the exam →]]

# Exercise 3 — Constrained optimization (Lagrange)

Typical questions: a) write the constraint as $g(x,y) = 0$; b) Lagrange conditions and $x^{*},y^{*}$; c) the optimal value $f\left( x^{*},y^{*} \right)$. The quantities are amounts or concentrations, so **only positive solutions are accepted**.

**Recipe** (§5.4):

1.  **Constraint:** move everything to the left: e.g. $x^{2} + y^{2} = 8 \Rightarrow g(x,y) = x^{2} + y^{2} - 8 = 0$.
2.  **Lagrange conditions:** $\overrightarrow{\nabla}f = \lambda\overrightarrow{\nabla}g$, i.e. $\frac{\partial f}{\partial x} = \lambda\frac{\partial g}{\partial x}$, $\frac{\partial f}{\partial y} = \lambda\frac{\partial g}{\partial y}$, plus $g = 0$ (equivalently $\mathcal{L =}f - \lambda g$ and all its partial derivatives $= 0$).
3.  **Eliminate** $\lambda$: **divide** the two equations (or **multiply** them, as in the solution keys) to get a relation between $x$ and $y$, e.g. $y^{2} = x^{2}$. If $\lambda^{2} = k$ comes out, keep the sign of $\lambda$ that gives positive $x,y$ and say why the other is discarded (“negative concentration, impossible”).
4.  **Substitute** the relation in the constraint and solve; keep the positive solution.
5.  **Value:** compute $f\left( x^{*},y^{*} \right)$.

**Worked example (Practice 3).** Maximize $f(x,y) = xy$ with $x^{2} + 4y^{2} = 8$.

1)  $g(x,y) = x^{2} + 4y^{2} - 8 = 0$.

2)  $\frac{\partial f}{\partial x} = y = \lambda \cdot 2x$, $\frac{\partial f}{\partial y} = x = \lambda \cdot 8y$. Multiplying: $xy = 16\lambda^{2}xy \Rightarrow \lambda^{2} = \frac{1}{16} \Rightarrow \lambda = \pm \frac{1}{4}$. $\lambda = - \frac{1}{4}$ gives $y = - x/2$ (negative amount, impossible), so $\lambda = \frac{1}{4}$ and $y = 2 \cdot \frac{1}{4}x = \frac{x}{2}$. Constraint: $x^{2} + 4\frac{x^{2}}{4} = 2x^{2} = 8 \Rightarrow x^{*} = 2$, $y^{*} = 1$.

3)  $f(2,1) = 2$.

**Other practice exams:**

| Problem | $g(x,y) = 0$ | Relation | $x^{*},y^{*}$ | Value |
|:---|:---|:---|:---|:---|
| max $xy$, $x^{2} + y^{2} = 8$ (P1) | $x^{2} + y^{2} - 8$ | $y = 2\lambda x$, $x = 2\lambda y \Rightarrow y = x$ | $2,\ 2$ | max 4 |
| min $x^{2} + y^{2}$, $xy = 2$ (P2) | $xy - 2$ | $2x = \lambda y$, $2y = \lambda x \Rightarrow \lambda = 2$, $x = y$ | $\sqrt{2},\ \sqrt{2}$ | min 4 |
| min $x^{2} + 4y^{2}$, $2xy = 1$ (P4) | $2xy - 1$ | $x = \lambda y$, $8y = 2\lambda x \Rightarrow \lambda = 2$, $x = 2y$ | $1,\ 1/2$ | min 2 |
| max $xy$, $x^{2} + y^{2} = 2$ (P5) | $x^{2} + y^{2} - 2$ | $y = x$ | $1,\ 1$ | max 1 |

## 8.4 Exercise 4 — Probability: diagnostic test and Bayes’ theorem

*Bayes’ theorem has not been written on the whiteboard yet; the formulas below are from the slides (6 – Probability) and are the ones used in all the solution keys.*

**Vocabulary.** $D$ = the person has the condition (variant, infection…), $\overline{D}$ = not; $+$ = positive test.

- **Prevalence:** $P(D)$, and $P\left( \overline{D} \right) = 1 - P(D)$.
- **Sensitivity:** $P( + \mid D)$, probability that a sick person tests positive.
- **False positive rate (FPR):** $P\left( + \mid \overline{D} \right)$, probability that a healthy person tests positive.
- **Positive predictive value (PPV):** $P(D \mid + )$, what the exam asks.

**Recipe:**

1.  **Total probability of a positive test** ($D$ and $\overline{D}$ form a partition, slides: $P(A) = \sum_{i}^{}P\left( A \mid B_{i} \right)P\left( B_{i} \right)$):

$$
P( + ) = P( + \mid D)\, P(D) + P\left( + \mid \overline{D} \right)\, P\left( \overline{D} \right)
$$

2.  **Bayes’ theorem** (from $P(D \cap + ) = P( + \mid D)P(D) = P(D \mid + )P( + )$, §6.5):

$$
P(D \mid + ) = \frac{P( + \mid D)\, P(D)}{P( + )}
$$

- The numerator is the first term of $P( + )$ (the **true positives**); the second term of $P( + )$ are the **false positives**.

3.  **Comment** (1 point). Template: *the prevalence is low, so the many healthy people produce a number of false positives comparable to or larger than the true positives; therefore even with high sensitivity most positive results are false (base-rate effect). With high prevalence (e.g. 50%) the same test has a good PPV.*

**Worked example (Practice 1).** $P(V) = 0.01$, $P( + \mid V) = 0.98$, $P\left( + \mid \overline{V} \right) = 0.05$.

1)  $P( + ) = 0.98 \cdot 0.01 + 0.05 \cdot 0.99 = 0.0098 + 0.0495 = 0.0593$.

2)  $P(V \mid + ) = \frac{0.0098}{0.0593} = \frac{98}{593} \approx 0.165 = 16.5\%$.

3)  Prevalence is only 1%: the 99% of non-carriers, even with a 5% false-positive rate, give 0.0495 false positives against 0.0098 true positives, so only about 1 positive in 6 is a real carrier.

**Variant with counts (Practice 4): contingency table.** 2,000 patients, 100 carriers of which 95 positive, 1,900 non-carriers of which 95 positive. Build the table first (fill the missing cells by difference):

|              | Test + | Test − | Total |
|:-------------|:-------|:-------|:------|
| Carriers     | 95     | 5      | 100   |
| Non-carriers | 95     | 1805   | 1900  |
| Total        | 190    | 1810   | 2000  |

Sensitivity $= 95/100 = 0.95$; FPR $= 95/1900 = 0.05$. Then $P\left( \text{carrier} \mid + \right) = \frac{\text{true positives}}{\text{all positives}} = \frac{95}{190} = \frac{1}{2}$: read it directly from the “Test +” column, no formula needed.

**Inverse variant (Practice 5): unknown false positive rate** $f$**.** $P(R) = 1/5$, $P( + \mid R) = 9/10$. a) Write the PPV as a function of $f$:

$$
P(R \mid + ) = \frac{\frac{9}{10} \cdot \frac{1}{5}}{\frac{9}{10} \cdot \frac{1}{5} + f \cdot \frac{4}{5}} = \frac{9/50}{9/50 + 4f/5}
$$

2)  Impose $P(R \mid + ) \geq 9/10$ and solve the inequality for $f$ (the denominator is positive, so cross-multiply without changing the direction): $10 \cdot \frac{9}{50} \geq 9\left( \frac{9}{50} + \frac{4f}{5} \right) \Rightarrow \frac{9}{50} \geq \frac{36f}{5} \Rightarrow f \leq \frac{1}{40} = 2.5\%$.

**Other practice exams:** P2: $P( + ) = 0.95 \cdot 0.005 + 0.03 \cdot 0.995 = 0.0346$, $P(D \mid + ) = 0.00475/0.0346 \approx 13.7\%$. P3: $P( + ) = \frac{4}{5} \cdot \frac{1}{2} + \frac{1}{5} \cdot \frac{1}{2} = \frac{1}{2}$, $P(I \mid + ) = \frac{2/5}{1/2} = \frac{4}{5} = 80\%$ (prevalence 50%: the test discriminates well).

---
> [[MBD 23 - Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimization|← Module 8 – Exam Exercises – How to Solve Them · Exercise 2 – Derivatives and optimization]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 25 - Module 8 – Exam Exercises – How to Solve Them · Exercise 5 – Distributions or correlation + Checklist for the exam|Module 8 – Exam Exercises – How to Solve Them · Exercise 5 – Distributions or correlation + Checklist for the exam →]]
