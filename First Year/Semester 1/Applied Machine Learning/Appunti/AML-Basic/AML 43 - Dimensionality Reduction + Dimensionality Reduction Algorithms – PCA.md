---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 43
tags: [note, aml]
---

> [[AML 42 - Support Vector Machines (SVM)|← Support Vector Machines (SVM)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 44 - Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs|Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs →]]

# Dimensionality Reduction

> Real-world applications often face ML practitioners with thousands/ millions of features. The main problem in this case is that it becomes **extremely slow** to train the model, and convergence becomes problematic.
>
> Dimensionality issues are also a problem for **data visualisation**, reducing dimensions to 2 or 3 would allow to plot condensed view of high-dimensional training set, which in turn may allow to gain **insights** by **visually detecting patterns**.
>
> Luckily in many real-world problems, it is possible to reduce the number of features considerably. It is always necessary anyway to consider that reducing dimensionality implies always **losing some information**, attacking the performance. The best idea is to try to train your system with original data before considering using **DR techniques** and consider doing it only if training is indeed too slow.
>
> Visually and numerically is it difficult to consider things in more than 3D. 2 approaches:

- **Projection**

- **Mainfold Learning**

> **Projection**

![[AML-image300.jpg|642]]

> In most real-world problems suffering from high dimensionality, training instances are not spread out uniformly across all dimensions. all training instances actually lie within (or close to) **a much lower-dimensional subspace of the high-dimensional space.** **Manifold Learning** a d-dimensional manifold is a part of an n-dimensional space (d \< n) that locally resembles a d-dimensional hyperplane. The roll: d = 2, n = 3: it locally resembles a 2D plane, but it is rolled in the 3rd dimension.

- “**manifold assumption/hypothesis**”: most real-world high-D datasets lie close to a much lower-D manifold. Very often empirically observed, giving solidity to the approach

- as a result, **manifold learning algos are DR algos that work by modelling the manifold on which the training instances lie**

- the task (classification or regression) **will be simpler if expressed in the lower D space of the manifold** the last assumption could be true but it might not always be the case

![](media/media/image303.jpeg)

> As a result, reducing the dimensionality of a training set before training a model will usually **speed up training**, but it may not always lead to a better or simpler solution: it all depends on the dataset.

## DIMENSIONALITY REDUCTION ALGORITHMS: PCA

> **PCA:PRINCIPAL COMPONENTS ANALYSIS**
>
> It first identifies **the hyperplane that lies closest to the data**, then it projects the data onto it. It is the most popular DR algorithm, it identifies hyperplane closest to the data and project onto it.

![[AML-image305.jpg|609]]

> Axis a in this case, preserves the **max amount of variance**, so it will most likely loose less information. This identifies a **first axis** that accounts for the largest amount of variance in the training set. But it also inherently finds a second axis, orthogonal to the first one, that accounts for the largest amount of remaining variance.
>
> 2D dataset → 1st axis is “a”, 2nd (orthogonal) axis is “c”. D=2 axes.
>
> • higher-D dataset → PCA would also find a third axis, orthogonal to both previous axes, and a fourth, a fifth, and so on - as many as D.
>
> The versor that defines the -ith axis is called the -ith principal component (PC). 2D dataset → the 1st PC is c1, the 2nd PC is c2.

![[AML-image306.jpg|642]]

> **Appling PCA: Singlìular Value Decomposition (SVD)**
>
> SVD is a standard matrix factorisation technique that decomposes the training set matrix (X) into the matrix multiplication of three matrices U Σ VT, where V contains all the PCs I need. compute Xd-projected = X Wd, i.e. the matrix multiplication of the training set matrix X by the matrix Wd, defined as the matrix containing the first d PCs (i.e. the matrix composed of the first d columns of V).

![](media/media/image2580.jpg)

> **PCA implementation in sklearn**
>
> ![[AML-image309.jpg|361]]Sklearn’s PCA class implements PCA using **SVD decomposition**. After fitting the PCA transformer to the dataset, you can access the **principal components** using the *components\_*
>
> *variable* (PCs are horizontal vectors): Sklearn also offers the explained variance ratio of each PC, via the *explained_variance_ratio\_* variable.
>
> Number of dimensions to choose: Instead of arbitrarily choosing the number of dimensions, it is preferable to choose the number of dimensions that add up to a sufficiently large portion of the variance (95%).
>
> Plot explained variance as a function of number dimensions: the elbow is where the explained variance stops growing fast as nb dimensions increases. This can be thought of as the “**intrinsic**” dimensionality of the dataset: reducing dimensionality down to that would not lose too much explained variance.

![[AML-image310.jpg|430]]

> **Randomised PCA**
>
> Finding PCs via SVD can be slow when you need to go from D down to d\<\<D. Randomised PCA is a **stochastic algorithm** able to quickly find an approximation of the first d PCs, with a **reduced computational complexity** w.r.t to the “full SVD” approach. Sklearn’s PCA implementation has a hyper-parameter (*svd_solver*) that can be specifically set to “randomized" to use this also:

![[AML-image311.jpg|642]]

> **Incremental PCA**
>
> Incremental PCA (IPCA) algos have been developed: I can split the training set into **minibatches** and feed an IPCA algo 1 mini-batch at a time.

- similar logic to mini-batch GD

- this is useful for large training sets

- this also applies to online learning, i.e. use of PCA online (i.e. on the fly, as new instances arrive)

## Collegamenti
- [[MBD 20 - Module 8 – Principal Component Analysis]] — PCA: formulazione e algoritmo
- [[MBD 11 - Module 3 · Null space, eigenvalues, eigenvectors]] — autovalori e autovettori

---
> [[AML 42 - Support Vector Machines (SVM)|← Support Vector Machines (SVM)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 44 - Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs|Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs →]]
