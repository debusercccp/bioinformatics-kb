---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 3
tags: [note, mbd]
---

> [[MBD 02 - Module 1 – Vectors and Hyperplanes · Definitions, biological examples, notation|← Module 1 – Vectors and Hyperplanes · Definitions, biological examples, notation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 04 - Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different|Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different →]]

# Vector operations — how they are actually computed

All the operations below are **component-wise**, except the inner product, which collapses to a scalar. The recipe is always: *align the components by index, apply the rule, done.*

### 1.2.1 The basic operations

| Operation | Recipe (component $i$) | Input → Output | Worked example |
|----|----|----|----|
| Scalar multiplication | $(\lambda A)_{i} = \lambda A_{i}$ | vector + scalar → vector | $3A = (6,6,3)^{T}$ |
| Addition | $(A + B)_{i} = A_{i} + B_{i}$ | 2 vectors → vector | $A + B = ( - 1,2, - 3)^{T}$ |
| Difference | $(A - B)_{i} = A_{i} - B_{i}$ | 2 vectors → vector | $A - B = (5,2,5)^{T}$ |
| Inner (dot) product | $\langle A,B\rangle = \sum_{i}^{}A_{i}B_{i}$ | 2 vectors → **scalar** | $- 6 + 0 - 4 = - 10$ |
| Hadamard (element-wise) product | $(A \odot B)_{i} = A_{i}B_{i}$ | 2 vectors → vector | $( - 6,0, - 4)^{T}$ |

**Conformability.** Addition, subtraction, Hadamard product and inner product require *the same dimension* $n$. Scalar multiplication never does. There is no vector division, and no element-wise division unless explicitly defined (used in practice for fold-changes, $\log(A \oslash B)$).

**Biological meaning of the three original operations**

- **Scalar multiplication — library-size normalisation.** Multiplying raw read counts by $10^{6}/\text{total reads}$ yields **CPM** (counts per million), making samples of different sequencing depth comparable. RPKM and TPM apply the same logic with an additional gene-length scaling.
- **Addition — merging signals.** Adding two RNA-seq profiles merges expression signals. Bulk RNA-seq of a tissue is the weighted sum of its constituent cell-type expression vectors.
- **Difference — differential expression.** Tumour vector minus normal vector. Positive components are up-regulated genes, negative components down-regulated ones.

> **Note on the Hadamard product.** Absent from the slides, but it is what you actually write in code (`a * b` in NumPy) and what gives log-fold-changes gene by gene. Do not confuse it with the dot product (`a @ b` / `np.dot`), which returns a single number.

### 1.2.2 Vector space axioms

For all $u,v,w \in V$ and scalars $a,b \in F$:

| Axiom | Statement |
|----|----|
| Associativity of addition | $u + (v + w) = (u + v) + w$ |
| Commutativity of addition | $u + v = v + u$ |
| Additive identity | there is $0 \in V$ with $v + 0 = v$ |
| Additive inverse | for every $v$ there is $- v$ with $v + ( - v) = 0$ |
| Compatibility of scalar multiplication | $a(bv) = (ab)v$ |
| Scalar identity | $1v = v$ |
| Distributivity over vector addition | $a(u + v) = au + av$ |
| Distributivity over field addition | $(a + b)v = av + bv$ |

### 1.2.3 Linear combination, span, independence, basis

This block is **missing from the slides**, and every later module — change of basis, eigenvectors, diagonalisation, PCA — depends on it.

- **Linear combination** of $v_{1},\ldots,v_{k}$ with scalars $c_{1},\ldots,c_{k}$:

$$
w = c_{1}v_{1} + c_{2}v_{2} + \ldots + c_{k}v_{k}
$$

- *How to compute:* scale each vector, then add component by component.

<!-- -->

- **Span.** $span\{ v_{1},\ldots,v_{k}\}$ is the set of **all** linear combinations. Geometrically a line (one vector), a plane (two independent vectors), and so on.

- **Linear independence.** $v_{1},\ldots,v_{k}$ are independent iff

