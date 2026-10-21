---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 13
tags: [note, aml]
---

> [[AML 12 - Logistic Regression · Decision Boundary|← Logistic Regression · Decision Boundary]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 14 - Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression|Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression →]]

# Cost Function

![[AML-image77.jpg|280]]Understanding the cost function in logistic regression is crucial for fine-tuning the hypothesis and determining the parameter values (theta).

This process allows us to fit the model effectively to our training data.

In logistic regression, we typically work with a training set containing m examples, each comprising a feature vector and binary labels for binary classification.

The binary labels, denoted as y, represent the outcomes we aim to predict.

In logistic regression, our hypothesis is formulated by applying the logistic function to the regression hypothesis. The regression hypothesis represents the relationship between the input features and the output, and the logistic function transforms this relationship into a probability estimate.

The theta parameters are part of our hypothesis and are embedded within it. These parameters determine the shape and behavior of the hypothesis function.

By adjusting the values of theta, we can influence how well the hypothesis fits the training data. In other words, theta parameters control the decision boundary that separates different classes in the feature space, allowing the model to make accurate predictions about the probability of each class given the input features.

> ![[AML-image78.jpg|296]]In linear regression, we utilized a cost function, often denoted as J, to measure the error between predicted and actual values. However, when transitioning to logistic regression, using the same cost function isn't suitable. Attempting to minimize the same cost function for logistic regression leads to non-convexity issues, rendering it ineffective for optimization.
>
> Convexity refers to the property of a function shaped like a bowl, with a single minimum point. This makes it easy to find the minimum of the curve, which is what we aim to do when minimizing the cost function during optimization.

Using a cost function that leads to non-convexity in logistic

regression makes the optimization process less effective and may prevent us from finding the best parameters for our model. Therefore, it's essential to develop a new cost function specifically tailored to logistic regression to ensure smooth optimization and accurate model fitting.

![[AML-image79.jpg|697]]

This passage discusses a strategy for **constructing a convex cost function for logistic regression.**

The idea is to use the negative logarithm of the hypothesis for y = 1 and the negative logarithm of (1 - hypothesis) for y = 0 as the components of the cost function.

By using this approach, it's suggested that we can obtain a convex function that can be minimized effectively. The convexity of the function is crucial because it ensures that gradient descent optimization methods will converge to a global minimum.

When you take the logarithm of a positive value z, the result increases as z increases.

However, as z approaches zero, the logarithm approaches negative infinity. This means that the curve of the logarithm function steeply rises as z gets larger, but it flattens out and approaches negative infinity as z gets closer to zero.

![[AML-image80.jpg|369]]Similarly, when you take the negative logarithm of a value, the resulting curve behaves in the opposite manner. As the value approaches zero, the negative logarithm approaches positive infinity, and as the value increases, the negative logarithm decreases, approaching zero.

Therefore, the behavior of the negative logarithm mirrors that of the logarithm, but in the opposite direction.

When taking the logarithm of a value z, the resulting curve approaches negative infinity as z approaches zero and increases slowly as z increases.

This behavior is mirrored when considering the negative logarithm.

Let's consider our hypothesis *h*(*x*) as *z* and focus on the negative logarithm of the hypothesis when *y* = 1. When *y* = 1, the negative logarithm of *h*(*x*) represents the cost incurred for the positive class. This cost can be visualized as a curve in the first quadrant of a Cartesian coordinate system, akin to the green line in the diagram. On this graph:

- the x-axis corresponds to *h*(*x*), which is equivalent to *z*

- the y-axis represents the cost, a component of the *J* cost function

As *h*(*x*) approaches 1 (the truth for *y* = 1), the cost diminishes, approaching zero.

Conversely, as *h*(*x*) tends towards 0 (indicating strong confidence in the negative class when the true label is positive), the cost increases drastically, approaching infinity.

> ![[AML-image81.jpg|381]]

This reflects the severe penalty imposed by misclassifying positive instances, especially when the model is overly confident.

Now, consider the scenario when *y* = 0, where we evaluate the negative logarithm of 1 − *h*(*x*).

In this case, the negative class is the truth, and if our hypothesis correctly predicts 0, the cost is minimal. However, as *h*(*x*) approaches 1 (incorrectly predicting the positive class when the true label is negative), the cost escalates.

![[AML-image82.jpg|505]]

When the cost is high, it signifies that our hypothesis is significantly deviating from the truth, resulting in substantial penalties. Conversely, if our hypothesis accurately aligns with the truth, the cost gradually diminishes, eventually reaching zero. Therefore, we incur substantial costs when our hypothesis misclassifies instances, such as predicting 1 when the true label is 0 (left representation), or predicting 0 when the true label is 1 (right representation). However, if our predictions match the truth, meaning we predict 1 when the true label is 1, or predict 0 when the true label is 0, then the cost is negligible because we have correctly guessed the labels. In essence, high costs are associated with misclassifications, while correct classifications incur no cost.

![[AML-image83.jpg|411]]

## Collegamenti
- [[MBD 18 - Module 6 – Probability Theory · Maximum likelihood estimation and sampling distributions]] — massima verosimiglianza

---
> [[AML 12 - Logistic Regression · Decision Boundary|← Logistic Regression · Decision Boundary]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 14 - Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression|Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression →]]
