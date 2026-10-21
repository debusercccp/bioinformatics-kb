---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 2
tags: [note, mbd]
---

> [[MBD 01 - Introduction to Modeling Biological Data|← Introduction to Modeling Biological Data]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 03 - Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed|Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed →]]

# Definitions, biological examples, notation

A **vector space** (or linear space) over a field $F$ is a set $V$ of objects called **vectors** which can be added together and multiplied (“scaled”) by elements of $F$ called **scalars** — typically $\mathbb{R}$, sometimes $\mathbb{C}$. In an $n$-dimensional space a vector is described by an $n$-tuple of real numbers. A vector carries a direction, an orientation and a length.

**Biological representations of vectors**

| $n$ | Object | Entry $A_{i}$ |
|----|----|----|
| 2 | point in the Cartesian plane | coordinate |
| 3 | atom in space | spatial coordinate |
| $\approx 20,000$ | transcriptome / proteome | expression of gene $i$ / abundance of protein $i$ |
| $\approx 1,000$ | metabolome | concentration of metabolite $i$ |
| $\approx 10,000$ | microbiome | OTU count |
| $\binom{L}{2}$ | protein contact map | contact between a residue pair (see correction below) |
| $\approx 90$ | brain connectome | ROI of the AAL atlas |

> **Correction.** The slides give $n = L^{2}$ for the contact map of a protein of length $L$. $L^{2}$ counts *ordered* pairs; the contact map is symmetric with a trivial diagonal, so the number of distinct residue pairs is $\binom{L}{2} = L(L - 1)/2$. The $L^{2}$ figure is the size of the full matrix, not the dimension of the independent description.

**Notation.** A vector is written with an overhead arrow $\overrightarrow{a}$, in boldface $\mathbf{a}$, or as a column array; the row form is its transpose:

$$
A = \begin{pmatrix}
A_{1} \\
A_{2}
\end{pmatrix},\quad\quad A^{T} = \begin{pmatrix}
A_{1} & A_{2}
\end{pmatrix}
$$

**Running example.** Used throughout this module:

$$
A = \begin{pmatrix}
2 \\
2 \\
1
\end{pmatrix},\quad\quad B = \begin{pmatrix}
 - 3 \\
0 \\
 - 4
\end{pmatrix}
$$

---
> [[MBD 01 - Introduction to Modeling Biological Data|← Introduction to Modeling Biological Data]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 03 - Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed|Module 1 – Vectors and Hyperplanes · Vector operations – how they are actually computed →]]