$$
c_{1}v_{1} + \ldots + c_{k}v_{k} = 0 \Longrightarrow c_{1} = \ldots = c_{k} = 0,
$$

- i.e. no vector is a combination of the others. *How to test:* stack them as columns of a matrix $M$ and check $\det(M) \neq 0$ (square case) or $\operatorname{rank}(M) = k$ (general case).

<!-- -->

- **Basis.** A set that is independent *and* spans the space. Every vector then has **unique** coordinates in it. The **standard basis** of $\mathbb{R}^{n}$ is $e_{1} = (1,0,\ldots,0)^{T},\ldots,e_{n} = (0,\ldots,0,1)^{T}$, so $A = \sum_{i}^{}A_{i}e_{i}$.

- **Dimension** = number of basis vectors = $n$.

> *Biological reading.* A bulk RNA-seq profile is approximately a linear combination of cell-type reference profiles, the coefficients $c_{i}$ being cell-type proportions. **Deconvolution** (CIBERSORT, MuSiC) is exactly the problem of recovering the $c_{i}$ given $w$ and the basis. Independence of the reference profiles is what makes the solution unique.

### 1.2.4 Normalisation: producing a unit vector

$$
\widehat{A} = \frac{A}{\parallel A \parallel},\quad\quad \parallel \widehat{A} \parallel = 1
$$

*Steps:* compute the norm, then divide every component by it. Example: $\parallel A \parallel = 3 \Rightarrow \widehat{A} = (2/3,\, 2/3,\, 1/3)^{T}$.

This is the geometric counterpart of library-size normalisation. Note *which* norm is used: CPM divides by the $L^{1}$ norm (total counts), cosine similarity by the $L^{2}$ norm.

### 1.2.5 Projection and orthogonal decomposition

Missing from the slides, but it is the computational core of §1.4 (hyperplanes), of Gram–Schmidt, and of PCA scores.

- **Scalar projection** (signed length of $A$ along $B$):

$$
p = \frac{\langle A,B\rangle}{\parallel B \parallel} = \parallel A \parallel cos\vartheta
$$

- **Vector projection** (the component of $A$ along $B$):

$$
{proj}_{B}(A) = \frac{\langle A,B\rangle}{\parallel B \parallel^{2}}\, B
$$

- **Orthogonal residual:** $A_{\bot} = A - {proj}_{B}(A)$, which satisfies $\langle A_{\bot},B\rangle = 0$.

*Worked example.* ${proj}_{B}(A) = \frac{- 10}{25}( - 3,0, - 4)^{T} = (1.2,\, 0,\, 1.6)^{T}$, of norm $2 = |p|$. The sign $p = - 2$ says $A$ leans *against* $B$. Residual $A_{\bot} = (0.8,\, 2,\, - 0.6)^{T}$, and indeed $\langle A_{\bot},B\rangle = - 2.4 + 0 + 2.4 = 0$.

> *Why it matters.* A **PC score** is nothing but the scalar projection of a sample onto a unit eigenvector ($y_{i} = \langle x,u_{i}\rangle$, with $\parallel u_{i} \parallel = 1$ so no denominator appears). Regressing out a covariate — batch, cell cycle — is subtracting a projection.

### 1.2.6 Operations that exist only in specific dimensions

- **Cross product** ($\mathbb{R}^{3}$ only): $A \times B$ is orthogonal to both, with $\parallel A \times B \parallel = \parallel A \parallel \parallel B \parallel sin\vartheta$. Used for molecular geometry — dihedral angles, chirality, normals to a peptide plane — not for omics data.
- **Outer product** (any dimensions): $AB^{T} \in \mathbb{R}^{m \times n}$, a matrix of rank 1 (Module 2). The dot product contracts, the outer product expands.

---
> [[MBD 02 - Module 1 – Vectors and Hyperplanes · Definitions, biological examples, notation|← Module 1 – Vectors and Hyperplanes · Definitions, biological examples, notation]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 04 - Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different|Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different →]]
