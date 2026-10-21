---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 9
tags: [note, aml]
---

> [[AML 08 - Multivariate Model Regression|← Multivariate Model Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 10 - Classification|Classification →]]

# Polynomial Regression

Now that we've covered linear regression with multiple variables, let's delve into the power of feature selection and engineering, particularly in the context of polynomial regression. When a linear hypothesis is not enough to fit the dataset, a possible solution is to use a polynomial function

The question arises: should we use existing features or create new ones? It's essential not to assume that all features are inherent attributes or a predetermined subset. Instead, we can engage in **<u>feature engineering</u>**, where we **create new features derived from the existing data.**

Feature engineering does not involve adding new information to the dataset; rather, it's about choosing how to present the data to the learning algorithm. For example, if we're dealing with binary answers like "yes" or "no," we might need to convert them into a numerical format, effectively creating new data points.

While creating new features, there's a possibility of introducing bias. However, when combining existing features, we're simply adjusting the data without artificially adding to it. This process might seem unconventional, even akin to "inventing data," but in reality, it's about optimizing the representation of the data for the learning algorithm.

![[AML-image53.jpg|350]]Consider an example: Suppose we're predicting house prices. In Amsterdam, where houses are historically narrow, the facade width becomes a meaningful parameter. In contrast, elsewhere, this parameter might be less significant. Depending on the scenario, we might choose to use existing features like facade width (x1) or total size in square meters (x2), or we could create a new feature by multiplying these parameters (x1 \* x2).

The decision to define new features depends on the insights we have into the problem at hand, rather than merely relying on the features initially available. Sometimes, by crafting new features, we can achieve a more effective model that better captures the underlying patterns in the data.

![](media/media/image500.jpg)

Polynomial regression is a technique closely tied to feature selection, particularly when standard linear models fail to adequately capture the relationship between variables. In essence, it involves **fitting a polynomial function to the data** instead of a straight line.

Consider the housing price dataset depicted in the provided plot. A linear hypothesis would struggle to accurately estimate the prices of large houses, potentially leading to overestimations. To address this limitation, we can introduce quadratic terms, allowing for greater flexibility in modeling the relationship between the features and the target variable.

![[AML-image56.jpg|380]]In polynomial regression, we extend the feature space by introducing higher-order terms of the original features. For instance, if we have a single feature 'x', we might include 'x<sup>2</sup>', ‘x<sup>3</sup>' and so on.

Although these higher-order features may not exhibit linear relationships individually, polynomial regression allows us to capture more complex patterns in the data.

![[AML-image57.jpg|291]]**By introducing these additional features, we effectively transform the problem into a multivariate regression scenario, where each higher-order feature corresponds to a distinct parameter.** This approach enables the model to learn which powers of 'x' are most relevant for accurately predicting the target variable.

It's essential to note that feature scaling becomes crucial in polynomial regression to ensure that the optimization process converges efficiently. Moreover, polynomial regression allows us to explore a broader range of functions beyond linear ones, with the training process guiding us to identify the best model for our dataset. Essentially, we can employ any function, and the training process will determine which model best fits the data.

Polynomial regression is a technique used to fit polynomial functions, such as quadratic, cubic, or higherdegree polynomials, to data points. Unlike linear regression, which fits a straight line to the data, polynomial regression **allows** for **<u>more flexible curve fitting by incorporating polynomial terms</u>**.

In polynomial regression, the choice of features refers to the input variables or predictors used to build the model. These features can be manipulated or transformed in various ways to create new features. For example, instead of using a single feature as-is, we can create new features by multiplying two features together, taking the square or cube of a feature, or applying other mathematical transformations like square roots or logarithms.

**The process of selecting which features to include in the model can be guided by experience or automated algorithms.** Experience involves leveraging domain knowledge or intuition to decide which features are likely to be relevant for predicting the target variable. Alternatively, automated feature selection algorithms analyze the data to identify the most informative features, often based on statistical metrics or machine learning techniques.

