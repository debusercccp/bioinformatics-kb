---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 17
tags: [note, aml]
---

> [[AML 16 - Alternatives to GD|← Alternatives to GD]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 18 - Model Diagnostics|Model Diagnostics →]]

# Regularisation

## 10.1 OVERFITTING FOR LINEAR REGRESSION

Overfitting is a common issue in machine learning where a model learns to fit the training data too closely, resulting in poor performance when presented with new unseen data. **Overfitting** manifests as: —\> **<u>inability of the model to generalize beyond the training data.</u>**

> ![[AML-image88.jpg|486]]

It's evident that the data points don't conform to a linear trend, this phenomenon is called under-fitting. While in traditional statistics, it may be interpreted simply as a linear fit, here it highlights a bias in our analysis: we’re attempting to impose a straight line on data that doesn't conform to linearity.

To address this issue, we seek to adjust the curve to better capture the underlying patterns in the data.

On the other hand, while increasing the polynomial order can improve the fit and minimize errors, excessively complex models can lead to overfitting. In such cases, the model becomes overly sensitive to the training data, resulting in poor performance when applied to unseen data points.

Overfitting is characterized by high variance. The model may accurately predict the training data but fails to generalize to new observations, leading to erroneous estimations between data points.

Therefore, while achieving minimal error on the training set may seem ideal, it is essential to **strike a balance between model complexity and generalization ability** to avoid overfitting in machine learning applications. This phenomenon often occurs when the model has too many features or parameters, allowing it to capture noise and spurious patterns present in the training set.

When a model overfits, the cost function *J*(*θ*) may approach or even reach zero, indicating that the model perfectly fits the training data, however this optimal performance on the training set does not guarantee good performance on unseen examples.

The concept of "***GENERALIZATION***" in machine learning refers to **<u>how well a hypothesis applies to new</u> <u>examples that were not included in the training set</u>**. A model that generalizes well can accurately predict outcomes for unseen data points, demonstrating its ability to capture underlying patterns rather than memorize specific instances from the training set.

For example, in a housing price prediction scenario, an overfitted model might perfectly predict prices for houses in the training set but fail to accurately predict prices for new houses not encountered during training.

This lack of generalization can lead to unreliable predictions and diminish the model's practical utility.

**Overfitting vs Underfitting**

Overfitting arises when a model is too complex and captures noise in the training data, while underfitting occurs when a model is too simplistic and fails to capture the underlying patterns. Achieving an optimal balance between model complexity and generalization ability is essential for developing effective machine learning models. Regularization techniques, cross-validation, and careful model selection can help mitigate both overfitting and underfitting issues.

**Overfitting** occurs when a model learns the training data too well, capturing noise or random fluctuations in the data rather than the underlying pattern. In an overfitted model, the algorithm essentially memorizes the training data, including its noise and outliers, rather than learning the underlying relationships that generalize well to new, unseen data. Characteristics of an overfitted model:

- **Low training error**: The model performs well on the training data, achieving low error or high accuracy.

- **High testing error**: When applied to new, unseen data (testing or validation data), the model performs poorly, yielding high error rates.

- Complex decision boundaries: The model's decision boundaries are highly irregular and convoluted, often capturing noise and specific data points rather than general patterns.

- Overfitting is often a result of **excessively complex models** or insufficient regularization.

**Underfitting** occurs when a model is too simplistic to capture the underlying structure of the data.

In an underfitted model, the algorithm fails to learn the patterns present in the data, resulting in poor performance on both the training and testing datasets. Characteristics of an underfitted model:

- **High training error**: The model fails to capture the patterns present in the training data, resulting in high error rates or low accuracy.

- **High testing error**: Similarly, the model performs poorly on unseen data, indicating a lack of generalization.

- Oversimplified decision boundaries: The model's decision boundaries are overly simplistic and fail to capture the complexities present in the data.

- Underfitting often occurs when the model is too simple relative to the complexity of the underlying data, such as using a linear model for non-linear data.

**Optimization vs Generalisation**

Optimization focuses on improving performance on the training data, while generalization focuses on ensuring that the model performs well on unseen data, thereby demonstrating its ability to capture underlying patterns in the data. Balancing optimization and generalization is essential for building effective machine learning models.

