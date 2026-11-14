---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 14
tags: [note, aml]
---

> [[AML 13 - Logistic Regression · Cost Function|← Logistic Regression · Cost Function]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 15 - Multiclass Classification|Multiclass Classification →]]

# Simplified Cost Function and Gradient Descent

To simplify the logistic regression cost function and prepare it for application to the entire training set, we start from the J cost function and express its components explicitly. We then proceed to refine it as follows:

We'll rewrite the cost function as a single expression by incorporating the separate components for:

- When *y* = 1 (meaning the actual label is positive): −*y* log(*h*(*x*)) becomes −log(*h*(*x*)), penalizing low values of *h*(*x*) (i.e., when the model is not confident in predicting a positive outcome)

- When *y* = 0 (meaning the actual label is negative): −(1 − *y*)log(1 − *h*(*x*)) becomes −log(1 − *h*(*x*)), penalizing high values of *h*(*x*) (i.e., when the model is not confident in predicting a negative outcome). Combining these cases into a single expression, we arrive at the simplified cost function:

cost(*h*(*x*),*y*) = − *y* log(*h*(*x*)) − (1 − *y*)log(1 − *h*(*x*))

This simplified cost function effectively captures the essence of logistic regression by penalizing deviations between the predicted probabilities and the actual labels. It is commonly used as the objective function in logistic regression models, making it suitable for optimization techniques like gradient descent.

This simplification allows us to condense the cost function into a single formula that dynamically adjusts based on the value of y, ensuring that the appropriate component is selected depending on whether y is 0 or This adjusted cost function will facilitate the application of gradient descent to fit the parameters of logistic regression effectively.

![[AML-image84.jpg|432]]

The choice of the **cross-entropy/log loss function** in logistic regression is not arbitrary, here's why we choose this particular function:

- Maximum Likelihood Estimation (MLE): The cross-entropy loss function can be derived from statistical principles, particularly the concept of maximum likelihood estimation (MLE). MLE is a method for estimating the parameters of a statistical model by maximizing the likelihood function, which measures how well the model explains the observed data.

- Convexity: The c**ross-entropy loss function has a convex shape**, meaning it forms a "bowl-shaped" curve. This convexity property ensures that gradient-based optimization algorithms, such as gradient descent, will converge to the global minimum. Convexity guarantees that there are no local minima to get stuck in, and the optimization process is efficient and reliable.

1.  **Fit Parameters Minimize**

After defining the cost function, our objective is to fit the parameters *θ* by minimizing *J*(*θ*). This involves an iterative optimization process where we adjust the parameters to reduce the cost function until convergence, typically using gradient descent or other optimization algorithms. This optimization yields a set of parameter values that best describe the relationship between the features and the target variable.

2.  **Make Predictions**

Once we have obtained the optimized parameters *θ*, we can use them to make predictions for new examples with a given set of features *x*. By applying the learned parameters to our hypothesis function *h*(*x*), we can output a prediction *h* For the target variable *y*.

3.  **Interpretation**

It's important to note that the output of our hypothesis should be interpreted as the probability that *y* = 1, given the input *x* and parameterized by *θ*. This probability indicates the confidence of our model in predicting the positive class.

![[AML-image85.jpg|697]]

## 7.5 GD LINEAR REGRESSION VS GD LOGISTIC REGRESSION

The GD algorithm expression for linear regression and logistic regression may seem similar due to the shared optimization algorithm, the underlying distinction in the hypothesis function *h*(*x*) leads to different models and optimization objectives.

- In linear regression, the hypothesis function is defined as the dot product of the feature vector *x* and the parameter vector *θ* —\> *h*(*x*) = *θ<sup>T</sup> x*

> This represents a linear relationship between the features and the target variable.

- In logistic regression, the hypothesis function is the sigmoid of the linear combination of the feature vector and parameters —\>\
  $$
  h_{\theta}(x) = \frac{1}{1 + e^{- \theta^{T}x}}
  $$

> This sigmoid transformation ensures that the output of the hypothesis lies between 0 and 1, suitable for binary classification tasks, where the output is interpreted as the probability of the positive class.
>
> ![[AML-image86.jpg|335]]

**Feature scaling** and **mean normalization**, which are techniques used to preprocess data in linear regression, can also be beneficial in logistic regression.

By applying feature scaling and monitoring the convergence of GD, logistic regression models can be trained more effectively, leading to better predictive performance and faster convergence.

In logistic regression, when features are on vastly different scales, applying feature scaling can aid in faster convergence of gradient descent (GD). Similar to linear regression, feature scaling involves scaling all features to a similar range, typically between 0 and 1 or -1 and 1. This ensures that the GD algorithm can converge more efficiently as it navigates the cost function landscape.

Additionally, mean normalization can be employed to center the features around zero by subtracting the mean from each feature. This can further enhance the performance of GD by preventing numerical instability and ensuring that the optimization process is not biased towards any specific feature.

Monitoring the convergence of GD in logistic regression follows similar principles to those applied in linear regression. It involves tracking the value of the cost function over iterations and observing how it changes. If the cost function decreases with each iteration and eventually converges to a stable value, then GD is deemed successful. However, if the cost function exhibits erratic behavior or fails to decrease over time, adjustments may be required, such as tuning the learning rate or employing more advanced optimization techniques.

---
> [[AML 13 - Logistic Regression · Cost Function|← Logistic Regression · Cost Function]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 15 - Multiclass Classification|Multiclass Classification →]]
