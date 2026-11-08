---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 16
tags: [note, mbd]
---

> [[MBD 15 - Module 4 – Calculus in One Variable · Extreme points|← Module 4 – Calculus in One Variable · Extreme points]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 17 - Module 4 – Calculus in One Variable · Taylor series|Module 4 – Calculus in One Variable · Taylor series →]]

# Numerical approximation of minima (gradient descent)

When $\left. \ \frac{df}{dx} \right|_{x_{0}} = 0$ is not solvable, the minima are found iteratively. Starting from a point $x^{0}$, move against the derivative:

$$
x^{0} \rightarrow x^{1} = x^{0} - \left. \ \frac{df}{dx} \right|_{x^{0}} \cdot \eta \rightarrow x^{2} = x^{1} - \left. \ \frac{df}{dx} \right|_{x^{1}} \cdot \eta \rightarrow x^{3} = x^{2} - \left. \ \frac{df}{dx} \right|_{x^{2}} \cdot \eta \rightarrow \ldots
$$

$\eta$ is the **step** (learning rate). Stop when $\left| \left. \ \frac{df}{dx} \right|_{x^{n}} \right| < \varepsilon$ (small). The procedure goes downhill to the nearest local minimum, so the minimum found depends on the starting point.

The value of the learning rate must be set: too small and the iterations are slow, too large and they can jump over the minimum.

### 4.6.1 Application: training a neuron

A neuron receives an input $x$ through a weight $w$ and gives an output $z$:

$$
a = wx,\quad\quad z = g(a) = \frac{1}{1 + e^{- a}}
$$

*Training set:* $x^{i} \rightarrow d^{i}$ ($M$ examples, $d^{i}$ = desired output). With a random $w$ the neuron gives $x^{i} \rightarrow z\left( x^{i} \right)$, and the error is

$$
E = \frac{1}{2}\sum_{i = 1}^{M}\left( z\left( x^{i} \right) - d^{i} \right)^{2}
$$

*Training procedure:* find the $w$ that minimises $E$ by gradient descent:

$$
w^{0} \rightarrow w^{1} = w^{0} - \left. \ \frac{dE}{dw} \right|_{w^{0}} \cdot \eta,\quad\quad w^{2} = w^{1} - \left. \ \frac{dE}{dw} \right|_{w^{1}} \cdot \eta,\quad\ldots\quad\text{until}\ \left| \frac{dE}{dw} \right| < \varepsilon
$$

*In the slides* the same example is written for a single training pair ($x$ should be associated to $d$), with $E(w) = \frac{1}{2}(z - d)^{2}$ and

$$
\frac{dE}{dw} = \frac{dE}{dz}\frac{dz}{da}\frac{da}{dw} = (z - d) \cdot z(1 - z) \cdot x
$$

The whiteboard version sums this over the $M$ examples of the training set.

*Computing* $dE/dw$ with the chain rule ($x \rightarrow a = wx \rightarrow z = \frac{1}{1 + e^{- a}}$):

$$
\frac{dE}{dw} = \frac{1}{2}\sum_{i = 1}^{M}2\left( z\left( x^{i} \right) - d^{i} \right) \cdot \frac{dz}{da} \cdot \frac{da\left( x^{i} \right)}{dw},\quad\quad\frac{da\left( x^{i} \right)}{dw} = x^{i}
$$

$$
\frac{dz}{da} = \frac{0 \cdot \left( 1 + e^{- a} \right) - 1 \cdot \left( - e^{- a} \right)}{\left( 1 + e^{- a} \right)^{2}} = \frac{e^{- a}}{\left( 1 + e^{- a} \right)^{2}} = \frac{e^{- a} + 1}{\left( 1 + e^{- a} \right)^{2}} - \frac{1}{\left( 1 + e^{- a} \right)^{2}} = \frac{1}{1 + e^{- a}} - \left( \frac{1}{1 + e^{- a}} \right)^{2} = z(1 - z)
$$

## Collegamenti
- [[AML 05 - Univariate Model Regression · Gradient Descent Algorithm]] — gradient descent in ML

---
> [[MBD 15 - Module 4 – Calculus in One Variable · Extreme points|← Module 4 – Calculus in One Variable · Extreme points]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 17 - Module 4 – Calculus in One Variable · Taylor series|Module 4 – Calculus in One Variable · Taylor series →]]
