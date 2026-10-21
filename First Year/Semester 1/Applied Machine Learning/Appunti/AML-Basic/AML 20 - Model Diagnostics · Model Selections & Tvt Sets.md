---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 20
tags: [note, aml]
---

> [[AML 19 - Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error|← Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 21 - Model Diagnostics · Bias and Variance|Model Diagnostics · Bias and Variance →]]

# Model Selections & Tvt Sets

We've explored the challenge of overfitting, where a model may fit a training set well but fail to generalize to new examples. This underscores the limitation of using the training set error as a predictor of a hypothesis's performance on unseen data.

The error calculated on the training set *J*<sub>train</sub>(*θ*) is not necessarily indicative of how well the hypothesis will perform on new examples. This is because the model might have learned to accommodate the specific quirks and noise present in the training data, rather than capturing the underlying patterns that generalize to unseen data. Therefore, relying solely on the training set's error to assess the model's performance can be misleading. To address this, we introduced the concept of a test set.

To **<u>select the most effective algorithm from a range of hypotheses,</u>** we **consider** a **spectrum from simple to complex models:**

1.  We **evaluate each hypothesis** by **training it** on the training set and computing the

> **training error** *J***<sub>train</sub>**(*θ*)

2.  Then we **repeat this process for the test set** to obtain the **test error** *J***<sub>test</sub> for each hypothesis** 3. The **<u>model with the lowest test error</u>**, indicating superior performance on unseen data, is **<u>chosen</u>**.

> ![](media/media/image980.jpg)

For instance, if the fifth model has the lowest test error, suggesting that a polynomial of degree 5 fits the data well, we consider it for deployment.

It's crucial to acknowledge that using the test set for model selection means that the **test data has been 'used up'.** In other words, the **test set** has **served** its purpose in evaluating and **selecting** t**he best-performing model.** Therefore, to ensure that the selected model can generalize effectively to new, unseen data in realworld scenarios, it's necessary to obtain additional data beyond the training and test sets, therefore this additional data enables the model to generalize more robustly and accurately to unseen situations or inputs.

> ![[AML-image110.jpg|502]]

We can divide our dataset into three distinct subsets: the training set, validation set, and test set.

Typically, we allocate 60% of the data for training, while splitting the remaining 40% equally between validation and test sets. This ensures a robust statistical basis for training while providing separate datasets for model validation and evaluation.

- **TRAINING SET (60%)**

This subset is exclusively used for **training the model**. It forms the backbone of our learning process, allowing the algorithm to learn from the data and **adjust its parameters to minimize errors.**

- **VALIDATION SET (20%)**

The validation set serves as a means to **validate the model's performance during training**.

By **assessing the model's performance on unseen data from the validation set**, we can **<u>fine-tune</u> <u>hyperparameters</u> and <u>prevent overfitting</u>**.

- **TEST SET (20%)**

The test set is **reserved** for **evaluating the model's generalization ability**. It provides an unbiased assessment of the **model's performance on completely unseen data**, helping us understand how well the model will perform in real-world scenarios. Unlike the validation set, which may be used multiple times during training, the test set is only used once, typically at the very end of the machine learning pipeline, to obtain a final evaluation of the model's performance.

Using separate datasets for training, validation, and testing offers both advantages and disadvantages. While this division allows us to utilize 80% of the data for model training, it also means that we cannot assess the entire dataset due to the unavailability of the 20% test set.

The advantage of this approach lies in the ability to work with a substantial portion of the data during model training, which can lead to more effective learning and parameter optimization. However, the inability to examine the entire dataset poses a limitation, particularly when assessing the model's performance on unseen data.

If we **<u>look at the test set</u>**, we **<u>risk introducing irreversible bias into our results</u>**, as we cannot use this data to directly improve the model. Therefore, it's essential to refrain from using all available data and maintain a clear separation between training, validation, and test sets to ensure unbiased evaluation and reliable model performance assessment.

By defining clear boundaries between the training, validation, and test sets, we can accurately compute three key metrics:

- Training error *Jtrain*

- Cross-validation error *Jcv*

- ![[AML-image111.jpg|286]]Test error *Jtest*

These metrics provide valuable insights into the model's performance across different stages of development, ensuring robust evaluation and reliable conclusions.

The **TVT (Training, Validation, Test)** procedure involves three key phases in developing and assessing machine learning models.

1.  **Training Phase**

During the training phase, the model is exposed to the labeled data from the training set, typically comprising 70-80% of the total dataset. The model learns from this data by adjusting its parameters iteratively to minimize the training error and improve its performance. The objective is to develop a model that can accurately predict outcomes based on the patterns and relationships present in the training data.

2.  **Validation Phase**

Once training is complete, the model's **performance is evaluated using the validation set,** which contains data that the model hasn't seen during training.

This phase is crucial for assessing how well the trained model generalizes to new, unseen data.

By comparing the model's predictions with the actual labels in the validation set, we can measure its performance and identify any issues such as overfitting or underfitting.

Additionally, **hyperparameters can be fine-tuned** based on the validation results to optimize the model's performance

3.  **Test Phase**

In the final phase, the model's performance is assessed using the test set, which serves as an independent dataset that hasn't been used for training or validation. The test set allows us to obtain an unbiased estimate of the model's performance in real-world scenarios, as it **simulates how the model would perform when deployed.** By evaluating the model on unseen data, we can verify its ability to generalize and make accurate predictions outside the training and validation datasets. This step is crucial for validating the effectiveness of the trained model and ensuring its reliability in practical applications.

![](media/media/image102.jpg)

*Kaggle is a popular online platform that hosts datasets, tutorials, and forums where users can collaborate, share knowledge, and learn from each other. It also provides tools and resources for data exploration, visualization, and machine learning model development [(http://kaggle.com)](http://kaggle.com/)*

---
> [[AML 19 - Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error|← Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 21 - Model Diagnostics · Bias and Variance|Model Diagnostics · Bias and Variance →]]
