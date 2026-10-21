---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 7
tags: [note, aml]
---

> [[AML 06 - Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum|← Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 08 - Multivariate Model Regression|Multivariate Model Regression →]]

# Applying GD to Linear Regression

1.  **Hypothesis function**

We start with a hypothesis function *hθ* that predicts the values *y* from the features *x* using a linear equation: *h<sub>θ</sub>*(*x*(*i*)) = *θ*<sub>0</sub> + *θ*<sub>1</sub> ⋅ *<sup>x</sup>*<sub>1</sub>(*i*) + *θ*<sub>2</sub> ⋅ *<sup>x</sup>*<sub>2</sub>(*i*) + … + *θ<sub>n </sub>*⋅ *x<sub>n</sub>*(*i*) (generic, not univariate) where *θ*0,*θ*1, ..., *θn* are the parameters that the gradient descent algorithm aims to optimize.

2.  **Cost Function (J)**

![[AML-image31.png|205]]The cost function J measures the error between the predicted values *hθ*(*x*<sup>(*i*)</sup>) and the true values Y. For linear regression, a common cost function is the Mean Squared Error (MSE):

> *i*=1

where:

- *m* is the number of training examples

- *h<sub>θ</sub>*(*x*(*i*<sup>)</sup>) is the predicted value for the i-th example

- *Y*<sup>(*i*)</sup>is the true value for the i-th example

**3. Gradient Descent Update**

The gradient descent algorithm updates the parameters iteratively to minimize the cost function. This involves computing the partial derivatives of J with respect to each parameter *θj* and simultaneously updating all parameters:

$$
\theta_{j}: = \theta_{j} - \alpha\frac{\partial}{\partial\theta_{j}}J(\theta)
$$

4.  **Partial Derivatives of the Cost Function**

The partial derivatives of J with respect to the parameters *θj* are computed to determine the direction and magnitude of the parameter updates. These derivatives indicate how much the cost function would change with a small change in each parameter:

> 
> ``` math
> \frac{\partial}{\partial\theta_{j}}J(\theta) = \frac{1}{m}\sum_{i = 1}^{m}\left( h_{\theta}\left( x^{(i)} \right) - y^{(i)} \right)x_{j}^{(i)}
> ```

This derivative is then used in the update rule to adjust the parameters.

5.  **Simultaneous Parameter Update**

The parameters *θ*0,*θ*1,…,*θn* are updated simultaneously using the computed derivatives and the learning rate. This process is repeated iteratively until convergence, gradually reducing the cost function and optimizing the parameters for the linear regression model.

![](media/media/image304.jpg)

Gradient Descent applied to linear regression is guaranteed to converge to the global optimum due to the convexity of the cost function, provided that an appropriate learning rate is chosen.

This property makes Gradient Descent a reliable optimization method for linear regression models.

- Susceptibility to Local Optima

One of the properties of Gradient Descent is its susceptibility to local optima.

Depending on the initial parameter values, the algorithm may converge to different local optima instead of the global optimum.

- Convex Quadratic Cost Function for Linear Regression

In the case of linear regression, the cost function is always a convex quadratic function, meaning it has "bowshaped" curve.

This convexity ensures that the cost function has only one global optimum and no other local optima.

- **<u>Convergence to Global Optimum</u>**

Because the cost function for **linear regression is convex,** Gradient Descent on this type of cost function will **always converge to the global optimum**. Unlike other optimization problems where multiple local optima may exist, in linear regression, there's only one optimal solution, and Gradient Descent will reliably find it.

- Importance of Learning Rate

It's important to note that the convergence to the global optimum is subject to the choice of the learning rate. If the learning rate is too large, Gradient Descent may overshoot the minimum and fail to converge. Therefore, it's essential to choose a suitable learning rate to ensure convergence to the global optimum.

![[AML-image35.jpg|433]]

![](media/media/image3310.jpg)

## 3.8 BATCH GRADIENT DESCENT (BGD)

Starting from our initialization and the first parameter θ, we iteratively update the parameters using Gradient Descent until the line of our hypothesis best fits our data.

Understanding Gradient Descent (GD) for linear regression: Essentially, we begin with an initial guess for our hypothesis, then refine it by repeatedly applying GD equations tailored for linear regression.

This iterative process gradually improves the accuracy of our hypothesis.

This algorithm is commonly known as **batch Gradient Descent (BGD)** and **considers the entire batch (all training examples**) in each step of the algorithm.

This means that when computing the derivatives to update parameters, **we sum over all training examples i from 1 to m, where m is the number of training examples.**

This approach ensures that we make informed updates to the parameters by considering the collective information from all data points.

While batch Gradient Descent is a widely used approach for optimizing linear regression models, it's essential to be aware of alternative methods and their respective advantages and disadvantages.

Each method offers a unique perspective on the optimization process and may be more suitable depending on the specific characteristics of the dataset and the problem at hand.

An alternative to using Gradient Descent (GD) for finding the minimum of the cost function in linear regression is the **Normal Equation method.**

The Normal Equation method provides a direct **analytical solution** for finding the optimal parameters that minimize the cost function Jin linear regression. Rather than iteratively updating parameters as in GD, the Normal Equation computes the optimal parameter values directly. Mathematically, the Normal Equation is given by: *θ* = (*X<sup>T</sup> X*)<sup>−1</sup>*X<sup>T</sup>y*

Where:

- *θ* is the vector of parameters (including the intercept term if applicable).

- X is the matrix of input features. - Y is the vector of target values.

This equation yields the optimal parameter values that minimize the cost function J without requiring iterative updates. It provides a computationally efficient alternative to GD, especially for smaller datasets where the inverse operation (*XT X*)−1is feasible.

The Normal Equation method is particularly useful when:

- The dataset is not too large

- Features are not highly correlated, as in such cases, the matrix inversion is stable and efficient

However, for very large datasets, the computational cost of matrix inversion can be prohibitive, and GD or its variants may be more practical.

## Collegamenti
- [[MBD 14 - Module 5 – Multivariable Calculus and Optimisation]] — gradiente di funzioni di più variabili
- [[MBD 09 - Module 2 – Matrices and Linear Systems · Linear systems Ax=b]] — soluzione in forma chiusa di Ax=b / minimi quadrati

---
> [[AML 06 - Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum|← Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 08 - Multivariate Model Regression|Multivariate Model Regression →]]
