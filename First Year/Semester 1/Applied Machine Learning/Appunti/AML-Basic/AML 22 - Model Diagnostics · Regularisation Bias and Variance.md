---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 22
tags: [note, aml]
---

> [[AML 21 - Model Diagnostics · Bias and Variance|← Model Diagnostics · Bias and Variance]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 23 - Model Diagnostics · Learning Curves|Model Diagnostics · Learning Curves →]]

# Regularisation Bias and Variance

**Regularization** serves as a crucial **tool** to **combat overfitting** in machine learning models. It achieves this by penalizing overly complex models, thereby promoting simpler models that generalize well to unseen data.

When applying regularization to a polynomial hypothesis, the choice of the regularization parameter lambda plays a pivotal role. Setting ***lambda*** to a:

- **Large** value results in **excessive regularization,** leading to a flat hypothesis that fails to capture the underlying patterns in the data.

- **Small** value effectively **disables regularizatio**n, allowing the model to become overly complex and prone to overfitting.

> ![[AML-image118.jpg|414]]

Achieving the right balance between regularization and model complexity requires selecting an appropriate lambda value. To <u>**select the regularization parameter lambda**,</u> we **employ the model selection procedure** discussed previously. This involves defining three error metrics: training error, validation error, and test error.

> ![[AML-image119.jpg|375]]

1.  **<u>Initializing Lambda</u>**

Start by setting lambda (regularization parameter) to 0 and gradually increase lambda, doubling its value at each step to cover an order of magnitude.

2.  **<u>Model Training</u>**

Train a model at each lambda value, resulting in 12 different models with varying regularization strengths. Minimize the training error for each model to obtain the corresponding set of theta parameters.

3.  **<u>Validation Error Evaluation</u>**

Evaluate the performance of each model on the validation set. Compute the validation error for each model, which may be time-consuming due to training multiple models.

4.  **<u>Optimal Lambda Selection</u>**

**Select the lambda value that corresponds to the smallest validation error.**

This lambda value represents the optimal regularization parameter for the model.

5.  **<u>Test Error Reporting</u>**

Report the test error using the theta parameters derived from the selected lambda value.

This comprehensive process of model selection and hyperparameter tuning ensures the performance and generalization ability of the model.

![[AML-image120.jpg|697]]

So we have seen that the process of model selection also applies to choosing the best regularization parameter lambda. This logic underlies various hyperparameter scan methods that you can readily import and use in your code.

One crucial aspect to understand is how cross-validation and training errors change as we vary the regularization parameter 𝜆.

Plotting the training error *Jtrain* and the validation error *Jcv* across different lambda values provides insight into the model's behavior, therefore for:

- small *λ* (on the left side of the plot): it indicates minimal regularization and the model tends to overfit the training data, resulting in a low training error but a high validation error.

- large *λ* (on the right side): regularization becomes more significant and the model underfits the data, leading to high errors in both training and validation.

As lambda increases, the validation error initially decreases until it reaches an optimal value where the model generalizes well. However, further increasing lambda can cause the validation error to rise again, indicating excessive bias in the model.

The process of selecting the best regularization parameter lambda is akin to model selection, involving the systematic evaluation of different lambda values.

This logic underlies various hyperparameter scan methods commonly used in machine learning.

During the validation phase, the model is trained on the training set and evaluated on the validation set. By monitoring the validation error as lambda varies, we can identify the optimal value that strikes a balance between fitting the training data well and generalizing effectively to unseen data.

![[AML-image121.jpg|662]]

> ![[AML-image122.jpg|679]]

---
> [[AML 21 - Model Diagnostics · Bias and Variance|← Model Diagnostics · Bias and Variance]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 23 - Model Diagnostics · Learning Curves|Model Diagnostics · Learning Curves →]]
