---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 21
tags: [note, aml]
---

> [[AML 20 - Model Diagnostics · Model Selections & Tvt Sets|← Model Diagnostics · Model Selections & Tvt Sets]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 22 - Model Diagnostics · Regularisation Bias and Variance|Model Diagnostics · Regularisation Bias and Variance →]]

# Bias and Variance

If a learning algorithm doesn't perform as expected, it's often due to either:

- High bias (underfitting)

- High variance (overfitting)

We can visualize this by **plotting** the **<u>training error and cross-validation error</u>** **against** the **<u>hypothesis</u>** **<u>complexity</u>** (typically represented by the degree of a polynomial).

> ![[AML-image115.jpg|463]]

**TRAINING ERROR**

When the hypothesis is simple, the model's **complexity is low**, and the **training error** is likely to be relatively **high**. This is because the model's simplicity may not capture all the nuances and patterns present in the training data, leading to errors in predictions.

As we move towards the right side of the plot, indicating an increase in the complexity of the hypothesis, the training error starts to decrease. This is because **more complex models have greater flexibility to fit the training data closely, resulting in lower errors.** Therefore, the process of minimizing the error is most impactful as we move towards the right side of the plot, where the hypothesis becomes more complex However, there's a point where further increasing complexity doesn't significantly reduce the error.

**VALIDATION ERROR**

The **validation error** may **start off higher compared to the training error**, this is because the validation set typically consists of a smaller dataset compared to the training set: **with fewer examples to learn from, the model may initially struggle to generalize well**, leading to a higher error.

As we continue to increase the complexity of our hypothesis, the validation error usually improves.

This improvement occurs as the model captures more of the underlying patterns in the data.

However, beyond a certain point, **increasing the complexity further can lead to overfitting and as result, the validation error begins to increase again.**

Overfitting occurs when the model starts capturing noise in the data rather than the underlying patterns.

**<u>The optimal value usually lies somewhere in the middle of the complexity spectrum.</u>**

(While we typically don't plot the test error, we assume it follows a similar pattern to the validation error, as the test set is similar to the validation set, so *Jtest* and *Jcv* would look similar.)

Suppose we have a learning algorithm that performs below our expectations and we want to understand whether there's a bias or variance issue, by **plotting the training error and validation error on the same graph**, we can observe their trends.

> ![[AML-image116.jpg|392]]

The ultimate goal in model optimization is to strike a balance between bias and variance, aiming for an optimal point where both errors are minimized. This optimal point indicates that the model has learned to generalize effectively beyond the training data without overly memorizing them, achieving a desirable level of performance on unseen data.

**<u>High variance (overfitting)</u>** —\> simplify the model

It is characterized by a significant **divergence** between the **training** **error** and the **validation error**.

In this scenario, as the complexity of the model increases, the training error decreases because the model begins to memorize intricate details from the training data. However, despite the decrease in training error, the validation error remains high or even increases. This discrepancy indicates that the **model fails to generalize effectively to new, unseen data during the validation phase.**

**<u>High bias (underfitting)</u>** —\> further complicate to capture more complex patterns

It occurs when both the **training error** and the **validation error** **remain consistently high** and do not decrease as the model's complexity increases. This situation arises when the **model is too simplistic to capture the underlying complexity of the data adequately**. Consequently, the model fails to fit the training data well, resulting in persistently high errors for both training and validation datasets.

> ![[AML-image117.jpg|491]]

---
> [[AML 20 - Model Diagnostics · Model Selections & Tvt Sets|← Model Diagnostics · Model Selections & Tvt Sets]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 22 - Model Diagnostics · Regularisation Bias and Variance|Model Diagnostics · Regularisation Bias and Variance →]]
