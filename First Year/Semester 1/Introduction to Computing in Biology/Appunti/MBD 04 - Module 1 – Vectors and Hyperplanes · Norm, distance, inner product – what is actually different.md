---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 4
tags: [note, mbd]
---

> [[MBD 03 - Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed|← Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 05 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification →]]

# Norm, distance, inner product: what is actually different

This is the section most often confused. The three objects differ in **arity** (how many vectors they take), in **what they measure**, and in **their axioms**.

### 1.3.1 The hierarchy

$$
\text{inner product}\mspace{6mu} \rightarrow \mspace{6mu}\text{norm}\mspace{6mu} \rightarrow \mspace{6mu}\text{distance}
$$

|  | Inner product $\langle A,B\rangle$ | Norm $\parallel A \parallel$ | Distance $d(A,B)$ |
|----|----|----|----|
| **Arity** | 2 vectors → scalar | **1 vector** → scalar | 2 vectors → scalar |
| **Measures** | alignment, scaled by both lengths | length of **one** object | separation between **two** objects |
| **Sign** | any sign (negative = obtuse angle) | $\geq 0$ always | $\geq 0$ always |
| **Defined from** | primitive | $\parallel A \parallel = \sqrt{\langle A,A\rangle}$ | $d(A,B) = \parallel A - B \parallel$ |
| **Translation** | changes | changes | **invariant**: $d(A + c,B + c) = d(A,B)$ |
| **Biological question** | do these two profiles point the same way? | how much total signal does this sample have? | how different are these two samples? |

In one line: **a norm is about a single vector, a distance is about a pair, and the distance is the norm of the difference.** The inner product is the more primitive object from which both are built — and, unlike them, it carries *directional* information through its sign.

**Explicit formulas and biological meaning**

$$
\parallel A \parallel = \sqrt{\sum_{i}^{}A_{i}^{2}} = \sqrt{\langle A,A\rangle},\quad\quad d(A,B) = \parallel A - B \parallel = \sqrt{\sum_{i}^{}\left( B_{i} - A_{i} \right)^{2}}
$$

$$
c = A \cdot B = \langle A,B\rangle = \sum_{i}^{}A_{i}B_{i} = \parallel A \parallel \, \parallel B \parallel cos\vartheta
$$

- *Norm* measures total transcriptional activity (“global activity”). Two cells can share identical relative expression profiles and still have very different norms, because of cell size, RNA content or sequencing depth.
- *Distance* drives hierarchical clustering in expression space: samples with small $\parallel A - B \parallel$ fall into the same molecular subtype (Luminal A vs Basal breast cancer in TCGA).
- *Inner product* gives the angle, hence **cosine similarity**, which compares two samples independently of sequencing depth.

**Geometric proof of** $\langle A,B\rangle = \parallel A \parallel \parallel B \parallel cos\vartheta$**.** Choose a reference frame in which $B$ is collinear with the $x_{1}$-axis, $B = \left( B_{1},0 \right)^{T}$. The sum reduces to $A_{1}B_{1} = ( \parallel A \parallel cos\vartheta) \parallel B \parallel$.

**Angle and orthogonality**

$$
\vartheta < 90^{\circ} \Leftrightarrow \langle A,B\rangle > 0,\quad\quad\vartheta > 90^{\circ} \Leftrightarrow \langle A,B\rangle < 0,\quad\quad\vartheta = 90^{\circ} \Leftrightarrow \langle A,B\rangle = 0
$$

**No cancellation rule.** Unlike real numbers, $A \cdot B = A \cdot C \nRightarrow B = C$. It only implies $\langle A,B - C\rangle = 0$, i.e. $(B - C)\bot A$.

### 1.3.2 The identity that ties them together

$$
\parallel A - B \parallel^{2} = \parallel A \parallel^{2} + \parallel B \parallel^{2} - 2\langle A,B\rangle
$$

