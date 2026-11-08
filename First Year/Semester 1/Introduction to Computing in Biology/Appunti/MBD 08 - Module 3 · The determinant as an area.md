---
course: "[[Introduction to Computing in Biology]]"
module: "[[Introduction to Modeling of Biological Data]]"
source: "MCB/I_C_in_Biology/ModelingBioData/ModelingBioData.docx"
order: 8
tags: [note, mbd]
---

> [[MBD 07 - Module 3 · Matrices as linear maps + Rotation matrix|← Module 3 · Matrices as linear maps + Rotation matrix]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 09 - Module 3 · Null space|Module 3 · Null space →]]

# The determinant as an area

$A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}$ sends the unit vectors to its columns:

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}\begin{pmatrix}
1 \\
0
\end{pmatrix} = \begin{pmatrix}
a \\
c
\end{pmatrix},\quad\quad\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}\begin{pmatrix}
0 \\
1
\end{pmatrix} = \begin{pmatrix}
b \\
d
\end{pmatrix}
$$

The unit square becomes the parallelogram with vertices $0$, $(a,c)$, $(b,d)$, $(a + b,c + d)$. Its area is the area of the enclosing rectangle minus two pairs of triangles (1: $\frac{1}{2}ac$, 2: $\frac{1}{2}bd$) and two rectangles (3: $bc$):

$$
A = (a + b)(c + d) - 2 \cdot \frac{1}{2}ac - 2 \cdot \frac{1}{2}bd - 2bc = ac + ad + bc + bd - ac - bd - 2bc = ad - bc = \det(A)
$$

The area of the square defined by the basis vectors ($= 1$) is rescaled by the transformation $A$ to an area $= |A|$. In 3D, $|T|$ is the volume of the parallelepiped identified by the transformed basis vectors.

**Non-invertible transformations.** If $|A| = 0$ the transformed area is 0: the basis vectors are sent onto the same line. E.g. $A = \begin{pmatrix}
1 & - 2 \\
 - 1 & 2
\end{pmatrix}$ sends two different vectors to the same vector, $A\begin{pmatrix}
2 \\
0
\end{pmatrix} = A\begin{pmatrix}
0 \\
 - 1
\end{pmatrix} = \begin{pmatrix}
2 \\
 - 2
\end{pmatrix}$, so it is impossible to define the inverse transformation.

---
> [[MBD 07 - Module 3 · Matrices as linear maps + Rotation matrix|← Module 3 · Matrices as linear maps + Rotation matrix]] · [[Introduction to Modeling of Biological Data|↑ Modeling of Biological Data]] · [[MBD 09 - Module 3 · Null space|Module 3 · Null space →]]
