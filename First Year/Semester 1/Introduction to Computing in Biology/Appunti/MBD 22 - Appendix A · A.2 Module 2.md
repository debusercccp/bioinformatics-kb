---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/MBD/ModelingBioData.docx"
order: 22
tags: [note, mbd]
---

> [[MBD 21 - Appendix A · A.1 Module 1|← Appendix A · A.1 Module 1]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 23 - Appendix A · A.3 Module 3|Appendix A · A.3 Module 3 →]]

# A.2 Module 2

### A.2.1 $\mathbf{2}\mathbf{\times}\mathbf{2}$ invertibility (slide 83)

| Matrix | $\det$ | Inverse |
|----|----|----|
| $M_{1} = \begin{pmatrix}
1 & 4 \\
2 & 0
\end{pmatrix}$ | $- 8$ | $\begin{pmatrix}
0 & 1/2 \\
1/4 & - 1/8
\end{pmatrix}$ |
| $M_{2} = \begin{pmatrix}
0 & 4 \\
2 & 0
\end{pmatrix}$ | $- 8$ | $\begin{pmatrix}
0 & 1/2 \\
1/4 & 0
\end{pmatrix}$ |
| $M_{3} = \begin{pmatrix}
1 & 4 \\
2 & 8
\end{pmatrix}$ | $0$ | **not invertible (singular)** — row 2 is twice row 1 |
| $M_{4} = \begin{pmatrix}
1 & 1 \\
1 & - 1
\end{pmatrix}$ | $- 2$ | $\begin{pmatrix}
1/2 & 1/2 \\
1/2 & - 1/2
\end{pmatrix}$ |

Note that $M_{4}^{- 1} = \frac{1}{2}M_{4}$: the matrix is symmetric with $M_{4}^{2} = 2I$, so it is $\sqrt{2}$ times an orthogonal matrix (a reflection).

### A.2.2 $\mathbf{2}\mathbf{\times}\mathbf{2}$ linear systems (slide 87)

**(1)** $x + 2y = 3$, $x - y = 0$. $A = \begin{pmatrix}
1 & 2 \\
1 & - 1
\end{pmatrix}$, $det = - 3 \neq 0$, solvable:

$$
\begin{pmatrix}
x \\
y
\end{pmatrix} = \frac{1}{- 3}\begin{pmatrix}
 - 1 & - 2 \\
 - 1 & 1
\end{pmatrix}\begin{pmatrix}
3 \\
0
\end{pmatrix} = \begin{pmatrix}
1 \\
1
\end{pmatrix} \Longrightarrow x = 1,\ y = 1
$$

**(2)** $- 2x + 2y = 3$, $x - y = 0$. $A = \begin{pmatrix}
 - 2 & 2 \\
1 & - 1
\end{pmatrix}$, $det = 0$. By Rouché–Capelli, $rank(A) = 1 < rank\left( \left\lbrack A|b \right\rbrack \right) = 2$: **inconsistent, no solution**. Directly: $x = y$ forces $0 = 3$.

**(3)** $4x + 2y = 3$, $x + 2y = 0$. $A = \begin{pmatrix}
4 & 2 \\
1 & 2
\end{pmatrix}$, $det = 6 \neq 0$, solvable:

$$
\begin{pmatrix}
x \\
y
\end{pmatrix} = \frac{1}{6}\begin{pmatrix}
2 & - 2 \\
 - 1 & 4
\end{pmatrix}\begin{pmatrix}
3 \\
0
\end{pmatrix} = \begin{pmatrix}
1 \\
 - 1/2
\end{pmatrix} \Longrightarrow x = 1,\ y = - \frac{1}{2}
$$

### A.2.3 $\mathbf{3}\mathbf{\times}\mathbf{3}$ invertibility (slide 102)

The four matrices as printed on the slide:

$A_{1} = \begin{pmatrix}
1 & 0 & 1 \\
1 & 2 & 1 \\
0 & 2 & 0
\end{pmatrix}$**.** Expanding along row 3: $det = - 2(1 \cdot 1 - 1 \cdot 1) = 0$. **Not invertible (singular)**; column 1 equals column 3.

$A_{2} = \begin{pmatrix}
1 & 0 & 0 \\
1 & 2 & 0 \\
0 & 2 & 1
\end{pmatrix}$**.** Lower triangular, $det = 1 \times 2 \times 1 = 2 \neq 0$.

$$
A_{2}^{- 1} = \begin{pmatrix}
1 & 0 & 0 \\
 - 1/2 & 1/2 & 0 \\
1 & - 1 & 1
\end{pmatrix}
$$

$A_{3} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{pmatrix}$**.** Diagonal, $det = 2 \neq 0$, and the inverse of a diagonal matrix just inverts each diagonal entry:

$$
A_{3}^{- 1} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1/2 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

$A_{4} = \begin{pmatrix}
1 & 0 & 1 \\
1 & 2 & 1 \\
0 & 1 & 1
\end{pmatrix}$**.** $det = 1(2 - 1) - 0 + 1(1 - 0) = 2 \neq 0$.

