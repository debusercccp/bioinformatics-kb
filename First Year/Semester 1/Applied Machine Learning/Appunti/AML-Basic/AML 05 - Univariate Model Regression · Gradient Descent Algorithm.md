---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 5
tags: [note, aml]
---

> [[AML 04 - Univariate Model Regression · Minimization and Cost Function|← Univariate Model Regression · Minimization and Cost Function]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 06 - Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum|Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum →]]

# Gradient Descent Algorithm

![[AML-image23.jpg|348]]The gradient descent algorithm is an **ITERATIVE OPTIMIZATION** method used to **<u>minimize a cost function</u>** by **<u>adjusting the parameters of a model</u>**. While it's commonly associated with linear regression, it's a versatile technique applicable to various machine learning models.

While gradient descent is a powerful optimization algorithm, its effectiveness relies on appropriate parameter tuning and understanding the properties of the cost function. In the context of univariate linear regression, gradient descent **facilitates the estimation of the coefficients that best fit the observed data,** enabling predictive modeling and inference.

- **<u>Objective of Gradient Descent</u>**

The primary goal of gradient descent is to **iteratively minimize a cost function by adjusting the parameters θ.** It's crucial to understand that the algorithm aims to find the local minimum of the cost function, which may or may not be the global minimum.

- **<u>Iterative Process</u>**

Gradient descent involves iteratively **updating the parameters θ in the <u>direction of the steepest descent of</u> <u>the cost function</u>** (direction in which the cost function decreases most rapidly).

To understand the steepest descent intuitively, imagine the cost function as a surface with hills and valleys, where the elevation represents the value of the cost function. The steepest descent corresponds to moving downhill along this surface.

The gradient of the cost function indicates the direction of the steepest ascent.

Therefore, **<u>the negative gradient points in the direction of the steepest descent.</u>**

- **Gradient Descent Steps**

Start with initial values for the parameters θ. Calculate the gradient of the cost function with respect to θ. During each iteration of the gradient descent algorithm, the **parameters are adjusted in the direction opposite to the gradient**, effectively moving the model downhill toward lower cost values.

By iteratively updating the parameters in the direction of the negative gradient, the **algorithm seeks to find the local minimum of the cost function**, **where the model achieves the best possible fit to the training data**. This process continues **until:**

- **convergence** criteria are met

- or a **predefined number of iterations** is reached.

- **Choosing the Learning Rate**

The learning rate (often denoted as α) **determines the <u>size of the steps</u> taken during each iteration**.

A carefully chosen learning rate is essential for efficient convergence without overshooting or oscillating around the minimum.

**Convergence and Local Minima**

Gradient descent may converge to a local **minimum**, which **depends on the starting point and the properties of the cost function**. Strategies like momentum, adaptive learning rates, and random restarts can help mitigate issues related to convergence to suboptimal minima.

![[AML-image24.jpg|697]]

The logic of the algorithm revolves around a set of parameters θj (where j represents the index number of a specific feature), which are iteratively adjusted until convergence is achieved. At each iteration, these **parameters** are **updated** **based** **on the partial derivative of the cost function** **with respect to the specific parameters**, **multiplied by a hyperparameter α.**

![[AML-image25.jpg|326]]In this context, *θ* represents the parameters that the algorithm computes, while α serves as a hyperparameter known as the learning rate. The learning rate plays a crucial role in determining the magnitude of parameter updates. If the parameters change significantly, it indicates a large movement in the cost function space. The choice of α dictates the size of the step taken in adjusting the parameters: a larger α leads to more aggressive updates, while a smaller α results in more cautious adjustments.

![[AML-image26.jpg|301]]The iterative process involves **updating the parameters θ <u>simultaneously</u>** **to ensure convergenc**e. This simultaneous update applies to all parameters, whether there are two or more in the model. **It's essential to update all parameters at each iteration before reassigning them.**

Failure to update them simultaneously can lead to convergence issues. For instance, if one parameter is updated based on the newly adjusted value of another parameter, convergence may not be achieved.

## Collegamenti
- [[MBD 14 - Module 5 – Multivariable Calculus and Optimisation]] — gradiente e ottimizzazione multivariata

---
> [[AML 04 - Univariate Model Regression · Minimization and Cost Function|← Univariate Model Regression · Minimization and Cost Function]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 06 - Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum|Univariate Model Regression · GD Implementation – Derivative Term … Local Minimum →]]