This is the law of cosines. Memorise this one formula and you can move between the three objects at will. Inverting it gives the **polarisation identity**:

$$
\langle A,B\rangle = \frac{1}{4}\left( \parallel A + B \parallel^{2} - \parallel A - B \parallel^{2} \right)
$$

*Check on the running example:* $9 + 25 + 20 = 54$, and indeed $d(A,B) = \parallel (5,2,5)^{T} \parallel = \sqrt{54} \approx 7.348$.

Immediate consequence: if two samples are **orthogonal** then $d^{2} = \parallel A \parallel^{2} + \parallel B \parallel^{2}$ — Pythagoras.

### 1.3.3 The axioms

**Norm axioms.** $\parallel \cdot \parallel :V\mathbb{\rightarrow R}$ is a norm iff

1.  $\parallel X \parallel \geq 0$, and $\parallel X \parallel = 0 \Leftrightarrow X = 0$ (positive definiteness)
2.  $\parallel \lambda X \parallel = |\lambda|\, \parallel X \parallel$ (absolute homogeneity — **note the absolute value**)
3.  $\parallel X + Y \parallel \leq \parallel X \parallel + \parallel Y \parallel$ (triangle inequality)

**Metric axioms.** $d:V \times V\mathbb{\rightarrow R}$ is a metric iff

1.  $d(X,Y) \geq 0$, and $d(X,Y) = 0 \Leftrightarrow X = Y$ (identity of indiscernibles)
2.  $d(X,Y) = d(Y,X)$ (symmetry)
3.  $d(X,Z) \leq d(X,Y) + d(Y,Z)$ (triangle inequality)

**Inner product axioms** (real case).

1.  $\langle X,Y\rangle = \langle Y,X\rangle$ (symmetry)
2.  $\langle X + Y,Z\rangle = \langle X,Z\rangle + \langle Y,Z\rangle$ and $\langle\lambda X,Y\rangle = \lambda\langle X,Y\rangle$ (bilinearity)
3.  $\langle X,X\rangle \geq 0$, with equality **iff** $X = 0$ (positive definiteness)

**The implications only go one way.**

- Every inner product induces a norm, but **not every norm comes from an inner product**. Test: the **parallelogram law** $\parallel X + Y \parallel^{2} + \parallel X - Y \parallel^{2} = 2 \parallel X \parallel^{2} + 2 \parallel Y \parallel^{2}$ holds iff the norm is induced by an inner product (Jordan–von Neumann). $L^{1}$ and $L^{\infty}$ fail it, so there is **no angle, no orthogonality and no cosine similarity** in Manhattan geometry.
- Every norm induces a metric, but **not every metric comes from a norm** — the discrete metric, or any metric on a set with no vector structure, such as a phylogenetic tree distance.

A function failing one axiom gets a weaker name: a **semi-metric** fails the triangle inequality (Bray–Curtis), a **pseudo-metric** allows $d(X,Y) = 0$ for $X \neq Y$, a **quasi-metric** is asymmetric (KL divergence — which is why KL is *not* a distance).

### 1.3.4 Cauchy–Schwarz: why the cosine is well defined

$$
\left| \langle A,B\rangle \right| \leq \parallel A \parallel \cdot \parallel B \parallel
$$

with equality iff $A$ and $B$ are collinear. Dividing both sides is the only reason

$$
\cos\vartheta = \frac{\langle A,B\rangle}{\parallel A \parallel \, \parallel B \parallel}
$$

defines an actual angle, i.e. lands in $\lbrack - 1,1\rbrack$. It is also the reason Pearson’s $r \in \lbrack - 1,1\rbrack$ (§1.3.7). This inequality is absent from the slides and is the single most-used inequality in the course.

*Check:* $| - 10| = 10 \leq 3 \times 5 = 15$, giving $\cos\vartheta = - 2/3$ and $\vartheta \approx {131.81}^{\circ}$.

### 1.3.5 Beyond Euclidean: the family of norms