***Optimization*** refers to the process of **adjusting model parameters to minimize a chosen cost function** or error metric on the training data. The goal of optimization is to find the set of parameters that best fit the training data and enable the model to make accurate predictions. Techniques such as gradient descent and its variants are commonly used for optimization in machine learning. Optimization focuses on i**mproving the model's performance on the training data.**

**Generalization** refers to the ability of a trained model to perform well on new, unseen data that it hasn't encountered during training. A model that generalizes well is able to capture underlying patterns and relationships in the data without simply memorizing the training examples. Generalization is crucial because the ultimate objective of a machine learning model is to make accurate predictions on new, unseen data points. Overfitting, where a model performs well on the training data but poorly on unseen data, is a common obstacle to achieving good generalization.

## 10.2 OVERFITTING FOR LOGISTIC REGRESSION

![[AML-image89.jpg|311]]Initially, I attempt to establish a linear decision boundary using a linear hypothesis, however this initial hypothesis proves to be overly simplistic.

The second attempt at creating a decision boundary is more appropriate and better suited to the data.

A third attempt could be made to further refine the fit to the data. However, it's important to note that there is no assurance that the resulting decision boundary (represented by the pink line) will necessarily outperform the previous one (represented by the orange line).

## 10.3 ADDRESS OVERFITTING

Naively, one might think, "Why should I worry? I'll just plot hypotheses and use common sense." However, the reality is more complex. In scenarios:

- with a **large number of features,** the simplicity of visualizing data in one or two dimensions becomes impractical. Even with advanced data visualization techniques, such as 3D plots, the sheer volume of features can overwhelm the visualization process. Housing example with size, \# bedrooms, \# floors, age of house, average income in neighbourhood, size of the kitchen, presence of garage or not, etc

- with **small training datasets containing only a few examples**, overfitting becomes a serious concern. When we have many features and relatively little training data, the risk of overfitting increases significantly, potentially undermining the performance and reliability of the model.

Basically there are 2 main options to address overfitting. These are basic ideas and techniques, more refined approaches exist.

1.  **<u>Reduce the number of features</u>**

Reducing the number of features can be achieved by **manually reviewing the list of features and selecting** only those deemed **essential**, while discarding the rest.

However, this approach carries a significant drawback: **the potential loss of valuable information**.

By discarding certain features, we risk discarding valuable insights that could have been crucial for accurately describing the underlying patterns in the data.

These discarded features might have contained rich information that could have contributed to highlighting important patterns within the dataset, thus affecting the effectiveness of the data-driven model.

2.  **<u>Tune the importance of features</u>**

Another approach to address overfitting is to tune the importance of features, a process commonly referred to as "regularization". Instead of discarding features, we retain all of them but **adjust the magnitude of the parameters associated with each feature**. This method is particularly useful when dealing with **datasets containing numerous features**, where each feature contributes to predicting the value of the target variable to some extent. By fine-tuning the parameters, we can effectively **<u>control the influence of each feature on</u> <u>the model's predictions</u>**. The advantage of this approach is that it allows us to **retain all features** without the need for discarding any of them, thereby preserving potentially valuable information contained within the dataset.

## 10.4 REGULARISED COST FUNCTION

We want to mitigate overfitting observed in the pink curve by adjusting the parameters to obtain the blue curve, which strikes a balance between the orange and pink curves.

The idea is to not stop only at the orange case, but apply the pink case and tune down the parameters that are in the blue box.

- We force *θ*3 and *θ*4 to be significantly smaller - though not zero - compared to the other parameters. If we aimed for them to be zero, we'd achieve the orange curve

- ![[AML-image90.jpg|330]]While the blue curve may not perfectly match the orange curve, it effectively mitigates the overfitting problem by curbing the excessive complexity exhibited by the pink curve.

Instead of minimizing just the original cost function, an additional term (regularization term) is added to the cost function, which is the sum of the squares of the model's coefficients (thetas). This **REGULARIZATION TERM** is typically a **penalty term** that **discourages the model from fitting the training data too closely** and helps to prevent the model from becoming overly complex. In this way the features that are relevant stay relevant, the others are going to be tuned down.

The parameter **lambda** (*λ*) is introduced as a **hyperparameter** that controls the strength of regularization applied to a model. It determines how much importance is given to the regularization term compared to the original loss function during training, so it determines how much emphasis is placed on minimizing the sum of the squares of the coefficients relative to minimizing the original cost function.

- Higher value of λ increases the regularization strength, leading to simpler models with small parameter values, but aggressive regularization could lead to underfitting.

