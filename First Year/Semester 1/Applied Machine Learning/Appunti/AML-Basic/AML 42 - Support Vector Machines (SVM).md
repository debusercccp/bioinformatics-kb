---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 42
tags: [note, aml]
---

> [[AML 41 - ENSEMBLE – Stacking + Convolutional Neural Networks (CNN)|← ENSEMBLE – Stacking + Convolutional Neural Networks (CNN)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 43 - Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA|Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA →]]

# Support Vector Machines (SVM)

> A Support Vector Machine is another very powerful and versatile class of ML algo:

- capable of performing **linear/nonlinear classification**, regression, even outlier detection

- in particular, well suited for classification of complex but small- or mediumsized datasets

> SVM can be explained as a classifier that fit the widest possible space between the instances of the classes. SVM is a large margin classification that tries to **find the best boundary (hyperplane)** that separates data points of different classes **with the maximum margin**.

- ![[AML-image284.jpg|275]]**Hyperplane**: In 2D, it's a line; in 3D, it's a plane; in higher dimensions, it's called a hyperplane.

- **Margin**: The distance between the hyperplane and the nearest data points from each class. SVM maximizes this.

> **Support Vectors:**

- These are the data points **closest to the hyperplane**.

- They are critical in defining the margin and the optimal hyperplane.

> SVM can be divided into **Hard** and **Soft** margin classification. Hard margin SVM classification strictly impose all instances to be off the Hyperplane. This comes with 2 issues:

- First, it is **very sensitive to outliers** (see Case 1 and Case 2)

- Second, it just only works if the data is **linearly** **separable** (e.g. Case 2, but not Case 1)

![[AML-image285.jpg|642]]

> “Soft” margin **SVM classification**: limiting the margin violations, i.e. look for a trade-off between 1) keeping the street as large as possible (no matter what), and 2) allowing margin violations.
>
> **Regularize SVMs in sklearn**
>
> The sklearn implementation of the SVM class deals with hard vs soft margin classification via the **C hyperparameter**: a small C value leads to a wider street but more margin violations. Generally: if your SVM model shows symptoms of overfitting, you can try regularising it by reducing C.
>
> **SVM choices:**

- **SVC class** instead, i.e. SVC(kernel="linear", C=1) slower with large training sets, not recommended.

- **SGDClassifier class:** applies regular Stochastic Gradient Descent (SGD) to train a linear SVM classifier. It does not converge as fast as the LinearSVC class, but it can be useful to handle huge datasets that do not fit in memory (or even to handle online classification tasks).

- **LinearSVC: t**he LinearSVC class regularises the bias term, so you should centre the training set first by subtracting its mean. This is automatic if you scale the data using the StandardScaler. Make sure you set the loss hyperparameter to “hinge", if you want to run as shown before, as it is not the default value and for better performance you should set the dual hyperparameter to False, unless there are more features than training instances.

![](media/media/image287.jpeg)

> **Non linear SVM Classification**
>
> To tackle nonlinear datasets, we could add more feature, such as polynomial features. Adding polynomial features is simple and works great for all ML algos, the main problems are:

- a too **low polynomial** degree may not deal with very complex datasets

- a too **high polynomial** degree creates a huge nb features, i.e. model training too slow **Kernel Trick** allows to get same result as if you added many polynomial features, even with very highdegree polynomials, without actually having to add them. A kernel is a function capable of computing the dot product ɸ(a)Tɸ(b), based only on the original vectors a and b, without having to compute (or even to know about) the transformation ϕ

> Assume you would need to apply a d=2 polynomial transformation (ɸ) to a 2D training set:
>
> ![](media/media/image2450.jpg)
>
> Kernel functions have a special property that makes it particularly useful in training support vector models, and the use of this property in **optimising non-linear support** vector classifiers → the **kernel trick**.

![[AML-image290.jpg|642]]

> Anything that we need requires ɸ(a)Tɸ(b), for all instances a’s and b’s - which would be heavy to compute but it will eventually yield the same result as (aTb)2, which is much lighter to compute. The function ɸ is an example of a “kernel”: namely, here, a d=2 polynomial kernel

![](media/media/image293.jpeg)

> **Mercer’s theorem**
>
> If a function K(a, b) respects a few mathematical conditions called **Mercer’s conditions** (\*), then there exists a function ϕ that maps a and b into another space (possibly with much higher dimensions) such that K(a, b) = ɸ(a)Tɸ(b). (\*) e.g. K must be continuous and symmetric in its arguments so that K(a, b) = K(b, a)
>
> Note: you can use K as a kernel because Mercer’s theorem tells you that **ϕ exists,** even if you don’t know what ϕ is.

- e.g. **Gaussian RBF kernel**: it can be shown that ϕ exists but maps each training instance to an infinite-dimensional space, so it’s a good thing one doesn’t need to actually perform the mapping!

- e.g. some frequently used kernels (e.g. the Sigmoid kernel) don’t respect all of Mercer’s conditions: yet they generally work well in practice

![](media/media/image297.jpeg)

> **SVM for regression problems**

- Instead of trying to fit the largest possible street between two classes while limiting margin violations, SVM regression tries to fit **as many instances** as possible on the street while limiting margin violations (i.e. in this case instances off the street)

- The width of the street is controlled by a hyperparameter ϵ. Adding more training instances within the margin does not affect the model’s predictions (the model is said to be “ϵinsensitive”)

![[AML-image299.jpg|577]]

---
> [[AML 41 - ENSEMBLE – Stacking + Convolutional Neural Networks (CNN)|← ENSEMBLE – Stacking + Convolutional Neural Networks (CNN)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 43 - Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA|Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA →]]