The Euclidean norm is the case $p = 2$ of the **Minkowski /** $L^{p}$ **family**:

$$
\parallel X \parallel_{p} = \left( \sum_{i = 1}^{n}\left| X_{i} \right|^{p} \right)^{1/p},\quad\quad p \geq 1
$$

| Name | Formula | On $A - B = (5,2,5)^{T}$ | Where it is used |
|----|----|----|----|
| $L^{1}$ (Manhattan) | $\sum_{i}^{}\left| X_{i} \right|$ | $12$ | library size; LASSO penalty; robust to outliers |
| $L^{2}$ (Euclidean) | $\sqrt{\sum_{i}^{}X_{i}^{2}}$ | $\sqrt{54} \approx 7.35$ | default; ridge penalty; PCA; $k$-means |
| $L^{\infty}$ (Chebyshev) | $\max_{i}\left| X_{i} \right|$ | $5$ | worst-case deviation, QC thresholds |
| $L^{0}$ (“pseudo-norm”) | $\#\{ i:X_{i} \neq 0\}$ | $3$ | sparsity count — **not a norm**, violates homogeneity |

**Geometry of the unit balls** (the set $\parallel X \parallel = 1$): $L^{1}$ is a diamond, $L^{2}$ a circle or sphere, $L^{\infty}$ a square or cube. This is the whole explanation of why **LASSO (**$L^{1}$**) produces exact zeros and ridge (**$L^{2}$**) does not** — the diamond has corners on the axes, the circle does not. A direct link to the regularisation of Module 7.

**Weighted and Mahalanobis norms.** Replacing $\sum_{i}^{}X_{i}^{2}$ by $X^{T}MX$ for symmetric positive-definite $M$ still gives a norm. With $M = \Sigma^{- 1}$ (inverse covariance) you get the **Mahalanobis distance**

$$
d_{M}(A,B) = \sqrt{(A - B)^{T}\Sigma^{- 1}(A - B)}
$$

which rescales each direction by its standard deviation and removes correlation between features. It is the correct distance when variables are on different scales or strongly correlated, and it is exactly what a $z$-score generalises to in many dimensions. Used for outlier detection in QC and in LDA.

### 1.3.6 Distances that are not norms of a difference

For count, compositional or binary biological data, Euclidean distance is often the wrong tool.

| Distance | Formula | Data type / use |
|----|----|----|
| Cosine | $1 - cos\vartheta$ | magnitude-free comparison of expression profiles |
| Correlation | $1 - r$ | profile *shape*, scale- and offset-free; co-expression clustering |
| Hamming | $\#\{ i:X_{i} \neq Y_{i}\}$ | sequence comparison, SNP genotypes, binary vectors |
| Jaccard | $1 - |X \cap Y|/|X \cup Y|$ | presence/absence (OTU tables, peak sets) — a true metric |
| Bray–Curtis | $\sum_{i}^{}\left| X_{i} - Y_{i} \right|/\sum_{i}^{}\left( X_{i} + Y_{i} \right)$ | microbiome $\beta$-diversity — **semi-metric** |
| Canberra | $\sum_{i}^{}\left| X_{i} - Y_{i} \right|/\left( \left| X_{i} \right| + \left| Y_{i} \right| \right)$ | counts where low-abundance features still matter |
| Aitchison | Euclidean on CLR-transformed data | compositional data (relative abundances) |
| UniFrac | phylogeny-weighted | microbiome, when taxa relatedness matters |

**Practical rule for choosing.**

- absolute magnitude is biologically meaningful (protein concentration, biomass) → **Euclidean**
- only the *pattern* matters, depth is a nuisance → **cosine** (non-negative profiles) or **correlation** (to remove the offset too)
- presence/absence → **Jaccard**; ecological counts → **Bray–Curtis**; compositions → **Aitchison**
- correlated features on different scales → **Mahalanobis**

> **Curse of dimensionality.** In high $n$, Euclidean distances *concentrate*: the ratio between the farthest and the nearest neighbour tends to 1, so “nearest neighbour” loses meaning. This is why scRNA-seq pipelines build $k$-NN graphs on the top ~50 PCs rather than on 20,000 genes, and why cosine and correlation distances are preferred in high dimensions.

### 1.3.7 The unification: geometry $\mathbf{\leftrightarrow}$ statistics

This is the key insight the slides never state, and it makes Modules 6, 7 and 8 nearly free. Let $\widetilde{X} = X - \bar{X}\mathbf{1}$ be the **mean-centred** vector.

| Geometric object (on centred vectors) | Statistical object |
|----|----|
| $\frac{1}{n - 1}\langle\widetilde{X},\widetilde{Y}\rangle$ | $cov(X,Y)$ |
| $\frac{1}{n - 1} \parallel \widetilde{X} \parallel^{2}$ | $var(X)$ |
| $\frac{1}{\sqrt{n - 1}} \parallel \widetilde{X} \parallel$ | standard deviation $\sigma_{X}$ |
| cosine of the angle between $\widetilde{X}$ and $\widetilde{Y}$ | **Pearson’s** $r$ |
| orthogonality $\langle\widetilde{X},\widetilde{Y}\rangle = 0$ | $r = 0$, i.e. **uncorrelated** |
| Gram matrix of centred data, divided by $n - 1$ | covariance matrix $\Sigma$ |

Consequences worth stating:

- Cauchy–Schwarz on centred vectors *is* the proof that $- 1 \leq r \leq 1$.
- $\Sigma$ is a Gram matrix, hence **symmetric and positive semi-definite**, hence (spectral theorem, Module 3) it has **real non-negative eigenvalues and orthogonal eigenvectors**. This is *why* PCA works and why “variance explained” is never negative.
- For $z$**-scored** vectors ($\parallel \widetilde{X} \parallel^{2} = n$), Euclidean distance and correlation are the same thing up to a monotone transform:

$$
d^{2}(X,Y) = 2n\,\left( 1 - r_{XY} \right)
$$

- So clustering standardised profiles with Euclidean distance **is** clustering by correlation.

### 1.3.8 Cosine similarity vs Pearson correlation — not the same thing

$$
\cos\vartheta = \frac{\langle A,B\rangle}{\parallel A \parallel \parallel B \parallel}\quad\quad\text{vs}\quad\quad r = \frac{\langle\widetilde{A},\widetilde{B}\rangle}{\parallel \widetilde{A} \parallel \parallel \widetilde{B} \parallel}
$$

Pearson’s $r$ is the cosine **after mean-centring**. Cosine removes the effect of scaling (sequencing depth); correlation removes scaling **and** an additive offset (baseline expression).

*The running example makes the difference dramatic:*

- $\cos\vartheta(A,B) = - 2/3 \approx - 0.667$
- centred: $\widetilde{A} = (1/3,\, 1/3,\, - 2/3)^{T}$, $\widetilde{B} = ( - 2/3,\, 7/3,\, - 5/3)^{T}$
- $\langle\widetilde{A},\widetilde{B}\rangle = 5/3$, $\parallel \widetilde{A} \parallel \approx 0.8165$, $\parallel \widetilde{B} \parallel \approx 2.9439$
- $r \approx + 0.6934$

**Same pair of vectors: strongly negative cosine, clearly positive correlation.** Choose deliberately. On non-negative expression data the cosine is almost always positive and therefore less discriminative, which is why correlation is the default in co-expression analysis.

> **Correction to the slides.** The claim that $\langle A,B\rangle = 0$ means the two gene programmes are “statistically independent” is wrong on two counts. Orthogonality equals *uncorrelatedness* only after mean-centring, and uncorrelated does **not** imply independent — as Module 6 itself states correctly. The right statement: orthogonal centred signature vectors are **uncorrelated across samples**.

---
> [[MBD 03 - Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed|← Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 05 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification|Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification →]]