- Lower value of λ decreases the regularization effect, allowing the model to fit the training data more closely, but may increase the risk of overfitting.

Lambda is not learned from the training data but is set manually or through techniques like cross-validation.

![](media/media/image850.jpg)

## 10.5 REGULARISED LINEAR REGRESSION

In our exploration of linear regression, we previously examined two fundamental learning algorithms: one based on gradient descent (GD) and another on the normal equation. Now, our focus shifts to the realm of regularised linear regression, where we extend these algorithms to accommodate the incorporation of regularization.

*Admittedly: we will be brief for GD, and even more brief for the normal equation. Namely, just a glance (and no summary of concepts at the end of this section)*

**What remains unchanged**

The core principles underlying linear regression remain intact. We continue to seek the optimal parameters, denoted as *θ* to minimize the difference between predicted and actual values, as we know from the formula:

![[AML-image93.png|264]]

**What changes**

Regularisation introduces a penalty term that discourages overly complex models, effectively mitigating the risk of overfitting. This adjustment is encapsulated in the updated cost function:

![[AML-image94.png|278]] *i*=1 *j*=1

In this formula:

- *m* is the number of training examples.

- *h<sub>θ</sub>*(*x*(*i*<sup>)</sup>) is the hypothesis function for the *i*-th training example.

- *y*<sup>(*i*)</sup>is the actual output for the *i*th training example.

- *λ*s the regularization parameter.

- *n* is the number of features (excluding the bias term).

- *θj*is the parameter associated with the *j*-th feature.

![[AML-image95.jpg|700]]

To implement regularization in **normal gradient descent**, the update rule for the parameter *θj*will change to include the regularization term. Instead of the original update rule, which only considers the gradient of the cost function, the new update rule will also include the derivative of the regularization term with respect to *θj* This modified update rule ensures that the parameters are updated in a way that penalizes large values of *θj*, thus preventing overfitting.

To implement regularization with the **normal equation**, you would adjust the calculation of the parameter vector *θ* by incorporating the regularization term.

The normal equation without regularization is: *θ* = (*X<sup>T</sup> X*)<sup>−1</sup>*X<sup>T</sup>y* ![](media/media/image880.jpg)

With regularization, the normal equation becomes: *θ* = (*X<sup>T</sup> X* + *λI* )<sup>−1</sup>*X<sup>T</sup>y*

Where:

- *λ* is the regularization parameter.

- *I* is the identity matrix.

- *X* is the feature matrix.

- *y* is the target vector.

By adding *λI* to the matrix *X<sup>T</sup> X*, you ensure that the inverse exists even if *X<sup>T</sup> X* is not invertible due to linear dependence among features. This adjustment helps prevent overfitting by regularizing the model parameters.

![[AML-image98.jpg|530]]

## 10.6 REGULARISED LOGISTIC REGRESSION

For **logistic regression**, we previously talked mostly about one algorithm: Gradient Descent.

We can adapt any technique above and make them work for **regularised logistic regression**

> ![](media/media/image910.jpg)

For regularized logistic regression, the cost function with regularization is given by:

![[AML-image101.png|75]]*J*∑*m* \[*y*<sup>(*i*)</sup> log(*h<sub>θ</sub>*(*x*<sup>(*i*)</sup>)) + (1 − *y*<sup>(*i*)</sup>)log(1 − *h<sub>θ </sub>*\] *λ* ∑*n θj*2

> (*x*(*i*))) + 2*m*

*i*=1 *j*=1

- *m*: number of training examples

- *n*: number of features

- *θ*: parameters of the model

- *h<sub>θ</sub>*(*x*): hypothesis function that outputs the probability that *y* = 1given input *x*

- *λ*: regularization parameter

To implement regularization in gradient descent for logistic regression, you update the gradient descent rule as follows:

![[AML-image102.png|323]]

- *α*: Learning rate

- *x<sub>j</sub>*<sup>(*i*)</sup>: j-th feature of the *i*-th training example

- ![[AML-image103.jpg|425]]*m<u>λ</u> θj*: Regularization term

- *λ*: Regularization parameter

## Collegamenti
- [[MBD 19 - Module 7 – Correlation and Regression]] — regolarizzazione (ridge/lasso)

---
> [[AML 16 - Alternatives to GD|← Alternatives to GD]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 18 - Model Diagnostics|Model Diagnostics →]]