$$
A_{4}^{- 1} = \begin{pmatrix}
1/2 & 1/2 & - 1 \\
 - 1/2 & 1/2 & 0 \\
1/2 & - 1/2 & 1
\end{pmatrix}
$$

*Check:* $A_{4}A_{4}^{- 1} = I$.

### A.2.4 $\mathbf{3}\mathbf{\times}\mathbf{3}$ linear systems (slide 103) — corrected

> **These three solutions differ substantially from the earlier draft.** That draft transcribed the right-hand sides as $b = (0,0,1)^{T}$ for all three systems; the slide in fact gives $b = (3,0,1)^{T}$, $(3,0,1)^{T}$ and $(2,2,1)^{T}$. With the correct data, **two of the three systems are singular, and both turn out to be inconsistent** — so the earlier draft’s determinants ($10$, $- 6$, $- 3$) and its three solution vectors are all wrong.

**System 1.** $x + 2y + z = 3$, $x - y - z = 0$, $3x - z = 1$.

$$
A = \begin{pmatrix}
1 & 2 & 1 \\
1 & - 1 & - 1 \\
3 & 0 & - 1
\end{pmatrix},\quad\quad b = \begin{pmatrix}
3 \\
0 \\
1
\end{pmatrix}
$$

$\det(A) = 1(1 - 0) - 2( - 1 + 3) + 1(0 + 3) = 1 - 4 + 3 = 0$: **singular**, so $x = A^{- 1}b$ is unavailable. Applying Rouché–Capelli: $\operatorname{rank}(A) = 2$, $rank\left( \left\lbrack A|b \right\rbrack \right) = 3$. Since $\operatorname{rank}(A) < rank\left( \left\lbrack A|b \right\rbrack \right)$, the system is **inconsistent — no solution**.

*Seeing it directly:* row 3 $=$ row 1 $+$ 2·row 2 on the left-hand side ($1 + 2 = 3$, $2 - 2 = 0$, $1 - 2 = - 1$), but on the right $3 + 2(0) = 3 \neq 1$. The same linear combination of the equations yields $3 = 1$.

**System 2.** $x + 2y + z = 3$, $x - y = 0$, $3x + z = 1$.

$$
A = \begin{pmatrix}
1 & 2 & 1 \\
1 & - 1 & 0 \\
3 & 0 & 1
\end{pmatrix},\quad\quad b = \begin{pmatrix}
3 \\
0 \\
1
\end{pmatrix}
$$

$\det(A) = 1( - 1 - 0) - 2(1 - 0) + 1(0 + 3) = - 1 - 2 + 3 = 0$: **singular**. $\operatorname{rank}(A) = 2 < rank\left( \left\lbrack A|b \right\rbrack \right) = 3$, so again **inconsistent — no solution**.

*Directly:* row 3 $=$ row 1 $+$ 2·row 2 on the left, giving $3 = 3 + 0 \neq 1$ on the right.

**System 3.** $x + 2y + z = 2$, $x - y + z = 2$, $3x + z = 1$.

$$
A = \begin{pmatrix}
1 & 2 & 1 \\
1 & - 1 & 1 \\
3 & 0 & 1
\end{pmatrix},\quad\quad b = \begin{pmatrix}
2 \\
2 \\
1
\end{pmatrix}
$$

$\det(A) = 1( - 1 - 0) - 2(1 - 3) + 1(0 + 3) = - 1 + 4 + 3 = 6 \neq 0$: **solvable, unique solution**.

$$
A^{- 1} = \begin{pmatrix}
 - 1/6 & - 1/3 & 1/2 \\
1/3 & - 1/3 & 0 \\
1/2 & 1 & - 1/2
\end{pmatrix} \Longrightarrow \begin{pmatrix}
x \\
y \\
z
\end{pmatrix} = A^{- 1}\begin{pmatrix}
2 \\
2 \\
1
\end{pmatrix} = \begin{pmatrix}
 - 1/2 \\
0 \\
5/2
\end{pmatrix}
$$

*Check:* $- \frac{1}{2} + 0 + \frac{5}{2} = 2$ ✓; $- \frac{1}{2} - 0 + \frac{5}{2} = 2$ ✓; $- \frac{3}{2} + \frac{5}{2} = 1$ ✓.

> **Why this exercise set is well designed.** Two systems out of three cannot be solved by matrix inversion at all. The exercise is not really about inverting matrices — it is about recognising when inversion does not apply and reaching for rank instead (§2.5.1). Answering “det $= 0$, therefore no solution” would be *right here by luck*: a singular system can equally well have infinitely many solutions, and only the rank comparison distinguishes the two cases.

---
> [[MBD 21 - Appendix A · A.1 Module 1|← Appendix A · A.1 Module 1]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 23 - Appendix A · A.3 Module 3|Appendix A · A.3 Module 3 →]]
