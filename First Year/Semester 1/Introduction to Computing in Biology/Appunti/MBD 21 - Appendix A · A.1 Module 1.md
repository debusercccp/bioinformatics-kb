---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 21
tags: [note, mbd]
---

> [[MBD 20 - Module 8 – Principal Component Analysis|← Module 8 – Principal Component Analysis]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 22 - Appendix A · A.2 Module 2|Appendix A · A.2 Module 2 →]]

# A.1 Module 1

### A.1.1 Linear combinations (slide 10)

**Given.** $A = \begin{pmatrix}
2 \\
2 \\
3
\end{pmatrix}$, $B = \begin{pmatrix}
 - 1 \\
3
\end{pmatrix}$, $C = \begin{pmatrix}
 - 1 \\
3 \\
4
\end{pmatrix}$, $D = \begin{pmatrix}
 - 1 \\
3 \\
4 \\
0
\end{pmatrix}$, $E = \begin{pmatrix}
1 \\
 - 3 \\
 - 4 \\
0
\end{pmatrix}$.

**Conformability first.** Addition and subtraction require identical dimensions, so only two pairs can be combined: $(A,C)$ in $\mathbb{R}^{3}$ and $(D,E)$ in $\mathbb{R}^{4}$. $B \in \mathbb{R}^{2}$ combines with nothing. Note also $W_{3} = \frac{4}{12} \cdot 12V + \ldots$ reduces to $2V + U$.

**Pair 1:** $V = A$**,** $U = C$ **in** $\mathbb{R}^{3}$**.**

$$
W_{1} = 3A - 2C = \begin{pmatrix}
8 \\
0 \\
1
\end{pmatrix},\quad\quad W_{2} = A + C = \begin{pmatrix}
1 \\
5 \\
7
\end{pmatrix},\quad\quad W_{3} = 2A + C = \begin{pmatrix}
3 \\
7 \\
10
\end{pmatrix}
$$

*With the roles reversed* ($V = C$, $U = A$): $W_{1} = 3C - 2A = ( - 7,5,6)^{T}$, $W_{2} = (1,5,7)^{T}$ (unchanged, addition commutes), $W_{3} = 2C + A = (0,8,11)^{T}$.

**Pair 2:** $V = D$**,** $U = E$ **in** $\mathbb{R}^{4}$**.** Note first that $E = - D$ exactly, which makes everything collapse:

$$
W_{1} = 3D - 2E = 3D + 2D = 5D = \begin{pmatrix}
 - 5 \\
15 \\
20 \\
0
\end{pmatrix},\quad\quad W_{2} = D + E = \begin{pmatrix}
0 \\
0 \\
0 \\
0
\end{pmatrix},\quad\quad W_{3} = 2D + E = D = \begin{pmatrix}
 - 1 \\
3 \\
4 \\
0
\end{pmatrix}
$$

*Reversed:* $3E - 2D = 5E = (5, - 15, - 20,0)^{T}$ and $2E + D = E = (1, - 3, - 4,0)^{T}$.

> **The point of the exercise.** $D$ and $E$ are linearly *dependent* — they span only a line, not a plane — so every combination of them is again a multiple of $D$. The zero result for $W_{2}$ is not an accident of the numbers.

### A.1.2 Norm, scalar product and angle (slide 18)

**Given.** $A = (2,2,1)^{T}$, $B = ( - 3,0, - 4)^{T}$.

$$
\parallel A \parallel = \sqrt{4 + 4 + 1} = \sqrt{9} = 3,\quad\quad \parallel B \parallel = \sqrt{9 + 0 + 16} = \sqrt{25} = 5
$$

$$
\langle A,B\rangle = (2)( - 3) + (2)(0) + (1)( - 4) = - 10
$$

$$
\cos\vartheta = \frac{- 10}{3 \times 5} = - \frac{2}{3} \approx - 0.6667 \Longrightarrow \vartheta = arccos( - 2/3) \approx {131.81}^{\circ} \approx 2.30\ \text{rad}
$$

*Cross-checks:* Cauchy–Schwarz holds, $10 \leq 15$. Distance $d(A,B) = \parallel (5,2,5)^{T} \parallel = \sqrt{54} \approx 7.348$, matching the law of cosines, $9 + 25 + 20 = 54$.

---
> [[MBD 20 - Module 8 – Principal Component Analysis|← Module 8 – Principal Component Analysis]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 22 - Appendix A · A.2 Module 2|Appendix A · A.2 Module 2 →]]