The key insight here is that by carefully engineering or designing different features, we can create models that better capture the underlying patterns in the data. For example, if a linear model fails to adequately represent the relationship between the features and the target variable, creating new features or transforming existing ones can allow us to fit more complex functions to the data, resulting in a more accurate model.

This process of feature engineering enables us to extract more meaningful information from the data and improve the performance of our predictive models.

## 5.1 NORMAL EQUATION

The normal equation provides an alternative method for computing the optimal parameters in some linear regression scenarios.

The normal equation gives you the values of 𝜃s that minimises the cost function.

Unlike Gradient Descent (GD), which iteratively minimizes the cost function J(θ) to converge towards the optimal parameter values, the normal equation offers an **analytical solution,** solving for the parameters directly in a **single step**. This distinction highlights the difference between an iterative approach (GD) and an analytical approach (normal equation).

While the normal equation seems to offer a straightforward solution without the need for iterative steps, it's important to recognize that the choice between the normal equation and GD depends on the specific circumstances of the problem at hand.

The normal equation provides precise parameter values but may not always be suitable for large datasets or when certain assumptions are not met.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Normal Equation <u><em>Pros</em>:</u></strong></p>
<ol type="1">
<li><p>Provides an <strong>analytical solution</strong>: Calculates the parameters directly in a <strong>single step</strong>, eliminating the need for iterative optimization.</p></li>
<li><p>Guarantees convergence to the <strong><u>global minimum</u></strong>: As an analytical solution, it offers precise parameter values.</p></li>
<li><p>Efficient for <strong><u>small to medium-sized datasets:</u></strong> Suitable for problems where the number of features is relatively small.</p></li>
</ol>
<p><em><strong><u>Cons:</u></strong></em></p>
<ol type="1">
<li><p><strong>Computationally expensive</strong> for large datasets: Involves matrix inversion, which can be computationally intensive and impractical for datasets with a large number of features.</p></li>
<li><p>May not be numerically stable: Inverting the design matrix can lead to numerical instability, particularly if the matrix is ill-conditioned or singular.</p></li>
<li><p>Not applicable for non-linear models: <strong>Limited to linear regression</strong> problems and cannot be extended to non-linear regression models.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>Gradient Descent <u><em>Pros</em>:</u></strong></p>
<ol type="1">
<li><p>Iterative optimization: Gradually improves the parameter estimates by iteratively minimizing the cost function, making it suitable for a wide range of optimization problems.</p></li>
<li><p>Scalable to <strong>large datasets</strong>: Can handle large datasets with millions of samples and features since it processes data in batches or mini-batches.</p></li>
<li><p>Can handle <strong>non-linear models</strong>: Can be extended to non-linear regression models and other machine learning algorithms through variations like stochastic gradient descent and mini-batch gradient descent.</p></li>
</ol>
<p><em><strong><u>Cons:</u></strong></em></p>
<ol type="1">
<li><p>May converge to local minima: Depending on the choice of learning rate and initialization, GD may converge to local minima instead of the global minimum, leading to suboptimal parameter estimates.</p></li>
<li><p>Requires careful tuning of hyper parameters: Performance can be sensitive to the choice of learning rate and other hyper parameters, which may require manual tuning.</p></li>
<li><p>Slower convergence on ill-conditioned surfaces: May converge slowly or get stuck on ill-conditioned surfaces, especially in high-dimensional spaces or when the cost function has a complex shape.</p></li>
</ol></td>
</tr>
</tbody>
</table>

To apply the normal equation, we first build:

- A "design matrix" containing all the features from the training data

- a vector with the corresponding predicted values

This matrix is then inverted to extract the optimal parameter values.

![[AML-image58.jpg|407]]

![[AML-image59.jpg|462]]

![](media/media/image62.jpeg)

## Collegamenti
- [[MBD 19 - Module 7 – Correlation and Regression]] — regressione polinomiale e overfitting

---
> [[AML 08 - Multivariate Model Regression|← Multivariate Model Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 10 - Classification|Classification →]]
